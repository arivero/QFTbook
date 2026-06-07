# Issue #852 audit: cigar/Liouville source spectral measure

## Target

- Chapter: Volume VII, Chapter 09.
- Local objects: `constr:cigar-liouville-source-spectral-resolution`,
  `constr:cigar-liouville-matrix-spectral-measure`, and the paired
  `susy_2d_lg_glsm_checks.py` companion.
- Review concern: the previous source-measure formula added the signed
  phase-shift density `(2 pi)^-1 partial_s arg R` to a reference Plancherel
  measure and then multiplied by an independent source row.

## Before

- The finite-volume root-counting phase and a positive Hilbert-space source
  measure were described in one displayed formula.
- Normalizable discrete states and analytically continued resonances were
  both represented by pole-residue delta terms in the same real-`s` measure.
- The companion integrated the phase-density shift against a source row as if
  this were the source spectral theorem.

## After

- The phase derivative is a signed counting/spectral-shift diagnostic.
- The positive source measure is the weak limit of normalized finite-box source
  overlaps, equivalently a Plancherel/source Gram measure after continuum
  normalization is proved.
- The text displays the cancellation between finite-box level density and
  eigenfunction normalization in the sum-to-integral limit.
- Normalizable discrete states enter as separate positive energy masses with
  norming constants.
- Resonance poles are assigned to analytic continuation of resolvents or
  correlators, not to the Hilbert-space spectral measure.
- The companion now treats the old additive phase-density rule as a negative
  control that can fail positivity.

## Scope Boundary

This repair corrects the spectral-theorem interface and the finite companion
logic.  It does not derive the exact cigar/coset Plancherel theorem, construct
the Liouville path-integral normalization, prove operator completeness, or
transport the full mirror operator map.
