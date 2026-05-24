# Issue #249 Gupta--Bleuler Maxwell Pass

## Scope

- Oldest active GitHub issue: `#249`, on the absence of free Maxwell
  Gupta--Bleuler quantization in Lorenz gauge.
- Manuscript locus:
  `monograph/tex/volumes/volume_i/chapter18_maxwell_theory_constraints_and_gauge_fixing.tex`.
- Planning locus:
  `planning/chapter_dossiers/volume_i/chapter18_maxwell_constraints_gauge_fixing.md`.

## Content Added

- Added a Lorenz-gauge Gupta--Bleuler section after the covariant-gauge
  propagator and before field-strength one-photon states.
- Constructed the covariant one-particle Krein space with indefinite form
  \([f,g]_1=\int d\mu_0\,\eta^{\mu\nu}\bar f_\mu g_\nu\), the symmetric
  Krein-Fock space, and the covariant photon creation/annihilation algebra.
- Defined the Lorenz condition field \(B=\partial^\mu A_\mu\), its
  positive-frequency part \(B^{(+)}\), and the Gupta--Bleuler physical
  subspace \(B^{(+)}(f)\Psi=0\).
- Proved the weak Lorenz condition
  \(\langle\Phi|\partial^\mu A_\mu|\Psi\rangle=0\) between physical vectors.
- Identified the null subspace \(\mathcal N_1=\{k_\mu h(k)\}\), proved it is
  null and orthogonal inside \(k^\perp\), and constructed the positive
  quotient \(\mathcal K_{1,{\rm GB}}/\mathcal N_1\).
- Proved the Fock quotient
  \(\mathcal K_{\rm GB}/\mathcal N\simeq\mathcal F_s(\mathcal H_1^\gamma)\).
- Proved that field-strength smearings descend to the quotient and that free
  field-strength correlators agree with the reduced two-helicity
  quantization; longitudinal representative terms are killed by
  antisymmetrization.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
