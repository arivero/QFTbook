# 2026-05-29 Fifth Cross-Volume Wrapper Pass

Scope: continuation of issue #691 anti-wrapper audit.  This pass read the
next short-proof cluster and one assumption-heavy QSC cluster by substance.

Demotions made:

- Volume II, Wilsonian RG: demoted `Finite-reference critical surface` from
  theorem/proof form to an explicit Banach implicit-function construction.
  The text now says that the QFT burden is constructing the Banach RG chart,
  differentiable endpoint map, and invertible relevant derivative; the graph
  statement itself is ordinary functional analysis.
- Volume III, conformal group: demoted `Parabolic stabilizer of a Euclidean
  point` from proposition/proof form to representation-theoretic setup prose.
- Volume IV, charged Haag--Ruelle/LSZ: demoted `Ray dressing and axial gauge`
  to a worked axial-gauge coordinate calculation.
- Volume IV, charged Haag--Ruelle/LSZ: demoted `Compact dressing changes and
  LSZ coordinates` to a residue-coordinate calculation in prose.

Strengthenings made:

- Volume IV, charged Haag--Ruelle: strengthened the Gauss-law obstruction
  proof by spelling out the smeared large-sphere charge approximants, spacelike
  locality step, and passage to the limiting charge as a domain pairing.
- Volume VII, six-dimensional SCFT: strengthened the BPS string tension proof
  by writing the positive supercharge anticommutator matrix whose eigenvalues
  give \(T_q\pm |Z_q|\), making the BPS inequality and saturation condition
  explicit.

Assumption audit note:

- The local \(P\)-\(Q\) bridge in the planar QSC chapter was reread.  It is
  already phrased as an assumption plus local algebra paragraph rather than as
  a theorem; no additional demotion was needed in this pass.

Guard update: `tools/audit_theorem_form.py` now rejects recurrence of the four
newly demoted theorem titles.

Verification:

- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- stale-label scan for the four demoted labels
- `git diff --check`
- `tools/build_monograph.sh`

The full build completed cleanly with `monograph/tex/main.pdf` at 2581 pages.
The short-proof heuristic queue used for this pass moved from 43 to 38
candidates.  This queue is narrower than the broad all-title triage queue and
is not an assertion that the remaining entries are defects.
