# Build Audit: SUSY Moduli Hyperkahler Quotient

Date: 2026-05-27

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 08, `Moduli Spaces In
Supersymmetric Quantum Field Theory`, by replacing the bare statement that
\(\mathcal N=2\) Higgs branches are hyperkahler quotients with a fully worked
rank-one hypermultiplet quotient.

## Substantive Edits

- Added a proposition proving that the \(U(1)\) hypermultiplet quotient with
  \(N\) charge-one hypermultiplets and positive real FI parameter is
  biholomorphic to \(T^\ast\mathbb P^{N-1}\).
- Displayed the complex and real moment maps, the stable complex quotient
  \(\{\mu_{\mathbb C}=0,q\neq0\}/\mathbb C^\ast\), local coordinates
  \(z_i^{(a)}=q_i/q_a\), \(p_i^{(a)}=q_a\widetilde q_i\), and the
  complex-moment solution for \(q_a\widetilde q_a\).
- Proved the descent of the holomorphic one-form
  \(\Theta=\sum_i\widetilde q_i\,dq_i\) to the canonical cotangent one-form
  and checked the transition between two projective patches.
- Extended `calculation-checks/susy_moduli_space_checks.py` with exact
  rational checks for the hyperkahler quotient dimension ledger, one-form
  descent, and cotangent transition algebra.
- Updated the Chapter 08 dossier and the calculation-check README.

## Verification

- `python3 calculation-checks/susy_moduli_space_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the updated
  moduli-space quotient checks and the Wolfram gamma-trace gate.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean after the audit note was finalized.
- `tools/build_monograph.sh`: passed; generated `monograph/tex/main.pdf`
  with 1963 pages and file size 7856517 bytes after rebasing onto
  `origin/main`.
