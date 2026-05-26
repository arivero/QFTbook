# 2026-05-26 Volume IX Duality Defects Depth Pass

Scope: comprehensive depth pass on Volume IX, Chapter 10, in response to the
later-volume weakness that categorical symmetry examples were promised but not
developed with enough finite algebra and proof content.

## Manuscript Changes

Volume IX, Chapter 10 now treats finite gauging and duality defects as actual
constructions rather than informal examples.

- Defined finite symmetry backgrounds as principal \(G\)-bundles and flat
  cocycles modulo gauge transformations.
- Defined finite gauging by the groupoid-cardinality sum with explicit
  \(1/|\operatorname{Aut}(P)|\) factors.
- Proved disjoint-union multiplicativity of the finite gauging convention.
- Separated Dijkgraaf-Witten degree-\(D\) twists from degree-\(D+1\) anomaly
  trivialization.
- Proved the gauging-interface slab fusion relation
  \(\mathcal N_G^\dagger\mathcal N_G\simeq\oplus_{g\in G}D_g\).
- Defined the regular algebra defect \(A_G=\oplus_gD_g\) and proved
  \(A_G\otimes A_G\simeq |G|A_G\).
- Derived the two-dimensional orbifold local-operator decomposition and the
  pair-of-pants monodromy selection rule.
- Proved that self-dual anomaly-free finite gauging produces a
  noninvertible defect with quantum dimension \(\sqrt{|H|}\).
- Developed the Ising \(\mathbb Z_2\) and \(A_3\triangleleft S_3\) examples.
- Expanded gauge-theory line-lattice duality walls and proved \(S,T\)
  preservation of the Dirac pairing.
- Added the finite \(\mathbb Z_N^{\rm e}\oplus\mathbb Z_N^{\rm m}\) line
  example connecting \(T^p(0,1)=(p,1)\) to oblique confinement.

## Calculation Checks

Added `calculation-checks/duality_defect_gauging_checks.py`, which checks:

- regular algebra multiplicities \(A_H\otimes A_H=|H|A_H\);
- normality of \(A_3\triangleleft S_3\);
- quotient multiplication \(S_3/A_3\simeq\mathbb Z_2\);
- \(S_3\) conjugacy-class and centralizer sizes for orbifold sectors;
- pair-of-pants monodromy \(g_1g_2g_3^{-1}=e\);
- preservation of the integral and finite Dirac pairing by \(S\), \(T\), and
  \(T^p\);
- \(T^p(0,1)=(p,1)\) for finite oblique-condensate directions.

The calculation-check README and Volume IX chapter dossier were updated.

## Verification

Completed before commit:

- `python3 calculation-checks/duality_defect_gauging_checks.py`
- `python3 -m py_compile calculation-checks/duality_defect_gauging_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The build completed with a clean log scan and produced
`monograph/tex/main.pdf` with 1782 pages.
