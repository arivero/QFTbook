# Volume X Schwinger-Keldysh Hydrodynamic Action Deepening Audit

## Scope

This pass addresses the later-volume thinness directive and the
assertion-as-derivation concern for Volume X, Chapter 6.  The chapter is
rewritten around the explicit quadratic Schwinger-Keldysh action for charge
diffusion, with source-response signs and noise normalization derived rather
than asserted.

## Edits

- Rewrote
  `monograph/tex/volumes/volume_x/chapter06_schwinger_keldysh_hydrodynamic_effective_actions.tex`.
- Added the closed-time-path constraints
  \(I[A,A]=0\), SK reality, and \(\operatorname{Im}I\ge0\).
- Defined the gauge-invariant Stueckelberg variables
  \(B_{s\mu}=A_{s\mu}+\partial_\mu\varphi_s\).
- Replaced the previous schematic diffusion action by the sourced action
  \[
    I_{\rm diff}=\int
    [\chi B_{a0}B_{r0}-\sigma B_{ai}\partial_tB_{ri}
    +iT\sigma B_{ai}B_{ai}],
  \]
  which gives both diffusion and the correct scalar-source response.
- Derived the continuity equation, diffusion equation, density response
  kernel, transverse Ohm response, Hubbard-Stratonovich noise correlator,
  and classical dynamical-KMS coefficient \(T\sigma\).
- Added `calculation-checks/sk_diffusion_action_checks.py` and documented it
  in `calculation-checks/README.md`.
- Rewrote the Volume X Chapter 6 dossier.

## Verification

- `python3 calculation-checks/sk_diffusion_action_checks.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf` at 1317 pages.
