# Temporal-Spatial Coupling in Gravitational Lensing: A Reinterpretation of Dark Matter Observations
**Matthew Lukin Smawfield**
Version: v0.8 (Tortola)
First published: 19 December 2025 · Last updated: 30 September 2026
DOI: 10.5281/zenodo.17982540

---

## Abstract

Standard gravitational lensing analysis relies on the
*Isochrony Axiom*—the implicit assumption that the observed image
represents a synchronous spatial snapshot of the source. For evolving
sources, this approximation breaks down in the presence of conformal
metric couplings, creating a "temporal composite" image. This projects
temporal depth onto the spatial plane, generating a
*temporal-composite response* contribution sourced by the underlying
*Temporal Shear* field gradient—arising from gradients in the
scalar field's continuous spatial profile (*Temporal Topology*,
TEP)—whose propagating component is confined to the millisecond
(conservative-baseline) window while its chronometric component is
bounded by the ratio of differential delay to source-evolution time
and is accessible only through time-domain or variability-dependent
observables.
Within TEP, *Phantom Mass* is the excess dynamical mass
inferred when the scalar force on matter trajectories is analyzed
as gravitating mass. Its test is the mass difference inferred from
dynamics and lensing at matched radii and with compatible mass
models. At fixed gravitational metric $g_{\mu\nu}$, the conformal
factor does not alter photon paths; it does not prevent the scalar's
stress-energy from curving $g_{\mu\nu}$. For the SN Refsdal lens
benchmark in Paper 19, that backreaction supplies
$\kappa_\phi\sim10^{-5}$, roughly $2\times10^3$ below the
dark-matter-level convergence required there; the bound is not a
cosmological no-go theorem. Disformal transport and source-evolution
reconstruction are separately bounded on their tested paths. The
temporal-composite term vanishes for a stationary backlight and
cannot supply the observed CMB lensing deflection. Paper 18's
Planck-lensing likelihood retains a standard cold-dark-matter fluid
with $\Omega_{\rm cdm}h^2\simeq0.1155$; its agreement is therefore
not a CDM-free lensing prediction of TEP. The intended ontology
requires a source-independent metric potential from the stated TEP
fields and baryons that reproduces CMB, galaxy, and cluster lensing
without that fluid. This closure remains open. The present paper's
established scope is its bounded time-domain and
reconstruction-channel tests, not a completed replacement for the
dark-matter lensing potential.

Screening of the shear response in high-acceleration lensing environments is governed by the abstract environmental operator $\mathcal{S}_\Sigma(\mathcal{E})$, which pins the incremental field gradient where the ambient landscape is steep while the Temporal Topology persists. The same operator sets the environment-dependence of the phantom mass, which is accordingly largest in isolated, diffuse low-acceleration systems.

*Keywords:* gravitational lensing – dark matter – modified
gravity – cosmology: theory – galaxies: kinematics and dynamics –
temporal equivalence principle

## 1. Introduction

## 1.1 The Anomaly of the Dark Sector

The existence of dark matter, inferred from gravitational lensing (Walsh et al. 1979), cluster dynamics (Zwicky 1933), and cosmic microwave background observations (Planck Collaboration 2020), represents a significant challenge in modern physics. Despite decades of increasingly sensitive searches, no dark matter particle has been directly detected (Schumann 2019), and tensions persist between cosmological observations at different scales (Riess et al. 2022; Di Valentino et al. 2021). The prevailing paradigm assumes that these anomalies indicate the presence of an invisible *substance*. The question arises whether the apparent mass discrepancy can be resolved by relaxing the *Isochrony Axiom*—the assumption that temporal delays across an image are negligible.

Modified Newtonian Dynamics (Milgrom 1983) and its relativistic extensions (Bekenstein 2004; Skordis & Złośnik 2021) have challenged the dark matter hypothesis by modifying the gravitational force law. However, these approaches typically retain the standard metric assumptions regarding light propagation and causality. The present analysis interrogates a deeper, often unstated assumption underlying the interpretation of all astronomical signals: the nature of simultaneity in image formation.

## 1.2 The Isochrony Axiom

Gravitational lensing is conventionally treated as the spatial deflection of light rays by mass. Standard practice already models geometric and Shapiro time delays and, for variable sources, the light curves themselves. The closure examined here is narrower and operates one level deeper, in the reconstruction:

**Principle:**

**The Isochrony Axiom:** The closure in which static lens reconstructions treat the source surface-brightness distribution as effectively time-independent across the differential emission-time structure relevant to the reconstruction, after modeled propagation delays have been applied — so that source clocks, photon transport, and observer clocks are mapped onto a single general-relativistic time coordinate.

Stated this way, the axiom is not a claim that lensing analyses ignore time delays. It is the assumption that the residual emission-time structure, once known delays are removed, carries no further information — that the reconstruction may proceed as if the source were synchronous. TEP-GL names this closure and tests its breakdown.

While this axiom serves as a necessary simplification for standard analysis, it breaks down when the differential lookback time across an image becomes comparable to the evolutionary timescale of the source. Standard analysis corrects for the finite speed of light in the arrival time of signals (lookback time) but has typically neglected the differential arrival-time and clock-transfer structure across the image plane. In the presence of generalized metric couplings, this approximation fails. Gravitational lensing is fundamentally an *arrival-time* phenomenon. Images form at the stationary points of the Fermat potential, which encodes the total light-travel time (Blandford & Narayan 1986). In standard General Relativity, the difference in arrival times between images is attributed solely to geometric path differences and the Shapiro delay caused by mass. However, if the coupling between matter and gravity involves a second metric—specifically one that affects matter-clock rates or light-cone tilts—the arrival times of photons can be decoupled from the geometric definitions of "mass" used in standard GR.

If the Isochrony Axiom is violated, an observed "image" is not a snapshot of the source at one moment, but a *temporal composite*. Photons arriving at the same detector time may have left the source at significantly different emission times. For an evolving source, this temporal smearing is mathematically indistinguishable from a spatial distortion (convergence and shear) in a static reconstruction. The projected amplitude is bounded by the ratio of differential delay to source-evolution time—\(\lesssim10^{-7}\) for galaxy sources and identically zero for static sources—so the channel's domain is temporally structured sources, not the static-source lensing excess.

## 1.3 The Interpretive Bifurcation

Consider two mathematically equivalent interpretations of the same Fermat potential surface, distinguished only by their treatment of simultaneity:

**Interpretation A (Standard Framework):** Assumes the Isochrony Axiom. An Einstein ring is analyzed with apparent convergence \(\kappa_{\rm obs}\) exceeding what the visible baryonic mass can produce. A dark matter halo with mass \(M_{\rm DM} = M_{\rm obs} - M_{\rm baryons}\) is inferred. The "dark matter" is treated as an unseen substance required to explain the lensing geometry.

**Interpretation B (TEP Framework):** Rejects the Isochrony Axiom. The observed image is recognized as a *temporal composite*: photons arriving simultaneously at the detector left the source at different emission epochs, with differential emission structure set by the propagating delay surface (the gravitational Fermat surface plus the bounded disformal deformation) and with the conformal sector contributing the endpoint-determined clock-transfer field read by the reconstruction. For an evolving source, this temporal depth projects onto the image plane as an apparent spatial distortion, bounded in amplitude by the delay/evolution-time ratio. The differential temporal-transfer structure across the lens is computed, and apparent excess convergence in such reconstructions is identified as the signature of temporal-field gradients \(\nabla(\Delta \tilde{\tau})\) in the lens environment. Where the projection applies, unmodeled time can bias reconstruction at the bounded amplitude; where it does not, any lensing excess is real deflection requiring a gravitational-metric potential. Its CDM-free origin is not established by the temporal-composite mechanism.

**The Critical Point:** The frameworks diverge where the source is static. For evolving sources, temporal projection can contribute apparent spatial structure at the bounded amplitude and the distinction is settled by time-domain, variability-dependent, and multi-epoch observables. For a stationary backlight there is no source-evolution projection: light responds to the gravitational metric sourced by the baryons and any scalar stress. The matched dynamical–lensing mass difference tests the extra force on matter, but reproducing the absolute lensing signal without an independent CDM fluid remains a separate requirement.

This bifurcation illustrates that the inference of particulate dark matter is contingent, in part, on the Isochrony Axiom for temporally structured sources, while for the static-source excess it sets a sharp falsifiable boundary: where the shear supplies the dynamical anomaly, lensing should find less mass than dynamics.

## 1.4 The Temporal Equivalence Principle (TEP)

The Temporal Equivalence Principle (TEP), introduced in a companion paper (Smawfield 2025a), represents a shift in fundamental perspective, replacing the standard geometric framework with an operational one:

**Principle:**

**Temporal Equivalence Principle (TEP):** The operative physical observables in any non-local measurement are the proper-time intervals registered on physical clock worldlines, together with the phase, frequency, and arrival-time transport connecting those clock events along null signal paths. Under TEP, "gravity" includes the phenomenology of differential clock-transfer structure. The decomposition of this structure into "spatial curvature" (mass) and "temporal dilation" (metric coupling) is gauge-dependent; only the total integrated transport is invariant.

Under TEP, the central question is not "how much mass is bending the light?" but "what is the total emission-to-reception clock-transfer history associated with the signal?" In the conformal-only limit of a two-metric theory, null cones are preserved, meaning the "speed of light" is unchanged, yet the *rate* of proper time accumulation varies. This creates a disconnect between the "gravitational metric" \(g_{\mu\nu}\), which carries the gravitational field dynamics and the tensor sector, and the causal "matter metric" \(\tilde{g}_{\mu\nu}\), to which all nongravitational matter — test bodies, atomic clocks, and photons alike — couples universally.

The same distinction extends to cosmology. In the canonical TEP interpretation the underlying spatial scale is static, \(a_m=1\), while observed redshift is carried by the conformal clock map \(A_{\rm clock}=(1+z)^{-1}\) (Athens, Paper 26; Thika, Paper 27). Quantities conventionally written as a cosmological scale factor or Hubble evolution may therefore be used as observational or reference variables without implying physical expansion of space. TEP-GL adopts this correspondence: the lensing-sector reconstruction examined here is the local multipath analogue of the cosmological temporal-to-spatial reconstruction treated in those papers.

## 1.5 Redefining the Dark Sector

TEP's intended ontology does not posit particulate dark matter. It must nevertheless account for the real lensing and dynamical observations attributed to it. Temporal Shear can modify dynamical mass inference, and source-dependent clock transfer can affect time-domain reconstructions; neither statement by itself supplies the gravitational-metric potential required by cluster and CMB lensing. This paper tests those distinct channels and records where the CDM-free lensing calculation remains open. It is demonstrated that:

- **The tested deflection channels are bounded:** Conformal rescaling leaves null paths unchanged at fixed \(g_{\mu\nu}\), while scalar stress can curve that metric. For the SN Refsdal configuration, Paper 19 obtains \(\kappa_\phi\sim10^{-5}\), about \(2\times10^{3}\) below the required lensing convergence; the tested disformal delay is also subdominant (Steps 56, 61, 63). The dynamical–lensing mass difference tests Temporal Shear in matter trajectories but cannot substitute for the measured lensing potential. The source-evolution temporal-composite correction is bounded for evolving galaxies and does not supply CMB lensing; no CDM-free cosmological deflection solution is established here.

- **GW170817 is a differential constraint:** The multi-messenger constraint \(|c_{\gamma}-c_g|/c \lesssim 10^{-15}\) is explicitly reanalyzed. It is shown that this bounds only the *disformal* (cone-tilt) component of the coupling. The *conformal* component, which governs clock rates and drives the phantom-mass phenomenology, is not directly constrained by photon–graviton differential-propagation bounds because conformal transformations preserve null cones — and, symmetrically, it carries exactly zero propagated differential delay by the same invariance, its observable content being the common-mode endpoint calibration and reconstruction-space clock-transfer map. It remains indirectly constrained by PPN, source-screening, gravitational-redshift, clock-comparison, and equivalence-principle tests.

- **Regime I vs. Regime II:** The conservative baseline (Regime I) is the disformal multipath deformation at its GW170817-bounded normalization (Δτ_B = ½∫ D(∂_n̂φ)² dl ≲ 0.2 s per 2 Mpc), the even-parity channel of the same B(φ) sector the holonomy program bounds on the odd channel — so that the stated <0.1 ms lensed-FRB null threshold operates as a bound on the disformal normalization itself. Regime II collects the reconstruction-space and time-domain content of the conformal sector — endpoint clock calibration, chronometric bookkeeping, and the source-dependent temporal-composite response — whose propagated differential content is identically zero and whose image-space amplitude is bounded by the delay/evolution-time ratio. Neither regime supplies the absolute dark-matter-level spatial deflection in the tested lens geometry. A CDM-free gravitational-metric potential is required in addition to the phantom-mass comparison before the lensing sector can close.

Relaxing the isochronous reconstruction identifies bounded, testable temporal contributions to mass inference; it does not make measured photon deflection a reconstruction artifact. A CDM-free alternative must additionally predict the gravitational-metric potential traced by CMB, galaxy and cluster lensing.

TEP does not posit an alternative dark substance. Its proposed replacement of particulate dark matter therefore requires the same action and matter distribution to explain both the dynamical and optical channels. The present temporal-composite calculations bound one source-dependent contribution, while the required source-independent lensing amplitude remains an open quantitative test.

This paper does not deny any of the observations attributed to dark matter. It distinguishes real lensing, dynamical extra-force inference and source-dependent temporal reconstruction so that none is counted as an explanation of the others without an observable-level transfer calculation.

The claim-discipline framework for the TEP corpus, including the scope limitations of canonical precision tests, is established in TEP-EXP (Paper 9).

## 2. Theoretical Framework

### 2.1 The Two-Metric Postulate

The gravitational field dynamics and the matter sector are posited to be
governed by distinct metrics related by a scalar field \(\phi\). The
*Gravitational Metric* \(g_{\mu\nu}\) carries the gravitational field
dynamics and the tensor sector: it has Einstein–Hilbert form and gravitational
waves propagate on its null cones. All nongravitational matter — including
massive test bodies, atomic clocks, and electromagnetic fields — couples
universally to the *causal Matter Metric* \(\tilde{g}_{\mu\nu}\), on
which nongravitational dynamics, signals, and quantum phases evolve. This
universal coupling is the foundational TEP structure (Jakarta, Paper 0);
environmental screening can render matter-frame trajectories consistent with
the GR limit to high precision. The general two-metric relation
(Bekenstein 1993) is adopted:

\begin{equation} \label{eq:gl_matter_metric}
\tilde{g}_{\mu\nu} = A^2(\phi) g_{\mu\nu} + B(\phi)\nabla_\mu\phi
\nabla_\nu\phi
\end{equation}

Here, \(\tilde{g}_{\mu\nu}\) is the metric on which all nongravitational
matter propagates, and \(g_{\mu\nu}\) is the metric carrying the gravitational
field dynamics. The function \(A(\phi)\) defines the *Conformal Sector*
(isotropic scaling of proper time/length) and \(B(\phi)\) defines the
*Disformal Sector* (anisotropic stretching along field gradients).
TEP introduces the temporal field as the additional physical degree of
freedom: all physical rulers and clocks are built from matter coupled to
\(\tilde{g}_{\mu\nu}\), while the temporal field's stress-energy and
strong-field operators backreact on the Einstein-frame geometry
\(g_{\mu\nu}\). The structure is therefore not a reinterpretation of
measurement alone; sufficiently strong temporal structure induces genuine
geometric backreaction (Bahrain, Paper 28), and it is that backreaction —
together with the disformal sector — which carries any modification of
null-trajectory lensing.

**Principle:**

#### Box 2.0: Sector Dictionary — Three Projections of One Temporal Field

TEP-GL distinguishes three observational projections of the same temporal
field. They are complementary and must not be collapsed into a single
optical effect. This distinction organizes the remainder of the paper.

**Conformal open-path transport** \(A(\phi)\): changes
the matter-clock transfer associated with geometrically distinct
source–observer paths. This can alter arrival-time, distance,
velocity, and mass *reconstructions* without changing the
unparameterized null trajectories.

**Geometric optical response** \(g_{\mu\nu}[\phi]\),
\(B(\phi)\): scalar backreaction on the Einstein-frame metric,
together with any active disformal contribution, changes the optical
tidal matrix and therefore produces genuine angular convergence and
shear.

**Temporal-composite response:** for an evolving or
moving source, a path-dependent emission-time map produces an
additional source-dependent image distortion.

Accordingly, *Phantom Mass* is the apparent non-particulate dark
component generated by the combined temporal-field geometry and its
reconstruction under the Isochrony Axiom:

\begin{equation} \label{eq:gl_phantom_decomposition}
M_{\rm phantom}^{\rm TEP}
= \underbrace{M_{\rm rec}^{A}}_{\text{chronometric reconstruction}}
+ \underbrace{M_{\rm opt}^{g[\phi],B}}_{\text{coherent optical}}
+ \underbrace{M_{\rm TC}}_{\text{source-dependent}} .
\end{equation}

These are not three unrelated mechanisms substituted for particulate dark
matter. They are three observational projections of one dynamical
temporal field. Standard analysis combines them into a single inferred
mass distribution precisely because it assumes a universal isochronous
mapping between source clocks, photon transport, and observer clocks.
The three terms also sit on different carriers, which the remainder of
the paper keeps explicit: \(M_{\rm opt}^{g[\phi],B}\) is a propagated
optical contribution (backreacted geometry and the bounded disformal
deformation); \(M_{\rm TC}\) propagates only through the same
carriers — the conformal contribution to a propagated emission-time
map is identically zero; and \(M_{\rm rec}^{A}\) lives entirely in
reconstruction space, entering through the endpoint-determined
clock-transfer field and the inference degeneracy (mass-sheet and
normalization class) rather than through any propagated delay.

**Principle:**

#### Box 2.1: Relation to Established Scalar-Tensor Theories

TEP is a specific two-metric scalar–tensor effective field theory,
distinguished by the universal coupling of all nongravitational matter to
a single causal metric and by its dynamical-proper-time interpretation.
Its covariant operators draw on established scalar–tensor constructions,
while its operational ontology and observable sector decomposition are
specific to TEP. The correspondences are:

**Brans-Dicke Theory:** With \(B=0\), \(A(\phi)
= e^{\beta_A\phi/M_{\text{Pl}}}\), and the corresponding kinetic and
potential choice, the conformal sector contains a Brans–Dicke-like
limit in the Jordan frame, with \(\beta_A\) related to the
Brans–Dicke parameter \(\omega_{BD}\). The correspondence is a limit
of the conformal sector, not an identity of the full theory.

**Horndeski and Beyond:** Higher-derivative
scalar-tensor theories (Horndeski, DHOST) provide candidate
microscopic completions for the gradient-dependent branch of
\(\mathcal{S}_\Sigma(\mathcal{E})\). TEP-GL does not commit to a
specific completion; the canonical operator is defined at the
theory level independently of any particular Lagrangian.

**Screening and Temporal Topology:** The core TEP
framework formulates screening through the environmental operator
\(\mathcal{S}_\Sigma(\mathcal{E})\) acting on the Temporal Shear
\(\Sigma_\mu\), a continuous spatial profile. Imported
modified-gravity screening mechanisms are not part of the TEP
ontology; the screening object is \(\mathcal{S}_\Sigma(\mathcal{E})\)
alone.

**DHOST Theories:** Degenerate Higher-Order
Scalar-Tensor theories extend Horndeski by imposing a degeneracy
condition that eliminates the additional propagating mode, rather
than by keeping the field equations manifestly second-order. TEP is
compatible with this broader class but does not require it.

**Key Distinction:** TEP's distinguishing content is the
universal causal-metric coupling together with the
*observational interpretation* it licenses — specifically, the
recognition that conformal coupling creates a "temporal composite" image
whose residual timing structure a standard reconstruction absorbs as
mass. Individual covariant operators are drawn from established
scalar–tensor constructions; the sector dictionary, the universal
coupling, and the resulting lensing phenomenology are specific to TEP.

### 2.2 The Chronometric Lensing Framework

TEP-GL lensing contains three projections of one temporal field: coherent
optical response through scalar backreaction and any permitted disformal
contribution; conformal open-path chronometric reconstruction; and the
source-dependent temporal-composite response.

#### 1. The Static Clock-Transfer Contribution (Chronometric Reconstruction)

The conformal clock sector modifies the relation between accumulated
matter-frame time and the geometry reconstructed under an isochronous
model. The associated effective clock-transfer contrast is:

\begin{equation} \label{eq:gl_static_delay}
\Delta \tilde{\tau}_{\rm static} = \frac{1}{c} \int (A(\phi) - 1)\,
dl
\end{equation}

In the phenomenological isochronous reconstruction used here, this is represented as a source-independent correction to the inferred arrival-time surface. In multipath configurations, it is therefore operationally
degenerate with the mass normalization inferred from multipath timing,
distance, and joint image–delay reconstruction. The angular positions of
Einstein rings and major arcs remain governed by the optical geometry.

The expression above is a matter-clock transfer functional evaluated on a
timelike clock congruence associated with the path; it is not a photon
observable, and for photons its differential content vanishes identically.
That vanishing is a statement about a restricted net observable — the
static conformal contribution to an inter-image arrival-time contrast —
not that the photon is unaffected while traversing the topology: the
locally measured frequency rises descending into each well and falls
climbing out, asymmetric crossings slice residuals to the intervening
field difference, and lapse-geometry dwell through each structure accrues
monotonically. Only the frequency bookkeeping of a strictly static
conformal field telescopes to the endpoints.
Two equivalent statements fix this. First, null cones are conformally
invariant (Axiom 1, Appendix A.1): \(A(\phi)\) drops out of the null
transport equation, so the coordinate travel time along any fixed spatial
path is identical in \(\tilde{g}_{\mu\nu}\) and \(g_{\mu\nu}\), and the only
conformal content in an observed arrival time is the endpoint clock ratio —
a common-mode factor for all images of one system. Second, the underlying
Temporal Shear is an exact one-form, \(\Sigma_\mu = \nabla_\mu\ln A\): its
open-path integral is endpoint-determined, so the shear-sector contribution
to any path contrast between rays joining the same source and observer
cancels algebraically, before screening is even applied. The dedicated
strong-lensing transport pipeline confirms the result directly: the exact
additional static-conformal inter-image residual is \(0.0\) d (TEP-LENS,
Paper 19, step_56). The functional is therefore retained in a
sharply delimited role: it is the chronometric reconstruction map — the
field of clock-rate contrasts that an isochronous lens model would
misassign to mass-sheet normalization, distance, or time-delay
calibration if it were read as propagating emission-time structure — and
it bounds, rather than supplies, the arrival-time residual. Genuine
path-dependent null delay beyond the GR geometry arises only through
gravitational backreaction in \(g_{\mu\nu}\), the disformal sector
\(B(\phi)\), or another explicitly derived non-exact contribution: pure
multiplication by \(A^2(\phi)\) does not bend a photon onto a new null
trajectory and does not shift its arrival time relative to any other
photon on the same endpoints. The observable lensing signal in the
conformal sector is therefore a reconstruction-space discrepancy — the
difference between the clock-transfer field an isochronous GR lens model
assumes and the field the temporal landscape provides — rather than a
propagated delay or a refraction of null geodesics.

#### 2. The Source-Evolution Response (Temporal Lensing)

While the static term reshapes the clock-transfer field read by an
isochronous reconstruction, the gradient of the differential delay field
\(\nabla(\Delta \tilde{\tau})\) acts as a "shutter"
that modulates the arrival time of photons from different parts of the
source. For a source with evolution or motion, this creates a
*temporal-composite response*:

\begin{equation} \label{eq:gl_temporal_shear}
\gamma^{\rm TC} \propto \left(\frac{\partial I}{\partial t} +
\vec{v}_s \cdot \nabla I\right) \nabla(\Delta \tilde{\tau})
\end{equation}

The nomenclature follows the canonical corpus convention: Temporal
Shear denotes the field gradient \(\Sigma_\mu \equiv \nabla_\mu \ln
A(\phi)\), which generates the path-dependent clock-transfer field, whereas
*temporal-composite response* \(\gamma^{\rm TC}\) denotes the observable
source-dependent image response to that field. The two must not be conflated:
the former is a property of the temporal field, the latter of the
observation.

This source-evolution response supplies a source-dependent phantom-mass
component — an apparent mass that can fluctuate with source type. It operates
as a re-ordering of emission epochs rather than a deflection of rays, and for
galaxy
sources it is bounded by the ratio of differential delay to
source-evolution time at \(\lesssim 10^{-7}\) in shear, far below the
observed lensing excess. (See Section 3 for the full derivation).

Together, these two mechanisms constitute the TEP framework: the
clock-transfer contribution may contribute to the phenomenology
conventionally attributed to the dark matter halo, and the
source-evolution response may account for part of the apparent
"complexity" of
substructure. Any genuinely new null-trajectory bending beyond the
conformally related geometry must arise through gravitational
backreaction in \(g_{\mu\nu}\), a non-negligible disformal
contribution, or another explicitly derived part of the coupled field
solution.

### 2.3 Operational Axioms: The TEP Framework

The TEP framework rests on four foundational axioms. These are not
approximations or perturbative corrections to General Relativity; they
constitute a complete operational framework for interpreting gravitational
phenomenology. They are adopted as *primary postulates* from which
observational consequences are derived:

**Principle:**

**Axiom 1 (Causal Universality):** In the Conformal Limit
(\(B=0\)), the null cones of \(g_{\mu\nu}\) and \(\tilde{g}_{\mu\nu}\)
are identical. Photons and gravitational waves follow the same null
geodesics. No "speed of light" difference exists in this limit.
*This axiom is exact, not approximate.*

**Axiom 2 (Proper Time Primacy):** The fundamental
observables in any timing measurement are the proper-time intervals
\(\Delta \tilde{\tau}\) registered on physical emitter and receiver clock
worldlines, together with the phase, frequency, and arrival-time transport
connecting those clock events along \(\tilde{g}\)-null signal paths.
Coordinate time differences \(\Delta t\) are not observables; they are
inferred quantities dependent on the metric model. Null proper time along
the photon trajectory is identically zero (Jakarta); wherever this paper
refers to accumulated path time, the phrase denotes the operational
clock-transfer functional associated with the null path, not proper time
experienced by the photon.
This axiom establishes clock-registered proper time as the irreducible
physical observable; all other timing quantities are derived.

**Axiom 3 (Non-local temporal transport):** TEP admits two
distinct classes of non-local timing observable.

**(a) Synchronization holonomy:** A genuinely closed,
direction-reversing transport loop can exhibit residual non-closure only
when the transport connection contains non-exact structure, such as the
disformal \(B(\phi)\) sector. In the pure conformal limit, the
\(A(\phi)\) contribution is exact and its residual closed-loop integral
vanishes.

**(b) Differential path transport:** Distinct open propagation
paths may accumulate different temporal-transfer corrections. In
gravitational lensing, two images correspond to two open paths
\(\gamma_i, \gamma_j\), and the observable is the differential
transport residual
\[
\Delta\mathcal{T}_{ij}^{\rm resid}
= \left[\mathcal{T}[\gamma_i] - \mathcal{T}[\gamma_j]\right]
- \left[\mathcal{T}_{\rm GR}[\gamma_i] - \mathcal{T}_{\rm GR}[\gamma_j]\right],
\]
where \(\mathcal{T}[\gamma] \equiv \Delta\tilde{\tau}[\gamma]\) is the
time-transport functional. This is an open-path blind-prediction
residual, not a closed-loop synchronization holonomy. Two structural
properties delimit it. First, because each image has a single observed
arrival time, algebraic closure of measured pairwise delays around image
triplets vanishes identically: the axiom alters the relation between
lens geometry and observed arrival time without violating the algebraic
identity among the observed arrival times. Second, in the pure conformal
sector the residual itself vanishes identically, because
\(\Sigma_\mu = \nabla_\mu\ln A\) is an exact one-form and its open-path
integrals are endpoint-determined (§3.1.3); a nonzero
\(\Delta\mathcal{T}_{ij}^{\rm resid}\) is therefore a signature of
non-exact transport — the disformal sector or scalar backreaction — not
of the conformal clock-transfer map.

This axiom distinguishes open-path differential residuals (the GL
observable) from closed-loop holonomy (the domain of triangle
time-transfer and direction-reversing experiments), and is consistent
with the refined strong-lensing formulation in TEP-LENS (Paper 19).

**Measurement Protocol for the GL Observable.**
The lensing-sector observable is not algebraic delay closure. It is a
blind-prediction residual. For each image pair \((i,j)\), compare the
observed delay \(\Delta t_{ij}^{\rm obs}\) with the pre-specified GR
lens-model prediction \(\Delta t_{ij}^{\rm GR}\):
\[
R_{ij} = \Delta t_{ij}^{\rm obs} - \Delta t_{ij}^{\rm GR}.
\]
TEP predicts that these residuals should correlate with
temporal-transport tracers such as projected potential depth,
magnification, variability timescale, or other lens-environment proxies.
Algebraic closure of observed pairwise delays is not a TEP
discriminator, because it vanishes identically whenever each image has a
unique arrival time.

**Systematic Error Budget:** Several astrophysical
systematics can produce apparent residuals that must be distinguished
from true temporal-transport effects:

**Lens Model Degeneracies:** The mass-sheet degeneracy
and source-position transformation can bias predicted delays. These
affect the *predicted* delay (from the model), not the
*observed* delay. The test compares observed delays against
model predictions, and systematic lens-model error must be
propagated into the residual uncertainty.

**External Convergence:** Line-of-sight structure
acts approximately as an external mass-sheet transformation,
rescaling the Fermat-potential and time-delay normalization. If
omitted, it can generate coherent biases in \(R_{ij}\). Each lens
must therefore marginalize over \(\kappa_{\rm ext}\) and the
associated mass-sheet uncertainty before testing for a TEP residual.

**Microlensing:** Stellar microlensing in the lens
galaxy can shift apparent arrival times by hours to days. However,
microlensing is stochastic and uncorrelated between images; over an
ensemble of lens systems, microlensing-induced residuals should
average to zero with RMS scaling as \(1/\sqrt{N}\).

**Host Galaxy Delays:** Differential extinction or
scattering in the host can introduce chromatic delays, but TEP's
temporal-transport residual is achromatic. Chromatic residual
patterns indicate astrophysical contamination, not metric effects.

**Discriminator:** True temporal-transport residuals should
produce a *systematic* non-zero regression coefficient or
covariance between \(R_{ij}\) and a pre-specified temporal-transport
predictor, using a fixed image-pair ordering and hierarchical
marginalization over lens-model degeneracy, \(\kappa_{\rm ext}\),
microlensing, and host-galaxy delays, while astrophysical
systematics produce *random* residuals that average to zero
across multiple systems. An unconditional mean could cancel even when a
real path-dependent correlation exists. The correlation is the correct
TEP discriminator.

**Axiom 4 (Screening and Temporal Topology):** Screening
manifests as a continuous spatial profile (Temporal Topology) governed
by the non-linear superposition of field gradients (Temporal Shear),
suppressing the Temporal Shear where the ambient time-gradient is
steep (weak-field: high-acceleration environments)
while leaving cosmology accessible to dynamics. The suppression of
local Temporal Shear in deep potential environments continuously
reduces

\begin{equation}
\Sigma_\mu^{\rm obs} = \mathcal{S}_\Sigma(\mathcal{E})\,\Sigma_\mu .
\end{equation}

Channel-specific PPN responses are evaluated only after this
environmental projection is applied. Existing multi-messenger
constraints (e.g., GW170817) are interpreted within the standard
framework that assumes a single metric governs all sectors; in the TEP
framework, these constraints apply to specific parameter combinations
(primarily the disformal sector) and do not constitute blanket
exclusions of two-metric effects.
This axiom establishes that environmental suppression is a
geometric property of the field's spatial profile, not a binary
boundary condition, and that constraints derived under
Isochrony-assuming frameworks must be re-derived operationally
within TEP before being applied as exclusions.

These axioms are mutually consistent and together define the TEP
interpretation of gravitational phenomenology. They replace the implicit
Isochrony Axiom of standard lensing analysis with an explicit dynamical-time
framework.

**The Hidden Closure in Standard Practice:** In addition to the
Isochrony Axiom, most observational inference quietly assumes that time
transport is globally integrable: after correcting for known effects
(Sagnac, Shapiro, troposphere, etc.), a single global time coordinate can be
assigned such that closed-loop synchronization holonomy vanishes.
Operationally, this is the step that licenses the non-local conversion \(d =
c\,t\) and the inference “timing residual \(\Rightarrow\) mass residual.” In
TEP, this closure is not assumed; Axiom 3 treats open-path differential
residuals as the primary observables, while true synchronization holonomy
requires direction-reversing closed loops or non-exact transport structure.

### 2.4 Conformal vs. Disformal Phenomenology

The distinction between the two sectors is critical for interpreting
multi-messenger constraints, and it rests on a fundamental distinction
between *Single-Path* and *Multipath* measurements.
Furthermore, it necessitates a redefinition of the "speed of light":

**Conformal Sector (\(A(\phi)\)):**

**Geometry:** Preserves angles and null cones.
\(\tilde{g}_{\mu\nu}k^\mu k^\nu = A^2(\phi) g_{\mu\nu}k^\mu k^\nu = 0\).

**Local Invariance vs. Global Variability:** Local
\(c\) remains invariant (measured as \(299,792,458\) m/s by
any local clock; Paper 0, Theorem 2). What varies globally is
not any speed of propagation, but the inferred ratio between
spatial separation and matter-clock transfer registered between
endpoints along extended paths. Because the rate of proper
time accumulation \(d\tilde{\tau} = A(\phi) d\tau_g\) varies
with location, the clock transfer associated with traversing a
fixed spatial interval depends on the scalar field value: a
timelike clock transported through a halo well (\(A < 1\))
accumulates less matter-frame time than the ambient rate, and
one transported through a void (\(A > 1\) relative to ambient)
accumulates more. For photons this path-integrated content is
not observable at all — the null condition is conformally
invariant — and the conformal sector enters the photon sector
only through the endpoint clock ratio, the same channel that
carries cosmological redshift (Paper 0, §2.2). Any "variable
speed of light" language is therefore shorthand for an
operational endpoint ratio inferred under a universal-clock
assumption, never a change in local propagation.

**Single-Path Physics (GW170817):** Photons and
gravitational waves from the exact same source coordinate follow
the *same* null geodesic. Any temporal distortion
\(A(\phi)\) along this path is common-mode. The signals do not
diverge because they share the same history.

**Multipath Physics (Lensing):** Gravitational
lensing involves light rays taking *different* paths
around a mass distribution. These paths traverse different
regions of the scalar field \(\phi(\vec{x})\), but photon
transport along them is conformally invariant: the conformal
differential clock-transfer contrast is a reconstruction-space
field, not a propagated delay, and it generates the chronometric
component of the Phantom-Mass signature only as an inference
degeneracy. Genuine propagated differential delay is carried by
scalar backreaction (absorbed by lens models as mass) and by the
GW170817-bounded disformal deformation; coherent optical
convergence and shear arise through the same two channels.

**Disformal Sector (\(B(\phi)\)):**

**Geometry:** Tilts null cones. The effective speed
of light differs from the speed of gravity: \(c_{\gamma} \neq
c_g\).

**Observables:** Differential arrival times between
species, constrained by GW170817 to \(|c_{\gamma}-c_g|/c
\lesssim 10^{-15}\) for the path-averaged monopole.

### 2.5 The "Phantom Mass" Mechanism

Standard lensing reconstruction solves for a mass distribution
\(\Sigma(\vec{\theta})\) that reproduces the observed image distortions.
This reconstruction assumes the Isochrony Axiom: \(I_{\rm obs}(\vec{\theta}) =
I_{\rm src}(\vec{\beta})\). However, in the TEP framework, the observed image
at a given observation time \(t_{\rm obs}\) is the source evaluated at a
shifted effective time:

\begin{equation} \label{eq:gl_composite_image}
I_{\rm obs}(\vec{\theta},\, t_{\rm obs})
= I_{\rm src}\!\left[
\vec{\beta}_{\rm opt}(\vec{\theta}),\;
t_{\rm obs} - \Delta T_{\rm eff}(\vec{\theta})
\right],
\end{equation}

where \(\Delta T_{\rm eff}(\vec{\theta})\) is the effective emission-time
map along the line of sight at image position \(\vec{\theta}\), and
\(\vec{\beta}_{\rm opt}(\vec{\theta})\) is the optical ray map generated by
the scalar-backreacted and disformal geometry. The propagating content of
\(\Delta T_{\rm eff}\) decomposes into the ordinary geometric-plus-Shapiro
Fermat surface already contained in any GR lens model, the disformal
multipath deformation bounded by GW170817 (\(\lesssim 0.2\) s per \(2\) Mpc
halo path; Box 3.2), and the common-mode endpoint clock ratio; the
conformal sector contributes no path-dependent term, because null transport
is conformally invariant (§3.1.1) and its clock-transfer map is
endpoint-determined (§2.2). For a finite exposure over
\([t_1, t_2]\), the recorded image is the time-averaged quantity:

\begin{equation} \label{eq:gl_composite_image_exposure}
\bar I_{\rm obs}(\vec{\theta})
= \frac{1}{\Delta t_{\rm exp}}
\int_{t_1}^{t_2}
I_{\rm src}\!\left[
\vec{\beta}_{\rm opt}(\vec{\theta}),\;
t - \Delta T_{\rm eff}(\vec{\theta})
\right] dt .
\end{equation}

For a spatially varying temporal field, \(\Delta T_{\rm eff}\) varies
across the image plane through its propagating components — the
gravitational Fermat surface and the disformal deformation — while its
conformal clock-transfer content varies only in reconstruction space. If
the source has temporal variability (secular
evolution, rotation, or fluctuations) on the timescale of
\(\nabla_\theta (\Delta T_{\rm eff})\), the finite-exposure average smears
the recorded image.

**The Equivalence:** A gradient in the emission-time map
across an image
is mathematically equivalent to a shearing of the source frame. To a static
observer assuming isochrony, this "temporal shear" is indistinguishable from
the "gravitational shear" caused by mass. Thus, for temporally structured
sources,
purely temporal structure is misinterpreted as "Phantom Mass" (dark
matter). The channel is bounded at \(\lesssim 10^{-7}\) for galaxy sources and
vanishes for static sources; it is a source-dependent discriminator, not
the carrier of the observed static-source lensing excess.

#### One Quantity, Two Measurements

Phantom Mass is not a separate mechanism in each observable channel; it is
one quantity — the mass a standard analysis infers because it does not
model the TEP temporal field. It enters through two routes: in dynamics,
where the Temporal Shear supplies extra apparent acceleration
(\(M_{\rm ph}^{\rm dyn}\)); and in reconstruction, where the differential
source-clock history of an evolving source is read as spatial structure
(\(M_{\rm ph}^{\rm recon}\), zero for static sources). Each channel is
inferred independently: \(M_{\rm ph}^{\rm dyn} \equiv M_{\rm dyn}^{\rm GR} -
M_{\rm baryon}\) and
\(M_{\rm ph}^{\rm lens} \equiv M_{\rm lens}^{\rm GR} - M_{\rm baryon}\).
Comparing them is then a *test* of Phantom Mass rather than its
definition — the empirical question is
\(M_{\rm ph}^{\rm dyn} \overset{?}{=} M_{\rm ph}^{\rm lens}\). Particle dark
matter requires equality, since the same substance sources both inferences.
Under the present action the Temporal Shear acts on matter trajectories but
not on photon paths, so the prediction is
\(M_{\rm ph}^{\rm dyn} > M_{\rm ph}^{\rm lens}\), with the difference largest
where the shear is active — the isolated, low-acceleration systems where
\(\mathcal{S}_\Sigma \to 1\). This phantom-mass consistency test is the
framework's decisive dark-sector check: agreement would bound the Temporal
Shear's share of the dynamical anomaly; a positive difference is a signature
no particulate model reproduces.

### 2.6 Two Regimes of TEP-GL

**Principle:**

**Box 1: The Two Observational Regimes**

The TEP-GL framework operates in two distinct regimes, distinguished by
the magnitude of the differential clock-transfer residual
\(\Delta\tilde{\tau}\) across the lens:

---

**Regime I: the conservative baseline**

**Physical carrier:** The disformal multipath
deformation. For photons on the matter metric the phase velocity is
\(v_{\rm ph}/c \simeq 1 - \tfrac{1}{2}D(\partial_{\hat{n}}\phi)^2\)
with \(D \equiv B/A^2\) (Paper 0, App. B); a differently routed
image pair traverses different \(\nabla\phi\) structure, so the
inter-image residual is
\(\Delta\tau_B = \tfrac{1}{2}\int D(\partial_{\hat{n}}\phi)^2\,dl\),
evaluated at the GW170817-bound normalization
(\(D(\partial_{\hat{n}}\phi)^2 \lesssim 2\times10^{-15}\)
path-averaged). The deformation is direction-even
(\((\partial_{\hat{n}}\phi)^2\) is invariant under
\(\hat{n}\to-\hat{n}\)), so it appears as a propagation residual
between distinct paths rather than a same-path holonomy — the
even-parity channel of the same \(B(\phi)\) sector the corpus's
holonomy program bounds on the odd/non-exact channel. On the
corpus's weak-field branch \(B(\phi)\simeq B_0\varphi^2\) (Paper 0,
§2.2), the product \(D(\partial_{\hat{n}}\phi)^2\) carries the
quadratic field-depth suppression, so the stated ceiling is the
saturation value of the GW170817 bound rather than the envelope's
expectation on weak-field halo paths: the corpus-calibrated
admissible normalization lies parametrically below it. The
falsification threshold therefore bounds the normalization — not
merely tests an assumed saturation — and the conversion into a
constraint on the dimensionful \(B_0\) belongs to the same open
normalization map as the corpus's B-sector bookkeeping (Paper 0,
Appendix E).

**Constraint basis:** GW170817 bounds the path-averaged
monopole \(|c_{\gamma}-c_g|/c \lesssim 10^{-15}\); the conformal
sector contributes exactly zero propagated inter-image delay by
null-cone invariance (§3.1.3).

**Delay scale:** \(\Delta\tilde{\tau} \sim
10^{-3}\text{--}1\) s (milliseconds to seconds) on halo scales —
\(\Delta\tau_B \lesssim 0.2\) s per \(2\) Mpc halo path at the
bound — the only propagating inter-image delay the theory supplies.

**Primary observables:** Time-domain signatures in
rapidly varying sources—lensed FRBs, GRBs.

**Dark matter status:** TEP is a
*precision systematic* in time-delay cosmography, not a
wholesale DM replacement.

**Falsification:** Null detection of achromatic timing
residuals at < 0.1 ms on a \(2\) Mpc halo path bounds the
path-averaged disformal product
\(D(\partial_{\hat{n}}\phi)^2 \lesssim 5\times10^{-19}\) —
\(\sim 3.5\) orders of magnitude below the GW170817 level —
probing between the corpus-calibrated envelope and the saturated
ceiling: the same \(B(\phi)\) instrument as the holonomy
program, applied to the even-parity multipath channel.

---

**Regime II: the bookkeeping-inclusive case**

**Assumption (Sector Decoupling):** GW170817 constrains
only differential disformal coupling; common-mode conformal temporal
structure is not directly constrained by it, though it remains bounded
by clock, PPN, and redshift channels (see Axiom 4).

**Clock-transfer scale:** \(\Delta\tilde{\tau} \sim
1\text{--}10\) years, driven by the conformal factor \(A(\phi)\)
integrated over halo scales (Mpc). This is the
*reconstruction-space* scale — the reconstruction-space
clock-transfer map of §2.2 — not a propagated photon delay; the
conformal contribution to any inter-image arrival-time residual is
exactly zero, and the propagating differential channel remains the
disformal carrier at the ms–s level.

**Primary observables:** The reconstruction-space and
time-domain content of the conformal sector — chronometric
bookkeeping, endpoint clock-transfer maps, and the source-dependent
temporal-composite response — together with the
*dynamical–lensing mass difference* (which measures the
shear-induced phantom mass) in matched spatial observables. At
fixed gravitational metric the conformal factor does not deflect
photons; Paper 19 bounds scalar backreaction and disformal delay
for its tested Refsdal configuration, not every lens geometry.
Absolute CDM-free lensing remains a separate prediction to derive.

**Dark matter status:** Phantom Mass is the apparent
mass component an analyst infers when temporal structure is
reconstructed under the Isochrony Axiom. It is an inference
artifact, not a mechanism: for dynamics it mislabels the real
shear force; for temporally structured sources it mislabels the
projected image response (bounded \(\lesssim10^{-7}\)); for
static sources no projection exists and inferred lensing mass is
real gravitating content.

**Falsification:** An environment-resolved
dynamical–lensing mass comparison tests the extra-force channel;
an absolute CDM-free CMB/cluster/galaxy lensing calculation tests
the missing optical channel. Null source-variability correlations
constrain the temporal-composite contribution. Failure to supply
the observed absolute deflection rules out the proposed complete
dark-sector replacement, even if a phantom-mass difference exists.

This work demonstrates that
Regime II is viable as a time-domain and
reconstruction-space framework — not as a carrier of
dark-matter-level spatial deflection. Regime I
is the conservative baseline in which the only propagating inter-image
content is the disformal multipath deformation at its GW170817-bounded
normalization; the conformal clock sector, whose differential-propagation
channel is identically inert, contributes the reconstruction-space
clock-transfer map of Regime II. The phantom-mass prediction of §2.6
addresses the dynamical–lensing difference; it does not close the
source-independent deflection required by a CDM-free ontology.

### 2.7 Why Lensing May Not Be Purely Spatial

Standard gravitational lensing analysis contains a simplifying temporal
assumption that has typically been treated as exact. This assumption is made
explicit, and its breakdown under TEP leads directly to the dark matter
reinterpretation.

#### The Hidden Assumption in Image Formation

When a lensed galaxy is observed, photons are collected over an exposure
time and an "image" is reconstructed. This reconstruction implicitly
assumes:

All photons arriving during the exposure left the source at
approximately the same epoch

Differences in arrival angles correspond to differences in spatial
paths, not temporal paths

The reconstructed "shape" represents a spatial snapshot of the source at
one moment

These assumptions constitute the *Isochrony Axiom* applied to image
formation. Standard analysis corrects for the mean lookback time (distance),
but assumes that the variance in lookback time across the image is
negligible. This overlooked variance is defined as
*Differential Lookback Time*. In a two-metric framework, this
variance is an additional source-dependent reconstruction residual.

#### The temporal composite Mechanism

Consider an extended galaxy being lensed. Light from different parts of the
galaxy:

Leaves the source at different times (the source is evolving on Myr
timescales)

Takes different paths through the lens (different impact parameters)

Is accompanied by a different matter-clock transfer congruence through
regions with different \(A(\phi)\) values — a timelike reconstruction
field, not a photon propagation delay

- Arrives at the detector at the "same" observation time

If \(A(\phi)\) varies spatially—forming a halo-like configuration around the
lens—then the matter-frame path time

\begin{equation} \label{eq:gl_path_delay}
\Delta t_{\rm path} = \int_{\rm path} \frac{A(\phi)}{c}\,dl
\end{equation}

evaluated on the associated timelike clock congruence differs between rays
at different impact parameters. This functional is not a photon arrival
time: Axiom 1 makes the photon coordinate transit conformally invariant,
so no part of it propagates to any observed inter-image delay. What it
quantifies is the reconstruction-space contrast — the magnitude of the
clock-transfer field that a universal-clock reconstruction would
misassign to mass, distance, or time-delay normalization. For halo-scale
propagation depths \(L \sim 2\) Mpc and conformal variations \(\Delta A/A
\sim 10^{-6}\), that envelope contrast is:

\begin{equation} \label{eq:gl_delay_estimate}
\Delta \tilde{\tau}_{\rm env} \sim \frac{\Delta A}{A} \cdot \frac{L}{c} \sim
\text{years}
\end{equation}

The propagating residual on the same paths is exactly zero in the conformal
sector (Paper 19, step_56) and is bounded at the ms–s level on the
disformal carrier (Box 3.2). The relevant comparison for any claimed
observable is therefore the post-model residual — constrained to
\(\lesssim\) tens of days in existing strong-lens systems by the success of
GR mass models (Paper 19) — not the multi-hundred-day total delay, which
those models already reproduce. For slowly evolving galaxies the
source-dependent temporal-composite response is negligible. The dominant signal is
therefore the coherent static temporal-field sector: physical optical
shear/convergence arises from scalar backreaction and any permitted
disformal response, while the conformal sector supplies the associated
chronometric reconstruction. The temporal smearing (the source-motion term) becomes
the dominant propagating temporal-composite signal only for fast transients
(FRBs); for slowly evolving sources its observable content is the
shear-variance residual above the standard delay-map baseline (§3.4).

#### Why This Creates "Phantom Mass"

For a source that evolves on timescales comparable to the emission-time-map contrast \(\Delta T_{\rm eff}\):

If the source was more compact in the past → inner regions (earlier
epoch) appear smaller

If the source was less compact in the past → inner regions appear larger

The reconstructed "shape" is systematically distorted by temporal mixing

Standard lensing analysis interprets *any* systematic shape
distortion as evidence for mass (convergence and shear). The temporal
smearing is mathematically indistinguishable from gravitational lensing
distortion, but its amplitude is bounded by the ratio of the
emission-time-map contrast to the source-evolution timescale:
\(\lesssim 10^{-7}\) in shear for galaxy sources, vanishing for static
sources. It is therefore a source-dependent reconstruction signature, not
the carrier of the observed dark-matter-level lensing excess; that excess
is confronted through the dynamical–lensing mass comparison (§2.6).

#### Why This Effect Is Achromatic

The conformal factor \(A(\phi)\) rescales proper time identically for all
photon frequencies. Unlike plasma dispersion (which scales as \(\nu^{-2}\))
or dust extinction (wavelength-dependent), conformal temporal coupling is
*perfectly achromatic*. General relativistic lensing is likewise
achromatic, so achromaticity alone does not discriminate a temporal-field
contribution from ordinary gravitational lensing. The operational
significance is the converse: because the TEP contribution is achromatic, it
cannot be separated from GR lensing by colour information, but it *can*
be separated from plasma and dust systematics — which is precisely what makes
multi-frequency timing the discriminating measurement (Section 5.1).

#### The Central Thesis

Under TEP, the existence of "dark matter" is inferred rather than directly
observed. It is a *conclusion contingent on the Isochrony Axiom*. If
that axiom fails—if the universe is not temporally synchronous in the way
standard analysis assumes—then the inferred "dark mass" can be modeled as
unmodeled temporal structure. The dark sector is modeled not as a substance,
but as the shadow of time. No claim is made regarding uniqueness of the
two-metric realization, only the operational equivalence of temporal
gradients to inferred mass under isochrony.

## 3. The Phantom Mass Mechanism

### 3.1 The Canonical Disformal Metric and Null-Trajectory Structure

The Phantom Mass mechanism is derived from the canonical TEP matter metric. The foundational two-metric structure (Jakarta, Paper 0) relates the gravitational metric \(g_{\mu\nu}\) to the causal matter metric \(\tilde{g}_{\mu\nu}\) through the disformal map:

\begin{equation} \label{eq:gl_disformal_map}
\tilde{g}_{\mu\nu} = A^2(\phi)\,g_{\mu\nu} + B(\phi)\,\nabla_\mu\phi\,\nabla_\nu\phi
\end{equation}

where \(A(\phi)\) is the universal conformal coupling and \(B(\phi)\) is the disformal coupling. This is the canonical metric \(A^2 g_{\mu\nu} + B\,\nabla_\mu\phi\,\nabla_\nu\phi\), not a Newtonian-gauge metric with a conformal factor inserted only in the spatial sector.

#### 3.1.1 Conformal Invariance of Null Trajectories

In the purely conformal subclass (\(B=0\)), the matter metric reduces to \(\tilde{g}_{\mu\nu}=A^2(\phi)\,g_{\mu\nu}\). A standard result of conformal geometry in four dimensions is that null geodesics are preserved: if \(k^\mu\) is tangent to a null geodesic of \(g_{\mu\nu}\), the same path is a null geodesic of \(\tilde{g}_{\mu\nu}\) with a rescaled affine parameter. Therefore:

\begin{equation} \label{eq:gl_null_invariance}
B = 0 \quad \Longrightarrow \quad d\tilde{s}^2 = 0 \quad \Longleftrightarrow \quad ds^2 = 0.
\end{equation}

This has three immediate consequences for gravitational lensing:

- \(A^2\) alone does not change the null trajectory. Pure conformal rescaling preserves null cones; it cannot generate a spatial refractive index or bend photons onto new paths.

- Static geometric bending beyond the conformally related geometry must come from \(g_{\mu\nu}[\phi]\) backreaction — the scalar field modifying the Einstein-frame metric through the coupled field equations — or from \(B \neq 0\), which tilts the matter null cone relative to the gravitational null cone.

- The conformal sector can alter endpoint clock calibration, frequency transport, and timelike source evolution. It acts directly on timelike observables (orbital periods, spectroscopic velocities, standard-candle distance calibration) but cannot generate the printed spatial refractive index \(n_{\rm eff} \simeq 1 - 2\Psi + (A(\phi)-1)\) that would follow from inserting \(A^2(\phi)\) into the spatial sector of a Newtonian-gauge metric alone.

#### 3.1.2 Separating Null and Timelike Observables

The lensing deflection angle decomposes into two physically distinct channels:

\begin{equation} \label{eq:gl_deflection_decomp}
\delta\theta_{\rm lens} = \delta\theta_{g[\phi]} + \delta\theta_B
\end{equation}

where \(\delta\theta_{g[\phi]}\) is the deflection from scalar backreaction on the geometric metric \(g_{\mu\nu}\) — the scalar field modifying the Einstein-frame curvature through the coupled Einstein–scalar equations — and \(\delta\theta_B\) is the deflection from the disformal term \(B(\phi)\nabla_\mu\phi\nabla_\nu\phi\), which tilts the matter null cone along the field gradient. The conformal factor \(A(\phi)\) does not appear in \(\delta\theta_{\rm lens}\) at leading order because it cancels from the null condition.

The worked backreaction example is the scalar-Gauss-Bonnet (sGB) coupling studied in Bahrain (Paper 28, Appendix L). In shift-symmetric sGB, the scalar field \(\phi \sim Q_s/r\) backreacts on the geometric metric at \(\mathcal{O}(\eta^2)\) (where \(\eta = 3\alpha_{\rm GB}/M^2\)), producing a genuine correction to the null-trajectory bending. The conformal factor \(A = e^{-\phi}\) modifies clock rates at \(\mathcal{O}(\eta)\) — acting on timelike observables such as the ISCO — but does not contribute to the shadow at leading order because null geodesics are conformally invariant. Bahrain Appendix L explicitly isolates this sGB backreaction contribution and demonstrates the different coupling orders of the null and timelike observables: the shadow is sensitive to the geometric metric at \(\mathcal{O}(\eta^2)\) while the ISCO feels the conformal factor at \(\mathcal{O}(\eta)\).

#### 3.1.3 The temporal-composite observable

The conformal sector produces observable effects through timelike channels: endpoint clock calibration, frequency transport, and source evolution. These are captured by the temporal composite observable, which relates the observed image intensity to the emission-time shift induced by the temporal field:

\begin{equation} \label{eq:gl_composite_obs}
\delta I_{\rm obs} \simeq -\frac{\partial I_{\rm src}}{\partial t_{\rm em}}\,\delta t_{\rm em}
\end{equation}

where \(\delta t_{\rm em}\) is the differential emission-time shift between paths, sourced by the complete metric \(\tilde{g}_{\mu\nu}\) rather than an unmatched spatial conformal factor. The delay must come from the full disformal metric — including \(g_{\mu\nu}[\phi]\) backreaction, the disformal term \(B\), endpoint clock-rate differences through \(A(\phi)\), and frequency transfer — not from a path integral \(\int A(\phi)\,dl/c\) interpreted as photon proper-time accumulation. Null proper time is zero (Jakarta); any measured open-path effect must be formulated through emission and reception clocks, actual coordinate delay from the geometric and disformal metric, or frequency transfer.

The static clock-transfer contribution from the conformal sector modifies the relation between accumulated matter-frame time and the geometry reconstructed under an isochronous model. The associated effective clock-transfer contrast along a path \(\gamma\) is:

\begin{equation} \label{eq:gl_clock_transfer}
\Delta\tilde{\tau}_{\rm static} = \frac{1}{c} \int_\gamma \bigl(A(\phi) - 1\bigr)\,dl
\end{equation}

This is a clock-transfer discrepancy — a difference between the matter-frame time a timelike congruence accumulates along each path and the time an isochronous GR lens model infers — not a propagated photon delay and not a direct refraction of null geodesics. For photons its differential content vanishes identically: the null condition is conformally invariant (§3.1.1), and the underlying Temporal Shear is an exact one-form, \(\Sigma_\mu=\nabla_\mu\ln A\), whose open-path integral is endpoint-determined and cancels between any two rays joining the same source and observer; inserting the screening projection \(\mathcal{S}_\Sigma(\mathcal{E})\) inside a photon-path observable is a category error, since photons carry no clocks and do not respond to the shear sector. The dedicated strong-lensing pipeline evaluates the exact additional static-conformal residual at \(0.0\) d (Paper 19, step_56). The functional is retained as the chronometric reconstruction map — the field a universal-clock reconstruction would misassign to convergence, mass-sheet normalization, or delay calibration — and it contributes no term to the propagated Fermat surface. The angular positions of Einstein rings and major arcs are governed by the optical geometry; any TEP modification of those positions arises through scalar backreaction on \(g_{\mu\nu}\), the bounded disformal sector, or a source-dependent temporal-composite displacement. The physically propagating differential residual is carried by the disformal multipath deformation, bounded by GW170817 to \(\lesssim 0.2\) s per \(2\) Mpc halo path.

#### 3.1.4 The Amplification Matrix and Jacobian Decomposition

Integrating the geodesic deviation equation along the line of sight yields the amplification matrix \(\mathcal{A}_{ij}\), which maps source-plane displacements to image-plane displacements:

\begin{equation} \label{eq:gl_amplification}
\mathcal{A}_{ij} = \frac{\partial \beta_i}{\partial \theta_j} = \delta_{ij} - \int_0^{\chi_s} \frac{(\chi_s - \chi)\chi}{\chi_s}\, \mathcal{R}_{ij}(\chi)\, d\chi
\end{equation}

where \(\mathcal{R}_{ij}\) is the optical tidal matrix constructed from the Riemann tensor of the geometric metric \(g_{\mu\nu}[\phi]\), projected onto the screen space. The TEP correction to the optical tidal matrix comes from scalar backreaction on \(g_{\mu\nu}\) and from the disformal sector, not from a spatial conformal factor:

\begin{equation} \label{eq:gl_tidal_matrix}
\mathcal{R}_{ij} = \mathcal{R}^{(\Psi)}_{ij} + \mathcal{R}^{(g[\phi])}_{ij} + \mathcal{R}^{(B)}_{ij}
\end{equation}

where \(\mathcal{R}^{(\Psi)}_{ij}\) is the standard GR contribution, \(\mathcal{R}^{(g[\phi])}_{ij}\) is the scalar-backreaction correction to the geometric metric, and \(\mathcal{R}^{(B)}_{ij}\) is the disformal correction. The conformal factor does not appear at leading order because it cancels from the null trajectory.

The magnification of an image is \(\mu = (\det\mathcal{A})^{-1}\). To first order in the TEP correction \(\delta\mathcal{A}_{ij}\), the fractional change in magnification is:

\begin{equation} \label{eq:gl_mag_perturbation}
\frac{\delta\mu}{\mu} = \mathrm{Tr}\left(\mathcal{A}^{-1}_{\rm GR}\,\delta\mathcal{A}\right)
\end{equation}

This defines the lensing amplification kernel \(\mathcal{P}_\mu\), a projection operator that maps the scalar-backreaction and disformal Hessian to the observable magnification shift. Near a critical curve, where \(\det\mathcal{A}_{\rm GR} \to 0\), the kernel diverges as \(\mu_{\rm GR}^2\), amplifying small corrections into large observable residuals. Because the inverse reconstruction is correspondingly sensitive to small timing and geometric perturbations there, this supplies a candidate mechanism capable of closing the factor-of-\(\sim\)90–750 amplitude gap between direct potential-sampling and observed delay shifts identified in Paper 19 (SN Refsdal) — locating that discrepancy in Jacobian amplification rather than in a free phenomenological coefficient. A numerical resolution requires evaluation of the complete tensor and lens-model response, not the scalar log-magnification proxy alone; that calculation is not performed here.

Formally, the operational response proxy used in the blind-prediction tests (Paper 19, §2.3) is the first-order truncation of this kernel:

\begin{equation} \label{eq:gl_response_proxy}
\Gamma_t(i) = 1 + \kappa_{\rm lens}\,\mathcal{P}_\mu\big[\nabla\phi\big](i) \;\approx\; 1 + \kappa_{\rm lens}\log_{10}\!\big(\mu_{\rm norm}(i)\big)
\end{equation}

This is a phenomenological scalar truncation of the tensor response. Weak shear alone does not make it exact; exact reduction additionally requires an approximately isotropic response, \(\delta\mathcal{A}_{ij}\propto\delta_{ij}\). The log-magnification form follows from \(\delta\mu/\mu = \mathrm{Tr}(\mathcal{A}^{-1}\delta\mathcal{A})\) when \(\delta\mathcal{A}\) is proportional to the identity. The mu–kappa–gamma systematic is the residual error from truncating the full tensor kernel to a scalar log-magnification proxy. Eliminating it requires direct evaluation of \(\mathcal{P}_\mu\) from high-resolution mass models, which is the definitive next phase identified in Paper 19.

**Response-coefficient convention.** Following the corpus rule established in TEP-COS (Paper 10) for \(\kappa_{\rm MSP}\), the quantity \(\kappa_{\rm lens}\) is an *observable channel response coefficient*: it measures how strongly the lensing reconstruction responds to Temporal Shear. It is not the bare microscopic conformal coupling \(\beta_A\), not \(A-1\), and not the locally active PPN coupling, and it must not be numerically identified with the amplitudes of other channels — such as \(\epsilon_T^{\rm HC}\) (TEP-HC) or the line-of-sight amplitude of TEP-C0 — unless a solved environmental transfer function establishes that identification. Schematically, the lensing-channel observable takes the form \(\Delta O_{\rm GL} = \kappa_{\rm GL}\,\mathcal{S}_{\rm GL}(\mathcal{E})\,\mathcal{F}_{\rm GL}[\Delta\ln A, \Sigma_\mu, C_A;\ \Phi, \rho, z]\), with the environmental screening operator applied before comparison with any other channel.

**Amplitude dictionary.** The manuscript refers to several distinct quantities that must not be conflated:

- \(\beta_A\): the microscopic conformal parameter (bare Lagrangian quantity).

- \(\Sigma_\mu = \nabla_\mu \ln A(\phi)\): the underlying Temporal Shear.

- \(\Sigma_\mu^{\rm obs} = \mathcal{S}_\Sigma(\mathcal{E})\,\Sigma_\mu\): the observable environmentally projected Temporal Shear.

- \(\langle\Delta A\rangle_\gamma = \int_\gamma \Sigma_\mu^{\rm obs}\,dx^\mu\): the open-path clock-transfer contrast. In the unscreened limit this is the integral of an exact one-form, \(\int_\gamma \nabla_\mu\ln A\,dx^\mu = \ln A_{\rm obs} - \ln A_{\rm em}\), so it is endpoint-determined and its differential between two rays sharing the same endpoints vanishes identically; the environment-projected form is defined on the matter-clock congruence and inherits the same vanishing multipath photon content.

- \(\kappa_{\rm lens}\): the lensing reconstruction response coefficient relating temporal-field structure to inferred convergence.

These quantities are not numerically interchangeable without a solved environmental transfer function, and none of them is a propagated photon delay: the conformal entries act on clock calibration and reconstruction, while the propagating delay field is the disformal multipath deformation bounded in Box 3.2.

#### 3.1.5 Interpretation: Geometric vs. Temporal Contributions

The Jacobian decomposition reveals two physically distinct contributions to image distortion:

| Term | Source | Physical Origin | Observational Signature |
| --- | --- | --- | --- |
| **Geometric** | \(\Psi_{,ij}\) | Spatial curvature from mass | Standard convergence \(\kappa\) and shear \(\gamma\) |
| **Scalar backreaction** | \(g_{\mu\nu}[\phi]\) | Scalar field modifying Einstein-frame curvature | Coherent tangential shear mimicking DM halo |
| **Disformal** | \(B(\phi)\nabla_\mu\phi\nabla_\nu\phi\) | Null-cone tilt along field gradient | Direction-dependent deflection |
| **temporal composite** | \(\mu_s^{\,i}\,\partial_j \Delta T_{\rm eff}\) | Source motion × emission-time-map gradient | Kinematics-correlated shear variance; the residual above the standard delay-map baseline is the TEP-specific content |

The scalar-backreaction and disformal terms produce coherent contributions to the shear field. The temporal composite term arises when the source position evolves during the differential emission-time contrast \(\Delta T_{\rm eff}\) across the image; for a source with proper motion \(\vec{\mu}_s\), the effective source position becomes:

\begin{equation} \label{eq:gl_effective_source}
\beta_{\rm eff}^{\,i}(\vec{\theta}) = \beta_{\rm geom}^{\,i}(\vec{\theta}) - \mu_s^{\,i}\,\Delta T_{\rm eff}(\vec{\theta})
\end{equation}

where \(\mu_s^{\,i}\) is the \(i\)-th component of the source proper motion and \(\Delta T_{\rm eff}\) is the effective emission-time map of §2.5. The corresponding temporal-composite contribution to the Jacobian is:

\begin{equation} \label{eq:gl_tc_jacobian}
\delta\mathcal{A}^{\rm TC}_{ij} = -\mu_s^{\,i}\,\partial_j \Delta T_{\rm eff}
\end{equation}

This adds an asymmetric, source-dependent contribution to the Jacobian that does not average coherently but increases the variance of shear measurements.

**Principle:**

#### Summary: The Phantom Mass Decomposition

The full amplification matrix in TEP is:

\begin{equation} \label{eq:gl_jacobian_decomp}
\mathcal{A}_{ij} = \underbrace{\mathcal{A}^{\text{GR}}_{ij}}_{\text{Baryonic Lensing}} + \underbrace{\mathcal{A}^{(g[\phi],\text{static})}_{ij}}_{\text{"Dark Matter" (Coherent)}} + \underbrace{\mathcal{A}^{(\text{dyn})}_{ij}}_{\text{temporal composite (Stochastic)}}
\end{equation}

Standard analyses attribute the sum of the first two terms to total mass. TEP identifies the second term as the coherent optical component of the deflection ledger — a geometric effect of scalar backreaction on the Einstein-frame metric and disformal null-cone tilt — and evaluates both carriers from the action: scalar backreaction reaches \(\kappa_\phi\approx4\times10^{-5}\) (\(\sim2\times10^{3}\) short of dark-matter level; Paper 19, Step 61) and the disformal term is bounded \(\sim5\times\) below the Refsdal residual (Step 63). The coherent optical term is therefore a computed bound, not a dark-matter carrier: real deflection is matter-sourced at observable level. The third term supplies the source-dependent discriminating channel: shear variance correlated with source kinematics. The correlation's existence is not itself distinctive, since any emission-time map sources the same \(\mu_s\,\partial_j\Delta T\) structure — under particle dark matter and GR a moving source's effective source-plane position is \(\beta-\vec{\mu}_s\Delta T\), and the ordinary Fermat surface alone produces \(\gamma^{\rm std}=\mu_s\,\partial_\theta\Delta T_{\rm Fermat}\sim3\times10^{-8}\) for strong-lens geometries (\(\sim6\times10^{-10}\) at galaxy–galaxy scales; step_01). The discriminating observable is the residual over that computable baseline: on the propagating carrier it is the disformal emission-time deformation, bounded at \(\gamma^{\rm TC}_{\rm prop}\sim10^{-15}\) — seven orders below the standard baseline and tested directly by the timing residuals of §5.1 — while the reconstruction-space contribution is reconstruction-space and is bound-set rather than measured by the scatter test of §3.4. The conformal factor \(A(\phi)\) acts on timelike observables and clock calibration but generates neither null-trajectory bending nor any inter-image arrival-time residual — the latter is exactly zero in the static conformal sector (Paper 19, step_56).

**Principle:**

### Box 3.1: A Minimal Toy Model Estimate (Halo Scale Integration)

To demonstrate the order of magnitude, consider a simple spherical conformal halo profile, applied as a local interior model over the field-bearing extent of the halo:

\begin{equation} \label{eq:gl_halo_profile}
A(\phi) = 1 + \epsilon \ln(r/r_0), \qquad r \lesssim r_h \sim L_{\rm halo}/2
\end{equation}

For a coupling strength \(\epsilon \approx 10^{-6}\) and a characteristic scale \(r_0 = 10\) kpc, the excursion \(|A(\phi)-1|\) remains at the \(10^{-6}\) level throughout the domain (\(|\ln(r/r_0)| \lesssim 5\) for \(r \in [r_E, r_h]\)). The ambient boundary condition is imposed by environmental matching rather than by the toy form: beyond the halo matching radius \(r_h\) the screened field relaxes to the ambient baseline \(A_\infty = 1\), so the asymptotic divergence of the logarithm lies outside the domain of the estimate and is never extrapolated.

- **Integration Path:** The delay is integrated only over the effective halo depth (\(L_{halo} \approx 2\) Mpc), not the full cosmological path. This respects the locality of the potential well.

**Chronometric-Envelope Contrast:** Across an Einstein radius (\(r_E \approx 5\) kpc), the differential clock-transfer field corresponds to:

\begin{equation} \label{eq:gl_diff_delay}
\Delta \tilde{\tau}_{\rm env} \sim \frac{\epsilon}{2} \frac{L_{halo}}{c} \approx \frac{10^{-6}}{2} \cdot (6.5 \times 10^6 \text{ light-years}) \approx 3.2 \text{ years}
\end{equation}

- **Carrier status:** This ~3 year figure is the reconstruction-space scale — the reconstruction-space clock-transfer field of §2.2 and §3.1.3 — not a propagated photon delay. The exact additional static-conformal inter-image residual on the same paths is \(0.0\) d (Paper 19, step_56); the propagating differential residual is carried by the disformal multipath deformation at \(\lesssim 0.2\) s per \(2\) Mpc, and scalar backreaction enters the delay surface only as ordinary \(g\)-sector Fermat structure that lens models absorb as mass. The figure therefore does not compete with observed strong-lens delays — which are already reproduced by GR mass models — but bounds the post-model residual an isochronous reconstruction could misassign; the correct empirical comparison set is the residual class measured by Paper 19 (\(\lesssim\) tens of days), not the multi-hundred-day totals.

- **Clock-transfer reconstruction:** The static gradient \(\nabla(\Delta \tilde{\tau}_{\rm env})\) defines the unmodeled clock-transfer field along existing lens paths. When a GR lens model is required to reproduce a path-dependent timing map while assuming isochrony, such a residual would be absorbed into inferred convergence, mass-sheet normalization, or distance calibration — the reconstruction-space "Phantom Mass" signature. It does not refract null geodesics onto new trajectories and does not shift propagated arrival times; the conformal sector preserves null cones. The corresponding physical optical-tidal contribution is carried by the scalar-backreaction and disformal channels of §3.1.4.

- **Source-motion term (stochastic):** The term \(\vec{\mu}_s \cdot \nabla(\Delta T_{\rm eff})\) couples source proper motion to whichever emission-time map propagates. On the propagating carrier it is the millisecond-to-second disformal contribution, which dominates the differential delay budget for fast transients (the lensed-FRB channel of §5.1); for slowly evolving galaxy sources its observable content is the shear-variance residual above the standard-map baseline, bounded per Box 3.2.

**Profile Dependence Check:** The ~3 year estimate uses a logarithmic profile for simplicity. Realistic dark matter halos follow the NFW profile:

\begin{equation} \label{eq:gl_nfw_profile}
\rho_{NFW}(r) = \frac{\rho_s}{(r/r_s)(1 + r/r_s)^2}
\end{equation}

If the clock-transfer field tracks the gravitational potential (\(A(\phi) - 1 \propto \Psi\)), then \(A(\phi) - 1 \propto \int \rho/r\, dr\), giving:

\begin{equation} \label{eq:gl_nfw_deflection}
(A(\phi)-1)_{\rm NFW}(r) \propto \ln(1 + r/r_s) - \frac{r/r_s}{1 + r/r_s}
\end{equation}

For a cluster with \(r_s \approx 200\) kpc and integration over \(L_{halo} \approx 2\) Mpc:

- The NFW profile concentrates more of the clock-transfer field near the core than the logarithmic profile.

- The differential envelope contrast across an Einstein radius (\(r_E \approx 5\text{--}50\) kpc) is enhanced by a factor of 2–5 relative to the logarithmic estimate.

- Result: \(\Delta\tilde{\tau}_{{\rm env},NFW} \sim 5\text{--}15\) years at the reconstruction-space scale — a reconstruction-scale figure with the carrier status stated above, not an observed-delay prediction.

The order-of-magnitude envelope estimate is robust to profile shape; realistic NFW profiles produce slightly larger chronometric contrasts than the toy logarithmic model.

**Principle:**

### Box 3.2: Order of Magnitude Estimate for stochastic shear

To estimate the magnitude of the *stochastic* shear contribution (the dynamic term \(\mu_s \nabla(\Delta \tilde{\tau})\)), the analysis uses the updated halo-scale delays:

- **Source Velocity:** Typical cluster transverse velocity \(v_s \sim 1000\) km/s at distance \(D_A \sim 1\) Gpc yields an angular proper motion \(\mu_s \approx 2 \times 10^{-7}\) arcsec/year (\(\sim 0.2\,\mu\)as/yr; the milliarcsec-scale figure appearing in earlier drafts reflected a unit slip).

- **Envelope Delay Gradient:** From Box 3.1, a reconstruction-space contrast of \(\sim 3\) years varying over arcsecond scales gives \(\nabla(\Delta \tilde{\tau}_{\rm env}) \sim 3\) years/arcsec at the envelope; the propagating-carrier gradient is \(12\) orders smaller (below).

**Resulting stochastic shear:** The product is dimensionless shear:

\begin{equation} \label{eq:gl_stochastic_shear}
\gamma_{stoch}^{\rm env} \approx (2 \times 10^{-7} \, \text{arcsec/yr}) \times (3 \, \text{yr/arcsec}) \approx 6 \times 10^{-7}
\end{equation}

This stochastic contribution (\(\gamma_{stoch} \sim 10^{-6}\) at the reconstruction-space scale) is small compared to typical weak lensing shear (\(\gamma \sim 0.01\text{--}0.1\)), confirming that the dynamic term is a perturbation (excess scatter), not the dominant signal. The coherent "Dark Matter" halo signature is the combined static temporal-field contribution as registered by the lens model: its physical optical-tidal component is carried by scalar backreaction on \(g_{\mu\nu}\) and any bounded disformal term, while the conformal sector modifies the associated clock-transfer and inference mapping (the clock-transfer reconstruction). It does not arise from source motion, and not from a spatial refractive index.

**Two scales, two roles.** The two delay scales of Box 3.3 sit on different carriers, and the applications of Section 5 must be read against the correct one. For photons the conformal clock-transfer map contributes exactly zero differential inter-image delay: null cones are conformally invariant (§3.1.1), so \(A(\phi)\) drops out of the photon transport equation and the open-path integral is endpoint-determined (Paper 19 verifies the vanishing residual explicitly). The physically propagating component of \(\Delta T_{\rm eff}\) is carried by the disformal multipath deformation, bounded by GW170817 to \(\lesssim 10^{-15}\) fractional — \(\Delta T \lesssim 0.2\) s over the \(2\) Mpc halo path, the conservative-baseline scale. On that carrier the same product gives \(\gamma^{\rm TC}_{\rm prop} \sim \mu_s\,\partial_\theta\Delta T \sim (2\times10^{-7}\,{\rm arcsec/yr})(6.5\times10^{-9}\,{\rm yr/arcsec}) \sim 10^{-15}\). The \(6\times10^{-7}\) figure is therefore the *reconstruction-space* value: it quantifies the reconstruction-space field a lens model would absorb *if* the clock-transfer map acted as a propagating emission-time field, and it bounds — rather than supplies — the shear-variance applications of §5. The photon-propagating channel is tested directly and most sharply by the arrival-time residual itself (§5.1).

### 3.2 Connection to Lens-Model Degeneracies

This mechanism parallels the *Source-Position Transformation (SPT)* (Schneider & Sluse 2013), which identifies a degeneracy class of mass models yielding identical observables but differing time delays. TEP extends this degeneracy into the metric sector itself. Rather than permuting the mass distribution \(\kappa(\vec{\theta})\) while holding the metric constant, TEP holds the baryonic mass constant and permutes the spacetime arrival surface \(\Delta \tilde{\tau}(\vec{\theta})\). Consequently, the "Phantom Mass" can be understood as a physical realization of the SPT, where the extra freedom resides in the time-transport sector rather than invisible spatial matter.

### 3.3 The Two Regimes: Parameter Thresholds

TEP phenomenology divides into two distinct regimes, distinguished by the magnitude of the differential clock-transfer residual and the resulting phenomenology:

**Principle:**

#### Box 3.3: Regime Definitions and Parameter Thresholds

| Regime | Clock-transfer scale | Phenomenology |
| --- | --- | --- |
| **conservative baseline** | ms–s (propagating, disformal carrier) | Time-domain residuals; static optical lensing effectively unchanged |
| **Regime II** | \(1\text{--}10\) years (reconstruction space; propagating channel unchanged at ms–s) | Coherent scalar-metric/disformal lensing combined with chronometric reconstruction and source-dependent temporal-composite response |

For a \(2\) Mpc path, the Regime-II envelope contrast is \(\langle\Delta A\rangle_\gamma \sim 10^{-7}\text{--}10^{-6}\), consistent with the halo-scale integration in Box 3.1; per §3.1.3 this contrast is endpoint-determined for photons and is realized in the data only through the reconstruction mapping, while the propagating residual remains the disformal channel.

**Operational Distinction:** The conservative baseline accepts the standard GW170817 translation (arrival-time offset → propagation-speed bound) at face value. Regime II applies if TEP's dynamical-time interpretation is correct, in which case the standard translation may require revision—the observed \(\Delta t = 1.74\) s constrains the *disformal* sector; it does not directly test the *conformal* sector, although conformal scalar sectors remain indirectly constrained by PPN, equivalence-principle, source-screening, and clock-comparison tests (Section 4).

**Empirical Discriminator:** The regime is determined by observation, not assumption. If lensed FRBs show only millisecond residuals, the conservative baseline applies. If strong-lens post-model residuals, reconstruction maps, or variability-correlated structure reveal clock-transfer structure at the envelope scale, Regime II is indicated.

**Independent Regime Criterion (Breaking Circularity):** To avoid circular reasoning, the following observable specifies the regime *independently* of TEP's correctness:

- **The Variability-Mass Correlation Test:** In Regime II, the inferred "dark matter" mass of a lens should correlate with the variability timescale of the background source population. Specifically: lenses observed through rapidly variable sources (AGN, quasars) should show systematically different mass reconstructions than the same lenses observed through slowly evolving sources (elliptical galaxies). This correlation is *forbidden* in standard CDM (mass is source-independent) but *required by the source-dependent temporal-composite component of Regime II*.

- **Decision Rule:** If existing strong-lens catalogs show no statistically significant correlation between inferred lens mass and source variability class at the >3σ level, the source-dependent temporal-composite component is disfavored. If such a correlation exists, it constitutes positive evidence for TEP independent of FRB timing. *Sensitivity floor:* the response enters through \(\delta\kappa \sim \gamma^{\rm TC} = \mu_s\,\partial_\theta\Delta T_{\rm eff}\) (Box 3.2), so a correlation search at the proposed 10% mass precision probes \(\gamma^{\rm TC} \gtrsim 10^{-1}\) — some five orders of magnitude above even the reconstruction-space value — and reaching the propagating carrier through mass reconstruction would require \(\delta M/M \sim 10^{-15}\), far below any achievable precision. A null result at the specified precision therefore bounds the envelope amplitude rather than testing the carrier; the carrier itself is tested by the timing residual of §5.1. Complementarily, the ordinary delay-absorption route already constrains the propagating field: a path-dependent delay \(\Delta T\) absorbed into a lens model shifts the inferred normalization by \(\sim\Delta T/\Delta t_{\rm Fermat}\), so the observed \(\sim 10\%\) closure of strong-lens mass models bounds any propagating residual at \(\lesssim 10\) days per \(100\)-day delay — excluding a propagating year-scale reading outright, consistently with the conformal null of §3.1.1.

- **Current Status:** This test can be performed with existing data (HST strong-lens archives, SDSS quasar lenses vs. galaxy-galaxy lenses) as an envelope-bounding correlation search; its discriminating power on the propagating carrier requires the timing channel of §5.1. This is flagged as a priority observational test.

Under the conservative baseline (Regime I), \(\Delta \tilde{\tau}\) is small (milliseconds to seconds). In this regime:

- **Static Lensing:** The phantom mass effect is negligible for slowly evolving sources (galaxies). Static mass maps are unaffected.

- **Time-Domain Lensing:** The effect is dominant for fast transients. A millisecond gradient across an image plane is huge for an FRB.

**Conclusion:** In the conservative baseline (Regime I), TEP is a precision correction to time-domain astrophysics. In Regime II, TEP offers a conditional geometric reinterpretation in which the component conventionally attributed to dark matter may contain an unmodeled temporal-transport contribution.

### 3.4 The Critical Discriminator: Variability Scatter

Since the dynamic term \(\mu_{s,i} \nabla_j (\Delta \tilde{\tau})\) is randomly oriented (depending on the direction of \(\vec{\mu}_s\)), it does not add to the mean shear profile but contributes to the *variance* of the shear measurement.

**Principle:**

**The Variability Scatter:** The inferred "shear noise" (RMS dispersion of ellipticities) should be higher for source populations with high proper motion or intrinsic variability. While the coherent "dark matter" signal is static, the *scatter* around that signal is dynamic. The amplitude is set by the bookkeeping of Box 3.2: \(\gamma^{\rm TC} \lesssim 6\times10^{-7}\) at the reconstruction-space scale and \(\sim10^{-15}\) on the propagating carrier, so the scatter excess contributes a variance \(\gamma_{\rm TC}^{2}\) that is orders of magnitude below shape noise on either branch. The observable content of the test is therefore a bound on the reconstruction-space scale — a non-detection at a stated scatter precision caps \(\nabla(\Delta\tilde{\tau})\) at that level — while the propagating channel is tested directly by timing residuals (§5.1).

The discriminating quantity is not the correlation's existence — the ordinary delay map produces kinematics-correlated dispersion at the standard level \(\gamma^{\rm std}=\mu_s\,\partial_j\Delta T_{\rm Fermat}\) under particle dark matter as well (step_01: \(\sim3\times10^{-8}\) strong-lens, \(\sim6\times10^{-10}\) galaxy–galaxy) — but the residual above that baseline. Particle dark matter predicts equality with the standard-map value at every source class; a statistically significant excess bounds, and at sufficient precision reveals, a non-standard emission-time field. At achievable shear precisions the reach is the envelope-scale field and its reconstruction-space bound; the propagating disformal carrier sits ~7 orders below the baseline and is accessed by the timing channel of §5.1 rather than by shear.

## 4. Reanalysis of GW170817: What is Actually Constrained?

### 4.1 The Measurement and the Standard Translation

The simultaneous detection of gravitational waves (GW170817) and gamma rays
(GRB 170817A) from a binary neutron star merger at approximately 40 Mpc
(Abbott et al. 2017) represents one of the most precise measurements in
astrophysics. The signals arrived within \(\Delta t_{obs} = 1.74 \pm 0.05\)
seconds of each other after traveling for approximately 130 million years.
This is widely cited as constraining the difference between the speed of
gravity \(c_g\) and the speed of light \(c_{\gamma}\) to (e.g., Baker et al.
2017; Creminelli & Vernizzi 2017; Ezquiaga & Zumalacárregui 2017; Sakstein &
Jain 2017):

Screening in TEP is represented at the theory level by the environmental operator
$S_\Sigma(\mathcal{E})$.
Quantities such as
$\rho_T$,
$R_T(M)$,
$S_\oplus(r)$,
compactness $\Phi/c^2$,
local stellar density,
geometric coherence length,
and channel-specific response coefficients
are domain-specific projections of $\mathcal{E}$,
not independent screening mechanisms
and not interchangeable universal thresholds.
Each is an observational transfer model
that parameterizes the same underlying operator
in a regime-appropriate form.

\begin{equation} \label{eq:gl_gw_speed}
\frac{|c_{\gamma}-c_g|}{c} \lesssim 10^{-15}
\end{equation}

This standard translation assumes that any delay is due to a uniform
difference in propagation speed accumulating linearly over the entire
cosmological distance. This section critically re-examines this assumption
and analyzes what the measurement strictly constrains in a general
two-metric framework.

### 4.2 The Common-Path Invariant: A Differential Measurement

A crucial but often overlooked geometric fact is that both messengers
originated from the *exact same coordinate* in distant space. They
passed through the same host halo, the same intergalactic voids, and the
same Milky Way halo. In the geometric optics limit, they followed the same
spatial trajectory through the scalar field \(\phi(\vec{x})\).

**The Common-Mode Cancellation:**

Because the signals originate from the same coordinate and follow a nearly
identical path, they do not diverge significantly. If the metric coupling
contains a conformal component \(\tilde{g}_{\mu\nu} = A^2(\phi) g_{\mu\nu}\),
this factor rescales the common-mode endpoint clock and frequency
calibration for
*both* species identically. Any time dilation caused by passing
through "time-warped regions" of space is experienced by both messengers. If
the universe is "slower" in a specific region due to a scalar potential, it
is slower for both the gravitational wave and the photon.

**Implication for Conformal Coupling (\(A(\phi)\)):**

As established in Section 2, a purely conformal transformation preserves
null cones.
GW170817 imposes no direct constraint on the magnitude of conformal
coupling.
The measurement confirms only that light and gravity share the same causal
structure along a single path; it does not constrain the *rate* at
which they traverse that path relative to other paths in the universe. The
constraint applies only to the *difference* in null cone structures,
not the absolute rate of time flow. The symmetry of this exemption must be
stated with equal precision: the same null-cone invariance that frees the
conformal amplitude from the differential bound also confines its
propagation content to the common-mode endpoint calibration — the conformal
sector contributes exactly zero propagated differential delay between any
two rays (Section 3.1.3; the static-conformal residual vanishes identically,
Paper 19 step_56). The exemption and the inertness are one theorem.

### 4.3 The Operational Reality: Decoupling the Sectors

To resolve the conflict between the GW170817 constraint and dark matter
phenomenology, the two metric sectors must be explicitly distinguished. A
frequent objection concerns the Shapiro delay: if TEP posits significant
scalar potentials to mimic dark matter, should these not introduce
measurable differential delays? The conformal sector can modify the
matter-frame clock-transfer calibration associated with a Shapiro-delay
measurement, while the geometric null-path delay is carried by the
gravitational metric and any backreacted strong-field solution. Same-path
EM–GW comparisons cancel common-mode conformal clock effects.

Since Axiom 1 establishes that photons and gravitational waves traverse the
same null geodesics defined by the geometric metric, they experience an
identical Shapiro delay as they propagate through the gravitational
potential. Consequently, a differential arrival-time measurement like
GW170817 cancels this common-mode geometric delay entirely. The conformal
clock-transfer contribution is also common-mode for same-path EM–GW
propagation and cancels in the differential measurement, so the magnitude of
the conformal potential is not directly constrained by such differential
propagation tests. It remains indirectly constrained by PPN,
equivalence-principle, source-screening, gravitational-redshift, and
clock-comparison tests — and, more bindingly for this paper's mechanism, by
the null-cone invariance itself: the conformal clock-transfer map is a
reconstruction-space field (what a lens model would absorb into convergence,
mass-sheet normalization, or delay calibration), not a propagating delay.
The physically propagating differential residual is the disformal multipath
deformation of Section 3.1.4, bounded by this same measurement to
\(\lesssim 0.2\) s per \(2\) Mpc halo path.

**Principle:**

**Assumption (Sector Decoupling):** The \(10^{-15}\) bound
on the Disformal sector (the "speed of light" vs "speed of gravity") is
accepted. The TEP-GL phenomenology relies on Conformal sector gradients
(the "rate of time"), which this bound does not directly constrain —
and which, by the same null-cone invariance, carry no propagated
differential content at all: their observable role is the
endpoint/common-mode calibration and reconstruction-space clock-transfer
map, bounded by clock-transfer, PPN, redshift, and lensing constraints
after environmental screening is applied, with the propagated sector
carried separately by the GW170817-bounded disformal channel.

This decoupling makes the TEP framework robust against propagation speed
constraints. Consistent with the general disformal relation (Bekenstein
1993), note that the speed of gravitational waves ($c_g$)
constrains the causal structure (the light cone) governed by the disformal
term \(B(\phi)\), while the chronometric component of Phantom Mass arises
from the conformal factor \(A(\phi)\) (the clock rate); coherent optical
lensing additionally involves scalar backreaction and any permitted
disformal response. As long as \(c_g =
c_\gamma\), the rate at which time accumulates along that path is not
determined by EM–GW arrival-time differences. GW170817 strictly constrains
cone tilting, but is insensitive to the common-mode conformal time dilation
that mimics mass.

**Summary of Constraints:**

**Conformal Sector:** Not directly constrained by the
GW170817 differential-propagation bound; independently constrained by
clock, redshift, PPN, equivalence-principle, source-screening and
lensing channels — and, as the binding constraint on the propagation
side, identically zero in propagated differential delay by null-cone
invariance (Section 3.1.3). Its observable content is the
endpoint/common-mode calibration and the reconstruction-space
clock-transfer map.

**Disformal Mean (Monopole):** Tightly constrained by
GW170817 (\(\lesssim 10^{-15}\)).

**Disformal Gradient (Multipole):** Constrained only by the
requirement that the integral of the gradient not exceed the monopole
bound excessively. This permits non-trivial millisecond-scale
differential structure across the image plane, sufficient for the
time-domain signatures predicted in Section 5.

By distinguishing between the *speed of transmission* (directly
constrained by GW170817) and the *rate of proper time accumulation*
(constrained instead by clock, PPN, and redshift channels, and identically
null in propagated differential delay), the conditional
phenomenological viability of TEP as a dark-sector reinterpretation is
established within the screening and amplitude-closure assumptions stated
here — with the propagating discriminator assigned, as in Section 5, to the
disformal multipath channel that GW170817 does bound.

### 4.4 Environmental Screening and Solar System Constraints

A critical quantitative challenge to the TEP framework is the magnitude of
the clock-transfer contrast required to affect cluster lensing
reconstructions. As established in Box 3.1, halo-scale integration over
\(L_{\rm halo} \sim 2\) Mpc gives \(L_{\rm halo}/c \simeq 6.5\times10^6\) yr,
so a path-averaged conformal contrast \(\langle \Delta A\rangle_{\rm path}
\sim 10^{-7}\text{--}10^{-6}\) yields a year-scale reconstruction-space
field — the reconstruction-space quantity of §3.1.3, not a propagated
photon delay. This replaces
the earlier cosmological-integration estimate, which produced unobserved
\(10^3\text{--}10^5\) year gaps and is not the scale required by the Extended
Regime. Even at this reduced contrast, if the same field gradients persisted
unmodified within the Solar System they would violate high-precision
ephemerides constraints (e.g. the Cassini parameter \(\gamma\)).

Screening in TEP is defined at the theory level by the canonical
environmental operator, which acts on the observable Temporal Shear
\(\Sigma_\mu \equiv \nabla_\mu \ln A(\phi)\):

\begin{equation} \label{eq:gl_screening_operator}
\Sigma_\mu^{\rm obs} = \mathcal{S}_\Sigma(\mathcal{E})\,\Sigma_\mu ,
\end{equation}

where the environmental state \(\mathcal{E}\) includes source structure,
scalar gradients, density, compactness, boundary conditions, and coherence
scale. These quantities determine the projection of the underlying temporal
field into an observable clock, dynamical, or lensing response. TEP
screening is defined directly by the environmental projection of Temporal
Shear. No separate screening radius, thin-shell boundary, or imported
modified-gravity mechanism is introduced.

**Principle:**

#### Box 4.1: Canonical Temporal-Gradient Suppression

TEP screening acts directly on the observable Temporal Shear,

\begin{equation}
\Sigma_\mu \equiv \nabla_\mu \ln A(\phi),
\end{equation}

through the canonical environmental operator:

\begin{equation}
\Sigma_\mu^{\rm obs} = \mathcal{S}_\Sigma(\mathcal{E})\,\Sigma_\mu,
\qquad 0 \leq \mathcal{S}_\Sigma(\mathcal{E}) \leq 1.
\end{equation}

The environmental state \(\mathcal{E}\) includes temporal-gradient
strength, density, compactness, source structure, boundary conditions,
and coherence scale. These quantities determine the projection of the
underlying temporal field into an observable clock, dynamical, or
lensing response.

In Solar-System conditions,

\begin{equation}
\mathcal{S}_\Sigma(\mathcal{E}_\odot)\,|\Sigma_\mu|
\ll |\Sigma_\mu|,
\end{equation}

suppressing the locally observable response and preserving precision
tests of GR. Across extended halo and intergalactic paths,

\begin{equation}
\int_\gamma \mathcal{S}_\Sigma(\mathcal{E})\,\Sigma_\mu\,dx^\mu
\neq 0,
\end{equation}

allowing a cumulative open-path clock-transfer contrast even when the
local response is strongly suppressed. The required hierarchy is
therefore a hierarchy in the environmental projection of Temporal
Shear.

The saturation density \(\rho_T\) may be used as an environmental
proximity indicator within \(\mathcal{E}\), but it is not a hard
universal threshold. The fundamental screening object remains
\(\mathcal{S}_\Sigma(\mathcal{E})\).

## 5. Observational Predictions: The Era of Chronometric Mapping

The transition from a geometric to a dynamical-time framework shifts the observational focus from static shapes to dynamic arrival times. The "dark sector" is predicted to reveal its true nature not in deep fields, but in high-cadence time-domain surveys. Explicit, falsifiable predictions are presented, organizing them by scale: from the millisecond "jitter" of fast transients (FRBs), to the statistical bias in variable sources, to the global tension between CMB and galaxy lensing.

### 5.1 The "Jittering" of Lensed Transients

**Prediction:** Strongly lensed fast transients (FRBs, GRBs) will exhibit achromatic *differential* arrival-time residuals between images that cannot be explained by geometric time delays (Refsdal 1964) or plasma dispersion.

In standard GR, the time delay \(\Delta t_{geom}\) between images is fixed by the mass distribution. In TEP, there is an additional propagated arrival-time residual \(\Delta \tilde{\tau}\), carried by the disformal multipath deformation — bounded by GW170817 to \(\lesssim 0.2\) s per \(2\) Mpc halo path — since the conformal sector contributes exactly zero propagated inter-image delay (§3.1.3; Paper 19, step_56). Because \(\phi\) fields in halos may have substructure (or "weather"), this residual varies across the image plane. For a millisecond-duration FRB (e.g., Muñoz et al. 2016), even a tiny gradient in \(\Delta \tilde{\tau}\) will manifest as a timing anomaly in the *relative* arrival times of the images. Unlike plasma dispersion (which scales as \(\nu^{-2}\)), this differential delay is *achromatic* (frequency-independent). The residual is expected to depend on integrated path depth and intervening temporal-field structure, and may therefore correlate with observed redshift; in TEP, redshift here is an observational clock-distance label, not a measure of physical spatial expansion. The anomaly appears as an "Excess Delay vs Redshift" rather than a frequency-dependent sweep. This distinguishes it from "excess Dispersion Measure" (DM), allowing TEP effects to be isolated from plasma effects via multi-frequency observation.

**Target Candidates:** Recent literature has identified specific anomalies suitable for this test. The repeating source *FRB 20190520B* exhibits a "Dispersion Measure Excess" (\(\sim 900\) pc cm\(^{-3}\)) relative to its redshift (Koch Ocker et al. 2022), currently attributed to extreme host density. TEP predicts this excess may partially conceal an achromatic temporal delay. Additionally, *FRB 20190308C* (Chang et al. 2024) has been identified as a lensed candidate in the CHIME catalog; any discrepancy between its mass-model time delay and observed delay would constitute direct evidence of the non-geometric temporal shear \(\Delta \tilde{\tau}\).

**Test Protocol.** No securely multiply-imaged FRB with a published independent lens model is available at the time of writing, so no lensed-FRB residual is claimed here as evidence. The prediction is instead stated as an identifiable measurement, using the blind-prediction residual of Axiom 3 (Section 2.3):

\[
R_{ij} = \Delta t_{ij}^{\rm obs} - \Delta t_{ij}^{\rm GR},
\]

where \(\Delta t_{ij}^{\rm GR}\) must be frozen from an independent lens model before the timing comparison is performed. Each element below is required for the test to be diagnostic; a measurement missing any one of them cannot discriminate TEP from astrophysical delay structure.

| Required element | Specification |
| --- | --- |
| **Secure multiple imaging** | Consistent sub-arcsecond localization and repeated burst morphology across images |
| **Independent lens model** | Frozen, pre-registered prediction \(\Delta t_{ij}^{\rm GR}\) with propagated model uncertainty |
| **Observed delay** | \(\Delta t_{ij}^{\rm obs}\) at high time resolution, corrected for plasma dispersion |
| **Residual** | \(R_{ij}\), with plasma, microlensing, and host-scattering budgets subtracted (Section 2.3) |
| **Discriminator** | Achromatic residual with non-zero ensemble mean, correlated with path environment |

*Table 5.1: Required elements of a diagnostic lensed-FRB timing test. The achromaticity requirement separates a temporal-transport residual from plasma dispersion (\(\propto \nu^{-2}\)); the non-zero ensemble mean separates it from microlensing, which averages to zero with RMS scaling as \(1/\sqrt{N}\).*

### 5.2 The Variability Scatter Relation

**Prediction:** The *dispersion* (scatter) of weak-lensing shear measurements should correlate with the variability/kinematics of the background source population.

A CDM-free coherent halo-lensing amplitude requires an adequate gravitational-metric potential from the TEP fields and baryons; the tested scalar-backreaction and disformal lens configurations have not yet supplied it. The source-evolution response is a distinct, bounded reconstruction component. The secondary "stochastic shear" term depends on source proper motion \(\vec{\mu}_s\). Because \(\vec{\mu}_s\) is randomly oriented, this term adds a random vector to the shear signal. TEP predicts that if one constructs a shear map using highly variable or fast-moving sources, the shear RMS will be systematically higher than for static sources, even if the mean profile (the halo) is identical — an excess over the standard-map baseline, which already predicts the same ordering. The predicted excess is bounded by the Box 3.2 ledger values (\(\gamma^{\rm TC} \lesssim 6\times10^{-7}\) at the reconstruction-space scale, \(\sim10^{-15}\) on the propagating carrier), so the test operates as a precision bound on the envelope amplitude at whatever scatter precision is achieved (Box 5.1). Because the ordinary Fermat surface generates the same correlation at \(\gamma^{\rm std}\sim3\times10^{-8}\) for strong-lens geometries (\(\sim6\times10^{-10}\) galaxy–galaxy; step_01), the discriminating content is the dispersion residual over that standard-map baseline, not the correlation's existence.

**Principle:**

#### Box 5.2: The Einstein Cross Test (Existing Data)

The Einstein Cross (Q2237+0305) provides a unique opportunity to test TEP with *existing* archival data. This quadruply-imaged quasar has:

- **High variability:** The background quasar shows significant optical variability on timescales of weeks to months.

- **Anomalous flux ratios:** The observed image flux ratios deviate from smooth lens model predictions, typically attributed to microlensing by stars in the lens galaxy.

- **Extensive monitoring:** Decades of photometric data exist (OGLE, Gaia, HST).

**Amplitude estimate.** Two response routes connect the temporal field to the observed flux ratios, and the bookkeeping of Box 3.2 applies to both. The Jacobian route gives \(\delta\mu/\mu \sim \mu\,\gamma^{\rm TC}\): at magnification \(\mu \sim 10\) this is \(\sim 6\times10^{-6}\) at the reconstruction-space scale and \(\sim10^{-14}\) on the propagating carrier — four orders of magnitude below the observed 10–30% anomalies even at the envelope. The emission-time route gives \(\delta F/F \sim \dot{\nu}\,\delta t_{\rm em}\): for a quasar varying fractionally at \(\dot{\nu} \sim 10\%\) per month, the propagating-carrier delay (\(\lesssim 0.2\) s) contributes \(\delta F/F \sim 10^{-8}\), while a year-scale propagating reading of the clock-transfer map would produce order-unity phase-correlated flux swings that are not observed. The Einstein Cross anomalies therefore remain in the stellar-microlensing regime and are not claimed as a TEP signal at any admissible amplitude.

**TEP Prediction:** The discriminating content of this test is the correlation structure, not the anomaly amplitude. If a residual emission-time contrast \(\delta t_{\rm em}\) exists between the four sightlines, the apparent flux-ratio anomaly amplitude scales with the source's instantaneous variability rate:

- During periods of rapid quasar variability, the temporal-composite contribution to flux ratios is *larger* (\(\delta F/F \propto \dot{\nu}\,\delta t_{\rm em}\)).

- During quiescent periods, it regresses toward the smooth-lens prediction.

- Unlike stellar microlensing, which is uncorrelated with the source's intrinsic state, the temporal contribution is coherent with the quasar's own variability phases—effectively turning "on" during violent source activity.

**Status:** This test can be performed immediately using archival OGLE light curves cross-correlated with flux ratio measurements, and it functions quantitatively as a bound: at \(\sim 1\%\) photometric precision and \(\dot{\nu} \sim 10\%\) per month, the absence of a variability-phase-correlated residual bounds any coherent emission-time contrast at \(\delta t_{\rm em} \lesssim\) a few days — sitting between the millisecond propagating carrier and the excluded year-scale propagating reading. Detection of the conservative-baseline carrier itself requires the arrival-time residual protocol of §5.1. This is flagged as a priority archival analysis.

### 5.3 The CMB-Galaxy Lensing Tension

**Prediction (Regime II):** TEP-GL predicts that galaxy weak-lensing measurements can contain a source-dependent covariance contribution absent from CMB lensing, even when their mean inferred amplitudes are statistically consistent.

While the CMB is effectively a static backlight (zero intrinsic evolution), galaxy sources are dynamic population. Under TEP, the stochastic component of the clock-transfer signal (driven by source proper motion, see Section 5.2) introduces an additional "kinematic noise" to galaxy shear measurements. Because the CMB is static, it is immune to this effect. Consequently, TEP predicts that precision cosmology inferred from galaxy weak lensing carries an unmodeled source-dependent covariance term absent from CMB lensing. The quantitative reach of that term is set by Box 3.2: its variance contribution \(\gamma_{\rm TC}^{2} \sim 4\times10^{-13}\) at the reconstruction-space scale (\(\sim2\times10^{-30}\) on the propagating carrier) is far below the shape-noise variance \(\sim 0.09\), so it cannot supply the percent-level amplitude of the observed \(S_8\) tension. The prediction is the existence and source-class structure of the covariance term, not an explanation of the tension's magnitude.

**Principle:**

#### Box 5.3: Source-Class-Dependent Shear Covariance

**Observed Situation:** Current weak-lensing results are survey-dependent: DES Y6 continues to favour a lower \(S_8\) than the combined CMB determination, whereas KiDS-Legacy is statistically consistent with Planck. TEP-GL therefore does not identify a universal mean \(S_8\) offset as its prediction; its distinctive prediction is an additional source-dependent covariance that should track source temporal structure and survey selection.

- *Planck* CMB (2018): \(S_8 = 0.834 \pm 0.016\)

- DES Y6 (2025): \(S_8 = 0.789 \pm 0.012\), \(\sim 2.6\sigma\) from combined Planck+ACT+SPT

- KiDS-Legacy (2025): \(S_8 = 0.815^{+0.016}_{-0.021}\), \(0.73\sigma\) from Planck

**TEP Interpretation:** Previous iterations of TEP considered secular source evolution as a driver for coherent shear offsets, but the magnitude (\(\sim 10^{-6}\)) is too small to explain the 5% tension. The stochastic-shear covariance term is likewise bounded: \(\gamma_{\rm TC}^{2}/\sigma_{\rm sh}^{2} \sim 4\times10^{-12}\) relative to shape noise at the reconstruction-space scale, so this channel does not resolve the \(S_8\) tension; its role is diagnostic — a source-dependent covariance signature whose presence, not its magnitude, is the observable.

**Mechanism:** Standard maximum-likelihood estimators weight data by the inverse covariance (\(C^{-1}\)). Standard analyses assume shear noise is dominated by random galaxy orientations ("shape noise"). If the covariance matrix omits a source-dependent kinematic term (\(\sigma^2_{\mu}\)), the relative weighting of high-variance regions such as cluster outskirts is misspecified, and the recovered clustering amplitude is biased.

- **Source-Dependent:** Correlated with galaxy type and redshift (via proper motion).

- **Unmodeled:** Not present in standard covariance matrices.

**Result:** Unmodeled excess variance in the likelihood analysis acts as a potential source of systematic bias. However, a zero-mean covariance term does not by itself determine the sign of the inferred \(S_8\) shift; establishing the direction requires an explicit estimator-level calculation for each survey pipeline, which is not carried out here. The CMB, being static, carries no such kinematic covariance term.

**Prediction:** The falsifiable TEP-GL prediction is not a specific \(S_8\) shift but the existence of an additional source-dependent shear covariance: after standard shape-noise controls, residual shear covariance should vary with source variability, proper motion, or temporal structure. The cosmological mean-growth prediction belongs to the TEP-HC (Paper 18) perturbation closure; the GL-specific discriminator is this source-class dependence. Whether it contributes to the observed \(S_8\) tension, and in which direction, depends on the survey estimator.

### 5.4 Comparison of Predictions: TEP-GL vs. Particle Dark Matter

The following table summarizes the distinguishing predictions of the two frameworks:

| Observable | Particle DM Prediction | TEP-GL Prediction |
| --- | --- | --- |
| **Lensed FRB timing** | GR lens delays from baryons, particle dark matter and substructure; no TEP-specific residual correlated with temporal-field environment after lens-model controls | Achromatic *residual* anomaly (ms-scale) |
| **Source-dependent Shear** | No TEP-specific source-temporal correlation after intrinsic-alignment, selection and measurement-systematic controls | **Excess Scatter** (noise scales with \(\mu_s\); bounded amplitude per Box 3.2) |
| **Source variability–lens mass correlation** | None (mass is source-independent) | Source-class-dependent reconstruction residual correlated with source temporal structure; amplitude determined by \(\kappa_{\rm lens}\) and the environmental transfer function |
| **CMB lensing** | Standard convergence | Source-dependent temporal-composite term absent at leading order; the required CDM-free scalar-metric lensing amplitude remains to be derived and tested against $C_\ell^{\phi\phi}$ |
| **Galaxy weak lensing** | Source-independent shear consistent with the physical mass distribution; no TEP-specific source-temporal covariance | Additional source-class-dependent covariance absent from the CMB temporal-composite channel; TEP-GL does not independently fix the sign of the mean shift |
| **Chromatic dependence** | None | None (both achromatic) |
| **Direct detection experiments** | Expected signal (WIMP recoil accounting for lensing/rotation/CMB) | No particulate signal required by the intended ontology; Phantom Mass alone does not close the CMB and cluster lensing requirement |

A distinctive TEP-GL discriminator is the additional source-dependent component of the inferred lensing signal above the standard delay-map baseline. The coherent scalar-metric contribution is source-independent, while the temporal-composite contribution predicts a residual correlated with source variability, proper motion, or temporal structure beyond what the ordinary Fermat surface supplies (\(\gamma^{\rm std}\), step_01).

### 5.5 Falsification Criteria

TEP-GL is a falsifiable hypothesis. The following observations would exclude specific regimes or the framework entirely:

- **conservative baseline Exclusion:** If precision timing of strongly lensed FRBs yields achromatic residuals consistent with zero to better than 0.1 ms across diverse lens environments, the conservative baseline parameter space is excluded.

- **Universal Shear Scatter:** If the intrinsic scatter of weak-lensing shear measurements, after correcting for measurement noise, equals the standard delay-map prediction \(\gamma^{\rm std}=\mu_s\,\partial_j\Delta T_{\rm Fermat}\) across all source kinematic classes — i.e., no residual above the baseline — the stochastic temporal shear mechanism is excluded at that precision.

- **CMB-Galaxy Agreement:** CMB–galaxy agreement below 1%, after source and survey controls, excludes a temporal-composite contribution above that level. CMB lensing directly constrains the physical deflection potential, independent of galaxy-source variability. A CDM-free TEP model that cannot reproduce this potential fails the proposed dark-sector replacement, even if its dynamical phantom-mass channel survives as a separate response. Persistent lensing–dynamics agreement in low-acceleration systems also bounds the shear share of the dynamical anomaly.

- **Phantom Mass (decisive):** In isolated, low-acceleration systems where \(S_\Sigma\to1\), the mass inferred from dynamics should exceed the mass inferred from lensing by the shear share—of order unity where the shear is fully active. Environment- and acceleration-resolved comparison of rotation-curve and weak-lensing mass on the same systems is the decisive test: detection of the predicted dynamical–lensing difference—the phantom mass—is a distinctive positive signature no particulate model reproduces; its persistent absence, given TEP's matter-only deflection, caps the shear's contribution to the dynamical anomaly at the observed consistency level.

- **Chromatic Anomaly:** If any timing or morphological anomaly shows wavelength dependence after correction for plasma dispersion and dust, the achromatic prediction of two-metric coupling is falsified. This would indicate conventional astrophysical systematics rather than metric effects.

- **Direct Detection:** A confirmed detection of dark matter particles that quantitatively accounts for the relevant lensing, rotation-curve, and CMB phenomenology would falsify the strong TEP dark-sector ontology. Detection of an exotic particle that does not account for these observations would not by itself falsify TEP; the particle would be an additional component, and TEP would then be tested by whether temporal-transport geometry still predicts residuals unaccounted for by the particle model.

Joint satisfaction of these null thresholds excludes the distinctive chronometric and temporal-composite predictions at the amplitudes specified here. The coherent scalar-backreaction sector is separately tested by CMB and galaxy lensing consistency against its frozen HC/GL prediction. The framework does not claim immunity from observation; the claim is that the observations required to test TEP have not yet been performed with sufficient precision.

**Principle:**

#### Box 5.1: Quantitative Falsification Thresholds

To ensure rigorous falsifiability, explicit null-result thresholds are specified for each prediction channel:

| Test | Sample Size | Precision Required | Null-Result Threshold | Regime Falsified |
| --- | --- | --- | --- | --- |
| **Lensed FRB Timing** | ≥10 lensed FRBs | <0.1 ms timing | 95% upper bound on ensemble achromatic residual amplitude below 0.1 ms | conservative baseline |
| **Shear-Variability Correlation** | ≥1000 lenses per class | <0.5% shear scatter | No correlation at >3σ | temporal-composite dynamic channel |
| **CMB-Galaxy \(S_8\) Tension** | CMB-S4 + LSST | <1% \(S_8\) agreement | Statistically consistent agreement (< 1\(\sigma\)) | temporal-composite contribution above 1% |
| **Variability-Mass Correlation** | ≥100 lenses with varied sources | 10% mass precision | No correlation at >3σ | Source-dependent reconstruction channel |

**Amplitude probed by each threshold.** The thresholds act on different carriers (Box 3.2), and the table is populated accordingly. The lensed-FRB row acts on the propagating delay field directly: a 0.1 ms ensemble bound excludes the disformal multipath carrier at three orders of magnitude below the GW170817-saturating level (\(\sim0.2\) s per \(2\) Mpc halo path) — equivalently, it bounds the disformal normalization \(D(\partial_{\hat{n}}\phi)^2\) to \(\sim 2\times 10^{-18}\) on halo paths, the flagship, fully powered test of the same \(B(\phi)\) instrument the holonomy program probes on the odd-parity channel. The shear-variability row bounds \(\gamma^{\rm TC} \lesssim 5\times10^{-3}\), equivalent to a delay-gradient bound \(\nabla(\Delta\tilde{\tau}) \lesssim 2\times10^{4}\) yr/arcsec — a weak upper limit on the reconstruction-space scale, not a test of the carrier. The \(S_8\) row bounds fractional source-dependent covariance at the percent level; the temporal-composite term sits at \(\sim4\times10^{-12}\) relative to shape noise even at the envelope, so this row's content is the structural existence test rather than an amplitude reach. The variability–mass row probes \(\delta\kappa \sim \gamma^{\rm TC} \gtrsim 10^{-1}\) directly, and through the delay-absorption route bounds any propagating residual at \(\lesssim 10\%\) of the Fermat delay (\(\sim10\) d per 100 d) — already excluding a propagating year-scale reading, consistent with the conformal null of §3.1.1. Together the rows bound the propagating delay field at every scale between the millisecond and the tens-of-days level, with the chronometric sector confined to the reconstruction space where the Paper-19 residual program operates.

**Joint Channel Exclusion:** If all four null-result thresholds are met simultaneously, the distinctive chronometric and temporal-composite predictions of TEP-GL are excluded at the amplitudes specified here. The coherent scalar-backreaction sector remains independently testable through its frozen HC/GL prediction for CMB and galaxy lensing. TEP-GL as a complete lensing realization is excluded only if both the time-domain/source-dependent channels and the independently specified coherent optical prediction are ruled out.

**Timeline:** Tests (1) and (4) are achievable within 5–10 years (CHIME, DSA-2000, Rubin/LSST). Tests (2) and (3) require next-generation surveys (CMB-S4, Euclid) with ~10-year horizons. A definitive verdict on TEP-GL is therefore expected by ~2035.

## 6. Discussion: The Dark Sector — Phantom Mass in Dynamics and Lensing

### 6.1 Limitations of the "Stack of Corrections"

Gravitational physics has historically advanced by refining the fundamental
geometric framework rather than adding ad-hoc corrections. TEP represents a
similar upgrade to the fundamental object, following the natural historical
progression of physical theory:

- **Newton:** Gravity is a Force; Time is Absolute.

**Einstein:** Gravity is Geometry; Time is Relative
(Coordinate-Dependent).

**TEP:** Gravity is Geometry; Time is a
*Dynamical Field*.

By treating the rate of proper time accumulation as a physical field with
its own degrees of freedom (rather than a fixed function of the metric), TEP
unifies the "stack" into a single framework. The "dark matter" anomaly is
the observation that this field has spatial gradients.

### 6.2 CMB Lensing and the Integrated Sachs-Wolfe Constraint

A scalar field capable of generating year-scale reconstruction-space
contrasts on
cluster scales raises a critical question: what are the implications for the
Cosmic Microwave Background (CMB)? Two potential tensions must be addressed.

#### 6.2.1 The ISW Effect

The Integrated Sachs-Wolfe (ISW) effect arises when CMB photons traverse
time-evolving gravitational potentials. In TEP, the conformal factor
\(A(\phi)\) contributes an additional term to the photon temperature
perturbation:

\begin{equation} \label{eq:gl_isw}
\frac{\Delta T}{T}\bigg|_{\text{TEP}} = \int \frac{\partial \ln
A(\phi)}{\partial t}\, dt
\end{equation}

For TEP to remain consistent with *Planck* constraints on the ISW
amplitude, one of the following must hold:

**Quasi-Static Regime:** The scalar field evolves slowly
(\(\partial_t A \ll H_0 A\)), so the TEP contribution to ISW is
subdominant to the standard \(\dot{\Psi}\) term. This is natural if
\(\phi\) tracks the matter distribution adiabatically.

**Cancellation:** In some scalar-tensor theories, the
conformal ISW contribution partially cancels the metric ISW, leaving the
net effect within observational bounds (cf. Amendola et al. 2008).

**Principle:**

#### Box 6.1: Order-of-Magnitude ISW Consistency Check

Conditional on the HC tracking closure in which \(\phi\) follows the
matter distribution adiabatically, the resulting order-of-magnitude
estimate satisfies the quasi-static ISW bound.

**Setup:** The conformal factor is \(A(\phi) = e^{-u}
\approx 1 - u\), with the field excursion \(u \sim 10^{-6}\) on halo
scales (\(u\) is the canonical dimensionless field of Paper 0; the symbol
\(\alpha(\phi) \equiv d\ln A/d\phi = \beta_A\) is reserved for the
coupling function). The following
estimate uses the conventional reference-background variables employed by
the HC linear-transfer representation (Paper 18). Here \(H_{\rm ref}(z)\)
is an observational/reference inverse-time scale and \(a_{\rm eff}=
A_{\rm clock}\); neither denotes physical expansion of the underlying
spatial geometry. The ISW constraint requires:

\begin{equation} \label{eq:gl_isw_constraint}
\left|\frac{\partial \ln A}{\partial t}\right| =
|\dot{u}| \ll
H_0
\end{equation}

**Estimate of \(\dot{u}\):** If \(\phi\) tracks the
matter distribution adiabatically (sourced by \(T^\mu_\mu\)), then
\(u\) evolves on the timescale of structure formation:

\begin{equation} \label{eq:gl_u_dot}
\dot{u} \sim u \cdot \frac{\dot{\rho}}{\rho} \sim u
\cdot H_{\rm ref}(z) \cdot f_{\rm ref}(z)
\end{equation}

where \(f_{\rm ref}(z) \equiv d\ln D/d\ln a_{\rm eff} \approx
\Omega_m(z)^{0.55}\) is the growth rate and \(a_{\rm eff}=A_{\rm clock}\).
At \(z \sim 0.5\) (peak ISW sensitivity), \(f_{\rm ref} \approx 0.8\)
and \(H_{\rm ref}(z) \approx 1.2 H_0\).

**Result:**

\begin{equation} \label{eq:gl_isw_result}
\frac{|\dot{u}|}{H_0} \sim u \cdot f_{\rm ref} \cdot \frac{H_{\rm ref}(z)}{H_0}
\sim 10^{-6} \times 0.8 \times 1.2 \approx 10^{-6}
\end{equation}

This is six orders of magnitude below the ISW
constraint threshold (\(\lesssim 0.1\)). The quasi-static approximation
is therefore satisfied under this tracking closure; the result should
not be interpreted as independent derivation of that closure within
TEP-GL.

**Physical Interpretation:** The scalar field \(\phi\)
varies spatially (creating "dark matter" halos) but evolves temporally
only as fast as the underlying matter distribution. Year-scale
*spatial* delays across an image plane are compatible with
cosmologically slow *temporal* evolution because the delay
gradient is set by the static \(\nabla u\), not by \(\dot{u}\).

#### 6.2.2 CMB Lensing Power Spectrum

The CMB lensing convergence power spectrum \(C_\ell^{\kappa\kappa}\) is
measured to high precision by *Planck* and ACT. In standard
\(\Lambda\)CDM, this is sourced entirely by the integrated mass
distribution. Consistent with the optical-tidal decomposition of §3.1.4, the
physical angular remapping in TEP is carried by the baryonic term, the
scalar-backreaction correction to the Einstein-frame geometry, and any
permitted disformal contribution:

\begin{equation} \label{eq:gl_kappa_tep}
\kappa_{\text{TEP}}^{\rm phys}
= \kappa_{\text{baryon}}
+ \delta\kappa_{g[\phi]}
+ \delta\kappa_{B}
\end{equation}

The conformal sector may additionally enter the *inferred*
convergence through the chronometric reconstruction mapping,

\begin{equation} \label{eq:gl_kappa_inferred}
\kappa_{\text{TEP}}^{\rm inferred}
= \kappa_{\text{TEP}}^{\rm phys}
+ \delta\kappa_{A,\,\rm recon},
\end{equation}

but it does not independently deflect the CMB rays, since conformal
transformations preserve null cones (Axiom 1).

For the CMB (a static, non-evolving source), the temporal-composite response
term vanishes identically—there is no source proper motion or intrinsic
variability on lensing timescales to couple to the delay gradient. Removing
that term does *not* make the CMB insensitive to TEP: it means CMB
lensing constrains the coherent scalar-metric perturbation sector rather than
source-evolution smearing.

**Implication:** CMB lensing tests the source-independent
gravitational-metric potential, not the temporal-composite response of a
variable galaxy. Paper 18 evolves scalar perturbations through its
Bellini–Sawicki implementation, but its Planck low-$\ell$ and lensing
likelihood retains the standard cold-dark-matter fluid
($\Omega_{\rm cdm}h^2=0.1155\pm0.0042$ in the primary posterior).
That fit validates an implementation under a CDM-containing background;
it does not establish that the TEP scalar and baryons source the observed
CMB lensing potential without CDM. A CDM-free prediction of
$C_\ell^{\phi\phi}$, with the same field configuration checked against
galaxy and cluster lensing, remains the required ontology test.

#### 6.2.3 Parameter Space Constraints

Combining ISW and CMB lensing constraints with the continuous gradient-suppression
screening framework (Box 4.1) defines a narrow but viable parameter window:

| Constraint | Requirement | Status |
| --- | --- | --- |
| Solar System (Cassini) | \(\mathcal{S}_\Sigma(\mathcal{E}_\odot)\,|\Sigma| \ll |\Sigma|\) | Satisfied via environmental suppression |
| Cluster Lensing | Optical-sector requirement: \(\kappa\sim10^{-2}\text{--}10^{-1}\) via scalar backreaction; chronometric integral \(\left|\int_{\gamma_{\rm halo}} \mathcal{S}_\Sigma(\mathcal{E})\,\Sigma_\mu\,dx^\mu\right| \sim 10^{-7}\text{--}10^{-6}\) is reconstruction-space only | **Not closed in the tested SN Refsdal configuration:** scalar backreaction evaluated at \(\kappa_\phi\approx4\times10^{-5}\), \(\sim2\times10^{3}\) short (Paper 19, Step 61); the tested disformal path is \(\sim5\times\) short (Step 63). This profile-specific bound is not a no-go theorem for every cosmological scalar-metric configuration |
| ISW (*Planck*) | \(\partial_t \ln A / H_0 \lesssim 0.1\) | Conditional on HC tracking closure |
| CMB Lensing | \(\delta\kappa_{g[\phi]} + \delta\kappa_B\) must satisfy the HC/CMB lensing spectrum constraint; \(\delta\kappa_{A,\rm recon}\) treated separately | Open CDM-free source-to-metric closure. Paper 18 includes a standard CDM density in the lensing likelihood; that result alone cannot satisfy this requirement |

The scalar-backreaction calculation on the adopted SN Refsdal lens
geometry (Paper 19, Step 61) gives
\(\kappa_\phi\approx4\times10^{-5}\), about \(2\times10^{3}\) below the
convergence needed in that reconstruction; the tested disformal path is
also below the Refsdal delay residual under the measured halo
deprojection (Step 63). This excludes those specific configurations
as the missing optical amplitude, not every metric potential that could
be generated by a cosmological TEP field. The dynamical–lensing mass
difference separately tests the phantom-force response. A CDM-free
calculation of the absolute cluster and CMB lensing potentials remains
open and cannot be inferred from that difference.

**Principle:**

#### Box 6.3: Cross-Scale Temporal-Gradient Constraint

A viable TEP realization must produce a strongly suppressed observable
Temporal Shear in local high-precision environments while retaining a
nonzero integrated temporal-gradient response across extended halo
paths:

\begin{equation}
\mathcal{S}_\Sigma(\mathcal{E}_\odot)\,|\Sigma|
\leq \Sigma_{\rm local}^{\rm max},
\end{equation}

\begin{equation}
\left|
\int_{\gamma_{\rm halo}}
\mathcal{S}_\Sigma(\mathcal{E})\,\Sigma_\mu\,dx^\mu
\right|
\sim 10^{-7}\text{--}10^{-6}.
\end{equation}

These are constraints on one continuous environmental operator, not
independently adjusted couplings at different scales. The Solar-System
bound is satisfied when the environmental projection
\(\mathcal{S}_\Sigma(\mathcal{E}_\odot)\) suppresses the locally
observable Temporal Shear below precision-test thresholds. The halo
constraint is satisfied when the same operator, acting across an
extended path through lower-density environments, permits a cumulative
clock-transfer contrast of order \(10^{-7}\text{--}10^{-6}\) on the
matter-clock congruence — the reconstruction-space field of §3.1.3,
which is endpoint-determined for photons and is not a propagated delay.

### 6.3 Interpretational Challenges

TEP effects mimic standard lensing signatures, making them difficult to
distinguish without time-domain analysis.

**Static Degeneracy:** Most lensing data are analyzed under
static assumptions. In this limit, the conformal sector enters as a
reconstruction degeneracy — the endpoint-determined clock-transfer map
defined through $A(\phi) = \exp(\beta_A \phi/M_{\rm Pl})$ and the
line-of-sight field profile $\phi(r)$ is absorbed into mass-sheet and
delay normalization rather than into propagated arrival times (Section
3), while optical convergence and shear are carried by the
scalar-backreaction and disformal channels. The predicted
reconstruction-space map is qualitatively similar to the observed map;
a full quantitative comparison requires the source light-curve model,
which is the next pipeline step.

**Differential vs. Common-Mode Effects:** The GW170817
constraint is often interpreted as excluding modified metric couplings.
However, as shown in Section 4, this constraint applies to the
differential disformal sector. Conformal proper-time dilation is a
*common-mode effect* for co-propagating signals, leaving the
"speed of gravity" constraint satisfied while permitting significant
time-domain phenomenology.

### 6.4 Reinterpreting the Evidence: Multipath vs. Single-Path

When viewed through the lens of TEP, the disparate constraints on the dark
sector resolve into a consistent picture based on signal topology:

**Lensing (Multipath):** Observations that require "dark
matter" (e.g., lensing) are fundamentally
*multipath* measurements. These different pathways sample
different values of the time field \(\phi\), creating a differential
clock-transfer field that isochronous reconstruction reads as "phantom
mass," while any propagated differential delay rides only on the
backreacted and disformal sectors.

**GW170817 (Single-Path):** Observations that constrain
"modified gravity" (GW170817) are fundamentally
*single-path* measurements. The signals originate from the same
coordinate and traverse the same time-warped regions. The temporal
distortions are common-mode and cancel out.

The apparent contradiction—"how can gravity be modified enough to create
dark matter but unmodified enough to pass GW170817?"—is resolved. TEP
introduces the temporal field as the additional physical degree of freedom;
its conformal sector governs clock transport without bending null geodesics
or shifting propagated arrival times,
while its stress-energy and strong-field operators can backreact on the
Einstein-frame geometry (Bahrain, Paper 28). The differential-propagation
bound constrains the disformal sector, not the common-mode conformal clock
sector. Time manifests as a propagated differential observable only through
non-exact transport on divergent paths; in the exact conformal sector it
manifests as a reconstruction degeneracy.

### 6.5 Path-Dependent Distance/Proper-Time Ratio

If TEP is correct, then local \(c\) remains invariant, but the
inferred ratio between spatial separation and matter-clock transfer
registered between endpoints
along extended paths is path dependent. This challenges the foundational
assumption used to interpret all astrophysical data.

**Standard Assumption:** The universal clock rate is
constant; therefore, any anomaly in \(t\) must be due to extra path
length (spatial curvature) or extra mass (Shapiro delay). Conclusion:
particulate *dark matter* is inferred.

**TEP Reality:** The matter proper-time accumulation rate
\(d\tilde{\tau} = A(\phi) d\tau_g\) varies with location. The anomaly
in inferred travel time is due to the scalar field gradient modulating
the clock-transfer field registered by matter congruences along the
path, not to a variation in local \(c\).
Conclusion: apparent *dark matter* is reconstructed temporal
transport.

TEP removes the need for an invisible substance by correcting the assumption
that a single universal clock rate governs all paths, rather than by
asserting a variable speed of light.

This is the local multipath analogue of the cosmological TEP mapping:
conventional cosmology reconstructs observed redshift as spatial expansion,
whereas TEP attributes it to the evolution of the conformal proper-time map
on an underlying static spatial geometry (Athens, Paper 26; Thika, Paper 27).
In lensing, the corresponding reconstruction can project temporal transport
into inferred spatial mass. The two effects — dark matter and cosmic
expansion — are parallel temporal-to-spatial reconstruction artefacts in
TEP, not independent ad hoc mechanisms.

### 6.6 TEP as a Bridge Between Paradigms

TEP offers a potential unification of competing frameworks:

**CDM:** For the dynamical sector, TEP offers a candidate
temporal-field origin for the mass anomaly ordinarily ascribed to Cold
Dark Matter: the Temporal Shear acts on matter trajectories as the
extra pull Newtonian analysis counts as a halo. In the lensing sector
the correspondence is an inference degeneracy, not a deflection
mechanism: real lensing is matter-sourced, so the CDM-like lensing
phenomenology is covered only to the extent that the inferred excess
is reconstruction-space or that the predicted phantom mass is
confirmed. That comparison is the decisive open test of this work.

**MOND:** In low-acceleration environments,
environmentally active Temporal Shear supplies a candidate common
origin for MOND-like scaling. This paper establishes the
acceleration-scale correspondence but does not independently derive
the complete MOND interpolation law.

TEP provides a single temporal-gradient framework within which CDM-like
large-scale phenomenology and MOND-like low-acceleration behaviour may
emerge in different environmental projections.

**Principle:**

#### Box 6.2: Relation to Low-Acceleration Phenomenology

In TEP, MOND-like phenomenology is associated with the environmental
activation of observable Temporal Shear in low-acceleration, weakly
suppressed systems. The canonical screening operator
\(\mathcal{S}_\Sigma(\mathcal{E})\) becomes weak in low-gradient
galactic environments, allowing the observable Temporal Shear response
to become active. This supplies a candidate origin for MOND-like
phenomenology without modifying the local value of \(c\).

The empirical coincidence

\begin{equation} \label{eq:gl_acceleration}
a_T \sim c H_0
\end{equation}

identifies the relevant observational acceleration scale, where \(H_0\)
is the conventional inverse-time scale encoded by the cosmological
clock map rather than physical spatial expansion. In TEP, \(H_0\) is
not identified with \(\dot a_m/a_m\), since \(a_m = 1\).

**Numerical Check:**

\begin{equation}
a_0 \sim c H_0 \approx (3 \times 10^8\ \text{m/s}) \times (2.2 \times
10^{-18}\ \text{s}^{-1}) \approx 6.6 \times 10^{-10}\ \text{m/s}^2
\end{equation}

This lies within a factor of about five of the empirical MOND value
\(a_0 \approx 1.2 \times 10^{-10}\) m/s². The canonical TEP acceleration scale is the derived cosmological-horizon scale \(g_t = cH_0/(2|\beta_A|) \approx 3.4 \times 10^{-10}\) m/s² (Paper 0 \S2.2, v0.15); the SPARC-extracted empirical benchmark \(g_{\rm TEP} \approx 5 \times 10^{-10}\) m/s² (Paper 0 \S7; Paper 10) independently corroborates the same order and matches the ambient Galactic shear \(a_{\rm amb} \approx 3.9 \times 10^{-10}\) m/s² at the solar circle. The environmental transition is supplied by the nested two-body operator \(\mathcal{R}(s)=\mathcal{S}_\Sigma(X_{\rm env})^2\,y(s)\) — the effective pairwise projection of the master environmental operator \(\mathcal{S}_\Sigma(\mathcal{E})\) under the derived kinetic completion \(P=X-V+X|X|/\Lambda_X^4\) (Paper 0 \S2.2, v0.15, machine-checked benchmark table). TEP attributes this
cross-scale relation to the same temporal-gradient structure
represented by \(\mathcal{S}_\Sigma(\mathcal{E})\). The defensible
statement is that TEP produces an acceleration scale of cosmological
magnitude, which suggests that TEP and MOND phenomenology may share a
common origin. This matches the level of claim established in TEP-UCD
(Paper 6); TEP-GL does not independently derive the numerical MOND
acceleration scale.

**Physical Interpretation:** Low-acceleration
phenomenology arises in TEP because the environmental operator
\(\mathcal{S}_\Sigma(\mathcal{E})\) leaves the Temporal Shear response
active precisely in low-gradient regions. Regions with internal
accelerations \(a \lesssim g_t\) are weakly screened and the temporal
gradient contributes; regions with \(a \gtrsim g_t\) are strongly
screened and follow Newtonian dynamics. The low-gradient scalar
profile, its metric backreaction, and the reconstruction response must
be fitted jointly to galaxy and lensing data before the MOND
transition can be claimed as derived.

### 6.7 Convergence of Evidence

While TEP-GL is a theoretical proposal, it is notable that multiple
independent anomalies in current cosmology converge on the phenomenology
predicted by this framework. These tensions, often treated as separate
puzzles, may represent a single systemic failure of the isochrony
assumption.

| TEP-GL Prediction | Existing Observational Anomaly | Status |
| --- | --- | --- |
| **Source-Dependent Shear**
(Kinematic noise bias; bounded at
\(\gamma_{\rm TC}^2/\sigma_{\rm sh}^2 \sim 4\times10^{-12}\),
Box 5.3) | **\(S_8\) Tension**
Survey-dependent: DES Y6 lower than CMB; KiDS-Legacy
consistent with Planck. | **Motivating Consistency** |
| **Mass-Sheet Degeneracy**
(Temporal vs Spatial) | **\(H_0\) Tension**
Time-delay cosmography (\(H_0 \approx 73\)) conflicts with
CMB (\(H_0 \approx 67\)). The chronometric entry is a
degeneracy statement, not a supply channel: a common-mode
endpoint rescaling acts on inferred \(D_{\Delta t}\) exactly
as an external convergence sheet does, but under the
present-epoch convention its amplitude is the uniform
local-well residual \(A_o \approx 1-10^{-7}\) — far below
the tension and identical for every lens system. The full
channel audit on the real TDCOSMO-2025 systems (Paper 19,
Step 58) confirms the propagated sector is clean at
\(\lesssim 10^{-8}\) fractional (\(\sim 10\) ms
ceilings on \(10\,R_{\rm E}\) traverses) and finds the only
order-percent route to be the dynamical–lensing mass
difference in the velocity-dispersion prior — in the direction that elevates
inferred \(H_0\) — while the mundane mass-model floor is
\(\sim 6\%\) (SDSS1206+4332 power-law vs composite). The
corpus's quantitative \(H_0\) channel is the Cepheid
clock-bias sector (TEP-H0, Paper 11), a different
projector. | **Degeneracy-level** |
| **temporal-composite response**
(source-evolution response) | **Flux Ratio Anomalies**
Substructure required to explain ratios is often not found;
"phantom" substructure. TC contribution bounded at
\(\delta\mu/\mu \lesssim 10^{-5}\) (Box 5.2). | **Amplitude-bounded** |
| **Variability-Shear Correlation** | **Einstein Cross Anomalies**
Existing Einstein Cross monitoring provides archival data
suitable for testing the predicted variability-phase
correlation; no dedicated TEP correlation analysis has yet
been performed (Eigenbrod et al. 2008). | **Untested** |

The theory supplies testable temporal channels on existing lensing and
timing observations; the present analysis does not claim that their
source-independent lensing amplitudes have already been reproduced.

### 6.8 The Path Forward

The analysis shows that a new particulate dark component is not
required by the temporal-field ontology: the same scalar configuration
can produce dynamical mass-inference and source-dependent reconstruction
signatures. Whether that suffices for the full dark sector is decided by
two distinct tests — the matched dynamical–lensing phantom-mass
comparison and a CDM-free calculation of the absolute lensing potential.
For particulate dark matter to remain necessary, the distinctive TEP
residuals must be excluded at the required precision.

Three concrete consequences follow directly from the phantom-mass mechanism and require no further
model-building:

*Lensing radial-acceleration relation.* Because photon trajectories track the matter-sourced
geometry alone, the acceleration profile reconstructed from weak-lensing mass maps should follow the
baryonic distribution — $g_{\rm lens} \simeq g_{\rm bar}$ — in the same systems where the dynamical
radial-acceleration relation departs from it. The dynamical–lensing divergence is therefore predicted
to be systematic in the radial-acceleration plane, not a scatter of independent anomalies, and is
testable galaxy-by-galaxy wherever both inference channels exist.

*Isolation dependence.* The phantom mass is largest for isolated, diffuse, low-acceleration
systems ($a \lesssim g_t$, $\mathcal S_\Sigma \to 1$) and is suppressed toward zero for galaxies embedded
in high-acceleration environments — cluster members, compact groups, satellites in deep host potentials —
where the environment screens the Temporal Shear. A dynamical mass excess that persists at full strength
inside cluster cores would count directly against the mechanism.

*Dissociative mergers.* The Bullet Cluster is the discriminating case. TEP predicts that lensing
peaks track the true gravitating mass while the phantom component appears only in dynamical inference;
the observed lensing peaks sit on the galaxies, offset from the dominant baryonic gas. This outcome is
the standard argument for collisionless dark matter and is a live tension for the present framework:
the conformal sector cannot move photon paths onto the galaxy peaks, so consistency requires either that
the true mass distribution is concentrated at the galaxies (with the gas not dominant in the relevant
projected columns) or that a photon-sector channel — scalar backreaction or the disformal sector —
contributes at a level the current action bounds have not yet shown to be sufficient. The Bullet Cluster
is therefore recorded as an unresolved test, not an established success: a persistent lensing excess
centred on collisionless components with no dynamical-analogue counterpart would falsify the
phantom-mass account of the dark sector.

## 7. Conclusions

### 7.1 Limitations of the Isochrony Axiom

For nearly a century, dark-matter inference has been developed within a
framework that treats the residual source-time structure relevant to static
reconstruction as effectively synchronous once standard propagation delays
are modeled. By
treating the photons in telescopes as representing a single spatial slice of
the source, standard models have been forced to interpret all observed
distortions as spatial deflections caused by mass. It has been shown that
this *Isochrony Axiom* is an effective approximation that may break
down in the presence of generalized metric couplings. In the TEP ontology,
the dark sector is not fundamental matter or energy; it is part of the
residual produced when dynamical temporal transport is forced into a
synchronous spatial reconstruction. The same interpretive principle applies
cosmologically: observed redshift is reconstructed conventionally as physical
spatial expansion, whereas TEP attributes it to the conformal proper-time map
on an underlying static spatial geometry (Athens, Paper 26; Thika, Paper 27).
Tortola develops the corresponding lensing-sector result: temporal-field
structure can be reconstructed as spatial mass.

Under TEP, conformal rescaling preserves null paths at fixed
\(g_{\mu\nu}\); it does not prevent scalar stress from sourcing that
gravitational metric. The tested SN Refsdal scalar-backreaction channel
gives \(\kappa_\phi\sim10^{-5}\), about \(2\times10^{3}\) below the
required lensing convergence there (Paper 19, Step 61), while the
evaluated disformal path is also bounded (Step 63). Phantom Mass denotes
the matched dynamical–lensing inference difference generated by the
scalar force on matter; source-dependent temporal reconstruction is a
separate, bounded contribution. Neither replaces the absolute CMB or
cluster deflection. A CDM-free source-to-metric lensing solution is
therefore required alongside the dynamical phantom-mass test.

### 7.2 Summary of Findings

**Phantom Mass as Dynamical–Lensing Difference:** The
scalar force can increase mass inferred from matter dynamics without
directly deflecting photons through the conformal factor. Source
evolution generates a bounded temporal-composite reconstruction
response, absent for a stationary backlight; conformal inter-image
propagation delay remains zero at fixed gravitational geometry.
Under the tested SN Refsdal profile, scalar backreaction and the
evaluated disformal path fall below the required lensing and delay
amplitudes (Paper 19, Steps 61, 63). This local result neither
supplies nor globally excludes the gravitational-metric potential
required for CDM-free CMB, galaxy and cluster lensing.

**The GW170817 "Speed Limit" is Nuanced:** The standard
multi-messenger constraint was deconstructed. Because the conformal
component of the metric coupling preserves null cones, it is
*invisible* to differential speed-of-gravity tests. Photons and
gravitational waves share the common-mode dilation. While GW170817
constrains disformal propagation speeds to \(|c_\gamma - c_g|/c \lesssim
10^{-15}\), it does not directly constrain common-mode conformal clock-rate structure along the shared path, although conformal scalar sectors remain indirectly constrained by PPN, equivalence-principle, source-screening, and clock-comparison tests. The analysis demonstrates that conformal gradients may reproduce specific timing-sensitive aspects of
dark-matter-like phenomenology—particularly timing-sensitive
signatures. The same invariance forbids a *direct conformal*
spatial deflection at fixed $g_{\mu\nu}$, not deflection generated
by stress-energy through that metric. The Refsdal backreaction and
disformal benchmarks fall short in their stated configuration (Paper
19, Steps 61, 63); an adequate CDM-free cosmological optical sector
has not been demonstrated.

**A New Observational Era:** Two regimes for testing TEP
are defined. In the conservative baseline (Regime I), the
effects are millisecond-scale and detectable only in
high-time-resolution astrophysics (FRBs, pulsars). In the
Regime II, where environmental screening and/or a revised
operational mapping allow a year-scale reconstruction-space field —
with the propagating inter-image delay remaining bounded at the ms–s
level — the temporal field supplies the reconstruction-space and
time-domain phenomenology quantified here. The dark-sector ontology
requires two distinct tests: the environment-resolved phantom-mass
difference on co-located dynamical and weak-lensing samples, and a
CDM-free prediction of the absolute lensing potential seen by CMB,
galaxy and cluster observations.

### 7.3 Future Outlook: Time, Not Mass

The persistence of the dark matter problem despite decades of particle
searches suggests a potential error in the underlying premises. The error
may lie in the treatment of time. By treating time as a passive parameter
rather than an active dynamical field, there is a risk of blinding analysis
to the true nature of the "dark" universe.

The path forward lies in *Chronometric Lensing*. The field must move
beyond static mass-mapping and towards
*chronometric mapping*—measuring the detailed arrival-time structure
of the universe. The dark-sector tests are the dynamical–lensing mass difference on
matched low-acceleration systems and the absolute CDM-free lensing
potential, including $C_\ell^{\phi\phi}$. Lensed-FRB residuals
separately test the disformal transport sector. The focus of inquiry must shift from searching for missing mass
to characterizing the dynamical structure of time.

### 7.4 The Paradigm Shift

Within the operational axioms adopted here, the dynamical phenomenology
traditionally attributed to a particulate dark sector can be reinterpreted
as the projection of two-metric time transport onto inference pipelines that
assume isochrony; in the lensing sector the framework instead predicts a
testable dynamical–lensing mass difference, while the observed static-source excess
remains an open confrontation rather than an explained effect. The anomalies
are real; the claim is that their standard "missing mass" interpretation is
not unique once the Isochrony Axiom is relaxed.

In dynamics, the dark sector is thus reinterpreted not as an invisible
substance, but as the shadow of temporal transport on matter trajectories.

The observational program outlined herein—time-domain lensing of fast
transients, precision strong-lens residual timing, source-variability-dependent
shear consistency tests, and above all the environment-resolved
dynamical–lensing mass measurement—provides a viable route
to distinguish particle dark matter from temporal transport while
maintaining a conservative baseline anchored to existing
multi-messenger constraints, thereby offering a decisive, falsifiable
avenue for confronting the dark matter problem.

**Principle:**

#### Updated Operational Interpretation

The later dedicated strong-lensing analysis (TEP-LENS, Paper 19) refines
the observational implementation used here. In particular, ordinary
image-arrival delays remain algebraically integrable; the strong-lensing
test is formulated as an observed-versus-GR-predicted transport residual
rather than a literal closure violation. The framework presented here is
consistent with that refinement: Axiom 3 already distinguishes open-path
differential residuals (the GL observable) from closed-loop holonomy,
and the static clock-transfer contribution is identified as a
clock-transfer discrepancy rather than a direct refraction of null
geodesics. The two papers now state one answer for the conformal
sector: the exact additional static-conformal inter-image residual is
\(0.0\) d (Paper 19, step_56), and every year-scale figure quoted here
is a reconstruction-space amplitude, with the
propagating differential channel carried by the disformal deformation
at the ms–s level. Readers should consult TEP-LENS for the current canonical
strong-lensing time-delay formulation.

## References

Abbott, B. P., et al. (LIGO/Virgo Collaboration) 2017,
*Phys. Rev. Lett.*, 119, 161101

Abbott, T. M. C., et al. (DES Collaboration) 2022,
*Phys. Rev. D*, 105, 023520

Abbott, T. M. C., et al. (DES Collaboration) 2026,
arXiv:2601.14559 (DES Year 6 3×2pt cosmological constraints)

Asgari, M., et al. (KiDS Collaboration) 2021, *A&A*, 645, A104

Wright, A. H., et al. (KiDS Collaboration) 2025,
*A&A*, 703, A158 (arXiv:2503.19441) (KiDS-Legacy cosmic shear)

Baker, T., Bellini, E., Ferreira, P. G., Lagos, M., Noller, J., &
Sawicki, I. 2017, *Phys. Rev. Lett.*, 119, 251301
(arXiv:1710.06394)

Bartelmann, M., & Schneider, P. 2001, *Phys. Rep.*, 340, 291

Bekenstein, J. D. 1993, *Phys. Rev. D*, 48, 3641
(arXiv:gr-qc/9211017)

Bekenstein, J. D. 2004, *Phys. Rev. D*, 70, 083509
(arXiv:astro-ph/0403694)

Blandford, R. D., & Narayan, R. 1986, *ApJ*, 310, 568

Bullock, J. S., & Boylan-Kolchin, M. 2017, *ARA&A*, 55,
343

Burrage, C., & Sakstein, J. 2018, *Living Rev. Relativ.*, 21,
1

Chang, C., et al. 2024, *arXiv e-prints*, arXiv:2406.19654

Clifton, T., Ferreira, P. G., Padilla, A., & Skordis, C. 2012,
*Phys. Rep.*, 513, 1 (arXiv:1106.2476)

Clowe, D., et al. 2006, *ApJ*, 648, L109

Creminelli, P., & Vernizzi, F. 2017, *Phys. Rev. Lett.*, 119,
251302 (arXiv:1710.05877)

Damour, T., & Esposito-Farèse, G. 1992,
*Class. Quantum Grav.*, 9, 2093

Di Valentino, E., et al. 2021, *Classical Quantum Gravity*, 38,
153001

Eigenbrod, A., et al. 2008, *A&A*, 490, 933 (arXiv:0810.0011)

Ezquiaga, J. M., & Zumalacárregui, M. 2017,
*Phys. Rev. Lett.*, 119, 251304 (arXiv:1710.05901)

Fian, C., Jiménez-Vicente, J., Mediavilla, E., et al. 2018,
*ApJ*, 859, 50 (arXiv:1805.09619)

Gilman, D., et al. 2016, *MNRAS*, 462, 219 (arXiv:1601.01671)

Hu, W., Barkana, R., & Gruzinov, A. 2000, *Phys. Rev. Lett.*,
85, 1158 (arXiv:astro-ph/0003365)

Hui, L., Ostriker, J. P., Tremaine, S., & Witten, E. 2017,
*Phys. Rev. D*, 95, 043541 (arXiv:1610.08297)

Khoury, J., & Weltman, A. 2004, *Phys. Rev. D*, 69, 044026
(arXiv:astro-ph/0309411)

Koch Ocker, S., et al. 2022, *ApJ*, 931, 87

Kochanek, C. S. 2002, *ApJ*, 578, 25 (arXiv:astro-ph/0205319)

Leitherer, C., Schaerer, D., Goldader, J., et al. 1999, *ApJS*,
123, 3 (arXiv:astro-ph/9902334)

Li, Z.-X., Gao, H., Ding, X.-H., Wang, G.-J., & Zhang, B. 2018,
*Nat. Commun.*, 9, 3833 (arXiv:1708.06357)

Lintott, C. J., Schawinski, K., Keel, W., et al. 2009, *MNRAS*,
399, 129 (arXiv:0906.5304)

McGaugh, S. S., et al. 2016, *Phys. Rev. Lett.*, 117, 201101

Milgrom, M. 1983, *ApJ*, 270, 365

Muñoz, J. B., Kovetz, E. D., Dai, L., & Kamionkowski, M. 2016,
*Phys. Rev. Lett.*, 117, 091301 (arXiv:1605.00008)

Narayan, R., & Bartelmann, M. 1996, in
*Formation of Structure in the Universe*, ed. A. Dekel & J.
P. Ostriker (Cambridge Univ. Press) (arXiv:astro-ph/9606001)

Navarro, J. F., Frenk, C. S., & White, S. D. M. 1996, *ApJ*,
462, 563

Nityananda, R., & Samuel, J. 1992, *Phys. Rev. D*, 45, 3862
(arXiv:astro-ph/9205001)

Planck Collaboration 2020, *A&A*, 641, A6

Rathna Kumar, S., Tewes, M., Stalin, C. S., Courbin, F., et al. 2013,
*A&A*, 557, A44 (arXiv:1306.5105)

Refsdal, S. 1964, *MNRAS*, 128, 307

Riess, A. G., et al. 2022, *ApJ*, 934, L7

Rubin, V. C., & Ford, W. K., Jr. 1970, *ApJ*, 159, 379

Sakstein, J., & Jain, B. 2017, *Phys. Rev. Lett.*, 119,
251303 (arXiv:1710.05893)

Schawinski, K., Koss, M., Berney, S., & Sartori, L. F. 2015,
*MNRAS*, 451, 2517 (arXiv:1505.06733)

Schneider, P., & Sluse, D. 2013, *A&A*, 559, A37
(arXiv:1306.0901)

Schneider, P., & Sluse, D. 2014, *A&A*, 564, A103
(arXiv:1306.4675)

Schumann, M. 2019, *J. Phys. G*, 46, 103003

Skordis, C., & Złośnik, T. 2021, *Phys. Rev. Lett.*, 127,
161302

Sluse, D., Hutsemékers, D., Courbin, F., Meylan, G., & Wambsganss,
J. 2012, *A&A*, 544, A62

Smette, A., Surdej, J., et al. 1992, *ApJ*, 389, 39

Smawfield, M. L. (2025). *Temporal Equivalence Principle: Dynamic Time & Emergent Light Speed*. Preprint v0.15 (Jakarta). Zenodo. DOI: [10.5281/zenodo.16921911](https://doi.org/10.5281/zenodo.16921911) (Paper 0)

Smawfield, M. L. (2025). *Global Time Echoes: Distance-Structured Correlations in GNSS Clocks*. Preprint v0.27 (Jaipur). Zenodo. DOI: [10.5281/zenodo.17127229](https://doi.org/10.5281/zenodo.17127229) (Paper 1)

Smawfield, M. L. (2025). *Global Time Echoes: 25-Year Analysis of CODE Precise Clock Products*. Preprint v0.20 (Cairo). Zenodo. DOI: [10.5281/zenodo.17517141](https://doi.org/10.5281/zenodo.17517141) (Paper 2)

Smawfield, M. L. (2025). *Global Time Echoes: Raw RINEX Consistency Test*. Preprint v0.8 (Kathmandu). Zenodo. DOI: [10.5281/zenodo.17860166](https://doi.org/10.5281/zenodo.17860166) (Paper 3)

Smawfield, M. L. (2025). *Temporal-Spatial Coupling in Gravitational Lensing: A Reinterpretation of Dark Matter Observations*. Preprint v0.8 (Tortola). Zenodo. DOI: [10.5281/zenodo.17982540](https://doi.org/10.5281/zenodo.17982540) (Paper 4 — this work)

Smawfield, M. L. (2025). *Global Time Echoes: Empirical Synthesis*. Preprint v0.7 (Singapore). Zenodo. DOI: [10.5281/zenodo.18004832](https://doi.org/10.5281/zenodo.18004832) (Paper 5)

Smawfield, M. L. (2025). *Temporal Topology Saturation Scale: Cross-Scale Consistency of ρ_T*. Preprint v0.8 (New Delhi). Zenodo. DOI: [10.5281/zenodo.18064365](https://doi.org/10.5281/zenodo.18064365) (Paper 6)

Smawfield, M. L. (2025). *The Soliton Wake: Exploring RBH-1 as a Temporal Topology Candidate*. Preprint v0.4 (Blantyre). Zenodo. DOI: [10.5281/zenodo.18059250](https://doi.org/10.5281/zenodo.18059250) (Paper 7)

Smawfield, M. L. (2025). *Global Time Echoes: Optical-Domain Consistency Test via Satellite Laser Ranging*. Preprint v0.6 (Mombasa). Zenodo. DOI: [10.5281/zenodo.18064581](https://doi.org/10.5281/zenodo.18064581) (Paper 8)

Smawfield, M. L. (2025). *What Do Precision Tests of General Relativity Actually Measure?*. Preprint v0.8 (Istanbul). Zenodo. DOI: [10.5281/zenodo.18109760](https://doi.org/10.5281/zenodo.18109760) (Paper 9)

Smawfield, M. L. (2026). *Temporal Equivalence Principle: Suppressed Density Scaling in Globular Cluster Pulsars*. Preprint v0.9 (Caracas). Zenodo. DOI: [10.5281/zenodo.18165798](https://doi.org/10.5281/zenodo.18165798) (Paper 10)

Smawfield, M. L. (2026). *The Cepheid Bias: Resolving the Hubble Tension*. Preprint v0.10 (Kingston upon Hull). Zenodo. DOI: [10.5281/zenodo.18209702](https://doi.org/10.5281/zenodo.18209702) (Paper 11)

Smawfield, M. L. (2026). *Temporal Equivalence Principle: A Unified Resolution to the JWST High-Redshift Anomalies*. Preprint v0.7 (Kos). Zenodo. DOI: [10.5281/zenodo.19000827](https://doi.org/10.5281/zenodo.19000827) (Paper 12)

Smawfield, M. L. (2026). *Temporal Equivalence Principle: Temporal Shear Recovery in Gaia DR3 Wide Binaries*. Preprint v0.6 (Kilifi). Zenodo. DOI: [10.5281/zenodo.19102061](https://doi.org/10.5281/zenodo.19102061) (Paper 13)

Smawfield, M. L. (2026). *Temporal Equivalence Principle: A Blind-Prediction Residual Test in Multiply-Imaged Supernovae*. Preprint v0.2 (Lisboa). Zenodo. DOI: [10.5281/zenodo.20572720](https://doi.org/10.5281/zenodo.20572720) (Paper 19)

Smawfield, M. L. (2026). *Temporal Equivalence Principle: Black Holes and the Temporal Horizon*. Preprint v0.3 (Bahrain). Zenodo. DOI: [10.5281/zenodo.21677826](https://doi.org/10.5281/zenodo.21677826) (Paper 28)

Tie, S. S., & Kochanek, C. S. 2018, *MNRAS*, 473, 80
(arXiv:1707.01908)

Treu, T., & Marshall, P. J. 2016, *A&ARv*, 24, 11
(arXiv:1605.05333)

Wambsganss, J. 2006, in
*Gravitational Lensing: Strong, Weak and Micro*, Saas-Fee
Advanced Course 33, ed. G. Meylan et al. (Springer)
(arXiv:astro-ph/0604278)

Wong, K. C., et al. (H0LiCOW Collaboration) 2020, *MNRAS*, 498,
1420

Walsh, D., Carswell, R. F., & Weymann, R. J. 1979, *Nature*,
279, 381

Zwicky, F. 1933, *Helv. Phys. Acta*, 6, 110

#### Contact Information

**Author:** Matthew Lukin Smawfield

**Affiliation:** Independent Researcher

**Email:**
matthew@mlsmawfield.com

**ORCID:**
[0009-0003-8219-3159](https://orcid.org/0009-0003-8219-3159)

**GitHub:**
github.com/matthewsmawfield

**License:** This work is licensed under a
Creative Commons Attribution 4.0 International License.

Version: v0.8 (Tortola) · First published: 19 December 2025 · Last updated: 30 September 2026

## Data Availability & Reproducibility

This work follows open-science practices. This is a theoretical framework paper developing 
the TEP-GL (Temporal Equivalence Principle - Gravitational Lensing) model. The analysis builds 
upon established dark matter phenomenology from the literature and derives new observational 
predictions from first principles.

### Repository & Code

**GitHub Repository:** [github.com/matthewsmawfield/TEP-GL](https://github.com/matthewsmawfield/TEP-GL)

The repository contains the complete theoretical framework, mathematical derivations, 
and observational predictions for the TEP-GL model.

#### Repository Structure

```
TEP-GL/
├── manuscripts/               # Markdown manuscript sources
│   └── manuscript-tep-gl.md
├── site/
│   ├── components/            # HTML manuscript sections
│   │   ├── abstract.html
│   │   ├── section_1_introduction.html
│   │   ├── section_2_theoretical_framework.html
│   │   ├── section_3_quantitative_comparison.html
│   │   ├── section_4_gw170817.html
│   │   ├── section_5_observational_predictions.html
│   │   ├── section_6_discussion.html
│   │   ├── section_7_conclusions.html
│   │   ├── acknowledgments.html
│   │   ├── references.html
│   │   └── appendix_a.html
│   └── manifest.json
├── scripts/                   # Analysis scripts
│   ├── steps/
│   │   └── step_01_amplitude_ledger.py   # temporal-composite amplitude
│   │                                   # ledger (Boxes 3.2, 3.3, 5.1–5.3)
│   └── utils/
├── results/
│   └── step_01_amplitude_ledger.json    # machine-readable ledger output
├── requirements.txt           # Python dependencies
├── CITATION.cff               # Citation metadata
└── README.md                  # Repository documentation
```

The amplitude bookkeeping quoted in Boxes 3.2, 3.3 and 5.1–5.3 — the
source proper motion, the reconstruction-space and propagating-carrier
temporal-composite amplitudes, the standard delay-map baseline
\(\gamma^{\rm std}=\mu_s\,\partial_\theta\Delta T_{\rm Fermat}\) of
§3.4/§5.2, the delay-field amplitude probed by
each falsification threshold, and the exact-one-form cancellation audit
of §3.1.3 (the endpoint-determination of the shear integral on two
multipath rays of the Box-3.1 toy halo) — is reproduced by
`scripts/steps/step_01_amplitude_ledger.py`, whose output is
archived at `results/step_01_amplitude_ledger.json`.

### Data Provenance

This is a theoretical framework paper. Primary data references:

- **GW170817:** LIGO/Virgo gravitational wave and EM counterpart data (public)

- **Dark matter phenomenology:** Established lensing results from the literature (fully cited)

- **SPARC database:** For TEP-UCD cross-paper validation

### Reproduction Instructions

#### Quick Start (Manuscript Build)

```
# 1. Clone repository
git clone https://github.com/matthewsmawfield/TEP-GL.git
cd TEP-GL

# 2. Build manuscript website
cd site
npm install
npm run build

# 3. Output in site/dist/
```

#### System Requirements

- **Node.js** 16+ (for site building)

- **Storage:** < 50 MB

### Theoretical Framework Documentation

The TEP-GL framework derives from three foundational postulates:

- **Two-Metric Postulate:** Gravitational dynamics and universal causal matter coupling are distinguished by \(g_{\mu\nu}\) and \(\tilde{g}_{\mu\nu}\).

- **Temporal Transport:** Conformal structure produces open-path clock/frequency transport, while residual closed-loop synchronization non-integrability requires a disformal or otherwise non-exact sector.

- **Chronometric Reconstruction:** Temporal-field transport and scalar-induced geometry can project into conventionally inferred spatial mass.

### Software Versions

- **Node.js** 16+

- **Python** 3.8+ (optional utilities)

## Appendix A: Mathematical Derivations

### A.1 Proof of Null Cone Invariance in the Conformal Limit

**Proposition:** If two metrics are conformally related by \(\tilde{g}_{\mu\nu} = A^2(\phi) g_{\mu\nu}\), they share the same null geodesics as unparameterized curves.

**Proof:**

Let \(k^\mu = dx^\mu / d\lambda\) be a null vector in \(g_{\mu\nu}\), satisfying \(g_{\mu\nu}k^\mu k^\nu = 0\) and the geodesic equation \(k^\nu \nabla_\nu k^\mu = 0\) (where \(\nabla\) is the Levi-Civita connection of \(g\)).

In the metric \(\tilde{g}_{\mu\nu}\), the null condition holds immediately:

\begin{equation} \label{eq:gl_null_condition}
\tilde{g}_{\mu\nu} k^\mu k^\nu = A^2(\phi) g_{\mu\nu} k^\mu k^\nu = 0
\end{equation}

The connection coefficients \(\tilde{\Gamma}^\lambda_{\mu\nu}\) for \(\tilde{g}\) are related to \(\Gamma^\lambda_{\mu\nu}\) by:

\begin{equation} \label{eq:gl_christoffel}
\tilde{\Gamma}^\lambda_{\mu\nu} = \Gamma^\lambda_{\mu\nu} + \delta^\lambda_\mu \partial_\nu \ln A(\phi) + \delta^\lambda_\nu \partial_\mu \ln A(\phi) - g_{\mu\nu} g^{\lambda\sigma} \partial_\sigma \ln A(\phi)
\end{equation}

Substituting this into the geodesic equation for \(\tilde{g}\):

\begin{equation} \label{eq:gl_geodesic_full}
k^\nu \tilde{\nabla}_\nu k^\mu = k^\nu \nabla_\nu k^\mu + 2 k^\mu k^\nu \partial_\nu \ln A(\phi) - g_{\nu\sigma} k^\nu k^\sigma \dots
\end{equation}

Since \(k\) is null (\(g_{\nu\sigma}k^\nu k^\sigma = 0\)) and \(k^\nu \nabla_\nu k^\mu = 0\), this yields:

\begin{equation} \label{eq:gl_geodesic}
k^\nu \tilde{\nabla}_\nu k^\mu = 2(k^\nu \partial_\nu \ln A(\phi)) k^\mu
\end{equation}

This is the geodesic equation with a non-affine parameterization (\(Dk/d\lambda \propto k\)). Thus, the curve is a geodesic of \(\tilde{g}\), differing only by the parameterization (the clock rate). \(\square\)

---

*This document was automatically generated from the TEP-GL research site. For the interactive version with figures and enhanced formatting, visit: https://mlsmawfield.com/tep/gl/*

*Related Work:*
- [**TEP Theory**](https://doi.org/10.5281/zenodo.16921911) (Foundational framework)

*Source code and data available at: https://github.com/matthewsmawfield/TEP-GL*
