# 2026-06-06 Issue #597 Instanton Density-Gate Audit

## Scope

- Volume II `chapter20d_instantons_and_physical_amplitudes.tex` now begins
  its instanton-amplitude construction with a one-loop density gate.
- The new block imports the Chapter 20 density result and separates its
  physical origins: collective-coordinate Jacobian, bosonic zero-mode
  normalization, running BPST action, zero-mode-deleted fluctuation
  determinant logarithm, and finite scheme/orientation constant.
- The point is not to deepen ADHM geometry.  The pass makes explicit why the
  density is already fluctuation data and why a physical amplitude still needs
  zero-mode/source powers, endpoint control, projection, and scheme transport.

## Companion Check

- `calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  adds `check_one_loop_density_gate_rg_and_channel_power`.
- The check verifies the exact one-loop RG cancellation `alpha - b0 = 0`,
  distinguishes the density-only power from mass-saturated and hard
  four-source channel powers, and checks finite determinant constants cancel
  only in transported same-channel ratios.
- Negative controls reject a wrong determinant-log power, a density-only hard
  channel exponent, a changed gate treated as a same-channel ratio, and an
  absolute coefficient with the finite determinant convention dropped.

## Re-audit Notes

- Process notes remain in planning files only.
- The TeX block is placed before the channel definition so the reader sees
  the fluctuation/RG measure input before the chapter packages source and
  projection data into physical channels.
