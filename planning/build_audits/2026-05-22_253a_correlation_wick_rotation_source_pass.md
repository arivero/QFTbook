# 253a pp. 15--18 Correlation Functions And Wick Rotation Source Pass

Date: 2026-05-22

Source pages checked:

- `references/253a lectures 2022.pdf`, pp. 15--18, rendered as
  `/tmp/253a_015_018-015.png` through `/tmp/253a_015_018-018.png`
- `transcription/tex/253a/foundations.tex`, "Correlation Functions and Wick
  Rotation" block

Manuscript target:

- `monograph/tex/volumes/volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex`

Repairs made:

- Strengthened the source energy-eigenstate insertion to the corresponding
  spectral-measure statement using \(P_{\widehat H}\), \(\eta_q=\widehat
  q\ket0\), and \(\mu_q(B)=\langle\eta_q,P_{\widehat H}(B)\eta_q\rangle\).
- Derived lower-half-plane analyticity from the positivity of \(E-E_0\) and
  dominated convergence.
- Added the Euclidean spectral integral before the pure-point sum.
- Restored the complex-time contour form of the vacuum-projected path
  integral, with endpoint wavefunctions included in \([Dq]_{\Gamma,\psi}\).
- Added the source-faithful contour figure with the \(t_i\), \(0\), \(t\),
  and \(t_f\) segments in the \((\operatorname{Re}t,-\operatorname{Im}t)\)
  plane.
- Added the mode-cutoff explanation \(q(\tau)=\sum_{n=1}^{N_{\rm max}}
  q_nf_n(\tau)\) as the regulated meaning behind the formal \([Dq]\).

Rendered manuscript pages inspected:

- `/tmp/qft_253a_015_018_cert-063.png` through
  `/tmp/qft_253a_015_018_cert-066.png`

Checks:

- Spectral-measure formulas and Euclidean continuation fit in the text block.
- The complex-time contour figure has readable \(t_i,0,t,t_f\) labels and no
  collisions.
- The normalized contour path-integral formula fits in one displayed line.
- The Euclidean action sign convention \(L_E(q,q')=-L(q,\ii q')\) is present.
- The mode-cutoff paragraph is present before the harmonic oscillator example.

Verification commands:

- `tools/build_monograph.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
