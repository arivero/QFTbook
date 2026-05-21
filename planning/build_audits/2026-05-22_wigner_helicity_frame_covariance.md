# Wigner and Helicity Frame Covariance Pass

Date: 2026-05-22.

Development pass:
- Added the massive-spin-frame construction over the positive-energy mass
  shell, including the invariant measure, distributional spin-frame map,
  Wigner cocycle identity, and momentum-dependent standard-boost frame
  changes.
- Added the vacuum-to-particle equivariance condition relating Lorentz
  covariance of a field to Wigner rotation of the one-particle spin label.
- Added the corresponding helicity-frame construction for massless
  one-particle states, including the helicity character and conjugation law
  under little-group frame changes.
- Clarified how vector polarization representatives transform under a
  helicity-frame change: dual helicity phase plus the \(k_\mu\)-shift generated
  by the null-translation subgroup.
- Retouched the double-cover and polarization-representative TikZ figures to
  remove label crowding after the added material shifted pagination.

Verification:
- `tools/audit_monograph_text.sh`
- deferred-topic scan over active monograph TeX files
- hard-coded chapter-number scan over active monograph TeX files
- active-volume orphan chapter scan
- `tools/build_monograph.sh`
- Rendered and visually inspected the affected figure pages:
  `/tmp/qft_rep_figures_final/spin-126.png` and
  `/tmp/qft_rep_figures_final/pol-134.png`.

Result:
- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.
