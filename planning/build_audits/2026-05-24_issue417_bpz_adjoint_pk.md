# Issue 417: BPZ Adjoint of Translations and Special Conformal Generators

Date: 2026-05-24.

Issue:

- GitHub #417 flagged that the radial-quantization chapter asserted
  \(\widehat P_\mu^\dagger=\widehat K_\mu\) because inversion exchanges the
  corresponding flat-space vector fields.
- The missing step was the Hilbert-space realization: the equality must be an
  adjoint relation in the reflection-positive radial completion, using the BPZ
  bra construction rather than only a statement about conformal Killing
  vectors.

Fix:

- Added the dense local finite-energy domain
  \(\mathcal D_{\rm loc}\subset\mathcal H_{S^{D-1}}\) to the adjoint
  discussion.
- Displayed the BPZ bra limit
  \[
    \langle\!\langle\mathcal O|
    =
    \lim_{\tau\to+\infty}
    \ee^{\Delta\tau}
    \bra{\vac}\widetilde{\mathcal O}^{\,\Theta_{\rm int}}(\tau,n),
  \]
  with the spin-frame and Weyl factors supplied by the radial reflection map.
- Stated the finite reflected-transformation identity
  \[
    \langle A,T_aB\rangle_{\rm rad}
    =
    \langle C_aA,B\rangle_{\rm rad},
    \qquad C_a=\vartheta T_a\vartheta,
  \]
  for \(A,B\in\mathcal D_{\rm loc}\), and differentiated it to obtain
  \[
    \langle A,\widehat P_\mu B\rangle_{\rm rad}
    =
    \langle \widehat K_\mu A,B\rangle_{\rm rad}.
  \]
- Cross-referenced this domain adjoint relation from the unitarity-bounds
  chapter before using descendant Gram positivity.
- Updated the affected chapter dossiers.

Verification:

- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean.
- `pdfinfo monograph/tex/main.pdf` reports 781 pages.
