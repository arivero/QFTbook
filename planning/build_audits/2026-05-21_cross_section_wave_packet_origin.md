# Cross-Section Wave-Packet Origin Audit

Date: 2026-05-21.

Development pass:

- Corrected the \(T\)-kernel notation in the cross-section chapter so it is
  explicitly an asymptotic Fock-space matrix element, with the Haag--Ruelle
  kernel interpretation stated separately.
- Added a wave-packet definition of cross section as an integral of transition
  probability over transverse impact parameter.
- Explained the narrow-packet origin of the sharp-momentum phase-space formula
  and the invariant flux factor \(4E_1E_2v_{\mathrm{rel}}\).

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
