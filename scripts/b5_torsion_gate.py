#!/usr/bin/env python3
"""
B5 torsion compatibility gate.

Reads the first-pass torsion sensitivity CSV and assigns gate labels.
This is not a stellar-structure solver. It is a triage layer:

    proposed ΔR -> rough ΔΛ/Λ -> compatibility/work status

The goal is to keep the B5 positive search honest:
  - not any anomaly;
  - only spin/current-routed residuals that survive ordinary modeling;
  - tidal/radius implications checked immediately.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SENSITIVITY = ROOT / "data" / "b5-neutron-star-torsion-sensitivity.csv"
OUTPUT = ROOT / "data" / "b5-neutron-star-torsion-gate.csv"


def parse_float(value: str) -> float | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def classify_gate(row: dict[str, str]) -> tuple[str, str, str]:
    obj = row["object"]
    delta_lambda = parse_float(row.get("rough_Delta_Lambda_over_Lambda", ""))
    delta_r = parse_float(row.get("Delta_R_km", ""))
    triage = row.get("triage", "")

    if delta_r is None or delta_lambda is None:
        return (
            "G0-no-radius",
            "not radius-ready",
            "No radius anchor; use as spin/current stress case or mass/EOS constraint, not ΔR/ΔΛ gate.",
        )

    abs_lam = abs(delta_lambda)

    if obj == "PSR J0740+6620":
        if abs_lam >= 0.30:
            return (
                "G1-calibration",
                "worth modeling now",
                "Radius shift is below/near current uncertainty but rough tidal sensitivity is large; test against EOS + GW tidal constraints.",
            )
        return (
            "G1-calibration",
            "useful low-shift bound",
            "Smaller radius shift may hide in current radius uncertainty; still useful for bounding torsion correction.",
        )

    if obj == "GW170817-like BNS":
        if abs_lam >= 0.30:
            return (
                "G2-tidal-population",
                "must check tidal compatibility",
                "Rough tidal sensitivity is order-30%; any model with this ΔR must recompute Λ and EOS compatibility.",
            )
        return (
            "G2-tidal-population",
            "tidal sensitivity moderate",
            "Smaller shift still belongs in population/EOS check but is less immediately constraining.",
        )

    if obj == "PSR J0030+0451":
        return (
            "G3-control",
            "verify source data first",
            "Good lower-mass control, but current seed radius is a placeholder; verify before interpreting gate.",
        )

    return (
        "G4-generic",
        "triage only",
        triage or "No additional gate rule yet.",
    )


def main() -> None:
    with SENSITIVITY.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    output_rows: list[dict[str, str]] = []
    for row in rows:
        gate, action, reason = classify_gate(row)
        output_rows.append(
            {
                "object": row["object"],
                "Delta_R_km": row.get("Delta_R_km", ""),
                "rough_Delta_Lambda_over_Lambda": row.get("rough_Delta_Lambda_over_Lambda", ""),
                "gate": gate,
                "action": action,
                "reason": reason,
                "next_modeling_question": next_question(row["object"], gate),
            }
        )

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(output_rows[0].keys()))
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


def next_question(obj: str, gate: str) -> str:
    if gate == "G1-calibration":
        return "Can one EOS family fit J0740 mass/radius while allowing the torsion ΔR without violating BNS tidal constraints?"
    if gate == "G2-tidal-population":
        return "Does the torsion-induced ΔR survive full Love-number/EOS recomputation and GW tidal bounds?"
    if gate == "G3-control":
        return "After verifying J0030 radius/mass inference, does the same source lane predict a smaller/control residual?"
    if gate == "G0-no-radius":
        return "Can this object constrain spin/current scaling through mass, spin, maximum mass, or future radius/I data?"
    return "What ordinary explanation absorbs this residual, if any?"


if __name__ == "__main__":
    main()
