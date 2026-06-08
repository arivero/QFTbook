# Issue #729 Vol XII microlocal/pAQFT printed-order repair

Date: 2026-06-08.

Scope:

- Targeted Volume XII after the external review noted that microlocal and
  pAQFT foundations were printed after several chapters that consume them.
- Repaired printed order, opening dependency maps, and chapter dossiers.  No
  directive text was inserted into TeX.

Before:

- Printed order opened with locally covariant QFT and Hadamard states, then
  point splitting, trace anomalies, Unruh, Hawking, background gauge/index,
  global anomalies, cosmology, microlocal spectrum condition, pAQFT, and
  semiclassical backreaction.
- This made the wavefront-set product criterion, microlocal Hadamard
  condition, Hadamard recursion, and pAQFT local-renormalization framework
  appear after applications that implicitly rely on them.
- Several openings used adjacency prose such as `previous chapter` or
  `next chapter` in places that would become misleading after a structural
  repair.

After:

- Printed Volume XII order is now:
  microlocal spectrum condition; locally covariant QFT and Hadamard states;
  perturbative algebraic QFT; point splitting; trace anomalies; Unruh;
  Hawking; cosmological particle creation; semiclassical backreaction;
  background gauge/index theory; eta invariants and global anomalies.
- Application openings now name their upstream inputs:
  point splitting names the Hadamard wavefront condition, parametrix
  recursion, and product criterion; trace anomalies name the point-split
  stress tensor and finite local counterterms; Hawking and cosmology name the
  microlocal Hadamard state input; semiclassical backreaction names the
  Hadamard state class, locally covariant algebra, pAQFT/free-field composite
  stress prescription, point-splitting choices, and anomaly counterterm
  budget.
- The LCQFT control matrix was renamed from status language to
  claim-control language so the chapter reads as mathematical scope control
  rather than project metadata.
- The index-theory/global-anomaly pair remains adjacent, but the pair is now a
  later background-gauge anomaly lane rather than an interruption between
  horizon/cosmology and backreaction.

Anti-overclaim boundary:

- This pass is architecture and dependency repair.  It does not claim a new
  nonperturbative interacting curved-spacetime QFT, a full interacting
  horizon theorem, or a general semiclassical existence theorem.
- The pAQFT material remains a perturbative construction; the backreaction
  chapter remains conditional on state, stress tensor, EFT coordinates,
  response/noise window, and observable output.

Verification:

- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_xii`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_xii`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xii --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_xii/volume_xii_current.tex`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
