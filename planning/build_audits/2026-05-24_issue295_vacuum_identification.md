# Issue #295 Vacuum Identification Pass

## Scope

- Addressed GitHub issue #295:
  `[Vol V Chs 4, 8] Vacuum (Poincare vs conformal vs cylinder) not separated`.
- Target chapters:
  `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
  and
  `monograph/tex/volumes/volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`.

## Content Added

- Added Section `sec:flat-conformal-cylinder-vacua`.
- Defined separately:
  - \(\ket{\Omega_{\rm P}}\), the normalized flat Poincare-invariant Wightman
    vacuum;
  - \(\ket{\Omega_{\rm conf}}\), a normalized vector invariant under the
    connected conformal group;
  - \(\ket{\Omega_0}_{\rm cyl}\), the normalized zero-eigenvalue state of
    \(D_{\rm rad}\) on \(S^{D-1}\).
- Added Proposition `prop:poincare-vacuum-is-conformal-vacuum`, proving under
  conformal implementation, common-domain, Lie-algebra, and uniqueness
  hypotheses that the flat Poincare vacuum is conformally invariant.
- Included the argument that dilatation invariance follows from uniqueness of
  the translation-invariant vacuum plus the conformal commutator expectation,
  and that \(K_\mu|\Omega_{\rm P}\rangle=0\) follows because
  \(K_\mu|\Omega_{\rm P}\rangle\) is translation-invariant and transforms as a
  Lorentz vector.
- Identified the cylinder ground state through the Weyl/radial construction:
  the identity insertion in the empty Euclidean ball creates the zero-energy
  cylinder state.
- Added a Kontsevich--Segal style interpretation of literal radial
  quantization as cutting and gluing Euclidean bordisms, while keeping the
  chapter's radial reconstruction hypotheses explicit.
- Corrected the status of the state space in that interpretation: the generic
  cutting/gluing assignment is to a locally convex topological vector space
  (often a Fr\'echet or nuclear space), not automatically to a Hilbert space.
  The Hilbert space used in CFT radial quantization is obtained only after the
  conformal inversion pairing supplies a positive semidefinite Hermitian form,
  followed by null quotient and completion.
- Updated Chapter 8 so its Ward identities and BPZ limits use the common
  vacuum only after referring back to the Chapter 4 identification.
- Updated both chapter dossiers.

## Verification Targets

- The manuscript must not silently conflate flat, conformal, and cylinder
  vacua.
- The proof that the Poincare vacuum is conformally invariant must state its
  hypotheses and use the conformal algebra explicitly.
- The cylinder vacuum identification must mention the Weyl-map normalization
  and the possible local curvature/vacuum normalization convention.
- Literal radial quantization should be framed as a Kontsevich--Segal type
  cutting/gluing structure without treating that framework as a complete
  foundational axiom for all QFTs.
- The manuscript must not imply that a generic radial cutting/gluing
  construction directly produces a Hilbert space; this is a CFT-specific
  consequence of inversion/reflection positivity in the present chapter.
