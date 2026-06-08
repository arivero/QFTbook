# Issue #925 Kinetic H-Theorem Prefactor Audit

## Scope

- Target chapter: `monograph/tex/volumes/volume_x/chapter08_kinetic_theory_controlled_limit.tex`.
- Issue repaired: make the symmetrized H-theorem coefficient consistent with
  the chapter's entropy-current normalization and transition-measure
  convention.

## Substance Audit

- The entropy current uses \(2d\Pi\,p^\mu\), hence
  \(\partial_\mu S^\mu_{\rm kin}=-\sum_a\int 2d\Pi_a\,\mathcal C_a\log r_a\).
- The displayed collision operator has \(\mathcal C_1=\int W(Y-X)\), so the
  unsymmetrized entropy production starts with
  \(2\int W(X-Y)\log r_1\).
- Incoming exchange, outgoing exchange, and \(12\leftrightarrow34\)
  microreversibility supply a four-leg average \(1/4\).  Combined with the
  entropy-current factor \(2\), the net coefficient is \(1/2\).
- The transition weight convention is now explicit: physical-channel,
  initial-pair, final-pair, shell-projection, and regulator divisors live in
  \(\mathcal W\) or in the declared transition measure.  The entropy
  symmetrization adds no new channel-counting divisor.
- In the scalar full-product convention \(\mathcal W=\lambda_R^2/4\), the
  ordered four-particle H-theorem coefficient is \(\lambda_R^2/8\).

## Physics-Depth Reaudit

- This is a normalization repair tied directly to entropy production, kinetic
  irreversibility, and collision-kernel convention matching.  It preserves
  the finite symmetry-factor derivation rather than adding an adjacent lemma.
- The calculation check now derives the coefficient from the collision terms
  and entropy current, then rejects the old \(1/4\) prefactor while preserving
  positive integrand sign.

## Verification

- Passed: `python3 calculation-checks/kinetic_theory_checks.py`.
- Passed: `python3 calculation-checks/check_utils_checks.py`.
- Passed: `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_x/chapter08_kinetic_theory_controlled_limit.tex --fail`.
- Passed: `bash tools/audit_chapter_dossiers.sh`.
- Passed: `python3 tools/audit_calculation_evidence_contracts.py`.
- Passed: `python3 tools/audit_calculation_check_inventory.py`.
- Passed: `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_x/chapter08_kinetic_theory_controlled_limit.tex`.
- Passed: `tools/run_calculation_checks.sh --python-only`.
- Passed: `tools/build_monograph.sh`.
