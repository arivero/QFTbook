# Spinor Conventions Appendix Audit

Date: 2026-05-24.

Scope:

- Added `monograph/tex/appendices/spinor_conventions.tex` and included it
  after `\appendix` in `monograph/tex/main.tex`.
- Centralized the monograph's operative gamma convention:
  \(\eta=\operatorname{diag}(-,+,+,+)\),
  \(\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\),
  \(\beta=i\gamma^0\),
  \(\bar\psi=\psi^\dagger\beta\),
  \(S^{\mu\nu}=-(i/4)[\gamma^\mu,\gamma^\nu]\), and
  \(\gamma_5=-i\gamma^0\gamma^1\gamma^2\gamma^3\).
- Modeled the explicit four-dimensional basis and the
  Wess-Bagger-type comparison on the stringbook spinor appendix, while
  keeping all comparisons at the same mostly-plus Lorentzian metric.
- Recorded two-component block conventions, Majorana conjugation,
  dimensional-continuation rules for \(\gamma_5\), two- and three-dimensional
  Lorentzian spinors, Euclidean spinor recursion, and the \(SO(6)\)/\(SO(8)\)
  block identities needed later for supersymmetry.
- Cross-linked the massive-spin, spinor-field, and anomaly chapters to the
  appendix.
- Updated the relevant chapter dossiers.

Verification to run:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
