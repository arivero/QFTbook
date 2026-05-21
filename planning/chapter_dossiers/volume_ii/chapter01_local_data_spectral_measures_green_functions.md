# Volume II, Chapter 1 Dossier: Local Data, Spectral Measures, and Green Functions

## Source Placement

- Opens the second sequence by recalling only the data needed for the next
  constructions: local quantum data, spectral measures, time-ordered and
  Euclidean Green functions, and regulated path-integral calculus.
- Preserves the order of the source sequence:
  local QFT data, spectral representation, path-integral representation,
  then scattering and LSZ in the next chapter.
- Source material used:
  - `transcription/tex/253b/scattering_rg_qcd.tex`, roughly lines 1--260;
  - Volume I chapters on local fields, Kallen--Lehmann representation,
    Euclidean Green functions, and Lorentzian analytic continuation;
  - `references/sound_references/schmidt_euclidean_reconstruction_math-ph_9811002.pdf`
    for the theorem boundary between Wightman functions and Schwinger
    functions;
  - `references/sound_references/fredenhagen_rejzner_paqft_1208.1428.pdf`
    for the status of perturbative time-ordered products;
  - `references/sound_references/rosten_exact_rg_1003.1366.pdf` for the
    regulated/Wilsonian interpretation of path-integral cutoffs.

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

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Hilb\) | physical Hilbert space |
| \(U(a,\Lambda)\) | unitary Poincare representation |
| \(P^\mu\) | self-adjoint translation generators |
| \(\Omega\) | invariant vacuum vector |
| \(\Obs(O)\) | local algebra assigned to a bounded region \(O\) |
| \(\widehat\Phi_\alpha(f)\) | smeared local field with Lorentz index \(\alpha\) |
| \(E(\Delta)\) | joint spectral projection of \(P^\mu\) |
| \(\rho_\Phi(\mu^2)\) | Kallen--Lehmann spectral measure for a scalar interpolating field |
| \(G_N\) | Lorentzian time-ordered \(N\)-point distribution |
| \(S_N\) | Euclidean \(N\)-point distribution or Schwinger function |
| \(Z_\Lambda[J]\) | cutoff generating functional |
| \(\Lambda\) | ultraviolet cutoff or regulator scale |

## Claims Established

- The second sequence uses the same local Hilbert-space data as the first
  sequence and adds no new primitive notion of particle.
- A scalar two-point function is controlled by a positive invariant spectral
  measure.
- An isolated atom in the spectral measure is the input for stable
  one-particle scattering; continuous support is the input for multiparticle
  thresholds, branch cuts, and later resonance analysis.
- Time-ordered and Euclidean Green functions are related by analytic
  continuation only under hypotheses; in perturbative calculations this is a
  boundary-value statement.
- A regulated path integral is a calculus for Green functions. Removing the
  regulator requires counterterms, tuning, or a separate construction.
- The next constructions depend on three distinct operations:
  Green-function expansion, LSZ pole extraction, and renormalization of cutoff
  dependence.

## Figure Requirements

- A dependency diagram from local data to spectral measures to Green functions
  and then to scattering constructions.
- A spectral-measure picture showing a one-particle atom and a continuum
  threshold.
- A regulator diagram separating cutoff definition, counterterm choice, and
  continuum Green-function limit.

## Exclusions

- No new definition of the S-matrix.
- No perturbative scattering diagrams.
- No renormalization group equation.
- No claims of equivalence among Wightman, Euclidean, AQFT, and path-integral
  frameworks beyond local theorem boundaries already stated.
