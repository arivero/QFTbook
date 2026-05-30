# Liouville DOZZ Shift Connection Pass

Date: 2026-05-30

Scope:
- `monograph/tex/volumes/volume_v/chapter13_liouville_cft.tex`
- `calculation-checks/liouville_bpz_checks.py`
- `planning/chapter_dossiers/volume_v/chapter13_liouville_cft.md`

Purpose:
- Reduce the Volume V quoted-theorem proof debt around the DOZZ formula by
  making the degenerate BPZ shift-equation mechanism explicit at the point of
  use.

Mathematical change:
- The proof of the degenerate BPZ block proposition now displays the full
  hypergeometric connection matrix from the \(z=0\) channel to the \(z=1\)
  channel.
- It writes the diagonal \(z=0\) four-point hermitian form with coefficients
  \(C_b(\alpha_1-b/2,\alpha_2,\alpha_3)\) and
  \(C_-(\alpha_1)C_b(\alpha_1+b/2,\alpha_2,\alpha_3)\).
- It derives the vanishing off-diagonal condition in the \(z=1\) OPE basis,
  \[
    A_s M_{--}M_{-+}+B_s M_{+-}M_{++}=0,
  \]
  and hence the finite-difference equation
  \[
    \frac{C_b(\alpha_1+b/2,\alpha_2,\alpha_3)}
         {C_b(\alpha_1-b/2,\alpha_2,\alpha_3)}
    =
    -\frac{M_{--}M_{-+}}{C_-(\alpha_1)M_{+-}M_{++}}.
  \]
- The text then identifies this ratio with the displayed DOZZ \(b\)-shift
  formula using the one-screening coefficient and gamma-ratio identities.

Calculation check:
- `calculation-checks/liouville_bpz_checks.py` now evaluates two nonresonant
  numerical samples of the connection-matrix ratio and compares them with the
  DOZZ \(b\)-shift ratio in the same normalization.

Remaining theorem boundary:
- This pass proves the local BPZ/connection-matrix finite-difference
  mechanism used by the DOZZ bootstrap argument.  It does not prove the full
  probabilistic construction, analytic continuation, crossing, or
  functorial/sewing closure of Liouville theory.
