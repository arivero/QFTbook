# 2026-05-22 253b Opening Spectral/LSZ Source Audit

## Scope

- Handwritten source:
  - `references/253b lecture notes 2023.pdf`, pp. 1--12.
- Rendered source trace:
  - `monograph/tex/build/source_visual_trace/253b_trace-001.png` through
    `253b_trace-012.png`.
- Manuscript files:
  - `monograph/tex/volumes/volume_ii/chapter01_local_qft_spectral_data_and_path_integrals_revisited.tex`;
  - `monograph/tex/volumes/volume_ii/chapter02_the_s_matrix_and_lsz_revisited.tex`;
  - `monograph/tex/volumes/volume_ii/chapter03_bound_states_from_exchange_amplitudes.tex`.

## Source Items Checked

- The opening outline is represented by the subject organization of Volume II:
  scattering and analytic structure, renormalization, and non-Abelian gauge
  theory/QCD. It is not reproduced as semester-note framing in the monograph.
- The Poincare representation data are now explicit:
  \(U(\Lambda',a')U(\Lambda,a)=U(\Lambda'\Lambda,\Lambda'a+a')\),
  \(U=1-i\epsilon^\mu P_\mu+i\omega_{\mu\nu}J^{\mu\nu}/2+\cdots\), and the
  stress-tensor formulas for \(P^\mu\) and \(J^{\mu\nu}\) with regulator/domain
  caveats.
- The field covariance convention
  \(U(\Lambda,a)\widehat\Phi_\alpha(x)U^{-1}
  =R(\Lambda)_\alpha{}^\beta\widehat\Phi_\beta(\Lambda x+a)\) is included.
- The scalar field-on-vacuum decomposition includes the one-particle term,
  the factor \(\bigl[Z_\phi/((2\pi)^d2\omega_{\vec p})\bigr]^{1/2}\), and the
  continuum/multiparticle contribution.
- The Wightman, time-ordered, and Euclidean spectral representations are all
  present, with the same positive Kallen--Lehmann measure and the source
  \(m,2m\) spectral-density figure.
- The Wick-rotation figure has been transcribed as a clean TikZ diagram with
  Lorentzian contour \(C\), ordered real-time points, the rotation
  \(x_a^0=e^{-i\alpha}\tau_a\), and Euclidean insertions.
- The regulated path-integral representation states that the integration
  symbol is regulator-supplied and not an unregulated measure on all field
  distributions.
- The in/out basis is tied to local fields through the Haag--Ruelle packet
  limit using \(f^{(T)}\), with support near the isolated mass shell.
- The LSZ formula is retained after the nonperturbative \(S\)-operator and
  includes a note translating between covariant and delta-normalized external
  factors.
- The first scalar exchange amplitude remains in the next chapter, after the
  nonperturbative scattering and LSZ setup.

## Verification

- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf` at 424 pages.
- Rendered manuscript trace
  `monograph/tex/build/manuscript_visual_trace/253b_opening_revised_actual-163.png`
  through `253b_opening_revised_actual-174.png` was visually inspected.
- A crowding issue in the Wick-rotation figure was corrected and re-rendered
  as `monograph/tex/build/manuscript_visual_trace/253b_wick_fixed-167.png`.
