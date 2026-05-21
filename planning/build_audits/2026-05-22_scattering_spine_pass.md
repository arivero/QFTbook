# Scattering Spine Pass

Date: 2026-05-22

Scope:

- `monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`

Purpose:

- Strengthen the algebraic Haag--Ruelle companion chapter so that the
  nonperturbative definition of scattering is stated before LSZ and before
  perturbative scattering rules.
- Make the assumptions and constructed objects explicit enough to align with
  the opening framework, the main Haag--Ruelle chapter, and the LSZ chapter.

Changes:

- Rewrote the chapter around a vacuum net, joint spectral projections,
  isolated mass shell, almost-local operators, spectral transfer, regular
  creators, velocity localization, Haag--Ruelle limits, wave operators, and
  asymptotic completeness.
- Corrected the LSZ interface diagram so that LSZ extracts matrix elements of
  an already-defined scattering operator from time-ordered Green functions,
  rather than appearing as an operation applied to \(S\) itself.
- Kept the perturbative interpretation strictly downstream of Green functions,
  Haag--Ruelle wave operators, and LSZ external-residue extraction.
- Rebuilt the spectral-transfer figure with notation consistent with the
  rewritten text.

Verification:

- `tools/audit_monograph_text.sh`;
- `git diff --check`;
- `tools/build_monograph.sh`;
- rendered PDF samples of the rewritten chapter at
  `/tmp/qft_scattering_visual_audit/page-135.png`,
  `/tmp/qft_scattering_visual_audit/page-136.png`,
  `/tmp/qft_scattering_visual_audit/page-137.png`,
  `/tmp/qft_scattering_visual_audit/page-138.png`, and
  `/tmp/qft_scattering_visual_audit/page-139.png`.
