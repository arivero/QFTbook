# Build Audit: Issue #308 Positive Measure Convexity Assumption

Issue:

- GitHub #308: `[Vol III Ch 1] Convexity-from-positive-measure: hypothesis
  hidden inline`.

Files changed:

- `monograph/tex/volumes/volume_ii/chapter23_generating_functionals_and_the_one_particle_irreducible_effective_action.tex`
- `planning/chapter_dossiers/volume_ii/chapter09_generating_functionals_1pi_effective_action.md`

Resolution:

- Promoted the positive-measure input for Euclidean convexity to the labeled
  assumption `ass:positive-euclidean-regulator-convexity`.
- The assumption now specifies a regulated measurable configuration space, a
  positive finite measure, a real source space, a convex source domain, a
  measurable source-field pairing, and the condition
  \(0<Z_{E,\Lambda}[J]<\infty\) throughout the source domain.
- The theorem `thm:volume-ii-euclidean-convexity-finite-regulator` is now
  explicitly conditional on this assumption, and the proof invokes Hölder's
  inequality with respect to the positive measure \(\mu_\Lambda\).
- The surrounding text now states that any continuum limit requires an
  independent existence theorem for the limiting Schwinger functional; the
  finite-regulator convexity argument alone does not prove such a limit.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.
