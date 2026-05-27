# 2026-05-27 Issue #503 Oscillator and Instanton Application Pass

## Scope

- Reviewed the live #503 issue and compared it with the current Volume II
  Chapter 10 asymptotics/resurgence material.
- Found that the foundational Borel, lateral-sum, transseries, thimble,
  conformal-Borel, renormalon, and regulated-status layers were already
  present, but that the live issue still left an application-level gap around
  the anharmonic oscillator and instanton examples.

## Manuscript Changes

- Added a quartic-oscillator spectral Borel datum, so the object being Borel
  summed is the spectral branch \(E_n(g)\) of a named Friedrichs
  Schrodinger operator.
- Added a quoted theorem for the Graffi--Grecchi--Simon Borel summability
  result, with explicit status language explaining that the proof relies on
  sectorial analyticity and resolvent estimates rather than diagram counting.
- Added a proposition proving that Gevrey-one coefficient growth gives only
  local Borel convergence and does not imply Borel summability of a named
  observable.
- Added a BPST one-instanton sector proposition in the active trace-delta
  Yang--Mills convention, tying the ledger factor
  \(\exp[-4\pi^2/g_{\rm YM}^2+\ii\theta]\) to the explicit BPST derivation in
  the anomaly chapter.
- Added a controlled-approximation block spelling out the additional data
  needed before the BPST ledger factor becomes a semiclassical formula for a
  continuum QFT observable.

## Calculation Checks

- Expanded `calculation-checks/borel_laplace_checks.py` with exact finite
  checks for the BPST trace-delta action conversion and for the local-only
  content of a Gevrey-one coefficient bound.

## Verification

- `python3 calculation-checks/borel_laplace_checks.py` passed.
- `python3 -m py_compile calculation-checks/borel_laplace_checks.py` passed.
- Edited-file long-line scan passed.
- `git diff --check -- <edited paths>` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` initially found a missing figure heading
  in the unrelated Chapter 16a spinor dossier; that metadata heading was added
  and the audit then passed.
- `tools/build_monograph.sh` passed after tightening one overfull line in the
  new quoted-theorem status paragraph.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported `Pages: 2133`.
