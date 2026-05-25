# 2026-05-25 Issue #454 Weinberg Leading Soft Theorems Audit

## Scope

- GitHub issue: #454, `[Vol II] Weinberg leading soft-photon / soft-graviton
  theorem not stated`.
- Manuscript target:
  `monograph/tex/volumes/volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_ii/chapter08_infrared_divergences_inclusive_qed.md`.

## Manuscript Changes

- Promoted the leading eikonal photon factor to a labeled Weinberg leading
  soft photon theorem in the hard-kernel convention of the infrared chapter.
- Stated the hypotheses: fixed infrared regulator, hard kernel smooth under
  addition of one soft photon, nonexceptional hard kinematics, signed physical
  charges \(g_n\), and incoming/outgoing signs \(\eta_n\).
- Derived
  \[
    \mathcal M_{\beta;k,h|\alpha}
    =
    \left[
      \sum_n\eta_ng_n \frac{p_n\cdot e_h^*(k)}{p_n\cdot k}
    \right]\mathcal M_{\beta|\alpha}+O(\omega^0)
  \]
  from external-line poles, with internal attachments identified as less
  singular at fixed nonexceptional hard kinematics.
- Added the Ward-identity derivation: under
  \(e_h^\mu\mapsto e_h^\mu+ck^\mu\), the leading pole shifts by
  \(c^*\sum_n\eta_ng_n\), so descent to physical photon helicities is hard
  charge conservation.
- Added a compact figure displaying the hard kernel, the soft photon, and the
  gauge-replacement test of the leading soft factor.
- Added the Weinberg leading soft graviton theorem with
  \(g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}\) and
  \(\mathcal L_{\rm int}=-(\kappa/2)h_{\mu\nu}T^{\mu\nu}\):
  \[
    S_{\rm grav}^{(0)}
    =
    \frac{\kappa}{2}\sum_n\eta_n
    \frac{p_n^\mu p_n^\nu\varepsilon_{\mu\nu}^*(k)}{p_n\cdot k}.
  \]
- Derived the spin-two gauge-invariance check:
  \(\varepsilon_{\mu\nu}\mapsto\varepsilon_{\mu\nu}+k_\mu\xi_\nu+k_\nu\xi_\mu\)
  shifts the factor by \(\kappa\xi_\nu^*\sum_n\eta_np_n^\nu\), which vanishes
  by hard momentum conservation; species-dependent spin-two couplings would
  fail for generic hard reactions.

## Dossier Changes

- Added Weinberg leading soft theorem references, construction requirements,
  symbol entries, claim-ledger items, figure requirement, and audit note.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 805 pages, PDF 1.5.
