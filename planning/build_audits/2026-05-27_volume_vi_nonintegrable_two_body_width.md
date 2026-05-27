# Volume VI Nonintegrable Bridge Two-Body Width Pass

## Scope

- `monograph/tex/volumes/volume_vi/chapter10_bridges_to_nonintegrable_two_dimensional_qft.tex`
- `planning/chapter_dossiers/volume_vi/chapter10_bridges_to_nonintegrable_two_dimensional_qft.md`
- `calculation-checks/nonintegrable_bridge_checks.py`
- `calculation-checks/README.md`

## Content Added

The nonintegrable-bridge chapter now contains an explicit derivation of the
two-particle decay-width formula in \(1+1\) dimensions from the finite-volume
golden-rule limit.  The new proposition defines the Kallen polynomial, the
threshold condition, the two on-shell orientations, and the labelled versus
unlabelled channel convention, then evaluates the delta functions and the
rapidity-to-momentum Jacobian:
\[
  \Gamma_{A\to rs}
  =
  \frac{\epsilon^2}{M_Ap_*}
  \sum_{\sigma=\pm1}
  |\mathcal F_{rs;A}(\theta_r^\sigma,\theta_s^\sigma)|^2
\]
for labelled ordered final particles, with a factor \(1/2\) for an unordered
identical-particle channel.

The calculation check now verifies the Kallen momentum identity, both
on-shell energy identities, and the squared inverse of the delta-function
Jacobian \(|p_*|M_A/(E_r^*E_s^*)\) using exact rational arithmetic.

## Verification

- `python3 calculation-checks/nonintegrable_bridge_checks.py`
- `python3 -m py_compile calculation-checks/nonintegrable_bridge_checks.py`
- `git diff --check`
- text audit for weak-language patterns in the edited TeX and dossier
- `tools/build_monograph.sh`
