# Volume VI Mirror Vacuum Luescher Pass

## Scope

- `monograph/tex/volumes/volume_vi/chapter07_mirror_channel_tba_finite_size_wrapping.tex`
- `planning/chapter_dossiers/volume_vi/chapter07_mirror_channel_tba_finite_size_wrapping.md`
- `calculation-checks/mirror_tba_wrapping_checks.py`
- `calculation-checks/README.md`

## Content Added

The mirror-channel finite-size chapter now contains a theorem-level derivation
of the leading vacuum Luescher correction from the TBA fixed point.  The new
proposition states the finite-species, positive-mass-gap, and integrable-kernel
hypotheses explicitly, proves existence and uniqueness of the small-occupation
branch by contraction, derives the one-winding coefficient
\[
  -\sum_a \frac{m_a}{\pi}K_1(m_aR),
\]
and proves the remainder bound
\[
  |\mathcal R_2(R)|\le C R^{-1/2}e^{-2m_*R}.
\]

The calculation check now verifies the factor of two in the full-line Bessel
integral, the conversion of the energy measure \(-m/(2\pi)\) to
\(-mK_1(mR)/\pi\), and the exponential threshold \(2m_*\) for the two
remainder sources \(q_a e^{-m_*R}\) and \(q_a^2\).

## Verification

- `python3 calculation-checks/mirror_tba_wrapping_checks.py`
- `python3 -m py_compile calculation-checks/mirror_tba_wrapping_checks.py`
- `git diff --check`
- text audit for weak-language patterns in the edited TeX and dossier
- `tools/build_monograph.sh`
