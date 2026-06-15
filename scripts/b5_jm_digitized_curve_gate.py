#!/usr/bin/env python3
"""
Gate digitized Jockel-Menger Fig. 4 rows.

Fill data/b5-jm-figure4-digitization-template.csv with manually digitized
R_GR and R_torsion values. This script then scores whether those rows pass the
B5 promoted lane:
  negative compactification,
  high-mass survival,
  BNS/tidal compatibility proxy.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "b5-jm-figure4-digitization-template.csv"
OUTPUT = ROOT / "data" / "b5-jm-digitized-curve-gate.csv"

J0740_MASS_GATE = 2.08
J0740_R_LOW = 11.79
J0740_R_HIGH = 15.01
BNS_R_LOW = 11.50
BNS_R_HIGH = 13.50


def parse_float(value: str) -> float | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def classify(row: dict[str, str]) -> tuple[str, str, str]:
    mass = parse_float(row.get("mass_Msun", ""))
    r_gr = parse_float(row.get("R_GR_km", ""))
    r_t = parse_float(row.get("R_torsion_km", ""))

    if mass is None or r_gr is None or r_t is None:
        return (
            "JM-D0-pending-digitization",
            "fill row",
            "Digitized mass/R_GR/R_torsion values are missing.",
        )

    delta = r_t - r_gr
    if delta >= 0:
        return (
            "JM-D1-wrong-sign",
            "deprioritize",
            "Digitized row does not show negative compactification.",
        )

    if mass >= J0740_MASS_GATE:
        if J0740_R_LOW <= r_t <= J0740_R_HIGH:
            return (
                "JM-D2-high-mass-pass",
                "promote to EOS/tidal gate",
                "Negative compactification survives the J0740 mass/radius gate for this digitized point.",
            )
        return (
            "JM-D3-high-mass-radius-fail",
            "check figure / model range",
            "High-mass point has negative compactification but misses the J0740 radius window.",
        )

    if BNS_R_LOW <= r_t <= BNS_R_HIGH:
        return (
            "JM-D4-bns-proxy-pass",
            "use as population proxy",
            "Lower-mass digitized point remains within the working BNS radius proxy.",
        )

    return (
        "JM-D5-bns-proxy-risk",
        "check tidal compatibility",
        "Lower-mass digitized point is outside the working BNS radius proxy.",
    )


def main() -> None:
    out: list[dict[str, str]] = []
    with INPUT.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            gate, action, reason = classify(row)
            r_gr = parse_float(row.get("R_GR_km", ""))
            r_t = parse_float(row.get("R_torsion_km", ""))
            delta = "" if r_gr is None or r_t is None else f"{(r_t - r_gr):.3f}"
            out.append(
                {
                    "source": row["source"],
                    "panel_or_curve": row["panel_or_curve"],
                    "EOS": row["EOS"],
                    "rotation_spec": row["rotation_spec"],
                    "rotation_value": row["rotation_value"],
                    "mass_Msun": row.get("mass_Msun", ""),
                    "R_GR_km": row.get("R_GR_km", ""),
                    "R_torsion_km": row.get("R_torsion_km", ""),
                    "Delta_R_km_computed": delta,
                    "gate": gate,
                    "action": action,
                    "reason": reason,
                }
            )

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
