#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "b5-jm-figure4-target-extraction.csv"
OUTPUT = ROOT / "data" / "b5-jm-lambda-i-proxy.csv"

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
    val = 0.237 * m * r * r * (1.0 + 4.2 * b + 90.0 * b ** 4)
    return val / 1.0e38


def main() -> None:
    rows = []
    with INPUT.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["EOS"] != "DD2":
                continue
            if row["rotation_spec"] not in {"pure", "f_Hz"}:
                continue
            if row["rotation_spec"] == "f_Hz" and row["rotation_value"] != "300":
                continue
            m = fnum(row.get("target_mass_Msun", ""))
            r = fnum(row.get("radius_km", ""))
            if m is None or r is None:
                continue
            cc = comp(m, r)
            rows.append({
                "EOS": row["EOS"],
                "rotation_spec": row["rotation_spec"],
                "rotation_value": row["rotation_value"],
                "mass_Msun": f"{m:.3f}",
                "radius_km": f"{r:.3f}",
                "compactness": f"{cc:.6f}",
                "k2_assumed": f"{K2:.3f}",
                "Lambda_proxy": f"{lam(cc):.3f}",
                "I_proxy_1e45_g_cm2": f"{inertia(m, r):.3f}",
                "source": "Figure4 vector extraction",
            })

    pure = {r["mass_Msun"]: r for r in rows if r["rotation_spec"] == "pure"}
    out = []
    for r in rows:
        p = pure[r["mass_Msun"]]
        l = float(r["Lambda_proxy"])
        l0 = float(p["Lambda_proxy"])
        ii = float(r["I_proxy_1e45_g_cm2"])
        i0 = float(p["I_proxy_1e45_g_cm2"])
        out.append({
            **r,
            "Delta_Lambda_vs_pure": f"{l - l0:.3f}",
            "Delta_Lambda_pct": f"{100.0 * (l / l0 - 1.0):.3f}",
            "Delta_I_vs_pure_1e45_g_cm2": f"{ii - i0:.3f}",
            "Delta_I_pct": f"{100.0 * (ii / i0 - 1.0):.3f}",
        })

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
