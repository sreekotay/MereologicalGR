#!/usr/bin/env python3
"""
B5 torsion sensitivity calculator.

This script is deliberately modest. It does not compute a neutron-star model,
Love number, or Einstein-Cartan/Poincare-gauge solution. It computes the first
ledger sensitivity:

    ΔΛ / Λ ≈ 5 ΔR / R

holding mass and Love-number response aside.

Use this only as a triage tool for deciding which objects/effects are worth a
real EOS/Love-number/torsion-model calculation.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_DELTAS_KM = (-0.9, -0.5, 0.5, 0.9)
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "b5-neutron-star-torsion-seed.csv"
DEFAULT_OUTPUT = ROOT / "data" / "b5-neutron-star-torsion-sensitivity.csv"


@dataclass(frozen=True)
class SourceRow:
    object: str
    role: str
    radius_km: float | None
    radius_minus_km: float | None
    radius_plus_km: float | None
    framework_status: str
    notes: str


def parse_float(value: str) -> float | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def read_sources(path: Path) -> list[SourceRow]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows: list[SourceRow] = []
        for row in reader:
            rows.append(
                SourceRow(
                    object=row["object"],
                    role=row["role"],
                    radius_km=parse_float(row.get("R_mean_km", "")),
                    radius_minus_km=parse_float(row.get("R_minus_km", "")),
                    radius_plus_km=parse_float(row.get("R_plus_km", "")),
                    framework_status=row.get("framework_status", ""),
                    notes=row.get("notes", ""),
                )
            )
    return rows


def classify(delta_r_km: float, radius_km: float, radius_minus_km: float | None, radius_plus_km: float | None) -> str:
    """Heuristic triage label for first-pass ledger use only."""
    abs_delta = abs(delta_r_km)
    rel = abs_delta / radius_km

    if radius_minus_km is None and radius_plus_km is None:
        if rel >= 0.05:
            return "sensitivity-only: large enough to model, no object uncertainty"
        return "sensitivity-only: small relative shift"

    # Use asymmetric uncertainty in the direction of the shift when available.
    if delta_r_km < 0 and radius_minus_km is not None:
        sigma = radius_minus_km
    elif delta_r_km > 0 and radius_plus_km is not None:
        sigma = radius_plus_km
    else:
        sigma = max(x for x in (radius_minus_km, radius_plus_km) if x is not None)

    ratio = abs_delta / sigma if sigma else float("inf")
    if ratio >= 1.0:
        return "at/above current radius uncertainty: testable if model-clean"
    if ratio >= 0.3:
        return "below but near current uncertainty: worth modeling"
    return "hidden under current radius uncertainty"


def sensitivity_rows(sources: Iterable[SourceRow], deltas_km: Iterable[float]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for src in sources:
        if src.radius_km is None or src.radius_km <= 0:
            out.append(
                {
                    "object": src.object,
                    "role": src.role,
                    "R_mean_km": "",
                    "Delta_R_km": "",
                    "Delta_R_over_R": "",
                    "rough_Delta_Lambda_over_Lambda": "",
                    "triage": "no radius anchor: cannot compute ΔR/R",
                    "framework_status": src.framework_status,
                    "notes": src.notes,
                }
            )
            continue

        for delta in deltas_km:
            rel = delta / src.radius_km
            rough_lambda = 5.0 * rel
            out.append(
                {
                    "object": src.object,
                    "role": src.role,
                    "R_mean_km": f"{src.radius_km:.3f}",
                    "Delta_R_km": f"{delta:.3f}",
                    "Delta_R_over_R": f"{rel:.4f}",
                    "rough_Delta_Lambda_over_Lambda": f"{rough_lambda:.4f}",
                    "triage": classify(delta, src.radius_km, src.radius_minus_km, src.radius_plus_km),
                    "framework_status": src.framework_status,
                    "notes": src.notes,
                }
            )
    return out


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError("no rows to write")
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def print_markdown(rows: list[dict[str, str]]) -> None:
    headers = [
        "object",
        "R_mean_km",
        "Delta_R_km",
        "Delta_R_over_R",
        "rough_Delta_Lambda_over_Lambda",
        "triage",
    ]
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---"] * len(headers)) + "|")
    for row in rows:
        print("| " + " | ".join(row[h] for h in headers) + " |")


def main() -> None:
    sources = read_sources(DEFAULT_INPUT)
    rows = sensitivity_rows(sources, DEFAULT_DELTAS_KM)
    write_csv(DEFAULT_OUTPUT, rows)
    print_markdown(rows)
    print(f"\nWrote {DEFAULT_OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
