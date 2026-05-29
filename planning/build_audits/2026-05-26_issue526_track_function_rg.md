# 2026-05-26 Issue #526 Track-Function RG Pass

GitHub issue: #526, concerning rigorous modern jet-substructure coverage.

## Manuscript Changes

Volume II, Chapter 19b now treats track functions as nonperturbative operator
coordinates with a paired real--virtual renormalization datum, rather than as
an informal substitute for IRC safety.

- The chapter defines a finite-kernel track-function evolution datum with
  species labels, splitting kernels \(K_{i\to jk}(z,\mu)\), and the paired
  loss rate \(\Gamma_i=\sum_{j,k}\int dz\,K_{i\to jk}\).
- The nonlinear evolution equation is written with the charged-fraction
  addition law \(x=zx_1+(1-z)x_2\).
- A later anti-wrapper pass demoted the finite-kernel moment calculation from
  a proposition to a worked paragraph.  The paragraph proves that paired
  evolution preserves \(\int_0^1 dx\,T_i(x,\mu)=1\) and derives the first
  charged-energy moment equation
  \[
    \mu {d m_i\over d\mu}
    =
    \sum_{j,k}\int_0^1 dz\,K_{i\to jk}(z,\mu)
    \bigl(zm_j+(1-z)m_k-m_i\bigr).
  \]
- The text explicitly separates the finite-kernel proof from the
  distributional renormalized QCD kernels, recording what algebraic
  real--virtual pairing must preserve in a full perturbative scheme.

## Calculation Checks

Added `calculation-checks/track_function_moment_checks.py`, which verifies in
exact rational arithmetic:

- unit normalization for discrete track measures;
- vanishing normalization derivative under the paired gain--loss evolution;
- equality between the first moment of the full evolved discrete measure and
  the closed first-moment formula.

`calculation-checks/README.md` and the chapter dossier were updated.

## Verification

Completed before commit:

- `python3 calculation-checks/track_function_moment_checks.py`
- `python3 -m py_compile calculation-checks/track_function_moment_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` with 1766 pages.
