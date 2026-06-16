#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "b5-jm-figure4-target-extraction.csv"
OUTPUT = ROOT / "data" / "b5-jm-source-scaling-proxy.csv"

G = 6.67430e-11
LIGHT = 299792458.0
MSUN = 1.98847e30
K2 = 0.09


def fnum(x: str) -> float | None:
    x = (x or "").strip()
    if not x:
        return None
    try:
        return float(x)
    except ValueError:
        return None


def comp(m_sun: float, r_km: float) -> float:
    return G * (m_sun * MSUN) / ((r_km * 1000.0) * LIGHT * LIGHT)


def lam(cmp: float) -> float:
    return (2.0 / 3.0) * K2 * cmp ** -5


def inertia(m_sun: float, r_km: float) -> float:
    m = m_sun * MSUN
    r = r_km * 1000.0
    b = comp(m_sun, r_km)
    return (0.237 * m * r * r * (1.0 + 4.2 * b + 90.0 * b ** 4)) / 1.0e38


def include_row(row: dict[str, str]) -> bool:
    if row["EOS"] != "DD2":
        return False
    if row["rotation_spec"] == "pure":
        return True
    if row["rotation_spec"] == "f_Hz" and row["rotation_value"] in {"100", "300"}:
        return True
    if row["rotation_spec"] == "omega_frac_kep" and row["rotation_value"] in {"0.1", "0.2"}:
        return True
    return False


def main() -> None:
    base_rows = []
    with INPUT.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not include_row(row):
                continue
            m = fnum(row.get("target_mass_Msun", ""))
            r = fnum(row.get("radius_km", ""))
            if m is None or r is None:
                continue
            base_rows.append((row, m, r))

    pure_radius = {}
    pure_lam = {}
    pure_i = {}
    for row, m, r in base_rows:
        if row["rotation_spec"] == "pure":
            key = f"{m:.3f}"
            cc = comp(m, r)
            pure_radius[key] = r
            pure_lam[key] = lam(cc)
            pure_i[key] = inertia(m, r)

    out = []
    for row, m, r in base_rows:
        key = f"{m:.3f}"
        cc = comp(m, r)
        l = lam(cc)
        ii = inertia(m, r)
        out.append({
            "EOS": row["EOS"],
            "rotation_spec": row["rotation_spec"],
            "rotation_value": row["rotation_value"],
            "mass_Msun": f"{m:.3f}",
            "radius_km": f"{r:.3f}",
            "Delta_R_vs_pure_km": f"{r - pure_radius[key]:.3f}",
            "compactness": f"{cc:.6f}",
            "k2_assumed": f"{K2:.3f}",
            "Lambda_proxy": f"{l:.3f}",
            "Delta_Lambda_pct": f"{100.0 * (l / pure_lam[key] - 1.0):.3f}",
            "I_proxy_1e45_g_cm2": f"{ii:.3f}",
            "Delta_I_pct": f"{100.0 * (ii / pure_i[key] - 1.0):.3f}",
            "gate_note": gate_note(row, m),
        })

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


def gate_note(row: dict[str, str], m: float) -> str:
    spec = row["rotation_spec"]
    val = row["rotation_value"]
    if spec == "pure":
        return "baseline"
    if spec == "f_Hz" and val == "300":
        return "strong source response / J0740 pass" if m > 2 else "strong source response / BNS proxy pass"
    if spec == "omega_frac_kep" and val == "0.2":
        return "strong source response / BNS proxy pass but high-mass cutoff"
    return "mild source response"


if __name__ == "__main__":
    main()
