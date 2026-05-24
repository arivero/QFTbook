# Issue 376: Anharmonic Second-Order Self-Energy Topologies

## Scope

GitHub issue #376 noted that the anharmonic-oscillator self-energy formula
\[
  \Sigma(k)=-\frac g4+\frac{g^2}{8}\left(\frac14+\frac{1}{k^2+9}\right)
\]
was correct but did not explicitly identify the two order-\(g^2\) terms with
their diagrammatic components and analytic structure.

## Fix

- Identified the momentum-independent term \(g^2/32=(g^2/8)(1/4)\) as the
  tadpole-bubble, equivalently the double-bubble insertion after external
  amputation.
- Identified \((g^2/8)(k^2+9)^{-1}\) as the sunset insertion.
- Explained the analytic origin of \(k^2+9\): the sunset convolution is the
  Fourier transform of \(\frac18 e^{-3|\tau|}\), so its nearest singularities
  are \(k=\pm 3i\), equivalently \(k^2=-9=-(3\omega)^2\) for \(\omega=1\).
- Updated the Chapter 5 dossier.

## Verification Plan

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
