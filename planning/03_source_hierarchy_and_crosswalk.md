# Source Hierarchy And Crosswalk

## Source Priority

No source is trusted blindly. Each source has a role.

### Primary Spine Sources

1. Xi Yin's handwritten QFT PDFs in `references/`.
2. The faithful transcription in `transcription/`.
3. Xi Yin's related string notes and appendices in
   `/Users/xiyin/ResearchIdeas/stringbook/`, used as inspiration,
   convention checks, and source leads rather than as an exposition to adapt.
4. Related formalization projects in `/Users/xiyin/StringGeometry/` and
   `/Users/xiyin/StringAlgebra/` where relevant.
5. The statmech project in `/Users/xiyin/statmech/` for workflow precedent and
   statistical-field-theory overlap.

These sources fix the project stance and logical order.

### Comparison Sources

The Ben Lou transcriptions in `references/` are comparison documents. They may
help identify omissions, alternate readings, figures, or notation choices, but
they are not authoritative. Any substantive use must be checked against the
handwritten PDFs or a reliable independent source.

### External References

External sources are mandatory for theorem-level claims whose proofs are not
given in the monograph. They supply hypotheses, theorem statements, proof
boundaries, examples, historical references, and frontier context.

External sources do not determine the monograph's logical order. Standard
textbooks are not models for organization. Rigorous references may force a
draft claim to be weakened, qualified, or moved to an open problem.

## Local Source Map

| Source | Local path | Role |
| --- | --- | --- |
| QFT handwritten notes, first sequence | `references/253a lectures 2022.pdf` | Primary spine for locality, fields, path integrals, spectral representation, scattering, spin, gauge fields, and QED. |
| QFT handwritten notes, second sequence | `references/253b lecture notes 2023.pdf` | Primary spine for scattering, analyticity, renormalization, RG, Yang--Mills, QCD, anomalies, EFT, and infrared structure. |
| QFT handwritten notes, third sequence | `references/253c 2023.pdf` | Primary spine for conformal field theory, bootstrap, two-dimensional CFT, supersymmetry, and large-\(N\) structures. |
| Current QFT transcription | `transcription/qft_notes.tex`, `transcription/tex/` | Source layer and audit aid, not the final monograph. |
| Ben Lou notes | `references/253a_notes.tex`, `references/253b transcribed lecture notes.tex`, `references/253c_notes.tex` | Non-authoritative comparison layer. |
| Sound reference shelf | `references/sound_references/` | Downloaded external sources for rigorous frameworks and theorem boundaries. |
| Statmech project | `/Users/xiyin/statmech/` | Workflow precedent and overlap with RG/statistical field theory. |
| String book | `/Users/xiyin/ResearchIdeas/stringbook/` | Inspiration, convention checks, and source leads for related QFT material; especially useful for later CFT and supersymmetric volumes, but never a substitute for an independent QFT monograph development. |
| StringGeometry | `/Users/xiyin/StringGeometry/` | Later-volume mathematical structures. |
| StringAlgebra | `/Users/xiyin/StringAlgebra/` | Algebraic and categorical structures for advanced volumes. |

## External Reference Roles

The current external shelf includes references for:

- algebraic and perturbative algebraic QFT;
- Euclidean reconstruction;
- Haag--Ruelle/scattering context;
- Poincare representation theory;
- exact renormalization group;
- conformal bootstrap.

Each chapter dossier must state precisely which external reference is being
used and for which claim. A reference is not a license to import its exposition
or ordering.

## Source Tags

Use these tags in dossiers and audits:

- `SRC-QFT-PDF`
- `SRC-QFT-TRANSCRIPTION`
- `SRC-BEN-COMPARISON`
- `SRC-STRINGBOOK`
- `SRC-STATMECH`
- `SRC-STRINGGEOM`
- `SRC-STRINGALG`
- `SRC-EXTERNAL`
- `SRC-DERIVED-IN-CHAPTER`
- `SRC-OPEN`

These tags are planning metadata. They should not appear obtrusively in the
finished prose.

## Import Rules

For imported material, record:

- source path or bibliographic reference;
- exact page, section, theorem, or equation when available;
- claim imported;
- framework of validity;
- whether the proof is reproduced, sketched, or cited;
- whether notation has been adapted;
- whether figures or diagrams were checked.

## Stringbook Boundary

For CFT and supersymmetric field theory, the stringbook appendices can identify
useful conventions, calculations, and reference trails.  They do not determine
the QFT monograph's organization, definitions, theorem status, or level of
detail.  A CFT or supersymmetry chapter may use the stringbook only after the
chapter dossier states:

- which appendix or calculation was consulted;
- whether the material is a convention check, an example, a source lead, or a
  calculation to rederive;
- which QFT-side definitions and hypotheses are being introduced independently;
- which external mathematical or physics references support theorem-level
  claims;
- what is deliberately not being imported from the string-theory context.
