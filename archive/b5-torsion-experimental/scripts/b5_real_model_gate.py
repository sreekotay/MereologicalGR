#!/usr/bin/env python3
"""
B5 real torsion model gate.

Consumes hand-extracted rows from real torsion neutron-star papers and assigns the
next action. This is deliberately qualitative until numeric tables/curves are extracted.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "b5-real-torsion-model-rows.csv"
OUTPUT = ROOT / "data" / "b5-real-torsion-model-gate.csv"


def gate(row: dict[str, str]) -> tuple[str, str, str]:
    source = row["source_routing_grade"]
    sign = row["sign_grade"]
    mag = row["magnitude_grade"]
    high_mass = row["high_mass_grade"]
    lam_i = row["lambda_I_grade"]

    if sign == "strong" and mag == "strong" and high_mass == "unknown":
        return (
            "G1-extract-curves",
            "extract numeric mass-radius rows first",
            "Sign and magnitude match the promoted lane, but high-mass and tidal gates need real curves.",
        )

    if source == "strong" and sign == "strong" and high_mass == "risk":
        return (
            "G2-source-clean-high-mass-risk",
            "extract Mmax and branch viability first",
            "Source routing is clean, but reported maximum-mass reduction may break the J0740/J0952 gate.",
        )

    if lam_i == "missing":
        return (
            "G3-needs-lambda-I",
            "derive or request Lambda/I outputs",
            "The model cannot be compared to tidal/moment-of-inertia gates yet.",
        )

    return (
        "G4-hold",
        "hold as background",
        "Not enough match to the promoted B5 lane yet.",
    )


def main() -> None:
    out: list[dict[str, str]] = []
    with INPUT.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            g, action, reason = gate(row)
            out.append(
                {
                    "model": row["model"],
                    "reference": row["reference"],
                    "gate": g,
                    "action": action,
                    "reason": reason,
                    "next_extraction": next_extraction(row["model"], g),
                }
            )

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


def next_extraction(model: str, gate_name: str) -> str:
    if model == "Jockel-Menger-2024":
        return "Extract rotation rate, M, R_GR, R_torsion, Delta_R, central density, mass shift; check whether M>=2.08 survives."
    if model == "Vashistha-Gannouji-Ganguly-2026":
        return "Extract coupling branch, DD2 Mmax_GR, Mmax_torsion, R(M), Delta_R(M), binding energy, central density."
    return "Extract mass-radius and source-scaling rows."


if __name__ == "__main__":
    main()
