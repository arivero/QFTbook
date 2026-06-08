# Issue #853 sine-Gordon soliton mass derivation repair

Date: 2026-06-08.

Scope:

- Targeted the duplicated sine-Gordon one-loop soliton mass discussion in
  Volume II Chapter 17c and Volume VI Chapter 08.
- Replaced the circular finite-counterterm presentation with one canonical
  mode-number/Born-subtracted derivation in Volume VI and a concise
  cross-reference in Volume II.

Before:

- Both chapters evaluated the divergent phase-shift density integral
  \(-m\operatorname{arsinh}(\Lambda/m)/\pi\) and then declared
  \(\Delta M_{\rm ct}=m\operatorname{arsinh}(\Lambda/m)/\pi-m/\pi\).
- The companion scripts verified only that the assigned finite counterterm
  cancelled the displayed expression.
- The exact lightest-breather comparison was available, but the semiclassical
  determinant calculation had not independently produced the finite
  \(-m/\pi\).

After:

- Volume VI now states the regulator:
  \(k_nL=\pi n\), \(q_nL+\delta(q_n)=\pi n\) after combining the parity
  channels into the total positive-momentum phase shift.
- The branch is fixed by \(\delta(0^+)=\pi\), \(\delta(\infty)=0\), so
  Levinson accounts for the translation zero mode.  Removing that mode from
  the oscillator determinant contributes \((0-m)/2\).
- The first Born phase is derived from the fluctuation potential
  \(V_K=-2m^2{\rm sech}^2(mx)\), with \(\int V_K=-4m\), giving
  \(\delta_1(k)=2m/k\).
- The no-tadpole normal-ordering counterterm cancels the first-Born tadpole
  graph only; no finite \(-m/\pi\) is inserted into the counterterm.
- The finite determinant is
  \[
    -\frac m2
    -\frac{1}{2\pi}\int_0^\infty
      \frac{k\,dk}{\sqrt{k^2+m^2}}\,[\delta(k)-\delta_1(k)].
  \]
  With \(s=k/m\), the finite integral is \(m(2-\pi)\), so the result is
  \(-m/\pi\).
- Volume II now points to the canonical Volume VI derivation rather than
  duplicating the cutoff/counterterm algebra.

Negative controls added:

- Omit the phase-shift surface term.
- Omit or double-count the translation zero mode.
- Leave the first Born term unsubtracted.
- Insert a finite counterterm.
- Use the exact breather answer as the counterterm definition.

Verification:

- `python3 calculation-checks/soliton_quantization_channel_checks.py`
- `python3 calculation-checks/sine_gordon_smatrix_checks.py`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii --root monograph/tex/volumes/volume_vi`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii --root monograph/tex/volumes/volume_vi --fail`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii --root monograph/tex/volumes/volume_vi`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii --root monograph/tex/volumes/volume_vi --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter17c_solitons_collective_quantization.tex monograph/tex/volumes/volume_vi/chapter08_sine_gordon_massive_thirring_affine_toda.tex`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
