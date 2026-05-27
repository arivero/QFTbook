# Build Audit: Volume X Schwinger--Keldysh Depth Pass

## Scope

- Branch: `main`.
- Files edited:
  - `monograph/tex/volumes/volume_x/chapter03_real_time_schwinger_keldysh.tex`
  - `planning/chapter_dossiers/volume_x/chapter03_real_time_schwinger_keldysh.md`
  - `calculation-checks/schwinger_keldysh_operator_checks.py`
  - `calculation-checks/README.md`

## Substantive Changes

- Added a closed-contour formulation as a trace identity with the backward
  branch orientation sign explicitly defined.
- Added a figure for the closed time path, final trace gluing, and optional
  Euclidean segment representing a thermal initial density matrix.
- Proved largest-time cancellation by factoring out common future evolution,
  using trace cyclicity and unitarity.
- Connected the largest-time identity to the cancellation of latest common
  physical-source insertions, clarifying the origin of causal response in the
  \(r/a\) formalism.
- Extended the public Schwinger--Keldysh calculation check to verify the
  \(G^{aa}=0\) two-point cancellation and the retarded-support contour
  combination in a finite two-level system.

## Verification Plan

- `python3 calculation-checks/schwinger_keldysh_operator_checks.py`
- `python3 -m py_compile calculation-checks/schwinger_keldysh_operator_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
