# 2026-05-26 Issue #526 Soft-Drop IRC Classification Pass

GitHub issue: #526, concerning rigorous modern jet-substructure coverage.

## Manuscript Changes

Volume II, Chapter 19b now corrects the soft-drop IRC statement.

- For \(\beta_{\rm SD}>0\), the groomed four-vector is collinear safe because
  \(z_{\rm cut}\theta^{\beta_{\rm SD}}\to0\) as the splitting angle
  \(\theta\to0\).
- For \(\beta_{\rm SD}=0\), the groomed four-vector is not collinear safe as a
  standalone observable: a collinear split with softer energy fraction
  \(z<z_{\rm cut}\) fails the mMDT condition and removes a finite fraction of
  the parent four-vector.
- The chapter now states that mMDT safety claims must name the measured
  functional of the groomed constituents, such as a groomed mass or
  energy-correlation shape, and check that functional directly.

This avoids the common loose statement that "soft drop is IRC safe" without
specifying the actual measured output.

## Calculation Checks

Added `calculation-checks/soft_drop_irc_checks.py`, which verifies in exact
rational arithmetic:

- the \(\beta_{\rm SD}=0\) collinear counterexample for the groomed
  four-vector;
- the \(\beta_{\rm SD}>0\) threshold behavior for the same rational
  collinear sample.

`calculation-checks/README.md` and the chapter dossier were updated.

## Verification

Completed before commit:

- `python3 calculation-checks/soft_drop_irc_checks.py`
- `python3 -m py_compile calculation-checks/soft_drop_irc_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` with 1765 pages.
