# The Ultralight Verdict Map

*Workbench — non-canonical. Numeric experiment supporting the D-lane (d1 / DR-2 / DR-3): which
gravitational meters decide which ultralight-boson masses, under what conditions, by when.
Assembled July 2026 from three independently-derived strands (PTA oscillation, black-hole
superradiance, structure formation), each re-derived from first principles before literature
compilation. Referee scripts in this directory. Not promoted; promotion requires A0 grading.*

## The principle the map tests

Interface meters (recoil, haloscope, annihilation) convict but never acquit — a null shrinks a
parameter that can shrink forever. Gravitational meters can do both, but the map splits
"coupling-blind" in two: every gravitational meter is blind to *our* couplings; only one is blind
to *theirs*.

```text
definitiveness = independence from both census columns' unknowns

interface meters:      conditional on our couplings (one-way)
structure floors:      conditional on our astrophysical modeling (IGM, galaxy-halo, equilibrium)
superradiance:         conditional on THEIR self-coupling (lambda <~ 1e-70 voids it)
PTA oscillation:       conditional on neither — the only two-column-blind instrument
```

## The map (boson mass, 1e-24 to 1e-10 eV; FDM = the dark matter unless noted)

| mass (eV) | meter | verdict | conspiracy price (what must all be wrong to evade) |
|---|---|---|---|
| < 1e-25.5 | CMB+LSS, linear | ≤5% of DM — near-unconditional | the expansion history itself |
| 1e-24 – 5e-24 | PTA (EPTA DR2) | decided: excluded at ρ_local | one convention choice (stochastic-amplitude marginalization reopens at factor-few; pulsar-term reanalysis closes ~2028) |
| 5e-24 – 1e-23 | PTA | decided ~2030 (IPTA DR3 class) | — |
| 1e-23 – 3e-23 | PTA | decided ~2035–2040 (SKA era) | structure already caps the region at ≤7–20% of DM (conditional); PTAs adjudicate the subcomponent systematics-free |
| 3e-23 – 1e-22 | **the wall** — no single two-column-blind meter, ever | exclusion side triangulates today | mixed-DM Lyα ∧ satellite counts ∧ binary-pulsar secular drifts — IGM history, galaxy-halo connection, and orbital dynamics failing coherently |
| 1e-22 – 2e-21 | Lyα + satellites + dSph kinematics | excluded as 100% of DM | three disjoint failures ∧ one shared production assumption (standard transfer function / misalignment ICs) |
| 2e-21 – 3e-19 | Rogers–Peiris Lyα; Dalal–Kravtsov UFD heating | contested — single-method each | R-P contradicted by a 2026 reanalysis (10× weaker); D-K carries a named tidal caveat, but a 2025 Schrödinger–Poisson check says its rate was conservative |
| ~1e-20 – 1e-17 | SMBH superradiance | disfavored, not excluded (grade C−/D) | selection-biased reflection spins, factor-2 masses, accretion re-spin — and the self-coupling loophole, less analyzed here |
| 1e-17 – 2e-13 | **the desert** — no gravitational meter | open | future lines (LVK continuous waves, LISA EMRI spectroscopy) ALL inherit the purity condition — one shared loophole, so added lines add sensitivity without robustness |
| 2e-13 – 6e-12 | stellar-BH superradiance (grade B+) | excluded iff gravitationally pure | their self-coupling: λ ≲ 1e-70 (f_a ≳ 1e13–1e14 GeV at the edges, ~3e11–2e12 GeV mid-window; no exclusion anywhere for f_a ≲ 3e11 GeV). Companion-tide appeals exist; 211-level exclusions resist them |

Grade notes: the stellar window rests on two independent spin methods (continuum + reflection),
an eclipsing anchor (M33 X-7), and an independent GW-population cross-check (GWTC-5:
1.7e-14–3.3e-12 eV assuming negligible self-interaction). Its edges degrade to grade C
(near-extremal spins and heaviest anchors carry the most systematics). The SMBH window's spin
sample is flux-limited with a radiative-efficiency selection toward high spin.

## Triangulation rules (how conditional meters combine)

1. N conditional exclusions with independent failure modes yield a verdict conditional only on
   the conjunction of their escape routes; the honest deliverable per region is the **conspiracy
   price** — the named list of things that must fail coherently.
2. Disjointness is audited, never assumed. The three structure meters share the FDM transfer
   function and standard misalignment initial conditions — one production-history variable under
   three "independent" bounds. (The same shared-variable discipline the README applies to
   retrodictive passes.)
3. Triangulation robustifies exclusion; it cannot manufacture discovery. Above 3e-23 eV no
   gravity-only detection channel exists at any pulsar count — the wall stands for positives.
4. A region whose available lines share one loophole (the desert: every cloud-based probe needs
   superradiance to operate) is independence-poor, not just meter-poor.

## Load-bearing numbers, re-derived and verified here

- **KR signal** (`kr_signal.py`): Ψ_c = πGρ/m² (coefficient confirmed via full linearized
  Einstein tensor, sympy, in the source strand); at 1e-23 eV and ρ = 0.4 GeV/cm³: f = 4.84 nHz,
  Ψ_c = 6.5e-16, Earth-term residual 21.3 ns; R ∝ ρ·m⁻³ exact; reach scales as
  (√(N_p·N_epoch)/σ)^(1/3) — the cube root is the wall. Correlation discrimination: monochromatic
  line at f = 2m with monopolar inter-pulsar correlation, orthogonal to the Hellings–Downs
  quadrupole in both frequency and angular structure. Self-interaction corrections O((A/f_a)²) ~
  1e-12; soliton structure only enhances the local signal.
- **Superradiance** (`sr1.py`–`sr3.py`): α = GMμ/ħc; ω < mΩ_H from horizon thermodynamics;
  Detweiler α⁹ scaling (l=m=1) implemented in full; window scan reproduces published edges to
  ~20% (stellar 5.7e-13–1.7e-11 eV at 5 M_⊙ … 9.8e-14–2.8e-12 at 30 M_⊙; SMBH 2.5e-20–8.3e-17
  across 1e6–1e9 M_⊙). Bosenova occupation N_bose ~ (n⁴/α³)(f_a/M_pl)²(M/M_pl)² reproduced
  analytically; the operative quench is perturbative level-mixing (saturation N_eq ∝ f_a²),
  which fails at larger f_a than bosenova recycling — treatments using only the latter overstate
  robustness.
- **Structure scales** (`fdm.py`): λ_dB = 12 kpc (1e-22 eV, 10 km/s); k_J = 103 h/Mpc·(m/1e-22
  eV)^{1/2} (matches the Hu–Marsh coefficient to 4%); half-mode k_{1/2} ≈ 4.5 (m/1e-22)^{4/9}
  Mpc⁻¹; the canonical core-cusp value m ~ 1e-22 eV puts power suppression exactly where the
  Lyα forest sees none — why it is dead.
- **Fractional allowance at 1e-23 eV**: ≤7% (newest mixed-DM Lyα), ≤20–30% (earlier analyses) —
  the PTA window tests a subcomponent; its unique value is locality and systematics-independence.

## Decision calendar

~2028: pulsar-term-inclusive PTA reanalysis firms the decided window · ~2030: 1e-23 eV decided
(IPTA DR3) · ~2035–2040: 3e-23 eV decided (SKA) · never (PTA-side): 3e-23–1e-22 eV — permanently
triangulation-only · LVK O5 and CW searches: subsolar fork and desert clouds (purity-conditional)
· LISA (2035+): EMRI cloud spectroscopy, same condition.

## Flags

Primary texts (arXiv, APS, ADS, INSPIRE) were egress-blocked; literature values come from search
snippets, secondary sources, and author-digitized contours (AxionLimits repository). Unverified
items are flagged in the strand reports: the NANOGrav 15-yr ρ(m) curve; the Dolan peak rate and
bosenova coefficient c₀ (order-validated only); exact satellite-count bound values; recent
(2025–2026) preprints not yet peer-reviewed. The forecast dates carry an empirical degradation
factor (~8× in residual, calibrated to reproduce today's published reach) for red noise, the GWB
foreground, and timing-model fitting.

Key sources: Khmelnitsky–Rubakov (1309.5888); Porayko+ 2018 (PRD 98, 102002); EPTA DR2 VI (PRL
131, 171001); Hu+ 2026 (2605.02172); NANOGrav 15-yr new physics (ApJL 951, L11); stochastic-
amplitude treatment (PRD 109, 055017); Baryakhtar+ 2021 (PRD 103, 095019); Witte–Mummery
(2412.03655); Hoof+ 2024 (2406.10337); GWTC-5 spin search (2607.01317); Cyg X-1 (Science 2021;
2102.09093); Iršič+ 2017 (1703.04683); Rogers–Peiris 2021 (PRL 126, 071302); Liu+ 2026
(2606.06969); Dalal–Kravtsov 2022 (2203.05750); May+ 2025 (2509.02781); Hložek+ (CMB/LSS ULAs);
binary-pulsar resonances (Blas–López Nacir–Sibiryakov class).
