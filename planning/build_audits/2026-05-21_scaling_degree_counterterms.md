# Scaling Degree Counterterm Audit

Date: 2026-05-21.

Development pass:

- Added a distribution-theoretic explanation of counterterm locality in the
  renormalizability chapter.
- Defined scaling degree for distributions on
  \(\mathbb R^n\setminus\{0\}\).
- Stated the extension theorem for distributions at a collision diagonal:
  uniqueness below critical scaling degree, and derivative-of-delta ambiguity
  above it.
- Connected derivative-of-delta ambiguities to momentum-space Taylor
  polynomial counterterms and to the forest-formula treatment of multiple
  collision diagonals.

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
