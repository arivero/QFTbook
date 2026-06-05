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
  Kinoshita--Lee--Nauenberg, Weinberg's leading soft photon and graviton
  theorem, Low, Gell-Mann--Goldberger,
  Burnett--Kroll, Kulish--Faddeev, Buchholz's Gauss-law theorem,
  Fröhlich--Morchio--Strocchi infraparticle analysis, large-\(U(1)\)
  asymptotic-symmetry and electromagnetic-memory analyses, and the
  Buchholz--Dybalski scattering review provide theorem and reference context
  for inclusive probabilities, soft exponentiation, subleading soft
  operators, mass singularity cancellation, infraparticle sectors, and dressed
  asymptotic states.

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
- the Low subleading soft-photon operator \(S^{(1)}\), its hypotheses, and
  the fact that leading-log Bloch--Nordsieck exponentiation uses only the
  leading eikonal factor \(S^{(0)}\);
- the Weinberg leading soft photon theorem as a theorem in the same hard-kernel
  convention, with the Ward-identity check
  \(e_\mu\mapsto e_\mu+ck_\mu\) and hard charge conservation
  \(\sum_n\eta_n g_n=0\);
- the leading soft graviton analogue, with
  \(g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}\),
  \(\mathcal L_{\rm int}=-(\kappa/2)h_{\mu\nu}T^{\mu\nu}\), and the
  linearized-diffeomorphism check that gives momentum conservation and
  universal spin-two coupling;
- the distinction between soft and collinear degeneracies;
- the Abelian-Higgs regulator as a gauge-invariant infrared deformation.
- the ordered Bloch--Nordsieck limiting statement: at fixed regulator, form
  the inclusive degeneracy sum, or at fixed perturbative order combine all
  degenerate real-emission terms and virtual terms contributing to that
  coefficient, and only then remove the infrared regulator;
- the Abelian scope of the Bloch--Nordsieck exponentiation and the
  cross-reference to QCD factorization, where nonabelian initial-state
  collinear singularities are absorbed into renormalized PDFs;
- a labeled finite-degeneracy KLN theorem with explicit hypotheses:
  finite-dimensional unperturbed degenerate subspaces, bounded self-adjoint
  perturbation, existence of the long-time inclusive transition probability
  after regulators, and unitary regulator-singular mixing inside the
  degenerate subspaces;
- the observable-algebra statement that limiting electric flux at spacelike
  infinity is a superselection datum in charged sectors;
- Buchholz's theorem that nonzero abelian gauge charge is incompatible with a
  sharp Wigner mass shell and ordinary charged Fock asymptotic space;
- the fact that the Faddeev--Kulish soft profile is not square-integrable in
  the photon one-particle Hilbert norm after the infrared cutoff is removed,
  hence implements a representation change rather than a vector in the
  original photon Fock space;
- a labeled open problem specifying the charged asymptotic-completeness theorem
  still missing for massless QED: asymptotic spaces with hard charged data,
  transverse photons, angular electric-flux labels, dressed or Wilson-line
  charged creators, wave operators into the charged physical Hilbert space,
  and agreement with inclusive detector probabilities.

Additional symbols introduced in the charged-sector discussion:

| Symbol | Meaning |
| --- | --- |
| \(\mathfrak A_{\mathrm{loc}}\) | gauge-invariant local observable algebra |
| \(E^i=F^{i0}\) | electric field |
| \(\Phi_R(f),\Phi_\infty(f)\) | large-radius smeared electric flux and its limiting asymptotic flux functional |
| \(\mathcal E_{g,\mathbf v}(\mathbf n)\) | boosted Coulomb radial flux density for charge \(g\) with velocity \(\mathbf v\) |
| \(\mathcal H_{1,\gamma}\) | physical one-photon Hilbert space |
| \(S_\gamma^{(0)}(k,h)\) | Weinberg leading soft photon factor |
| \(S_{\rm grav}^{(0)}(k,\lambda)\) | leading soft graviton factor |
| \(\kappa\) | spin-two coupling in \(g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}\) |
| \(\varepsilon_{\mu\nu}^{(\lambda)}(k)\) | physical graviton polarization tensor |

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
3a. Equivalently, the Weinberg leading soft photon theorem is
    \[
      \mathcal M_{\beta;k,h|\alpha}
      =
      \left[\sum_n\eta_n g_n
      {p_n\cdot e_h^*(k)\over p_n\cdot k}\right]
      \mathcal M_{\beta|\alpha}+O(\omega^0).
    \]
    Replacing \(e_h^\mu\) by \(e_h^\mu+ck^\mu\) shifts the bracket by
    \(c^*\sum_n\eta_n g_n\), so physical gauge invariance is hard charge
    conservation.
3b. With \(g_{\mu\nu}=\eta_{\mu\nu}+\kappa h_{\mu\nu}\) and universal
    coupling \(-(\kappa/2)h_{\mu\nu}T^{\mu\nu}\), the leading soft graviton
    theorem is
    \[
      \mathcal M_{\beta;k,\lambda|\alpha}^{\rm grav}
      =
      {\kappa\over2}
      \left[
      \sum_n\eta_n
      {p_n^\mu p_n^\nu\varepsilon_{\mu\nu}^{(\lambda)*}(k)
      \over p_n\cdot k}
      \right]\mathcal M_{\beta|\alpha}+O(\omega^0).
    \]
    The linearized-diffeomorphism shift of
    \(\varepsilon_{\mu\nu}\) gives \(\kappa\xi_\nu^*\sum_n\eta_np_n^\nu\),
    which vanishes by hard momentum conservation; species-dependent spin-two
    couplings would violate this identity for generic hard processes.
    This universal leading soft coupling is explicitly separated from the
    Weinberg--Witten stress-tensor hypothesis: the soft theorem does not
    construct a gauge-invariant local Lorentz-covariant stress tensor for the
    graviton.
4. Multiple real soft photons factorize into the product of the one-photon
   factors at leading order.
   The two-soft-photon identity on one external line should be displayed,
   since it explains how nested eikonal denominators become independent
   one-photon factors.
5. The subleading Low soft-photon operator is
   \[
     S_h^{(1)}(k)
     =
     -i\sum_n
     {g_ne^*_{h,\mu}(k)k_\nu J_n^{\mu\nu}\over
     \eta_n p_n\cdot k},
   \]
   with \(J_n^{\mu\nu}\) the total Lorentz generator on the \(n\)-th hard
   datum.  It is homogeneous of degree \(\omega^0\), so it gives finite
   real-emission endpoint behavior in the massive case and does not enter the
   leading logarithmic Bloch--Nordsieck exponent.
6. In QED the asymptotic-symmetry interpretation of the leading soft photon
   theorem is a large-\(U(1)\) Ward identity at null infinity with
   electromagnetic memory as the classical counterpart; BMS belongs to the
   gravitational soft theorem analogue.
7. After summing physical polarizations, charge conservation removes the
   gauge-vector terms in the polarization sum.
8. Real unresolved photons produce \((E_T/\mu)^{A_{\beta\alpha}}\) at leading
   soft logarithmic order.
   The angular integral defining \(A_{\beta\alpha}\) should be derived with a
   Feynman parameter and the polar-axis integral, not merely quoted.
9. Virtual soft photon exchange between distinct external lines exponentiates.
10. Same-line virtual soft singularities are accounted for by the infrared part
   of the LSZ factors \(Z_n^{1/2}\).
   The electromagnetic form-factor insertion should be used to identify this
   cancellation, including the scalar and spinor current decompositions and
   the finite \(G(0)=-g^2/(8\pi^2)+O(g^4)\), the relation between
   \(Z_{\rm IR}\), \(J_{12}\), and the formal \(J_{11}\), and the scalar
   self-energy derivative that produces the same logarithm in \(Z\).
11. The virtual rate factor is \((\mu/M)^{A_{\beta\alpha}}\), up to a phase at
   the amplitude level.
   The \(k^0\)-plane pole locations should be stated: photon poles determine
   the real logarithm, while matter poles contribute only to the phase.
12. The inclusive product is finite as \(\mu\to0\):
   \[
     (\mu/M)^{A_{\beta\alpha}}(E_T/\mu)^{A_{\beta\alpha}}
     =(E_T/M)^{A_{\beta\alpha}}.
   \]
13. The Bloch--Nordsieck cancellation is coefficientwise in perturbation
    theory only after the inclusive sum has been formed.  At order
    \(A_{\beta\alpha}^L\), the sum
    \[
      \sum_{N=0}^L
      \frac{[-\log(M/\mu)]^{L-N}}{(L-N)!}
      \frac{[\log(E_T/\mu)]^N}{N!}
      =
      \frac{[\log(E_T/M)]^L}{L!}
    \]
    is regulator independent, whereas an individual fixed-\(N\) term is not.
14. The Bloch--Nordsieck exponentiation in this chapter is an Abelian
    soft-photon statement with commuting scalar soft factors.  In QCD,
    soft-gluon factors act in color space and initial-state collinear
    singularities of colored partons are absorbed into renormalized light-ray
    PDF operators; the manuscript must cross-reference the QCD factorization
    formula and DGLAP equation.
15. For massless charged particles, collinear degeneracies require the KLN
   sum and average over detector-degenerate sectors.  The abstract
   finite-degeneracy theorem assumes finite-dimensional degenerate subspaces
   \(P_A\mathcal H_0\), \(P_B\mathcal H_0\), a bounded perturbation, an
   existing long-time inclusive limit, and unitary regulator-singular mixing
   inside the degenerate subspaces; under these hypotheses the trace
   \[
     d_A^{-1}\operatorname{Tr}_{P_B\mathcal H_0}
     (S_{\rm fin}S_{\rm fin}^\dagger)
   \]
   is regulator independent.
16. Dressed charged asymptotic states use the same eikonal data as coherent
   soft photon clouds, but the zero-cutoff Faddeev--Kulish profile is not an
   element of the photon one-particle Hilbert space, so the limiting dressing
   changes representation.  For velocities \(\mathbf v\neq\mathbf w\), the
   chapter displays the logarithmic norm
   \[
     \|f_{\mathbf v}-f_{\mathbf w}\|^2
     =
     {g^2\over 2(2\pi)^3}\log{\Lambda\over\mu}
     \int_{S^2}|V_{\mathbf v}(\mathbf n)-V_{\mathbf w}(\mathbf n)|^2
     \dd\Omega+O(1),
   \]
   with \(V_{\mathbf v}\) explicitly defined.
17. A small photon mass introduced through an Abelian-Higgs deformation is a
   consistent gauge-invariant infrared regulator.
18. Buchholz's Gauss-law theorem gives the nonperturbative structural
    boundary: charged QED sectors are infraparticle sectors, not ordinary
    Wigner-particle Fock sectors; asymptotic electric flux labels
    superselection data.  The theorem boundary is supported by an explicit
    shell-smeared flux-commutant argument, the distinction between total
    charge and higher angular flux modes, and the boosted-Coulomb-flux
    mechanism, including the normalization integral and the velocity-extraction
    ratio \((1+\beta)^2/(1-\beta)^2\).
19. The open charged-QED asymptotic-completeness problem asks for a single
    nonperturbative large-time theorem whose asymptotic data include hard
    charged labels, transverse radiation, Gauss-law flux at infinity, and the
    detector probabilities computed by inclusive or dressed perturbation
    theory.

## Recent Audit Notes

- 2026-06-02 flux-superselection proof pass: expanded the charged-sector
  discussion so the limiting electric-flux observable is reached through
  shell-smeared local fields \(\Phi_{R,\chi}(f)\).  The text now proves the
  local-commutant mechanism before taking the \(R\to\infty\) limit, states
  the sharp-limit hypothesis needed for spectral projections of
  \(\Phi_\infty(f)\), and records that zero total charge does not imply
  trivial angular flux.  This narrows the charged Haag--Ruelle/IR proof debt
  without claiming a completed nonperturbative charged scattering theorem.

## Figure Requirements

- External-line soft photon factorization, including the multiplication of
  factors for two photons emitted from the same line.
- Leading soft theorem schematic showing gauge replacement \(e\to e+ck\) and
  the corresponding charge-conservation Ward identity; the spin-two analogue
  may be a compact formula box rather than a separate diagram.
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
- 2026-05-24 issue #257 pass: pinned down the order of limits in the
  Bloch--Nordsieck construction and added a coefficientwise cancellation
  proposition showing exactly how the fixed-order sum over unresolved photon
  numbers cancels the regulator logarithms.
- 2026-05-24 issue #258 pass: added a labeled finite-degeneracy KLN theorem
  with hypotheses and proof, and separated that abstract theorem from the
  additional regulator and detector-cell construction needed in relativistic
  field theory.
- 2026-05-24 issue #259 pass: added a subleading soft photon remark with
  Low's \(S^{(1)}\) operator, explained why it lies outside the leading-log
  exponentiation, and stated the QED large-\(U(1)\)/memory interpretation
  separately from the gravitational BMS analogue.
- 2026-05-24 issue #260 pass: added an Abelian-scope remark for
  Bloch--Nordsieck exponentiation and cross-referenced the QCD factorization
  replacement through renormalized PDFs and DGLAP evolution.
- 2026-05-24 issue #332 pass: added a labeled open problem for charged
  asymptotic completeness in massless QED, including the required
  flux-labelled asymptotic space, dressed charged creators, wave operators,
  and matching to inclusive detector probabilities.
- 2026-05-25 issue #454 pass: promoted the leading eikonal formula to the
  Weinberg leading soft photon theorem, with a Ward-identity derivation and a
  schematic showing \(e\mapsto e+ck\) gives \(\sum_n\eta_ng_n=0\).  The same
  section now records the spin-two leading soft theorem with
  \(S_{\rm grav}^{(0)}=(\kappa/2)\sum_n\eta_n
  p_n^\mu p_n^\nu\varepsilon_{\mu\nu}^*/(p_n\cdot k)\), derives the
  linearized-diffeomorphism check, and states the universal-coupling
  consequence.
- 2026-06-05 issue #772 pass: cross-referenced the Weinberg--Witten
  theorem-boundary from the soft-graviton theorem, clarifying that infrared
  universality and a local graviton stress tensor are distinct questions.
- 2026-05-30 quoted-theorem debt pass: expanded the mechanism under
  Buchholz's infraparticle quoted theorem, deriving the boosted Coulomb flux
  normalization, the velocity-extraction ratio, and the logarithmic
  one-photon norm of differences of charged soft profiles.  The finite checks
  are in `calculation-checks/charged_flux_dressing_checks.py`.
