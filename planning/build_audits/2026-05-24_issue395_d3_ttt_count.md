# Issue 395: Three-Dimensional Parity-Even TTT Structure Count

Date: 2026-05-24.

Issue:

- GitHub #395 requested that the \(D=3\) stress-tensor three-point structure
  count be displayed explicitly as two parity-even separated structures and
  accompanied by references.

Existing content verified:

- `chapter08_correlation_functions_and_conformal_frames.tex` already displays
  the \(D=3\) Schouten degeneration
  \[
    \mathcal I^{(1)}_{D=3}
    -
    \mathcal I^{(2)}_{D=3}
    +
    2\mathcal I^{(3)}_{D=3}=0
  \]
  and concludes that the parity-even \(D=3\) separated \(TTT\) correlator has
  two independent structures before adding the parity-odd \(D=3\) structure.

Fix:

- Added an explicit footnote at the \(D=3\) count citing Maldacena--Zhiboedov
  for three-dimensional conserved-current/stress-tensor structures and the
  Costa--Penedones--Poland--Rychkov / Costa--Hansen--Penedones--Trevisani
  spinning-correlator technology.
- Updated the chapter dossier.

Verification to run:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
