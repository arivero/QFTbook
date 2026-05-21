# Haag-Ruelle Spectral Transfer Pass

Date: 2026-05-21.

Development pass:

- Added the energy-momentum transfer statement for spacetime-smeared local
  observables in the local-net Haag--Ruelle chapter.
- Defined regular Haag--Ruelle creators using almost locality, isolated-shell
  spectral support, adjoint transfer, and nonzero one-particle creation.
- Added a spectral-support figure showing the support of \(\widehat\chi\) in
  the isolating neighborhood and the reflected support controlling \(B^*\).
- Replaced an underdefined use of energy-decreasing operators by the regular
  creator hypothesis.

Verification:

- `tools/audit_monograph_text.sh`
- deferred-topic scan for AdS/CFT, supersymmetry, bootstrap, large \(N\),
  localization, and defect material in active volumes
- hard-coded chapter-number scan
- active-volume orphan chapter scan
- `tools/build_monograph.sh`
- rendered page check for the new spectral-transfer figure

Result:

- All checks passed.
- The compiled manuscript is `/Users/xiyin/QFT/monograph/tex/main.pdf`.
