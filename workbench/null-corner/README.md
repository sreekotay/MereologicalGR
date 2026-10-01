# Null corner: adjacency's strip corner, and a correction to sweep F1

Referee: `null_corner.py`, 15/15.

---

## Correction to F1

Sweep F1 said adjacency has no strip corner, because its magnitude is defined through flow:
*"strip flow, keep adjacency → adjacency's magnitude does not survive."* That holds for one
object, and F1 treated three objects as one:

| object | what it needs | check |
|---|---|---|
| `h(u) = g + u⊗u`, a projection onto a congruence's rest space | a congruence `u` | (a) |
| induced metric on a surface; proper length of a spacelike curve | nothing beyond `g` and the surface | (b) |
| radar distance: light out and back, half the elapsed proper time | ordering (light) and **one** writer's flow | (c) |

Geometrically, adjacency is no more flow-indexed than flow is. Proper length along a spacelike
curve is as intrinsic as proper time along a timelike one. F1 set *proper time on a worldline*
beside *a projection*, which are not the same kind of object.

What survives of F1 is operational. In the write-view, things accrue only along timelike curves:
no writer accrues length. Every length a writer holds was assembled from ordering plus its own
flow (radar). That distance depends on which worldline does the measuring (c), and it equals
proper length only when the event is simultaneous for that writer. This is Synge's chronometry,
Bondi's k-calculus and Marzke–Wheeler. It is prior art, and it is the defensible form of F1:
**operational separation is `(A, B, radar worldline)`**.

F1's corner claim does not survive. Here is the corner.

## The corner

A null hypersurface `N`, for example a light-sheet or a horizon:

```text
pullback of g to N        diag(0, 1, 1)   degenerate, rank 2           (d)
kernel                    the generator k                              (d)
proper time along k       0               flow stripped                (d)
transverse 2-metric       invariant; no slot for u                     (d)
area along generators     evolves with the affine parameter            (e)
                          (vacuum Raychaudhuri, zero proper time elapsed)
```

The transverse adjacency survives with flow stripped, and it changes along ordering, not
along flow. This is the companion of the photon corner:

| corner | dimension | survives | stripped | forced |
|---|---|---|---|---|
| photon | 1-d null | ordering, influence | flow | PB-3: no information in flight |
| light-sheet | 3-d null | ordering (affine), transverse adjacency; E-M enters via `T_kk` focusing | flow | see below |

The strip test now separates adjacency from flow **in both directions**, for adjacency's
codimension-2 part:

```text
strip adjacency, keep flow     an isolated worldline                 -> flow survives
strip flow, keep adjacency     a null hypersurface: transverse area  -> adjacency survives
```

The 3-d spatial part stays operationally flow-indexed, as in the corrected F1. **So the open
item "no strip corner yet" (CLAIMS, README glossary, USES Parked) has a candidate: the
light-sheet.** It is a foundation exhibit, which is the kind the criterion asked for, and it is
separate from USES's surface-code witness, which remains a use-claim.

Nextness at this corner is ordering's. Causal-set link counts across a horizon, anchored near
a spacelike or null cut, come out proportional to the area. This is Dou–Sorkin, including a
non-stationary horizon, and Barton et al. 2019 for any causal horizon cut by any spacelike
hypersurface. Unanchored link counts in Lorentzian sprinklings diverge
(Bombelli–Henson–Sorkin). The finite, area-proportional count is pinned to the null surface.

## Corner test: what the compositions do on a light-sheet

| composition | on the sheet | reading |
|---|---|---|
| `time = ordering + flow` | malformed | the affine parameter is ordering with ratios and no unit |
| `frame`, `information` | malformed | each carries flow |
| `space = ordering + adjacency` | well-formed | transverse area |
| `gravity = ordering + influence + E-M` | well-formed | focusing by `T_kk` (Raychaudhuri) |
| temperature / surface gravity | malformed without an imported flow | below |

**Surface gravity.** On a Killing horizon, `κ` is fixed only by normalising the Killing field at
infinity. That normalisation is a far writer's flow, imported. On dynamical horizons there are at
least five inequivalent definitions: Hayward–Kodama, Booth–Fairhurst, Fodor et al., Nielsen–Visser,
and others. The corner reading is that the question is malformed on the sheet, and **each
definition is one imported flow**. Kodama's vector is a flow. Booth–Fairhurst depends on a
foliation. Fodor et al. normalise at an asymptotic observer. Nielsen–Visser use a
Painlevé–Gullstrand time. This is a structural retrodiction and the ground is occupied: there is
a prior "causal perspective" paper (arXiv 2304.05609, unread here), and analogue-gravity work
already treats the measured temperature as detector-relative. To check: read each definition
and confirm it imports exactly one flow and no more.

**First law.** `dM = T dS` under Killing renormalisation `k → a k`: `κ → aκ`, `M → aM`, `S`
fixed. The invariant factor is the corner's surviving adjacency, and the flow-indexed factors
scale together. This is standard. In MGR terms it says the area is the only leg of the first law
that lives on the sheet.

**Information on the sheet.** The corner forces the PB-3 analogue: **nothing is constituted
on a light-sheet**, because constitution needs flow. Three consistency checks, all on occupied
ground:

- Bousso's covariant bound puts on the left-hand side the entropy *of matter crossing* the sheet,
  which is defined in matter's own flow. The area bounds what crosses; it does not store it.
- Causal-set horizon atoms are links *crossing* the horizon, between elements off it. They are
  not elements on it, which have measure zero.
- Bousso–Porrati, *Soft hair as a soft wig*: soft variables decouple from hard dynamics. This
  gives the same verdict for soft hair, but the mechanism is only partly shared. MGR's verdict is
  stronger: it covers hard data too, because no information resides on the sheet at all.

The could-fail is a derivation of `A/4` from microstates residing **on** the null surface, with
no timelike regulator (stretched horizon) and no imported flow. The stretched horizon is then
the minimal move that restores flow. Whether Carlip-type horizon-CFT counts need stretching is
an open check, not claimed here.

## Corpus items this touches (flagged, not edited)

- **CLAIMS / README / USES:** the "no strip corner yet" line for adjacency now has a candidate.
- **frontier/pb2 §10:** *"the Sorkin coincidence … is a fixed-point artifact. Off-horizon,
  link-count tracks volume/depth, not area."* Dou–Sorkin's non-stationary case and Barton et al.
  (any causal horizon) contradict this. The area-proportional count pins at null surfaces, not at
  bifurcation fixed points.
- **CLAIMS line 118** anchors adjacency to the "energy-momentum-face". **Line 79** anchors it to
  "spatial metric on slices (ADM 3+1)". The two anchors disagree.
- **Sweep F1** is amended in place to point here.

## Even accounting

No new physics. Every forcing at the corner lands on occupied ground: area laws, the covariant
bound, surface-gravity plurality, soft-hair decoupling. The yield is structural. Adjacency gets
its corner. The area law sits at adjacency's corner as PB-3 sits at flow's. The corpus's own
parked item and one frontier claim move. The one export with a could-fail ("nothing constituted
on a light-sheet") is so far a verdict without a discriminating experiment.
