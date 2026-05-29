# 2026-05-27 Issue #615 QED Form-Factor Formalization Pass

## Scope

- Reviewed `claude_review.md` and the live GitHub issue list.
- Treated GitHub issue threads as authoritative where the local review file is
  stale.
- Addressed the Volume I Chapter 20 residual from issue #615: the chapter had
  substantial QED renormalization and form-factor content but no labeled
  formal environments.

## Manuscript Changes

- Added `def:qed-regulated-explicit-coupling-coordinates`.
- Added Ward-organization current material; later anti-wrapper audit demoted
  it from proposition/proof form to convention prose because the statement is
  coordinate bookkeeping around \(Z_1=Z_\psi\), not an independent theorem.
- Added `prop:qed-photon-self-energy-transversality`.
- Added `prop:qed-one-loop-vacuum-polarization`.
- Added `def:qed-electron-electromagnetic-form-factors`.
- Added `prop:qed-electron-charge-normalization`.
- Added `prop:qed-magnetic-factor-from-form-factor`.
- Added `prop:qed-one-loop-vertex-schwinger`.

The goal of the pass was not wrapper text.  The claims now state their
coordinate conventions and normalization hypotheses explicitly, and the
existing derivations have been placed under propositions/proofs so later
audits can cite and improve specific mathematical objects.

## Calculation Check

- Added `calculation-checks/qed_form_factor_checks.py`, an exact rational
  check of:
  - the one-loop photon vacuum-polarization pole coefficient;
  - the Ward organization \(Z_1=Z_\psi\);
  - the \((F,G)\) to Dirac--Pauli basis conversion;
  - the \(k^2=0\) vertex Feynman-parameter integral;
  - \(G(0)=-e^2/(8\pi^2)\) and \(g_{\mathrm{mag}}-2=\alpha/\pi\).

## Verification

- `python3 calculation-checks/qed_form_factor_checks.py`
- `python3 -m py_compile calculation-checks/qed_form_factor_checks.py`
- edited-file long-line scan: clean
- `git diff --check` on edited paths: clean
- `tools/build_monograph.sh`: clean
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2129`
