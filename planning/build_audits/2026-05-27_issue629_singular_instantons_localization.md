# 2026-05-27 Issue #629 Singular Instantons In Localization Pass

## Scope

- Reviewed live GitHub issue #629 and the existing Vol VII localization and
  Seiberg-Witten chapters.
- Found that Vol VII ch07 already contains ADHM data, fixed-point theorem,
  and the \(k=1\) Nekrasov coefficient, but Vol VII ch16 still treated
  point instantons as a boundary phrase rather than as a compactification
  problem.

## Manuscript Changes

- Added a dedicated singular-instanton section to Vol VII ch16.
- Defined the Uhlenbeck, Gieseker/framed torsion-free-sheaf, and
  Donaldson--Uhlenbeck compactification roles.
- Proved the Uhlenbeck stratum codimension formula
  \(2\ell(N-1)\) in complex dimension.
- Defined ADHM stability and explained failure of stability as the
  finite-dimensional small-instanton mechanism.
- Added the Young-diagram tangent Euler-class formula and proved its
  one-box reduction to the \(U(N)\) one-instanton Nekrasov term.
- Added the \(k=1\) geometry
  \(\mathfrak M_{1,N}^{G}\simeq\mathbb C^2\times T^\ast\mathbb{CP}^{N-1}\).
- Added a field-theoretic Gieseker-matching hypothesis, explicitly separating
  theorem-level equivariant localization on the chosen resolved moduli space
  from the still-regulator-dependent claim that the \(S^4\) gauge-theory path
  integral produces that resolved integral.

## Calculation Checks

- Expanded `calculation-checks/susy_instanton_nekr_checks.py` with exact
  Uhlenbeck codimension arithmetic and one-box tangent Euler-class checks.

## Verification

- `python3 calculation-checks/susy_instanton_nekr_checks.py`
- `python3 -m py_compile calculation-checks/susy_instanton_nekr_checks.py`
- Edited-file long-line scan.
- `git diff --check --` on the edited manuscript, calculation-check,
  dossier, and audit files.
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported `Pages:           2146`.
