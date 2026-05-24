# Issue #298 Audit: Wiener Measure and Feynman--Kac in Euclidean QM

## GitHub Issue

- #298, opened 2026-05-22:
  `[Vol I Chs 7, 8] Wiener measure for Euclidean QM never invoked`.

## Manuscript Changes

- `monograph/tex/volumes/volume_i/chapter04_hamiltonian_evolution_and_time_sliced_path_integrals.tex`
  now contains Theorem `thm:wiener-feynman-kac-qm`.
- The theorem constructs Wiener measure on
  `C([0,\tau],\mathbb R^d)` from heat-kernel finite-dimensional
  distributions, identifies the diffusion constant `\hbar/m`, states the
  Feynman--Kac semigroup formula, and records the Brownian-bridge form of the
  fixed-endpoint Euclidean transition kernel.
- The proof derives consistency from heat-kernel convolution, obtains
  continuous-path support by Kolmogorov continuity, proves the bounded
  continuous case from the Markov property plus Trotter, and explains the
  bounded-below/Kato extension through monotone form convergence and Kato
  control.
- The same chapter now explicitly distinguishes this positive Borel-measure
  theorem from the general QFT path-integral problem: fermions use Berezin
  integration, gauge theories require quotient/gauge-fixing/BRST/BV or lattice
  data, and theta terms may make the Euclidean weight complex.
- The thermal trace subsection now identifies the Feynman--Kac trace, under
  the same hypotheses, as a Brownian-loop/endpoint-disintegrated construction.
- `monograph/tex/volumes/volume_i/chapter05_euclidean_correlation_functions_and_gaussian_perturbation_theory.tex`
  now explains that `[Dq]` means Brownian-bridge/Wiener expectation in the
  Schrödinger cases covered by Chapter 4, while later Gaussian and
  perturbative uses are different regulated mathematical objects.

## Planning Updates

- Updated the Chapter 4 dossier with the new theorem, notation, claim ledger,
  and the warning against treating Borel measures as the universal QFT
  foundation.
- Updated the Chapter 5 dossier with the Brownian-bridge interpretation and
  the same restriction.

## Verification

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; full TeX build and final log scan clean.
