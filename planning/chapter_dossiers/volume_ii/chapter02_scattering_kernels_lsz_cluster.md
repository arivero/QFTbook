# Volume II, Chapter 2 Dossier: Scattering Kernels, LSZ, and Cluster Decomposition

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
- The physical cluster theorem is stated with the quantitative estimate needed
  to pass from finite-time almost-local products to Haag--Ruelle scattering
  states.

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

## Claims Established

- The \(S\)-operator is a comparison of in/out wave operators and is not
  introduced by perturbation theory.
- The in/out wave operators are tied to local fields through the
  Haag--Ruelle packet limit
  \(\lim_{T\to\pm\infty}\widehat\phi_{f_1^{(T)}}\cdots
  \widehat\phi_{f_n^{(T)}}\Omega\), with Fourier support near the isolated
  one-particle shell.
- Kernel notation is shorthand for wave-packet distributions on mass shells.
- LSZ gives connected scattering kernels by extracting one-particle pole
  residues from connected time-ordered Green functions.
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
  mass gap, local commutativity, and a quantitative clustering estimate for
  finite-time Haag--Ruelle approximants, widely spacelike separated scattering
  processes factorize.
- The cluster theorem proof now displays the finite-time estimate, the
  \(\varepsilon\)-argument with Haag--Ruelle norm convergence uniform under
  translations, and the final moment-cumulant subtraction of proper-process
  products.
- The connected amplitude is the object whose poles, cuts, and analytic
  continuation will be studied in subsequent chapters.
- The physical equal-mass \(s\)-channel has \(s\ge4m^2\) and \(t,u\le0\);
  positive \(t\) or \(u\) in crossing and fixed-\(t\) arguments denotes a
  crossed-channel timelike invariant.

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
- No infrared-inclusive or dressed charged scattering construction.

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
