# 2026-05-28 Issue #633: Bound-State Pole Factorization Pass

## Scope

Reading-based correction to the reopened #633 backlog for Volume II,
Chapter 3, `Bound States from Exchange Amplitudes`.

The chapter already separated elementary exchange poles, composite bound
states, sheet conventions, and near-threshold caveats.  The remaining
substance gap was that the factorization statement was prose rather than a
conditional theorem with explicit spectral and LSZ hypotheses.

## Manuscript Changes

- Added Theorem `thm:bound-state-spectral-atom-first-sheet-pole`, deriving
  the first-sheet pole in a connected time-ordered channel correlator from an
  isolated finite-multiplicity one-particle spectral atom.
- Added Theorem `thm:bound-state-lsz-pole-factorization`, proving that LSZ
  amputation turns the internal spectral pole into the factorized invariant
  amplitude pole
  \[
    \mathcal M_{fi}(s,z)
    =
    \frac{\sum_\lambda
      \Gamma^{\rm out}_\lambda\Gamma^{\rm in}_\lambda}
         {M_B^2-s-\ii0}
    +\mathcal M^{\rm reg}_{fi}.
  \]
- Added the angular-residue/spin paragraph deriving the partial-wave spin
  selection from rotational covariance and the spherical-harmonic addition
  theorem.  This was later demoted from proposition form in the anti-wrapper
  audit.
- Preserved the existing caveat that these are conditional pole consequences,
  not a proof that an arbitrary attractive channel contains a stable bound
  state.

## Calculation Check

- Added `calculation-checks/bound_state_pole_checks.py`.
- The script verifies finite-rank spectral-residue factorization,
  \(P^2+M^2=M^2-s\) in the mostly-plus convention, Legendre orthogonality,
  spin-\(J\) partial-wave pole selection, and the scalar-QED
  \(P_1(\cos\theta)\) numerator check.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/bound_state_pole_checks.py`
- `python3 -m py_compile calculation-checks/bound_state_pole_checks.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build and final log scan are clean.  The generated
`monograph/tex/main.pdf` has 2323 pages.
