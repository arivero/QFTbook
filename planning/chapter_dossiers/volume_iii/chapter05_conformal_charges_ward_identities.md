# Volume III, Chapter 5 Dossier: Conformal Charges And Ward Identities

## Logical Role

- Role in the monograph: convert stress-tensor Ward identities into surface
  charges, local current Ward identities, and global conformal constraints on
  correlators.
- Immediate predecessor: stress-tensor Weyl structure and radial
  quantization.
- Immediate successor: primary operators and finite conformal
  transformations.

## Definitions And Results

The chapter establishes:

- Euclidean surface charges \(Q_\epsilon(\Sigma)\) for conformal Killing
  fields \(\epsilon^\mu\);
- the Lorentzian commutator interpretation obtained from charge fluxes across
  neighboring Cauchy surfaces;
- small-sphere actions on local insertions and their orientation convention;
- source-derived local translation, trace, and conformal-current Ward
  identities, including contact terms on collision diagonals;
- the passage from local current Ward identities to global Ward identities;
- the cylinder interpretation of conformal charges and the adjointness
  \(P_\mu^\dagger=K_\mu\) under reflection positivity;
- in \(D=2\), separated-point holomorphy of \(T(z)\), contour charges for
  holomorphic vector fields, Virasoro primary OPEs, the derivation of the
  Virasoro algebra from the \(TT\) OPE, the Schwarzian finite transformation
  law, and the \(c/24\) plane-cylinder vacuum shift.

## Claims To Verify

1. A conformal charge is a stress-tensor flux through an oriented
   codimension-one surface.
2. Surface deformation is valid in regions where the current has no
   distributional support.
3. The local current Ward identity is obtained by combining the
   source-derived translation and trace Ward identities in the chosen source
   chart.
4. Contact terms in conformal Ward identities are part of the source
   convention and agree with the opening fixed-point chapter.
5. The global Ward identity is the integral of the local current identity when
   the outer boundary and anomaly contributions vanish in the chosen
   background.
6. In \(D=2\), the Virasoro commutator follows from a contour-domain
   calculation, not from formal mode manipulation.  The central coefficient is
   the fourth-order-pole residue of the \(TT\) OPE, and the noncentral
   coefficient uses integration by parts on the closed contour.
7. The literal two-dimensional state--operator statement remains the radial
   finite-energy statement from Chapter 4: local scaling fields span a dense
   algebraic subspace after null quotient, and the Hilbert space is the
   BPZ/radial completion of that subspace.

## Figures

- The existing surface-deformation figures are conceptually useful and should
  remain tied to the local source Ward identities.
- Any future figure must clarify an orientation, boundary, or cylinder map
  convention.

## Checks

- Avoid deriving conformal transformation laws from informal generator
  shortcuts; derive them from local current Ward identities, charge fluxes,
  and the primary module data.
- Keep source-contact conventions aligned with
  `chapter01_fixed_points_conformal_data.md`.
- 2026-05-22 source-current pass: replaced the local Ward section with
  source-derived local translation, trace, and conformal-current Ward
  identities and removed an unnecessary negative framing in the Lorentzian
  commutator paragraph.
- 2026-05-25 stringbook absorption pass: added the two-dimensional
  chiral-stress-tensor mode construction, Virasoro algebra proof,
  Schwarzian/cylinder shift, and the state--operator density caveat; added
  `calculation-checks/virasoro_mode_checks.py` for the finite residue
  arithmetic.
- 2026-05-29 anti-wrapper pass: demoted the conserved-charge surface
  deformation from proposition form to derivation prose.  The argument is the
  Stokes/distributional-conservation step used before the later Ward identity,
  while theorem-family status is reserved for the local current Ward identity
  and Virasoro calculation.
