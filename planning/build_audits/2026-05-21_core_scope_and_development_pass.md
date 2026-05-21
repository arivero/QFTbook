# Core Scope and Development Pass

Date: 2026-05-21.

Scope:

- Narrowed the compiled monograph to the core QFT development.
- Moved premature advanced CFT/frontier chapters out of the compiled Volume
  III source tree into `deprecated/volume_iii_premature_topics/`.
- Preserved those drafts for possible later reconstruction, but removed them
  from the audited manuscript.
- Added core rigor expansions in the local-field, scattering, Wilsonian,
  BRST, OPE, and mathematical-scattering parts.

Deferred from the compiled monograph:

- conformal blocks and crossing-solution machinery;
- projective-lightcone and Casimir-recursion technology;
- survey/landscape chapters;
- two-dimensional extended conformal symmetry and modular material;
- supersymmetric and superconformal field theory drafts;
- large-\(N\), spin-chain, duality, conformal-manifold, holographic,
  Witten-diagram, Mellin-amplitude, localization, integrated-correlator, and
  defect drafts.

Core expansions added:

- analytic-status distinctions among regulated theories, continuum
  correlation theories, Hilbert-space/algebraic completions, and perturbative
  expansions;
- common invariant field domains and distributional matrix-element discipline;
- the integrable commutator and spectral-gap estimates behind
  Haag--Ruelle norm convergence;
- finite-regulator Gaussian convolution as the exact meaning of a Wilsonian
  shell integration;
- linearized Wilsonian fixed-point flow, scaling coordinates, critical
  surfaces, and the relation \(\Delta=D-y\);
- positivity of the BRST quotient and the role of \(Q\)-doublets;
- radial OPE convergence under explicit Hilbert-space spectral hypotheses;
- a new mathematical-framework chapter on Haag--Ruelle scattering for local
  nets and its relation to LSZ.

Verification to run:

- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
