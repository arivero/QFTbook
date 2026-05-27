# Build Audit: Wess-Zumino Gauge Closure

Date: 2026-05-27

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 03, `Supersymmetric Gauge Theory`,
at the point where Wess-Zumino gauge supersymmetry closure was previously
summarized as a standard assertion.

## Substantive Edits

- Replaced the closure assertion by a proposition proving the
  Wess-Zumino-gauge algebra from the full vector-superfield
  supertranslation algebra plus a local gauge-slice projection.
- Made the compensating chiral gauge parameter explicit as
  `Lambda_epsilon(V)` and separated the residual ordinary gauge parameter
  `Omega_12` from the covariant shifted parameter `Xi_12`.
- Stated the assumptions needed for the local formal slice and emphasized
  that off-shell closure uses the auxiliary field `D`, not equations of
  motion.
- Extended `calculation-checks/susy_gauge_foundation_checks.py` with an exact
  noncommutative-symbol check of the Hermitian-sign identity
  `a^rho F_{rho mu}+D_mu(a^rho A_rho)=a^rho partial_rho A_mu`, together with
  the analogous adjoint-field identity.
- Updated the Chapter 03 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_gauge_foundation_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_gauge_foundation_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the updated
  supersymmetric gauge-foundation check and the Wolfram gamma-trace gate.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` with 1956 pages and file size 7827664 bytes.
