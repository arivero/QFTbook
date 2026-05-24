# Volume II, Chapter 1 Dossier: Local Data, Spectral Measures, and Green Functions

## Source Placement

- Opens the second sequence by recalling only the data needed for the next
  constructions: local quantum data, spectral measures, time-ordered and
  Euclidean Green functions, and regulated path-integral calculus.
- Preserves the order of the source sequence:
  Poincare representation and local fields, field-on-vacuum one-particle
  projection, Kallen--Lehmann spectral representation, Lorentzian/Euclidean
  Green functions, Wick rotation, regulated path-integral representation,
  then scattering and LSZ in the next chapter.
- Source material used:
  - rendered handwritten trace
    `monograph/tex/build/source_visual_trace/253b_trace-001.png` through
    `253b_trace-006.png`;
  - `transcription/tex/253b/scattering_rg_qcd.tex`, roughly lines 1--260,
    used only as an index against the handwritten pages;
  - Volume I chapters on local fields, Kallen--Lehmann representation,
    Euclidean Green functions, and Lorentzian analytic continuation;
  - `references/sound_references/schmidt_euclidean_reconstruction_math-ph_9811002.pdf`
    for the theorem boundary between Wightman functions and Schwinger
    functions;
  - `references/sound_references/fredenhagen_rejzner_paqft_1208.1428.pdf`
    for the status of perturbative time-ordered products;
  - `references/sound_references/rosten_exact_rg_1003.1366.pdf` for the
    regulated/Wilsonian interpretation of path-integral cutoffs.
  - Volume I perturbative Green-function chapter for the status distinction
    between low-dimensional constructive scalar models, standard
    four-dimensional \(\lambda\phi^4\) triviality results, and finite-cutoff
    perturbative/EFT use.
  - Volume I scalar path-integral chapter, Table
    `tab:constructive-qft-status-catalog`, for the compact catalog of
    constructive existence, triviality, and open continuum-limit regimes.

## Framework

- Hilbert-space local QFT with a strongly continuous unitary Poincare
  representation, vacuum vector, spectrum condition, and local observable or
  smeared-field data.
- Scalar fields are used for formulas when spin is not relevant; tensor and
  spinor cases require the corresponding covariant projectors and indices.
- Green functions are distributions. Euclidean Green functions are analytic
  continuations or reconstructed Schwinger functions under stated hypotheses,
  not a separate primitive unless an Euclidean framework is explicitly chosen.
- Path integrals are regulated calculi for correlation functions. Their
  continuum limit is a construction problem.
- Four-dimensional scalar polynomial examples in this volume are interpreted
  as finite-cutoff perturbative/EFT models or as conditional exact-QFT inputs.
  The standard reflection-positive lattice \(\lambda\phi^4_4\) scaling-limit
  triviality theorem is recorded without claiming a universal nonexistence
  theorem for every possible UV-complete QFT matching formal \(\phi^4_4\)
  perturbation theory.
- Wilsonian cutoff removal is cross-referenced to the later conditional
  finite-coordinate continuum-limit theorem; the scalar-status section does
  not treat regulator removal as an informal claim of renormalizability.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Hilb\) | physical Hilbert space |
| \(U(\Lambda,a)\) | unitary Poincare representation |
| \(P^\mu\) | self-adjoint translation generators |
| \(J^{\mu\nu}\) | Lorentz generators |
| \(T^{\mu\nu}\) | stress tensor whose regulated charges generate Poincare transformations |
| \(\Omega\) | invariant vacuum vector |
| \(\Obs(O)\) | local algebra assigned to a bounded region \(O\) |
| \(\widehat\Phi_\alpha(f)\) | smeared local field with Lorentz index \(\alpha\) |
| \(R(\Lambda)\) | finite-dimensional Lorentz representation carried by the field |
| \(\Sigma_m^+\) | positive one-particle mass shell |
| \(Z_\phi\) | one-particle overlap of a scalar interpolating field |
| \(E(\Delta)\) | joint spectral projection of \(P^\mu\) |
| \(\rho_\Phi(\mu^2)\) | Kallen--Lehmann spectral measure for a scalar interpolating field |
| \(G_N\) | Lorentzian time-ordered \(N\)-point distribution |
| \(S_N\) | Euclidean \(N\)-point distribution or Schwinger function |
| \(Z_\Lambda[J]\) | cutoff generating functional |
| \(D_\Lambda^{\rm ref}\varphi\) | finite-dimensional bosonic scalar reference density |
| \(\dd\mu_{C_\Lambda}\) | Gaussian measure carrying the quadratic kinetic form |
| \(\Lambda\) | ultraviolet cutoff or regulator scale |

## Claims Established

- The second sequence uses the same local Hilbert-space data as the first
  sequence and adds no new primitive notion of particle.
- Scalar examples are classified by logical status: constructive
  low-dimensional continuum theories, four-dimensional finite-cutoff/EFT
  perturbative models, and conditional exact theories with separately supplied
  Hilbert-space and analytic data; the named catalog is
  Table `tab:constructive-qft-status-catalog`.
- The Poincare generators, field covariance law, stress-tensor charge
  formulas, and invariant-vacuum assumptions are stated explicitly with
  regulator/domain caveats.
- A local scalar field applied to the vacuum decomposes into an isolated
  one-particle contribution with residue \(Z_\phi\) and a continuum
  contribution.
- A scalar two-point function is controlled by a positive invariant spectral
  measure.
- An isolated atom in the spectral measure is the input for stable
  one-particle scattering; continuous support is the input for multiparticle
  thresholds, branch cuts, and later resonance analysis.
- Time-ordered and Euclidean Green functions are related by analytic
  continuation only under hypotheses; in perturbative calculations this is a
  boundary-value statement.
- The Wick-rotation sketch is transcribed as a complex-time contour figure
  with Lorentzian ordered points and Euclidean insertions.
- A regulated path integral is a calculus for Green functions. Removing the
  regulator requires counterterms, tuning, or a separate construction.
- The next constructions depend on three distinct operations:
  Green-function expansion, LSZ pole extraction, and renormalization of cutoff
  dependence.

## Figure Requirements

- A dependency diagram from local data to spectral measures to Green functions
  and then to scattering constructions.
- A spectral-measure picture showing a one-particle atom at \(\mu=m\), a gap,
  and a continuum threshold at \(\mu=2m\) in the source example.
- A complex-time Wick-rotation figure matching the source layout: Lorentzian
  contour \(C\), ordered real-time insertions, rotation
  \(x_a^0=e^{-i\alpha}\tau_a\), and Euclidean insertions on the imaginary-time
  axis.
- A regulator diagram separating cutoff definition, counterterm choice, and
  continuum Green-function limit.

## Exclusions

- No new definition of the S-matrix.
- No perturbative scattering diagrams.
- No renormalization group equation.
- No claims of equivalence among Wightman, Euclidean, AQFT, and path-integral
  frameworks beyond local theorem boundaries already stated.

## Audit Notes

- 2026-05-24 issue pass: addressed #217 by adding the scalar-model status
  paragraph to the chapter and recording the precise scope of
  four-dimensional \(\lambda\phi^4\) triviality versus the broader open
  UV-completion question.
- 2026-05-24 issue #300 pass: cross-referenced the Volume I constructive QFT
  status catalog from this chapter's scalar-model status section.
- 2026-05-24 issue #310 pass: recorded the scalar reference-density convention
  for \(D_\Lambda\varphi\), separated it from Gaussian-reference notation
  \(\dd\mu_{C_\Lambda}\), and required non-scalar regularizations to specify
  their integration object before source-functional formulas are used.
- 2026-05-24 issue #325 pass: cross-referenced the Wilsonian
  finite-coordinate continuum-limit theorem from the scalar-model status
  paragraph so that cutoff removal is tied to explicit tuning, semigroup, and
  generated-integral hypotheses.
