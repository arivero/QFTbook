# Derivation Audit Pass 1

Date: 2026-05-21.

Scope: first monograph-wide pass focused on hidden derivation steps, implicit
technical assumptions, convention-sensitive signs, and imprecise language in
reader-facing derivations.

Main corrections and expansions:

- Fixed the future-cone sign convention in the Wightman framework volume by
  stating the metric convention and using \(p^2\le 0\) consistently.
- Expanded the Euclidean vacuum-projection argument by decomposing the trial
  state into vacuum and orthogonal spectral components and deriving the
  gap-controlled convergence.
- Expanded the Kallen-Lehmann measure construction through the pushforward to
  invariant mass squared and the disintegration over Lorentz orbits.
- Added explicit ultraviolet radial estimates for the tadpole integral and an
  explicit Taylor-remainder power-counting step for the higher-order locality
  discussion in renormalization.
- Filled in the first-descendant coefficient in the scalar OPE by matching the
  small-\(x\) expansion of the conformal three-point function to the derivative
  term in the OPE.
- Replaced loose structural language in trace Ward identities, defect
  crossing, radial block recursion, parton-distribution definitions, bulk
  derivative expansions, Grassmann path integrals, and conformal perturbation
  theory with precise equations or regulated meanings.
- Made the conformal perturbation formula for
  \(\partial_a\Delta_{\mathcal X}\) convention-explicit and tied the sign to
  the displayed deformation convention.
- Replaced hidden domain assumptions in protected-sector cohomology by an
  explicit Hodge decomposition assumption.
- Replaced vague AQFT assumptions in Reeh-Schlieder and DHR-sector passages by
  the concrete hypotheses used in the text.
- Clarified the \(\hbar\)-restoration in oscillator variables, the hypotheses
  behind analytic continuation of amplitudes, and the condensate assumption in
  the chiral symmetry-breaking pattern.

Verification:

- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 373 pages.

Residual note: this pass is broad and structural. Further passes should
continue chapter-by-chapter, especially for long perturbative calculations and
for places where a displayed formula currently encodes a known theorem whose
full proof would occupy a separate section.
