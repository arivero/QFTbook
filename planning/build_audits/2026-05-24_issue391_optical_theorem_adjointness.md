# Issue #391: optical theorem adjointness versus reciprocity

## Scope

- `monograph/tex/volumes/volume_i/chapter14_cross_sections_partial_waves_and_unitarity.tex`
- `monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`
- `planning/chapter_dossiers/volume_i/chapter14_cross_sections_unitarity.md`
- `planning/chapter_dossiers/volume_ii/chapter06_analyticity_crossing_landau.md`

## Correction

The exact unitarity identity with \(S=1+iT\) is
\[
  -i(T_{fi}-T_{if}^*)=\sum_X T_{Xf}^*T_{Xi}.
\]
Thus the conjugated factor is obtained by Hilbert-space adjunction:
\[
  \langle f|T^\dagger|X\rangle=\langle X|T|f\rangle^*.
\]
It is not the complex conjugate of the reversed transition \(X\to f\) unless a
separate reciprocity or time-reversal statement is imposed.

The Vol I optical-theorem discussion already had the forward absolute square in
the correct form.  It now states explicitly that the forward equality
\[
  2\,\operatorname{Im}\mathcal M(i|i)
  =
  \sum_X\int d\Phi_X\,|\mathcal M(X|i)|^2
\]
uses unitarity and adjunction alone.  The Vol II discontinuity formula was
corrected from the reversed-process factor
\(\mathcal M_{\beta X}^*\) to the adjoint factor
\(\mathcal M_{X\beta}^*\).

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
