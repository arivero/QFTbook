# 2026-05-27 Volume VI: Integrable RG Flow Trace Sum Rule

## Scope

This pass deepens Volume VI, Chapter 6 by adding a local stress-tensor test
for integrable RG-flow identifications.  The goal is to sharpen the chapter
beyond endpoint TBA central-charge matching: a proposed flow must also pass a
trace-operator normalization and form-factor spectral-sum check.

Touched files:

- `monograph/tex/volumes/volume_vi/chapter06_integrable_rg_flows_perturbed_cft.tex`
- `calculation-checks/integrable_rg_flow_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_vi/chapter06_integrable_rg_flows_perturbed_cft.md`
- `planning/build_audits/2026-05-27_volume_vi_integrable_trace_sum_rule.md`

## Manuscript Content

- Added a Zamolodchikov sum-rule datum specifying the stress-tensor trace
  normalization, the connected trace two-point distribution, contact-term
  requirements, endpoint limits, and the radial \(C\)-function derivative
  relation.
- Proved the trace sum rule
  \[
    c_{\rm UV}-c_{\rm IR}
    =
    {3\over 4\pi}\int d^2x\,|x|^2
    \langle \Theta(x)\Theta(0)\rangle_{\rm c}.
  \]
- Derived the integrable form-factor version under absolute convergence:
  each spectral contribution carries the exact radial weight \(9/E^4\).
- Added the \(\phi_{1,3}\) minimal-model target: the trace form factors of a
  proposed \(\mathcal M(m,m+1)\to\mathcal M(m-1,m)\) flow must reproduce
  \(12/[m(m^2-1)]\), the central-charge drop proved earlier in the chapter.

## Calculation Checks

The companion `calculation-checks/integrable_rg_flow_checks.py` now also
checks:

- the exact cancellation of \(\pi\) in the coefficient
  \((3/(4\pi))(2\pi)3!=9\);
- the \(9/E^4\) energy weight for rational sample energies;
- the \(\phi_{1,3}\) central-charge targets for \(4\leq m<20\);
- a positive toy spectral atom reconstructing each target, which guards the
  coefficient and the direction of the central-charge drop.

## Verification

- `python3 calculation-checks/integrable_rg_flow_checks.py`: passed.
- `python3 -m py_compile calculation-checks/integrable_rg_flow_checks.py`:
  passed.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed and rebuilt `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2094`.
