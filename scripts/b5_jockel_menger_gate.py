#!/usr/bin/env python3
"""
Gate Jockel-Menger extraction rows against the B5 promoted lane.

Promoted lane:
  negative, source-scaled compactification
  with high-mass and BNS/tidal compatibility still to be checked.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "b5-jockel-menger-extraction.csv"
OUTPUT = ROOT / "data" / "b5-jockel-menger-gate.csv"


def gate(row: dict[str, str]) -> tuple[str, str, str]:
    source_lane = row["source_lane"]
    status = row["framework_status"]
    delta = row.get("reported_delta_R_km", "")
    high_mass = row["high_mass_status"]
    bns = row["bns_tidal_status"]

    if source_lane == "macroscopic angular momentum" and delta:
        if high_mass == "unknown" or bns == "unknown":
            return (
                "JM-G1-promote-extract-curves",
                "extract figures/tables next",
                "This row matches sign and magnitude, but high-mass and BNS/tidal gates are still unknown.",
            )
        return (
            "JM-G1-promoted",
            "run full gates",
            "Sign/magnitude/source lane is ready for compatibility scoring.",
        )

    if status == "formal-clean-but-hidden":
        return (
            "JM-G2-formal-hidden",
            "keep as formal note",
            "Intrinsic-spin lane is framework-clean but reported as observationally negligible.",
        )

    if status == "sign-support":
        return (
            "JM-G3-sign-support",
            "use as qualitative support",
            "General torsion trend supports negative compactification, but lacks source/magnitude rows.",
        )

    return (
        "JM-G4-hold",
        "hold",
        "No promoted-lane match yet.",
    )


def main() -> None:
    out: list[dict[str, str]] = []
    with INPUT.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            g, action, reason = gate(row)
            out.append(
                {
                    "row_id": row["row_id"],
                    "source_lane": row["source_lane"],
                    "reported_delta_R_km": row.get("reported_delta_R_km", ""),
                    "gate": g,
                    "action": action,
                    "reason": reason,
                    "next_required_data": next_required(row),
                }
            )

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


def next_required(row: dict[str, str]) -> str:
    if row["source_lane"] == "macroscopic angular momentum":
        return "rotation rate; mass; R_GR; R_torsion; Delta_R; central density; mass shift; EOS/polytrope; M>=2.08 check"
    if row["source_lane"] == "microphysical spin":
        return "parameter assumptions showing why realistic spin is negligible; useful as null/formal constraint"
    return "source-separated numeric rows"


if __name__ == "__main__":
    main()
