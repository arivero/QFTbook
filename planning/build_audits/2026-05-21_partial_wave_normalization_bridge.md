# Partial-Wave Normalization Bridge Audit

Date: 2026-05-21.

Development pass:

- Clarified the relation between the ordered \(2\to2\) amplitude and the
  Bose-symmetrized identical-particle amplitude used in the high-energy bound
  chapter.
- Derived the even-partial-wave projection and the factor of \(32\pi\) from
  \(\mathcal M_{\rm ord}(s,x)+\mathcal M_{\rm ord}(s,-x)\).
- Connected this convention explicitly to
  \(S_\ell(s)=1+2\ii\rho(s)a_\ell(s)\), removing an implicit normalization
  bridge between the cross-section chapter and the dispersion-bound chapter.

Verification:

- `tools/audit_monograph_text.sh`
- deferred-topic scan for AdS/CFT, supersymmetry, bootstrap, large \(N\),
  localization, and defect material in active volumes
- hard-coded chapter-number scan
- `tools/build_monograph.sh`

Result:

- All checks passed.
- The compiled manuscript is
  `/Users/xiyin/QFT/monograph/tex/main.pdf`.
