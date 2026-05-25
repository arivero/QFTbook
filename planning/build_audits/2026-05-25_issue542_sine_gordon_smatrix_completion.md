# 2026-05-25 Issue 542: Sine-Gordon Exact S-Matrix Completion

## Scope

Issue #542 flagged that the sine-Gordon chapter did not yet contain the full
exact scattering datum expected of the model-family chapter: the explicit
Zamolodchikov-Zamolodchikov soliton sector, soliton-breather amplitudes,
breather amplitudes, mass-coupling coordinate, and Coleman-Mandelstam map.

## Edits

- Added the UV-normal-ordered mass-coupling coordinate for the sine-Gordon
  perturbation in the \(1/(16\pi)\) free-boson normalization, with the
  conversion to the canonical kinetic normalization used earlier in the
  chapter.
- Added a Yang-Baxter proposition for the soliton matrix part, reducing the
  nontrivial \(8\times8\) component identities to hyperbolic addition
  formulae.
- Added the explicit soliton-breather scalar amplitude \(S_{sB_n}(\theta)\),
  with derivations of unitarity, crossing, direct and crossed soliton poles,
  and the redundant double-pole locations.
- Expanded the massive Thirring equivalence with the Mandelstam semi-local
  fermion operator, including the canonical momentum line integral and Klein
  factors.
- Extended `calculation-checks/sine_gordon_smatrix_checks.py` to verify
  soliton Yang-Baxter, soliton-breather unitarity and crossing, direct soliton
  pole kinematics, and redundant denominator locations.

## Targeted Verification

```text
python3 calculation-checks/sine_gordon_smatrix_checks.py
All sine-Gordon S-matrix checks passed.
```

```text
tools/audit_monograph_text.sh
Strict monograph text audit clean.

tools/audit_chapter_dossiers.sh
Chapter dossier metadata audit clean.

git diff --check
<no output>

tools/build_monograph.sh
Monograph build and log scan clean: /Users/xiyin/QFT/monograph/tex/main.pdf

pdfinfo monograph/tex/main.pdf
Pages:           1276
```
