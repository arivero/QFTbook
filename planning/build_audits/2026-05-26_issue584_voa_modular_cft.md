# Build Audit: Issue #584 VOA and Modular CFT

Date: 2026-05-26.

## Scope

- Added `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`.
- Included the chapter in `monograph/tex/volumes/volume_v/volume_v_current.tex`.
- Added `calculation-checks/cft_voa_modular_checks.py`.
- Updated `calculation-checks/README.md`.
- Added a chapter dossier in `planning/chapter_dossiers/volume_v/`.

## Mathematical Content

- Vertex operator algebra definition with vacuum, state-field map, conformal
  vector, translation, and locality axioms.
- OPE expansion derived from VOA locality and lower truncation.
- Ordinary modules, characters, and chiral conformal blocks as Ward-identity
  functionals.
- Higher-genus sewing through dual bases and annulus propagation factors.
- Rationality/sewing hypotheses before modular tensor category statements.
- Character modularity stated as theorem input; Verlinde formula proved from
  modular diagonalization.
- Ising modular \(S\)-matrix, quantum dimensions, and fusion rules.
- Full-CFT modular-invariant torus partition functions and leading Cardy
  high-temperature asymptotic under explicit vacuum/Tauberian hypotheses.
- Logarithmic CFT described through nonsemisimple \(L_0\), pseudo-traces, and
  finite tensor category replacements for semisimple modular data.

## Verification Plan

- `python3 calculation-checks/cft_voa_modular_checks.py`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

The final issue comment should record the actual outputs after verification.
