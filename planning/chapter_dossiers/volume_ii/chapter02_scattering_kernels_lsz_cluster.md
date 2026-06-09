# Volume II, Chapter 2 Dossier: Scattering Kernels, LSZ, and Cluster Decomposition
Source-File: monograph/tex/volumes/volume_ii/chapter02_the_s_matrix_and_lsz_revisited.tex

## Source Placement

- Follows the Volume II recap of local, spectral, and Green-function data.
- Reintroduces the already constructed S-operator only as the object whose
  matrix elements will be analyzed in bound-state, resonance, analyticity, and
  renormalization chapters.
- Source material used:
  - rendered handwritten trace
    `monograph/tex/build/source_visual_trace/253b_trace-007.png` through
    `253b_trace-011.png`;
  - `transcription/tex/253b/scattering_rg_qcd.tex`, roughly lines 260--430,
    used only as an index against the handwritten pages;
  - Volume I Haag--Ruelle and LSZ chapters;
  - `references/sound_references/buchholz_dybalski_scattering_2023.pdf`,
    Sections 2--3, for the Haag--Ruelle and LSZ theorem boundary.

## External Reference Boundary

- Buchholz--Dybalski is used to locate the rigorous statement: massive
  Haag--Ruelle wave operators exist under isolated-mass and locality
  hypotheses, and LSZ reduction restricts time-ordered boundary values to the
  mass shells.
- Haag--Ruelle/Ruelle/Araki/Reed--Simon theorem boundaries are used for the
  quantitative cluster-estimate hypothesis: almost-local approximants obey
  cluster bounds whose spacelike separation decay dominates the polynomial
  dependence on the finite Haag--Ruelle time parameter.
- The chapter does not claim asymptotic completeness for physical models.
- The chapter states massless, confined, and long-range charged sectors as
  different asymptotic domains without constructing them here.
- It explicitly excludes interpreting perturbative QED charged hard labels as
  exact on-shell LSZ electron particles of massless QED; the infrared chapters
  construct the appropriate inclusive and dressed replacements.

## Framework

- Massive scalar particle species with isolated one-particle mass shell
  \(\Sigma_m^+\), Haag--Ruelle in/out wave operators, and a unitary scattering
  operator on the corresponding scattering sector.
- The theorem-level Haag--Ruelle input is
  Theorem~\ref{thm:algebraic-haag-ruelle-scattering}; the scalar point-field
  Cook-estimate material in Volume I is referenced only as the construction
  model.
- Momentum kernels are distributional kernels to be tested against smooth
  compactly supported wave packets on mass shells.
- Connected kernels are defined by cluster decomposition of scattering
  matrix elements, matching connected time-ordered Green functions under LSZ.
- The part-wide mostly-plus Mandelstam convention is fixed at the opening of
  the scattering-kernel chapter: for incoming \(p_1,p_2\) and outgoing
  \(p_3,p_4\),
  \(s=-(p_1+p_2)^2\), \(t=-(p_1-p_3)^2\), and
  \(u=-(p_1-p_4)^2\), with \(s+t+u=\sum_i m_i^2\).
- Time-ordered correlators used in the scattering chapters carry an explicit
  status: exact Hilbert-space distributions with one-particle pole data,
  Euclidean reconstructed distributions after OS/analytic-continuation
  hypotheses, or formal/regulator-dependent perturbative coefficients.  No
  path integral defines the Haag--Ruelle \(S\)-operator.
- The chapter now opens a cross-volume scattering architecture section:
  massive Haag--Ruelle/LSZ amplitudes, charged QED inclusive/dressed
  observables, detector/event-shape distributions, analytic \(S\)-matrix
  continuations, confining QCD factorization, and integrable factorized
  scattering are compared by their primary objects, inputs, outputs, and
  failure modes.
- The physical cluster theorem is stated with the quantitative finite-time
  cluster estimate and an explicit joint Haag--Ruelle/separation diagonal
  \(T(a)=o(|a|)\) for independently translated asymptotic subclusters.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Hilb_1\) | one-particle Hilbert space of a stable scalar particle |
| \(\mathcal F_s(\Hilb_1)\) | symmetric Fock space over \(\Hilb_1\) |
| \(\Omega_{\mathrm{in/out}}\) | Haag--Ruelle in/out wave operators |
| \(\widehat\phi_f\) | local scalar field smeared against a test function \(f\) |
| \(f^{(T)}\) | Haag--Ruelle time-translated wave packet whose Fourier support lies near \(\Sigma_m^+\) |
| \(S\) | scattering operator \(\Omega_{\mathrm{out}}^*\Omega_{\mathrm{in}}\) |
| \(\dd\mu_m(\vec p)\) | Lorentz-invariant mass-shell measure |
| \(S_{\beta\alpha}\) | distributional scattering kernel |
| \(S^{\mathrm c}\) | connected scattering kernel |
| \(G_N^{\mathrm c}\) | connected time-ordered \(N\)-point distribution |
| \(\mathcal M\) | invariant amplitude after extracting the momentum-conservation delta function |
| \(s,t,u\) | mostly-plus Mandelstam variables \(s=-(p_1+p_2)^2\), \(t=-(p_1-p_3)^2\), \(u=-(p_1-p_4)^2\) |
| \(\Pi\) | partition of external labels into connected clusters |
| \(\rho(a,T)\) | spacelike separation of the two Haag--Ruelle localization tubes after relative translation \(a\) at finite time parameter \(T\) |
| \(\mathsf J_{A|B}\) | symmetrized Fock concatenation map for a fixed two-cluster label decomposition |
| \(U_F(a)\) | free Fock translation used to translate one asymptotic subcluster before concatenation |
| \(T(a)\) | diagonal Haag--Ruelle time used in the joint large-time/large-separation cluster limit |

## Claims Established

- The \(S\)-operator is a comparison of in/out wave operators and is not
  introduced by perturbation theory.
- The in/out wave operators are tied to local fields through the
  Haag--Ruelle packet limit
  \(\lim_{T\to\pm\infty}\widehat\phi_{f_1^{(T)}}\cdots
  \widehat\phi_{f_n^{(T)}}\Omega\), with Fourier support near the isolated
  one-particle shell.
- Kernel notation is shorthand for wave-packet distributions on mass shells.
- LSZ input is not reboxed here: the chapter references
  Theorem~\ref{thm:lsz-wave-packet} and uses only its kernel consequence,
  namely simultaneous external pole extraction after wave-packet smearing.
- The path-integral language used later for Feynman graphs and
  Feynman-parameter integrals is coefficientwise perturbative input for
  time-ordered kernels, not a nonperturbative definition of the scattering
  operator.
- The external normalizations are made explicit both in covariant kernel
  convention and in delta-normalized source convention.
- Cluster decomposition expresses scattering kernels as sums over products of
  connected kernels associated to partitions of the external process.
- The algebraic moment-cumulant recursion defining connected kernels is
  separated from the physical cluster theorem: under uniqueness of the vacuum,
  mass gap, local commutativity, a quantitative clustering estimate for
  finite-time Haag--Ruelle approximants, and a joint approximation bound for
  partially translated cluster vectors, widely spacelike separated scattering
  processes factorize.
- The cluster theorem proof now types the independently translated
  two-cluster state in asymptotic Fock space, replaces the earlier
  unitarity-based uniformity assertion with an explicit diagonal
  \(T(a)\to\infty\), \(T(a)=o(|a|)\), and separates the wave-packet theorem
  from the regular-kernel corollary.
- The kernel corollary is qualified by dimension and regular kinematics: in
  \(1+1\)-dimensional elastic scattering total momentum conservation itself
  pulls back to rapidity permutation graphs, so connected-kernel subtraction
  removes proper product blocks but does not erase all graph-delta support
  compatible with total conservation.
- The connected amplitude is the object whose poles, cuts, and analytic
  continuation will be studied in subsequent chapters.
- The physical equal-mass \(s\)-channel has \(s\ge4m^2\) and \(t,u\le0\);
  positive \(t\) or \(u\) in crossing and fixed-\(t\) arguments denotes a
  crossed-channel timelike invariant.
- The cross-volume architecture records three end-to-end routes:
  massive local fields to Haag--Ruelle wave operators, LSZ amplitudes, and
  cross sections; hard charged QED processes to soft/inclusive
  detector-resolved rates; and QCD sources to factorized operator data,
  jet/soft/parton-density functions, and detector measures.
- The analytic scattering route now separates continuation machinery from
  contingent singularity data: massive amplitudes plus unitarity, boundedness,
  and analyticity hypotheses supply partial-wave and dispersion-relation
  tools and the sheet framework in which resonance poles can be characterized
  if present, but a particular pole requires separate channel-specific
  dynamical or spectral evidence.
- The same architecture states non-maps used later: detector distributions do
  not determine unique amplitudes, resonance poles do not supply asymptotic
  particle vectors, inclusive QED rates do not restore bare charged LSZ
  states, and finite partonic or lattice checks do not supply continuum
  factorization or reconstruction theorems.
- 2026-05-25 issue #446 pass: removed the boxed LSZ restatement from the
  chapter, retained only the kernel-use paragraph pointing to
  Theorem~\ref{thm:lsz-wave-packet}, and changed the Haag--Ruelle input to the
  Volume IV theorem layer plus the Volume I Cook-estimate model.
- 2026-06-03 issue #734 correction pass: revised the cross-volume scattering
  architecture so analyticity no longer implies resonance-pole existence.  The
  monograph now states that analytic hypotheses give the continuation,
  partial-wave, and dispersion framework, while pole existence/location
  requires additional channel-specific dynamical or spectral evidence.
- 2026-06-09 issue #974 pass: replaced the cluster theorem's uniform-in-relative
  translation passage with a typed partial Fock translation and an explicit
  joint Haag--Ruelle/separation diagonal.  Added the \(1+1\)-dimensional
  elastic rapidity boundary so permutation-graph support is no longer
  confused with a failure of wave-packet cluster decomposition.

## Calculation Checks

- `calculation-checks/scattering_cluster_decomposition_checks.py` verifies the
  exact finite arithmetic behind the issue #974 repair: diagonal exponents for
  \(T(a)=o(|a|)\), negative controls for \(T\sim |a|\) and insufficient
  inverse-separation decay, the \(1+1\)-dimensional lightcone reconstruction
  of elastic permutation-graph support from total momentum conservation, and
  the distinction between proper product subtraction and removal of all graph
  delta support.
- Related standing checks: `calculation-checks/haag_ruelle_velocity_checks.py`
  for velocity-tube separation conventions,
  `calculation-checks/haag_ruelle_fock_inner_product_checks.py` for symmetric
  Fock contractions, and `calculation-checks/lsz_residue_checks.py` for the
  LSZ kernel-normalization conventions used by this chapter.

## Figure Requirements

- A clean in/out basis diagram showing the Hilbert-space comparison defining
  the scattering kernel.
- A mass-shell support diagram for \(\operatorname{supp}\widetilde f\) near
  \(\Sigma_m^+\), separated from the continuum.
- A residue-extraction diagram from connected Green functions to invariant
  amplitudes.
- A cluster partition diagram for a disconnected process decomposing into
  connected components.

## Exclusions

- No perturbative formula for a specific interaction.
- No bound-state or resonance derivation.
- No dispersion relation.
- No new infrared-inclusive, dressed charged, QCD factorization, detector, or
  integrable reconstruction construction; the new section is a status and
  routing layer pointing to the chapters where those constructions are
  developed.

## Audit Notes

- 2026-05-24 issue #319 pass: added
  `def:scattering-time-ordered-correlator-status` at the chapter opening.
  The manuscript now declares that \(G_N^{\mathrm c}\), \(Z_\phi\), and
  Feynman-parameter graph integrals in the scattering chapters are either
  exact Hilbert-space distributions, Euclidean reconstructed distributions,
  or formal/regulator-dependent perturbative coefficients.  The definition
  also states explicitly that the path integral does not define the
  Haag--Ruelle scattering operator.
- 2026-05-24 issue #435 pass: added the part-wide mostly-plus Mandelstam
  convention and physical-region sign statement before the analytic chapters
  use \(s,t,u\).
- 2026-06-03 issue #732 scattering architecture pass: added
  Section~\ref{sec:cross-volume-scattering-architecture}, a cross-volume
  comparison and status ledger that distinguishes amplitudes, inclusive
  charged rates, detector distributions, analytic continuations, QCD
  factorized observables, and integrable exact data.  This is architecture and
  theorem-boundary work, not a new physical gluing or reconstruction theorem.
  It coordinates the live detector/light-ray (#519), jet-substructure (#526),
  charged scattering (#527), and QCD-factorization (#630) lanes by routing
  later claims through the same status matrix instead of duplicating their
  detailed content here.
