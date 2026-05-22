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
- The chapter does not claim asymptotic completeness for physical models.
- The chapter states massless, confined, and long-range charged sectors as
  different asymptotic domains without constructing them here.

## Framework

- Massive scalar particle species with isolated one-particle mass shell
  \(\Sigma_m^+\), Haag--Ruelle in/out wave operators, and a unitary scattering
  operator on the corresponding scattering sector.
- Momentum kernels are distributional kernels to be tested against smooth
  compactly supported wave packets on mass shells.
- Connected kernels are defined by cluster decomposition of scattering
  matrix elements, matching connected time-ordered Green functions under LSZ.

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
| \(\Pi\) | partition of external labels into connected clusters |

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
- The external normalizations are made explicit both in covariant kernel
  convention and in delta-normalized source convention.
- Cluster decomposition expresses scattering kernels as sums over products of
  connected kernels associated to partitions of the external process.
- The connected amplitude is the object whose poles, cuts, and analytic
  continuation will be studied in subsequent chapters.

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
