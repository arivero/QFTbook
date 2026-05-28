# Volume VI, Chapter 1 Dossier: Factorized Scattering And Integrability

## Logical Role

- Role in the monograph: open the integrable-QFT volume after the general
  scattering and analyticity volumes have defined the S-matrix.
- Immediate predecessor: Volume II scattering and analytic structure.
- Immediate successor: detailed two-dimensional integrable models, form
  factors, and thermodynamic Bethe ansatz.

## Definitions And Results

- Massive two-dimensional one-particle rapidity variables.
- Ordered rapidity chambers and the mostly-plus invariant
  \(s_{ab}=-(p_a+p_b)^2\).
- Elastic factorized scattering datum on \(V\otimes V\).
- Unitarity, Hermitian analyticity, crossing, and Yang--Baxter compatibility.
- Separating higher-spin charge family, formulated as injectivity of a
  species-resolved moment map outside threshold and bound-state singular
  loci, with a concrete Newton-identity sufficient condition.
- Higher-spin conserved-charge argument excluding generic particle production
  as a distribution-kernel support statement under stated asymptotic-state
  and regularity hypotheses.
- Chamber groupoid representation by adjacent two-body scattering maps,
  with unitarity and Yang--Baxter proven equivalent to path-independent
  chamber continuation.
- Zamolodchikov--Faddeev algebra as the operator algebraic encoding of
  factorized scattering, with associativity proven equivalent to
  Yang--Baxter.
- \(S\)-symmetric finite-particle wavefunctions and well-defined extension
  from a fundamental chamber.
- Watson exchange previewed as a rapidity-boundary-value statement about
  ordered scattering bases, now stated as a proposition with proof from the
  ZF exchange relation; locality is reserved for cyclicity and reconstruction
  conditions.
- Boundary between on-shell scattering data and reconstruction of local
  fields through form factors.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\theta\) | rapidity |
| \(p^\mu(\theta)\) | massive two-dimensional momentum |
| \(s_{ab}(\theta)\) | positive invariant mass squared, \(-\bigl(p_a+p_b\bigr)^2\) |
| \(V\) | finite-dimensional species space |
| \(S_{12}(\theta)\) | two-body scattering operator on \(V\otimes V\) |
| \(C\) | charge-conjugation matrix used in crossing |
| \(Z_a^\dagger(\theta)\) | Zamolodchikov--Faddeev creation operator |
| \(Q_{s,\lambda}\) | conserved charge of Lorentz spin \(s\) |
| \(\Phi_N\) | higher-spin charge moment map on \(N\)-particle multisets |
| \(\mathsf T_i\) | adjacent chamber-transition map induced by two-body scattering |

## Claim Ledger

1. Factorization is a property of the scattering theory after asymptotic
   states exist.
2. Yang--Baxter consistency follows from equality of different pairwise
   scattering orderings.
2a. More precisely, unitarity and Yang--Baxter are the local relations that
    make adjacent chamber-crossing maps path independent.
3. Higher-spin charge conservation constrains the support of scattering
   distribution kernels to the common zero locus of charge differences.
4. Under the separating moment-map hypothesis, that common zero locus is the
   elastic permutation graph away from threshold and bound-state singular
   loci.
5. Watson exchange is a boundary-value identity for ordered scattering
   bases; it should not be compressed into the phrase "locality gives".
6. Local QFT reconstruction from factorized \(S\)-matrices requires separate
   form-factor and locality analysis.

## Figures

- Rapidity-space two-body scattering diagram.
- Three-particle Yang--Baxter braid diagram.
- Factorized scattering line ordering diagram.

## Audit Notes

- 2026-05-28 formalization pass: promoted the rapidity convention, chamber
  groupoid consistency, ZF associativity, \(S\)-symmetric wavefunction
  extension, and Watson exchange to definitions/propositions with proofs.
  Added `calculation-checks/factorized_scattering_algebra_checks.py` for the
  rapidity-sign convention, Newton identities, braid relations, rational
  Yang--Baxter identity, scalar unitarity, and Watson coefficient bookkeeping.
