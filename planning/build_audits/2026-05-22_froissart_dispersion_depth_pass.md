# Froissart and Dispersion Depth Pass

Date: 2026-05-22

Scope:
- Tightened the chapter on partial waves, dispersion relations, and high-energy bounds.
- Made the chapter hypotheses explicit: massive four-dimensional theory, stable lightest identical scalar, unitarity on the asymptotic space, first-sheet analyticity, crossing, and explicit treatment of omitted pole terms.
- Connected the identical-particle amplitude normalization to the earlier cross-section and unitarity chapter.
- Expanded the Lehmann-ellipse discussion with the \(\zeta=z+\sqrt{z^2-1}\) ellipse parameter and coefficient decay.
- Made the Froissart--Martin comparison more precise by using the rearrangement inequality for positive even partial-wave weights and evaluating the amplitude at \(0<t_*<t_0\), taking \(t_*\to t_0^-\) only after the estimate.
- Fixed the fixed-\(t<0\) absorptive comparison to use \(|P_\ell(x)|\le1\), rather than a positivity assertion that is only valid for \(x>1\).
- Added the identical-particle elastic integral used in the subtraction-count argument.

Verification:
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- Rendered affected PDF pages 171--180 at 150 dpi and inspected the Lehmann-ellipse figure, partial-wave normalization, Froissart profile figure, dispersion contour, and two-subtraction pages.

Follow-up:
- The adjacent analyticity chapter should later receive a matching pass on first-sheet domains and anomalous thresholds so that the assumptions used here are supported by a more systematic analytic-continuation framework.
