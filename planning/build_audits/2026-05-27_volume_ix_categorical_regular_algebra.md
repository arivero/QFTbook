# 2026-05-27 Volume IX: Categorical Regular Algebra Pass

## Scope

This pass deepens Volume IX, Chapter 9 by turning the abstract condensation
paragraph into explicit finite algebra.  It addresses part of the promised
categorical-symmetry examples gap by proving the regular-algebra and
self-dual-gauging fusion-ring identities inside the categorical-symmetry
chapter itself, while still separating this finite algebra from the existence
of an interacting continuum QFT realizing the data.

Touched files:

- `monograph/tex/volumes/volume_ix/chapter09_categorical_symmetry_and_defect_fusion.tex`
- `calculation-checks/ising_defect_fusion_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_ix/chapter09_categorical_symmetry_and_defect_fusion.md`
- `planning/build_audits/2026-05-27_volume_ix_categorical_regular_algebra.md`

## Manuscript Content

- Added the finite regular algebra
  \(A_H=\oplus_{h\in H}D_h\) in an untwisted pointed defect subcategory.
- Defined the normalized comultiplication
  \[
    \Delta(D_k)=|H|^{-1}\sum_{gh=k}D_g\otimes D_h.
  \]
- Proved the object identity \(A_H\otimes A_H\simeq |H|A_H\),
  separability \(m\circ\Delta=\operatorname{id}_{A_H}\), and the Frobenius
  identity by explicit finite-bijection arguments.
- Added the self-dual finite-gauging fusion ring
  \(D_gD_h=D_{gh}\), \(D_hN_H=N_HD_h=N_H\),
  \(N_H^2=\oplus_{h\in H}D_h\), with an associativity proof and
  \(d(N_H)=\sqrt{|H|}\).
- Added cyclic examples, with \(N=2\) identified as the Ising
  Kramers--Wannier fusion rule and \(N>2\) explicitly marked as fusion-ring
  data requiring additional associators, junction pairings, and QFT
  realization data.

## Calculation Checks

The companion `calculation-checks/ising_defect_fusion_checks.py` now also
checks:

- regular-algebra separability and Frobenius identities;
- self-dual gauging fusion-ring associativity;
- noninvertibility of the self-dual defect for nontrivial finite groups;
- cyclic groups \(C_N\), \(1\leq N<8\), and the nonabelian test group \(S_3\).

## Verification

- `python3 calculation-checks/ising_defect_fusion_checks.py`: passed.
- `python3 -m py_compile calculation-checks/ising_defect_fusion_checks.py`:
  passed.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed and rebuilt `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2097`.
