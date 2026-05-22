# Stress Trace MS Insertion Scope Audit

Date: 2026-05-22.

Development pass:

- Refined the stress-tensor trace chapter so the renormalized trace identity
  is stated as a flat-space separated-insertion proposition rather than a bare
  formula followed by an informal limit.
- Defined the finite MS insertion
  \(\mathcal O_{J,\epsilon}^{\rm MS}
  =\partial_{\lambda_J}(\sum_I g_I^\epsilon O_I)\) and its
  separated-point limit \([O_J]_\mu\) before using it in the trace identity.
- Proved the trace identity from bare \(\mu\)-independence and the finite
  source-renormalized insertion limit.
- Separated contact terms, total derivatives, equation-of-motion terms,
  improvements, and curved-background curvature terms from the flat-space
  separated-point identity.
- Tightened the fixed-point statement: \(\beta_J(\lambda_\ast)=0\) removes the
  beta-function contribution to the trace, while tracelessness requires the
  appropriate stress-tensor/improvement data.
- Updated the chapter dossier with these requirements.

Verification:

- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- rendered and visually inspected the affected Chapter 34 pages of
  `/Users/xiyin/QFT/monograph/tex/main.pdf`

Result:

- All checks passed.
- The trace-identity proposition, proof, and revised figures render cleanly.
