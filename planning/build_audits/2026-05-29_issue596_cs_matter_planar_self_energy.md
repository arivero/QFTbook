# Issue #596 Chern-Simons-Matter Planar Self-Energy Pass

Date: 2026-05-29.

Scope:

- Advanced GitHub issue #596 in
  `monograph/tex/volumes/volume_vii/chapter10_three_dimensional_chern_simons_matter.tex`.
- Strengthened the three-dimensional Chern-Simons vector-model light-cone
  treatment beyond the gauge-field Gaussian reduction and bilocal color
  closure.

Manuscript content:

- Added subsection `Planar Bilocal Saddle and Self-Energy Equation`.
- Defined the finite-regulator inverse free propagator `Q`, singlet bilocal
  expectation `G`, current matrices `V^+`, `V^perp`, and light-cone kernel
  `K = partial_-^{-1}` with the previously declared zero-mode prescription.
- Wrote the leading large-`N` light-cone bilocal interaction
  `I_LC[G] = -2 pi lambda V^+ G K V^perp G`.
- Derived the planar Dyson equation `G(Q+Sigma)=1` from the finite-regulator
  Schwinger-Dyson identity.
- Computed the self-energy `Sigma` explicitly as the functional derivative
  of the leading bilocal interaction, including both derivative terms.
- Kept the fermionic case at the correct status: the color/bilocal derivative
  is the same, while graded signs require the declared Berezin ordering and
  spinor-current convention.

Companion checks:

- Extended `calculation-checks/cs_matter_lightfront_checks.py` with exact
  finite-matrix checks of the bilocal-interaction derivative and of the
  index convention in `G(Q+Sigma)=1`.
- Updated `calculation-checks/README.md`.
- Updated the Volume VII Chern-Simons-matter chapter dossier and
  `claude_review.md`.

Verification:

- `python3 calculation-checks/cs_matter_lightfront_checks.py` passed.
- `python3 -m py_compile calculation-checks/cs_matter_lightfront_checks.py`
  passed.
- `git diff --check` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `python3 tools/audit_theorem_form.py` passed.
- `python3 tools/audit_negative_scope_prose.py` passed.
- `tools/build_monograph.sh` passed with a clean log scan.  The built
  monograph PDF had 2547 pages at this checkpoint.

Backlog impact:

- This pass advances the exact large-`N` Chern-Simons-matter solution layer
  requested in #596 by deriving the planar self-energy equation from the
  finite-regulator singlet Schwinger-Dyson identity.
- Issue #596 remains open because the monograph still needs the continuum
  solution of the resulting integral equations in specific bosonic and
  fermionic conformal charts, finite-temperature observables, higher-spin
  constraints, duality maps, and a broader light-front framework chapter.
