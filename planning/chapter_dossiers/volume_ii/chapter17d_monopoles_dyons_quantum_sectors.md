# Volume II, Monopoles, Dyons, and Quantum Sectors Dossier

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter17d_monopoles_dyons_quantum_sectors.tex`.
- Compiled in the gauge/anomaly part through
  `monograph/tex/volumes/volume_iv/volume_iv_current.tex`, immediately after
  `chapter17c_solitons_collective_quantization.tex`.
- Role in the monograph: begin the dedicated monopole/dyon quantum-sector
  chapter requested by the soliton/monopole/instanton depth lane.
- Relation to neighboring chapters: Ch17 supplies finite-energy monopole
  cores, BPS bounds, the phase coordinate, and Witten-effect charge shift.
  Ch17c supplies the companion soliton quantization chapter.  This chapter
  isolates asymptotic charge physics and the two-body Hilbert-space data.

## Definitions And Results

- `ch:monopoles-dyons-quantum-sectors`: dedicated chapter for monopoles and
  dyons as quantum sectors.
- `sec:dyonic-charges-dsz-pairing`: Witten-shifted charges and the
  Dirac-Schwinger-Zwanziger pairing.
- `prop:monopole-chapter-dsz-pairing`: proves theta independence and
  integrality of the DSZ pairing in primitive charge units.
- `sec:field-angular-momentum-monopole-harmonics`: field angular momentum and
  monopole harmonics in the two-body relative coordinate.
- `prop:monopole-chapter-monopole-harmonics`: records
  `j=|N|/2+ell` and the radial barrier `j(j+1)-N^2/4`.
- `sec:bps-alignment-no-force-benchmark`: leading BPS tail-force benchmark.
- `ca:monopole-chapter-aligned-bps-no-force`: same-ray BPS charge vectors
  cancel the leading vector-plus-scalar static tail.

## Claim Ledger

- The chapter advances #597 by starting the dedicated monopole component at
  the quantum-sector level rather than adding more classical core or
  moduli-space geometry.
- The central physics claim is that monopoles and dyons are long-range
  charged sectors.  Their asymptotic fields determine DSZ locality, field
  angular momentum, monopole-harmonic partial waves, and no-force benchmarks.
- The Witten-effect electric charge shift is physical, but pairwise locality
  is the theta-independent antisymmetric DSZ pairing.
- The field angular momentum is half the DSZ integer; odd DSZ pairing
  produces half-integer angular momentum before core spin is included.
- The BPS no-force benchmark is a vector/scalar tail cancellation, not a
  statement that a moduli-space coordinate automatically defines a protected
  spectrum.

## Figure Ledger

- No new figure in this pass.
- Future expansion may add a two-dyon asymptotic-field diagram showing the
  radial field angular momentum and the monopole-harmonic line bundle on the
  linking sphere.

## Calculation Checks

- `calculation-checks/monopole_dyon_sector_checks.py` carries the companion
  evidence contract.
- It checks theta-independent DSZ pairing, rejects a theta-dependent one-body
  electric-magnetic shortcut, verifies half-DSZ field angular momentum,
  enumerates finite monopole-harmonic angular momentum data, and verifies the
  aligned BPS no-force cancellation with negative controls.

## Audit Notes

- 2026-06-06 issue #597 monopole-chapter start: added the compiled
  `chapter17d_monopoles_dyons_quantum_sectors.tex` after the soliton chapter.
  The pass prioritizes long-range charge-sector physics over new monopole
  moduli-space mathematics.
- The frontmatter source map was updated so later listed chapter numbers shift
  after the new compiled chapter.
- No directives, GitHub issue text, or process-monitoring language was inserted
  into monograph TeX.
