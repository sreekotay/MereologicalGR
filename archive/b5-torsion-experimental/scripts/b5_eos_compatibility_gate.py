#!/usr/bin/env python3
"""
B5 EOS/tidal compatibility gate.

This script turns the first ΔR sensitivity table into a rough compatibility check.
It is intentionally conservative and explicitly assumption-driven.

It asks two first-pass questions:

1. For J0740, if the observed radius is R_obs and a torsion correction is ΔR,
   what GR/EOS baseline radius would be required?

       R_GR_required = R_obs - ΔR

   Is that baseline still inside the current J0740 radius interval?

2. For the population/BNS placeholder, if a generic radius R_ref is shifted by ΔR,
   does the shifted radius remain inside a rough working BNS/EOS radius window?

This is not a real EOS or Love-number calculation. It is a gate that says which
signs/magnitudes should be modeled first.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SENSITIVITY = ROOT / "data" / "b5-neutron-star-torsion-sensitivity.csv"
ASSUMPTIONS = ROOT / "data" / "b5-eos-compatibility-assumptions.csv"
OUTPUT = ROOT / "data" / "b5-eos-compatibility-gate.csv"


def parse_float(value: str) -> float | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def load_assumptions() -> dict[str, float]:
    values: dict[str, float] = {}
    with ASSUMPTIONS.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            parsed = parse_float(row["value"])
            if parsed is not None:
                values[row["key"]] = parsed
    return values


def classify_j0740(delta_r: float, a: dict[str, float]) -> tuple[str, str, str, float]:
    r_obs = a["J0740_R_mean"]
    required = r_obs - delta_r
    low = a["J0740_R_low_68"]
    high = a["J0740_R_high_68"]
    bns_high = a["BNS_R_working_high"]

    if required < low or required > high:
        return (
            "J0740-radius-fail",
            "outside J0740 radius interval",
            "The required GR/EOS baseline radius falls outside the current J0740 working interval.",
            required,
        )

    if required > bns_high:
        return (
            "J0740-pass-but-tidal-tension-risk",
            "model with stiff/EOS tidal caution",
            "J0740 can absorb this torsion correction, but the implied baseline radius is high relative to the rough BNS working ceiling.",
            required,
        )

    return (
        "J0740-pass",
        "model first",
        "J0740 can absorb this torsion correction within the working radius interval; next check EOS and BNS tidal compatibility.",
        required,
    )


def classify_bns(delta_r: float, a: dict[str, float]) -> tuple[str, str, str, float]:
    r_ref = a["Generic_R_reference"]
    shifted = r_ref + delta_r
    low = a["BNS_R_working_low"]
    high = a["BNS_R_working_high"]

    if shifted < low:
        return (
            "BNS-low-radius-risk",
            "check lower-radius EOS compatibility",
            "The shifted population radius falls below the rough working BNS floor; may be too compact unless EOS/posterior allows it.",
            shifted,
        )
    if shifted > high:
        return (
            "BNS-high-radius-risk",
            "check tidal exclusion first",
            "The shifted population radius exceeds the rough working BNS ceiling; positive ΔR of this size may be tidal/EOS constrained.",
            shifted,
        )
    return (
        "BNS-window-pass",
        "compatible at triage level",
        "The shifted population radius remains inside the rough working BNS window; still requires full Λ/k2/EOS recomputation.",
        shifted,
    )


def main() -> None:
    a = load_assumptions()
    rows: list[dict[str, str]] = []

    with SENSITIVITY.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            obj = row["object"]
            delta_r = parse_float(row.get("Delta_R_km", ""))
            if delta_r is None:
                continue

            if obj == "PSR J0740+6620":
                gate, action, reason, r_value = classify_j0740(delta_r, a)
                value_label = "R_GR_required_km"
            elif obj == "GW170817-like BNS":
                gate, action, reason, r_value = classify_bns(delta_r, a)
                value_label = "R_shifted_population_km"
            else:
                continue

            rows.append(
                {
                    "object": obj,
                    "Delta_R_km": f"{delta_r:.3f}",
                    value_label: f"{r_value:.3f}",
                    "rough_Delta_Lambda_over_Lambda": row.get("rough_Delta_Lambda_over_Lambda", ""),
                    "compatibility_gate": gate,
                    "action": action,
                    "reason": reason,
                    "next_question": next_question(obj, delta_r, gate),
                }
            )

    # Normalize variable radius columns so the CSV has stable headers.
    fieldnames = [
        "object",
        "Delta_R_km",
        "R_GR_required_km",
        "R_shifted_population_km",
        "rough_Delta_Lambda_over_Lambda",
        "compatibility_gate",
        "action",
        "reason",
        "next_question",
    ]
    normalized: list[dict[str, str]] = []
    for row in rows:
        normalized.append({field: row.get(field, "") for field in fieldnames})

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(normalized)

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


def next_question(obj: str, delta_r: float, gate: str) -> str:
    if obj == "PSR J0740+6620":
        if delta_r < 0:
            return "Can a high-baseline-radius EOS fit J0740 while surviving BNS tidal constraints after a negative torsion radius shift?"
        return "Can an ordinary-radius EOS fit J0740 if torsion adds positive radius without over-expanding BNS population radii?"
    if obj == "GW170817-like BNS":
        if gate == "BNS-high-radius-risk":
            return "Does positive torsion ΔR violate BNS tidal/radius posteriors after full Love-number recomputation?"
        if gate == "BNS-low-radius-risk":
            return "Does negative torsion ΔR make the population too compact for high-mass support or observed tidal constraints?"
        return "Does the torsion-shifted radius remain compatible once k2 and EOS response are recomputed?"
    return "What ordinary model absorbs this residual, if any?"


if __name__ == "__main__":
    main()
