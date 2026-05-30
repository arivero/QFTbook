# Issues #700 and #701: Yang-Baxter Datum And Depth Pass

## Target

Volume VI, Chapter 3 was identified twice:

- In #700 as a partial defining-property gap: the chapter had a narrow
  regular two-body \(R\)-system definition, but not an upfront datum for the
  full internal two-body scattering structure used downstream.
- In #701 as an underdeveloped central chapter: Yang-Baxter consistency is a
  foundational input for the rest of Volume VI and for the planar-integrability
  chapters, but the chapter previously gave only the shortest three-particle
  derivation and an \(O(N)\) projector example.

## Edit

- Replaced the narrow opening definition with an internal two-body
  \(R\)-matrix datum
  \[
    \mathfrak R=(\mathcal I,\{m_a,V_a\},\{S_{ab}\},\iota,\{C_a\},
    \mathcal A,\{\rho_a\}),
  \]
  including species, masses, internal spaces, meromorphic two-body maps,
  antiparticle/crossing data, and optional internal symmetry representation.
- Made the regular factorized-scattering condition explicit: physical
  two-body unitarity, real analyticity, crossing, residues, growth bounds, and
  the additive spectral-parameter Yang-Baxter identity.
- Added the \(n\)-particle reduced-word consistency explanation from Coxeter
  moves.
- Added additive/multiplicative spectral-parameter conventions, the
  braid-convention dictionary, and the formal classical-limit derivation of
  the spectral classical Yang-Baxter equation.
- Added the universal-\(R\) algebraic mechanism and the boundary
  Yang-Baxter/reflection equation, with explicit status language separating
  algebraic matrix identities from QFT construction.
- Updated the chapter dossier.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- Output: `monograph/tex/main.pdf`
- Page count: 2681

The first full build caught that this TeX preamble does not define
`\mathscr`; the universal element was renamed from `\mathscr R` to
`\mathcal R`, and the second full build completed with a clean log scan.
