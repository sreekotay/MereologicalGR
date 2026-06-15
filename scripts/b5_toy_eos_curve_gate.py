#!/usr/bin/env python3
"""
B5 toy EOS curve gate.

Cheap gate before real modeling. It asks which toy mass-radius curve shapes survive:
J0740 radius + BNS population radius + torsion correction sign/magnitude + source dependence.
This is not an EOS calculation.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURVES = ROOT / "data" / "b5-toy-eos-curves.csv"
OUTPUT = ROOT / "data" / "b5-toy-eos-curve-gate.csv"

J0740_LOW_KM = 11.79
J0740_HIGH_KM = 15.01
BNS_LOW_KM = 11.50
BNS_HIGH_KM = 13.50

DELTAS_HIGH_SOURCE_KM = (-0.9, -0.5, 0.0, 0.5, 0.9)
BNS_SOURCE_FACTORS = (0.0, 0.25, 0.5, 1.0)


def classify(r14: float, r21: float, delta: float, bns_factor: float, r_j0740: float, r_bns: float) -> tuple[str, str]:
    pass_j = J0740_LOW_KM <= r_j0740 <= J0740_HIGH_KM
    pass_b = BNS_LOW_KM <= r_bns <= BNS_HIGH_KM

    if pass_j and pass_b:
        if delta < 0 and r21 >= 13.8 and bns_factor <= 0.5:
            return "best-negative-lane", "promote"
        if delta < 0:
            return "negative-compatible", "model"
        if delta == 0:
            return "baseline-compatible", "control"
        if delta > 0 and r_bns > BNS_HIGH_KM - 0.1:
            return "positive-tidal-risk", "deprioritize"
        return "positive-compatible", "low-priority"

    if pass_j and not pass_b:
        return "bns-fail", "do-not-model-first"
    if not pass_j and pass_b:
        return "j0740-fail", "do-not-model-first"
    return "both-fail", "do-not-model-first"


def main() -> None:
    rows: list[dict[str, str]] = []
    with CURVES.open(newline="", encoding="utf-8") as f:
        for curve_row in csv.DictReader(f):
            curve = curve_row["curve"]
            r14 = float(curve_row["R14_GR_km"])
            r21 = float(curve_row["R21_GR_km"])
            notes = curve_row["notes"]

            for delta in DELTAS_HIGH_SOURCE_KM:
                for bns_factor in BNS_SOURCE_FACTORS:
                    r_j0740 = r21 + delta
                    r_bns = r14 + delta * bns_factor
                    gate, action = classify(r14, r21, delta, bns_factor, r_j0740, r_bns)
                    rows.append(
                        {
                            "curve": curve,
                            "R14_GR_km": f"{r14:.2f}",
                            "R21_GR_km": f"{r21:.2f}",
                            "Delta_R_high_source_km": f"{delta:.2f}",
                            "BNS_source_factor": f"{bns_factor:.2f}",
                            "R_J0740_after_km": f"{r_j0740:.2f}",
                            "R_BNS_after_km": f"{r_bns:.2f}",
                            "J0740_pass": str(J0740_LOW_KM <= r_j0740 <= J0740_HIGH_KM).lower(),
                            "BNS_pass": str(BNS_LOW_KM <= r_bns <= BNS_HIGH_KM).lower(),
                            "gate": gate,
                            "action": action,
                            "notes": notes,
                        }
                    )

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
