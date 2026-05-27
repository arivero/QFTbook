# Issue #628 Dense-QCD Magnetic Gap Leading-Log Pass

Date: 2026-05-27

## Scope

This pass continues the high-density QCD development in
`monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`.
It adds the controlled leading-log treatment of the magnetic contribution to
the color-superconducting gap in the trace-delta Yang-Mills convention used in
the monograph.

## Mathematical And Physical Content Added

- Stated the controlled approximation for the soft transverse HDL propagator in
  the regime \(T=0\), \(\mu_q \gg \Lambda_{\rm QCD}\), \(g(\mu_q)\ll 1\), with
  \(|\omega|\ll k_\perp\ll \mu_q\).
- Derived the Landau-damped transverse denominator
  \[
    D_T(\omega,k_\perp)^{-1}
    =
    k_\perp^2+\frac{\pi}{4}m_{D,\mu}^2\frac{|\omega|}{k_\perp}
  \]
  as the input responsible for the magnetic collinear logarithm.
- Derived the leading-log magnetic gap equation
  \[
    \Delta(p_0)=\lambda_{\rm mag}
    \int_0^{\Lambda_{\rm M}}
    \frac{dq_0\,\Delta(q_0)}
    {\sqrt{q_0^2+\Delta(q_0)^2}}
    \log\frac{\Lambda_{\rm M}}{|p_0-q_0|}
    +R(p_0),
  \]
  with no additional large collinear logarithm in \(R\).
- Fixed the trace-delta color coefficient
  \[
    \lambda_{\rm mag}=\frac{g^2C_{\rm qq}}{12\pi^2},
    \qquad
    C_{\rm qq}=\frac{N_c+1}{N_c},
  \]
  hence \(\lambda_{\rm mag}=g^2/(9\pi^2)\) for \(SU(3)\).
- Solved the reduced leading-log integral equation by converting the kernel
  \(\min(x,y)\) to the Sturm-Liouville problem
  \(\Delta''+\lambda\Delta=0\), \(\Delta(0)=0\), \(\Delta'(X)=0\), and obtained
  \[
    \log\frac{\Lambda}{\Delta_0}=\frac{\pi}{2\sqrt{\lambda}}+O(1).
  \]
- Recorded the trace-delta leading exponent
  \[
    \Delta_0=\Lambda_{\rm M}
    \exp\left[-\frac{3\pi^2}{2g}+O(1)\right],
  \]
  and the conversion to the half-trace coupling convention.
- Extended `calculation-checks/qcd_phase_checks.py` to verify the rational
  coefficient bookkeeping for the magnetic leading-log coefficient and
  exponent conversion.
- Updated the chapter dossier and calculation-checks README.

## Verification

- `python3 calculation-checks/qcd_phase_checks.py`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `git diff --check -- calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`
- `rg --pcre2 -n '\\over(?!line)' calculation-checks/README.md calculation-checks/qcd_phase_checks.py monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`
  returned no matches.
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reports 2208 pages.

## Remaining Dense-QCD Work

Issue #628 should remain open.  The next dense-QCD passes should develop the
gauge-invariant order-parameter diagnostics, Meissner screening and collective
modes, neutrality constraints, crystalline phases, anomaly matching across the
CFL phase, and the non-Fermi-liquid corrections with the same convention
discipline.
