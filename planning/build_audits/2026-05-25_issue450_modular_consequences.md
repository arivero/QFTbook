# Issue 450 modular consequences

GitHub issue: #450.

Scope addressed in
`monograph/tex/volumes/volume_iv/chapter04_superselection_sectors_and_locality_properties.tex`.

Added four substantive modular-theory sections after the KMS theorem and
before the wedge specialization:

- `Relative Modular Operators and Connes Cocycles`, including the relative
  Tomita operator, finite type-I standard-form calculation
  \(\Delta_{\psi|\omega}(X)=\rho_\psi X\rho_\omega^{-1}\), Araki relative
  entropy with the density-matrix reduction, and Connes cocycle derivative
  with the cocycle and modular-flow implementation identities.
- `Type III Local Algebras and Phase-Space Bounds`, including the
  Buchholz--Wichmann nuclearity map, the split-property consequence, and a
  cautious statement of the type-\(\mathrm{III}_1\) status of sharply local
  algebras under the standard additional regularity hypotheses.
- `Modular Hamiltonians and Energy Bounds`, including the
  finite-dimensional entropy--modular-energy identity, the first-law
  derivation, the type-III interpretation, and the wedge modular Hamiltonian
  normalization \(K_{W_R}=2\pi K_R\).
- `Half-Sided Modular Inclusions`, including the definition, the
  Borchers--Wiesbrock structure theorem, and the derivation of
  \([K_{\mathcal M},P]=-2\pi iP\) from the Borchers commutation relation.

Verification plan:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

Calculation-check scripts were not rerun because this is a TeX-only modular
theory edit and no calculation-check files or harness scripts were changed.
