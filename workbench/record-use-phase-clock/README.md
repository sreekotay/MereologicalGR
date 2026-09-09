# Record-use continuation: phase clocks and incomplete channel descriptions

## Why this run

The question is whether refusing to identify a record with its use continues to expose different physical dependencies, rather than merely redescribing the QEC/Szilard comparison. This run adds a specified phase-clock task, follows an apparently harmless record compression, and then tests whether a classical record channel is itself a sufficient description when a coherent system is present.

Base revision: `c2c7815b50d96b3b24494bb8391666ea4588d453`. A4 section 6 (metrology), B8 (clock interferometry), and B10 (marker/eraser operations) were read at this revision. The previous chat workbench, `MGR_causal_use/RESEARCH_NOTE.md`, supplies the two-task starting point. The formulas needed from it are rederived below, so this directory is self-contained. This is not the separate one-clock/two-metric investigation; it follows the user's later record-with-use prompt.

No A/B/C/D claim is edited here. This is an exploratory workbench, not a new ontology or a claim that every application must produce another independent functional.

## 1. Physical setup before assigning value to a record

Fix a fair binary variable S and the classical channel K(y|s) for the record actually available at the task's point of use. The record can include a delivery, reliability, or erasure flag. It is independent of the unknown phase parameter introduced below.

Define

\[
p_y=P(S=1|Y=y),\quad q_y=1-2p_y,\quad r_y=|q_y|,\quad e_y=(1-r_y)/2.
\]

The causal requirement is unchanged: information introduced by an independently variable source cannot be used outside the source's causal future. A record used in final statistical processing need only arrive before that processing, not necessarily before the sensor is measured. Signals can be null; neither this access condition nor the receiver's clock requires proper-time accrual on the signal carrier. The geometry supplies precedence and the proper-time parameter; the matter Hamiltonian, preparation, controls and costs remain explicit physical inputs.

For the comparisons below, all required data are available at the stipulated point of use. Varying K is not secretly changing a deadline or supplying an extra record for free.

## 2. The two existing tasks, with their boundaries

### Logical recovery

An arbitrary unknown logical qubit has undergone either I or Z according to S. This is the earlier I/X model in a rotated basis. No extra syndrome is available at the declared corrected handoff. Conditional on y,

\[
\mathcal N_y(\rho)=(1-p_y)\rho+p_y Z\rho Z.
\]

The maximal entanglement fidelity on the maximally mixed input is

\[
F_e^*=\sum_y P(y)\max(p_y,1-p_y)
      =\frac{1+\mathbb E r_y}{2}.
\]

This is optimal over deterministic CPTP recovery, not just Pauli guesses. Expanding each recovery Kraus operator as aI+bX+cY+dZ, trace preservation implies that the total squared coefficient magnitude is one; the entanglement fidelity is (1-p) sum|a|^2+p sum|d|^2, at most max(p,1-p). The selected Pauli reaches it. This is a specific handoff fidelity, not a general QEC architecture threshold or preservation of all output observables.

### Reversible gross feedback work

A binary Szilard system has equal initial compartment volumes, a bath at T, and an ideal work reservoir. With posterior probability p of the occupied side, a final compartment fraction v yields expected work

\[
W(v)/(k_BT)=p\ln(2v)+(1-p)\ln(2(1-v)).
\]

Differentiation gives v=p. Averaging,

\[
w\equiv W_{\rm rev}/(k_BT\ln2)
=\mathbb E\,g(r_y),\qquad
 g(r)=1-h_2((1-r)/2).
\]

This is a reversible gross-work ceiling. Preparation, transmission, processing, memory reset, finite-time dissipation and net cyclic accounting are not included. This distinction is essential, not a post-hoc exception. See S3.

## 3. A phase-clock use of the same record

Prepare a qubit clock in |+>. Its fixed internal Hamiltonian is H=(hbar omega/2)Z. An unknown proper-time offset u imprints theta=omega u. A Z phase kick occurs according to S. The same channel K supplies the available error record.

The conditional sensor state is

\[
\rho_{\theta,y}
=\tfrac12[I+q_y(\cos\theta\,X+\sin\theta\,Y)].
\]

The accessible complete state is the classical-quantum state

\[
\rho^{YQ}_\theta=\sum_y P(y)|y\rangle\langle y|\otimes\rho_{\theta,y}.
\]

No phase information is carried by P(y) itself. Solving the symmetric logarithmic derivative equation gives, in each block,

\[
L_y=q_y(-\sin\theta\,X+\cos\theta\,Y),\qquad
\tfrac12(\rho_yL_y+L_y\rho_y)=\partial_\theta\rho_y.
\]

Consequently the phase quantum Fisher information is

\[
\boxed{\mathcal J_Y=\mathbb E(q_y^2)=\mathbb E(r_y^2).}
\]

The proper-time Fisher information is omega^2 times this quantity. Clock-off (omega=0) removes time sensitivity without removing the record or causal precedence.

This result is not merely an unattained state diagnostic. Around a calibrated operating phase theta_0, measure the sensor along the equatorial tangent (-sin theta_0, cos theta_0). The two outcome probabilities are

\[
P(m|y,\theta)=\tfrac12[1+m q_y\sin(\theta-\theta_0)],\quad m=\pm1.
\]

At theta_0 their classical Fisher information is q_y^2. Retaining the pairs (y,m) attains the joint QFI locally. For n independent uses the usual local, regular, asymptotic precision is governed by n omega^2 J; this is not a global phase-unwrapping guarantee, an autonomous-clock construction, or a finite-sample unbiased-estimation promise. The phase reference and local calibration are held fixed and not thermodynamically priced. The distinction between QFI and attainable measurement is standard and important (S1,S2).

Thus the three functions were not selected to look different: Pauli recovery, reversible piston motion and a specified phase-sensitive measurement produced them.

## 4. A compression that is lossless for one use and lossy for another

Keep only the maximum-posterior correction label B=b(Y). Ties may be assigned arbitrarily (or randomized independently). Within each label the signed posterior q_y has a fixed sign, so

\[
\mathbb E|\mathbb E(q_Y|B)|=\mathbb E|q_Y|.
\]

Therefore this compression preserves the optimal logical fidelity exactly. It does not generally preserve phase precision:

\[
\boxed{\mathcal J_Y-\mathcal J_B
=\mathbb E\operatorname{Var}(q_Y|B).}
\]

The equality is the conditional variance identity, now obtained as the lost precision of the physical clock task. In the symmetric flagged-channel case it reduces to Var(r).

The corresponding reversible work loss is

\[
w_Y-w_B=I(S;Y|B)\quad\text{in bits}.
\]

Both losses are nonnegative, but different functions. No new noise dynamics was introduced.

Example: a flag says the bit is exact in 80% of trials and uninformative in 20%. In an uninformative trial the reported correction bit is a fair coin. Discard the flag and retain only that bit.

| Record available | F_e* | w | Phase J |
|---|---:|---:|---:|
| Bit and reliability flag | 0.9 | 0.8 | 0.8 |
| Correction bit alone | 0.9 | 0.531004406410719 | 0.64 |

The discarded flag was redundant for the optimal recovery score, not redundant for the complete quantum channel or every subsequent task. With free processing, a richer record can emulate a poorer one. A net engine can still prefer the cheaper record after actual costs are included; that is a different objective, not a violation of this ordering.

## 5. Even the two previous task values together do not determine the third

Construct channels by first selecting a publicly reported flag j with probability a_j, independently of S, then transmitting S through a binary symmetric channel with error e_j=(1-r_j)/2. The output is (j,b). Every distribution of r in [0,1] below is thereby a physical classical channel.

Channel B: r=1/4 or 3/4, each with probability 1/2.

Let

\[
w_*=[g(1/4)+g(3/4)]/2,\qquad
x=[w_*-g(1/2)]/[1-2g(1/2)].
\]

Channel A: r=0,1/2,1 with probabilities x,1-2x,x. Numerically x=0.10003738859752188, so all probabilities are valid. The equality of the first two task values is by analytic construction, not empirical fitting; it is a sufficiency test.

| Channel | F_e* | w | Phase J |
|---|---:|---:|---:|
| A | 0.75 | 0.251000776937719 | 0.300018694298761 |
| B | 0.75 | 0.251000776937719 | 0.3125 |

Exactly, J_A=1/4+x/2 and J_B=5/16. A matched pair under the two previous objectives still differs under the phase-clock objective.

This does not imply every new objective supplies an independent functional. For example, binary squared-error prediction also uses E[q^2]. The space of retained physical distinctions is not counted by listing scalar objectives.

## 6. Follow the coherent-availability fork: the channel can itself be incomplete

The preceding section fixed a *classical* record channel. To test its sufficiency under coherent composition, now use a different, explicitly quantum instrument. Do not identify its calibration bit with a simultaneously definite classical path in the coherent experiment.

Let

\[
D_\eta(\rho)=\tfrac{1+\eta}{2}\rho+
\tfrac{1-\eta}{2}Z\rho Z,\quad 0\leq\eta\leq1,
\]

and define two outcome maps

\[
\mathcal I_+^\eta(\rho)=D_\eta(\rho)/2,\qquad
\mathcal I_-^\eta(\rho)=ZD_\eta(\rho)Z/2.
\]

These have an elementary physical realization: initialize a marker in |0>, correlate it to the signal with CNOT, dephase the marker by D_eta, then measure marker X. Each map is completely positive and their sum is trace preserving.

For *every input state* and every eta:

\[
\operatorname{Tr}\mathcal I_\pm^\eta(\rho)=1/2,\qquad
\mathcal I_+^\eta+\mathcal I_-^\eta=D_0.
\]

Thus both the entire classical-outcome channel and the unconditional signal channel are identical. Nevertheless the joint outcome-conditioned state is not. For an equatorial phase input,

\[
\boxed{\mathcal J_{\text{signal+label}}=\eta^2,\qquad
\mathcal J_{\text{signal only}}=0.}
\]

At eta=1, the random outcome labels whether the state is rho or Z rho Z; applying the corresponding correction restores the full signal. At eta=0, each branch is already dephased, and the same label cannot restore phase. The output record has equal marginal statistics but unequal physical relations to the retained signal.

No signalling is hidden here. A marker operation alone never changes the unconditional signal. Conditional phase use requires either bringing the label into the readout's causal past or processing both records in their common future. Joint coherent control can also restore the eta=1 encoded signal: after CNOT, apply marker H followed by controlled-Z. It maps rho tensor |0><0| to rho tensor |+><+| without measurement. The workbench verifies this on arbitrary mixed inputs. No universal irreversible write is required for that operation.

This is the familiar quantum-eraser/instrument distinction made explicit (S4), not a proposed new erasure phenomenon. It reconnects with B10 and the earlier controlled-channel work: identical marginals do not specify their usable composition. There is no assertion of free physical erasure or zero cost to the control apparatus.

## 7. What remains open here

The phase-clock comparison gives another noninterchangeable use of the same classical record. The instrument example asks a further question: when is the record channel an adequate retained description at all?

The particular changes above are now pinned. MAP compression preserves one recovery objective but loses a calculable confidence variance for phase estimation. A full classical-outcome channel and a full unconditional signal channel together can still omit the correlation needed for conditional quantum use.

What has not been established is a universal minimal description for all composites, a universal timeliness law, a thermodynamic cost from the word 'write', or a new law beyond ordinary quantum theory. The geometrical causal-access condition remains necessary, not a generator of these task-specific Hamiltonians and probabilities. Conversely, the known ingredients do not make the new comparison a mere choice of synonyms: the physical operations fixed the functions before their equivalence was tested.

The question stays open at the new boundary: which reductions remain adequate when the subsequent operation is allowed to use coherent relations, costs, or memory that the original task never used? This workbench supplies explicit cases, not a termination of that inquiry.

## 8. Verification

Run:

```sh
python -m pip install numpy scipy
python -W error checks.py --output results.json
```

24 grouped checks pass. They include direct spectral QFI, explicitly attained classical FI, Bell-state recovery, independent piston optimization, 120 random record channels and their compressions, the analytically matched pair, 60 random inputs to explicit marker circuits, and coherent uncomputation. Results include the environment and fixed random seed. Numerical checks corroborate the analytic identities; they are not empirical tests or proofs of general continuum claims.

## Sources and lineage

Repository at the base revision:

- A4 section 6: the parameter-register/metrology comparison; its warning not to equate a Fisher bound with an implemented protocol.
- B8: proper-time accumulation, internal clock dynamics and readout as distinct dependencies. This run uses its own elementary Hamiltonian rather than importing B8's displayed visibility formula.
- B10: marker, coincidence readout and the distinction between local marker operations and changes in an unconditional signal.
- Prior conversation workbench: causal access plus binary logical recovery versus reversible Szilard feedback. The present note states all required assumptions and proofs anew.

Primary references (known physics; no priority claim):

S1. S. L. Braunstein and C. M. Caves, *Statistical distance and the geometry of quantum states*, Phys. Rev. Lett. 72, 3439 (1994), DOI 10.1103/PhysRevLett.72.3439. Optimal measurements and quantum Fisher information. Publisher abstract consulted.

S2. O. E. Barndorff-Nielsen and R. D. Gill, *Fisher information in quantum statistics*, arXiv:quant-ph/9808009v4. Full HTML consulted; distinguishes local bounds, measurement attainability and the operational task. Also W. Zhong et al., *Fisher information under decoherence in Bloch representation*, arXiv:1212.0917, Phys. Rev. A 87, 022337 (2013); abstract consulted. The qubit formula used here is derived directly above and independently checked, not asserted on the basis of the abstract.

S3. T. Sagawa and M. Ueda, *Second Law of Thermodynamics with Discrete Quantum Feedback Control*, arXiv:0710.0956v3, Phys. Rev. Lett. 100, 080403 (2008). Feedback work and controller accounting; abstract consulted. The piston optimization here is self-contained.

S4. X.-S. Ma et al., *Quantum erasure with causally disconnected choice*, PNAS 110, 1221-1226 (2013), DOI 10.1073/pnas.1213201110. Retrieved primary-source excerpt distinguishes which-way versus conjugate marker readout and conditional fringes. The eta-instrument calculation here is a self-contained finite model, not a reproduction of the experiment.

S5. M. Zych et al., *Quantum interferometric visibility as a witness of general relativistic proper time*, arXiv:1105.4531v2, Nat. Commun. 2, 505 (2011). Abstract consulted for the B8 lineage. The present task estimates an encoded proper-time offset; it is not that paper's full interferometer.
