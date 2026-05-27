# 2026-05-27 Issue #505 Fermionic Fixed-Point Benchmark Pass

## Scope

- Reviewed the live #505 issue and the existing rigorous-RG chapter.
- Found that the chapter already contained the Banach-space fixed-point
  definition, Newton--Kantorovich validation, projection-residual warnings, and
  universality datum, but the recent fermionic constructive-RG benchmark was
  still only summarized in prose.

## Manuscript Changes

- Added a constructive fermionic fixed-point output datum: fixed UV cutoff,
  Grassmann covariance, Banach kernel space, exact RG map, fixed interaction,
  source dimensions, response functions, and remainders.
- Added a quoted theorem for the long-range fermionic \(\psi^4_d\) fixed point
  in \(d=1,2,3\), recording the nontrivial fixed interaction, convergent tree
  construction of response functions, naive field exponent, anomalous analytic
  density exponent, and stretched-exponential cutoff-controlled remainder.
- Added a proposition proving that irrelevant tails are part of the RG theorem:
  a projected local-coordinate zero is not a Wilsonian fixed point unless the
  irrelevant residual vanishes or is solved by a controlled graph.

## Calculation Checks

- Expanded `calculation-checks/rg_projection_checks.py` with exact rational
  checks for a finite irrelevant-tail graph equation.

## Verification

- `python3 calculation-checks/rg_projection_checks.py`
- `python3 -m py_compile calculation-checks/rg_projection_checks.py`
- Edited-file long-line scan:
  `python3 - <<'PY' ...`
- `git diff --check --` on the edited manuscript, calculation-check,
  dossier, and audit files.
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported `Pages:           2134`.
