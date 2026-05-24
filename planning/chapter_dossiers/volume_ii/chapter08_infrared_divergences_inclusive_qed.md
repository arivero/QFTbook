# Volume II, Chapter 8 Dossier: Infrared Divergences And Inclusive QED

## Source Position

- Primary local source: second-sequence handwritten material, pages 56--70.
- Immediate predecessor: partial waves, dispersion relations, and high-energy
  bounds under a massive-theory hypothesis.
- Immediate successor in the source order: generating functionals and the 1PI
  effective action.
- Role in the monograph: explain how a massless Abelian gauge boson changes
  the construction of scattering probabilities, while keeping the
  nonperturbative definition of the massive S-matrix and LSZ logically
  upstream.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 56--70;
  figures checked against rendered page images.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  lines around the infrared section, used only as a comparison layer.
- `SRC-EXTERNAL`: Bloch--Nordsieck, Yennie--Frautschi--Suura,
  Kinoshita--Lee--Nauenberg, Kulish--Faddeev, Buchholz's Gauss-law theorem,
  Fröhlich--Morchio--Strocchi infraparticle analysis, and the
  Buchholz--Dybalski scattering review provide theorem and reference context
  for inclusive probabilities, soft exponentiation, mass singularity
  cancellation, infraparticle sectors, and dressed asymptotic states.

## Construction Task

The chapter must formulate the infrared problem positively:
resolution-inclusive transition probabilities are the constructed observables
for charged scattering in four-dimensional QED. Fixed-photon-number amplitudes
are treated as exclusive kernels whose regulator dependence is derived, not as
the main conceptual object.
The hard charged labels appearing in the soft-factor formulas are not to be
identified with exact regulator-independent LSZ external electron states of
massless QED; they are infrared-regulated hard data to be completed by the
inclusive or dressed construction.

The chapter should state:

- the spacetime dimension and metric convention;
- the hard external states and their charges;
- the incoming/outgoing sign \(\eta_n\);
- the soft energy \(\omega=k^0=|\vec k|\);
- the detector threshold \(E_T\);
- the auxiliary infrared regulator \(\mu\);
- the soft upper scale \(M\);
- the exponent \(A_{\beta\alpha}\) and the relative velocity \(\beta_{nm}\);
- the role of LSZ wavefunction factors in the same-line virtual loops;
- the distinction between soft and collinear degeneracies;
- the Abelian-Higgs regulator as a gauge-invariant infrared deformation.
- the observable-algebra statement that limiting electric flux at spacelike
  infinity is a superselection datum in charged sectors;
- Buchholz's theorem that nonzero abelian gauge charge is incompatible with a
  sharp Wigner mass shell and ordinary charged Fock asymptotic space;
- the fact that the Faddeev--Kulish soft profile is not square-integrable in
  the photon one-particle Hilbert norm after the infrared cutoff is removed,
  hence implements a representation change rather than a vector in the
  original photon Fock space.

Additional symbols introduced in the charged-sector discussion:

| Symbol | Meaning |
| --- | --- |
| \(\mathfrak A_{\mathrm{loc}}\) | gauge-invariant local observable algebra |
| \(E^i=F^{i0}\) | electric field |
| \(\Phi_R(f),\Phi_\infty(f)\) | large-radius smeared electric flux and its limiting asymptotic flux functional |
| \(\mathcal E_{g,\mathbf v}(\mathbf n)\) | boosted Coulomb radial flux density for charge \(g\) with velocity \(\mathbf v\) |
| \(\mathcal H_{1,\gamma}\) | physical one-photon Hilbert space |

## Claim Ledger

1. External-line emission of a soft photon in scalar QED gives the eikonal
   factor \(g p\cdot e^*/(p\cdot k-\ii\epsilon)\).
2. The leading soft factor is spin-independent: spin changes subleading terms.
   The spinor-QED check should display the nearly on-shell Dirac numerator and
   its reduction to the same eikonal factor.
3. For hard state labels \(\alpha,\beta\), the leading one-photon factor is
   \[
     \sum_n {g_n p_n\cdot e_h^*(k)\over \eta_np_n\cdot k-\ii\epsilon}.
   \]
4. Multiple real soft photons factorize into the product of the one-photon
   factors at leading order.
   The two-soft-photon identity on one external line should be displayed,
   since it explains how nested eikonal denominators become independent
   one-photon factors.
5. After summing physical polarizations, charge conservation removes the
   gauge-vector terms in the polarization sum.
6. Real unresolved photons produce \((E_T/\mu)^{A_{\beta\alpha}}\) at leading
   soft logarithmic order.
   The angular integral defining \(A_{\beta\alpha}\) should be derived with a
   Feynman parameter and the polar-axis integral, not merely quoted.
7. Virtual soft photon exchange between distinct external lines exponentiates.
8. Same-line virtual soft singularities are accounted for by the infrared part
   of the LSZ factors \(Z_n^{1/2}\).
   The electromagnetic form-factor insertion should be used to identify this
   cancellation, including the scalar and spinor current decompositions and
   the finite \(G(0)=-g^2/(8\pi^2)+O(g^4)\), the relation between
   \(Z_{\rm IR}\), \(J_{12}\), and the formal \(J_{11}\), and the scalar
   self-energy derivative that produces the same logarithm in \(Z\).
9. The virtual rate factor is \((\mu/M)^{A_{\beta\alpha}}\), up to a phase at
   the amplitude level.
   The \(k^0\)-plane pole locations should be stated: photon poles determine
   the real logarithm, while matter poles contribute only to the phase.
10. The inclusive product is finite as \(\mu\to0\):
   \[
     (\mu/M)^{A_{\beta\alpha}}(E_T/\mu)^{A_{\beta\alpha}}
     =(E_T/M)^{A_{\beta\alpha}}.
   \]
11. For massless charged particles, collinear degeneracies require the KLN
   sum and average over detector-degenerate sectors.
12. Dressed charged asymptotic states use the same eikonal data as coherent
   soft photon clouds, but the zero-cutoff Faddeev--Kulish profile is not an
   element of the photon one-particle Hilbert space, so the limiting dressing
   changes representation.
13. A small photon mass introduced through an Abelian-Higgs deformation is a
   consistent gauge-invariant infrared regulator.
14. Buchholz's Gauss-law theorem gives the nonperturbative structural
    boundary: charged QED sectors are infraparticle sectors, not ordinary
    Wigner-particle Fock sectors; asymptotic electric flux labels
    superselection data.

## Figure Requirements

- External-line soft photon factorization, including the multiplication of
  factors for two photons emitted from the same line.
- Same-line virtual soft loops and their absorption into the infrared part of
  external LSZ factors.
- Real-versus-virtual soft factor cancellation at the level of rates.
- Abelian-Higgs regulator figure showing the vacuum of the regulator scalar
  and the induced photon mass.

## Audit Notes

- No reader-facing references to source pages, course numbers, or the
  transcription workflow.
- Avoid presenting the chapter as a critique of Fock space. Derive the
  regulator behavior and then state the inclusive/dressed constructions.
- Define every symbol before use, especially \(A_{\beta\alpha}\),
  \(\eta_n\), \(E_T\), \(M\), \(\mu\), and \(\beta_{nm}\).
- 2026-05-22 source pass: handwritten pp. 56--70 checked against the chapter;
  missing two-soft-photon identity, spinor soft-factor derivation,
  angular-integral derivation, electromagnetic form-factor/LSZ same-line
  cancellation, \(G(0)\), self-energy derivative check, \(k^0\)-pole analysis,
  and same-line cancellation figure were added.
- 2026-05-24 issue #256 pass: added the charged asymptotic sectors section,
  including limiting electric flux superselection, Buchholz's infraparticle
  obstruction, the boosted Coulomb angular flux density, and the
  square-integrability calculation showing that the Faddeev--Kulish soft cloud
  is not a vector in photon Fock space after the infrared cutoff is removed.
