# Issue #642 Fake-Proof Audit

## Scope

Addressed GitHub issue #642, prompted by the review of the Standard Model
chapter proposition formerly titled "Minimal-subtraction running does not
supply a Wilsonian cutoff."  The target failure mode is a theorem-family
environment whose "proof" merely paraphrases surrounding definitions or states
that two kinds of data are logically distinct.

## Manuscript Changes

- Converted the Standard Model minimal-subtraction/Wilsonian-cutoff block into
  `remark[Scope of minimal-subtraction running]`.
- Converted `Logical parts of the hybrid definition` into a remark, retaining
  its component-by-component explanation as status prose rather than a proof.
- Converted the lattice-QCD/full-Standard-Model-regulator block into
  `remark[Lattice QCD inside the hybrid Standard Model]`.
- Converted the regulated-asymptotic-datum status block in the RG chapter into
  `remark[Scope of a regulated asymptotic datum]`.
- Split the chiral-lattice anomaly statement: the proposition now proves only
  the determinant-line obstruction necessity, while the sufficiency boundary is
  stated in a following remark.
- Retitled the borderline and genuine-proof blocks with forward positive
  headings: Gevrey-one Borel convergence, tempered-distribution counterexample,
  off-shell/on-shell supersymmetry multiplets, gamma5-Hermiticity determinant
  reality, finite-cutoff interpolation ambiguity, and Gauss-law charge
  annihilation.
- Began the broader theorem-form cleanup from issue #640 by demoting the AQFT
  field-coordinate tautology to a remark, converting the Gupta--Bleuler
  derivation tableau into a construction plus proposition, and replacing the
  duplicate unitarity-bounds theorem/section pair by one section with a
  collected reference list.

## Harness And Audit Tool

- Added a strict harness rule forbidding theorem-family environments for
  scope calibration, terminology policing, or absence-of-construction
  observations.
- Added `tools/audit_theorem_form.py`, a narrow audit for theorem-family
  headings framed as scope negations.

## Verification

- `tools/audit_theorem_form.py`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

The full build regenerated `monograph/tex/main.pdf` at 2355 pages and the
build-log scan was clean: no unresolved references and no retained overfull
headings from this pass.
