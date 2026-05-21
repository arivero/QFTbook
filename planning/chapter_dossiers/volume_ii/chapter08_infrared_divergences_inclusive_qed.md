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
  Kinoshita--Lee--Nauenberg, and Kulish--Faddeev provide theorem and
  reference context for inclusive probabilities, soft exponentiation, mass
  singularity cancellation, and dressed asymptotic states.

## Construction Task

The chapter must formulate the infrared problem positively:
resolution-inclusive transition probabilities are the constructed observables
for charged scattering in four-dimensional QED. Fixed-photon-number amplitudes
are treated as exclusive kernels whose regulator dependence is derived, not as
the main conceptual object.

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

## Claim Ledger

1. External-line emission of a soft photon in scalar QED gives the eikonal
   factor \(g p\cdot e^*/(p\cdot k-\ii\epsilon)\).
2. The leading soft factor is spin-independent: spin changes subleading terms.
3. For hard state labels \(\alpha,\beta\), the leading one-photon factor is
   \[
     \sum_n {g_n p_n\cdot e_h^*(k)\over \eta_np_n\cdot k-\ii\epsilon}.
   \]
4. Multiple real soft photons factorize into the product of the one-photon
   factors at leading order.
5. After summing physical polarizations, charge conservation removes the
   gauge-vector terms in the polarization sum.
6. Real unresolved photons produce \((E_T/\mu)^{A_{\beta\alpha}}\) at leading
   soft logarithmic order.
7. Virtual soft photon exchange between distinct external lines exponentiates.
8. Same-line virtual soft singularities are accounted for by the infrared part
   of the LSZ factors \(Z_n^{1/2}\).
9. The virtual rate factor is \((\mu/M)^{A_{\beta\alpha}}\), up to a phase at
   the amplitude level.
10. The inclusive product is finite as \(\mu\to0\):
   \[
     (\mu/M)^{A_{\beta\alpha}}(E_T/\mu)^{A_{\beta\alpha}}
     =(E_T/M)^{A_{\beta\alpha}}.
   \]
11. For massless charged particles, collinear degeneracies require the KLN
   sum and average over detector-degenerate sectors.
12. Dressed charged asymptotic states use the same eikonal data as coherent
   soft photon clouds.
13. A small photon mass introduced through an Abelian-Higgs deformation is a
   consistent gauge-invariant infrared regulator.

## Figure Requirements

- External-line soft photon factorization, including the multiplication of
  factors for two photons emitted from the same line.
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
