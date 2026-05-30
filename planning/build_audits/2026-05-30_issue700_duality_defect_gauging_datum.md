# Issue #700: Duality-Defect And Finite-Gauging Datum

## Target

Volume IX, Chapter 10 was listed as a partial issue #700 gap: the chapter had
definitions for the finite gauging sum and the regular algebra defect, but the
central object "QFT with finite gauging data and duality-defect structure" was
not aggregated before the finite algebra and examples were developed.

## Edit

- Added `hyp:finite-gauging-duality-defect-datum` near the chapter opening.
- The datum collects the QFT, finite symmetry group, background-bundle
  groupoids, anomaly class, anomaly trivialization / Dijkgraaf-Witten
  counterterm, topological symmetry defects, gauging interface and reverse
  interface, optional self-duality equivalence, and gauge-theory line-charge
  lattice data.
- Rewrote the finite-background, finite-gauging, and gauging-interface entry
  points to refer back to the named datum.
- Updated the Chapter 10 dossier.

## Scope

The finite slab-fusion and line-lattice calculations remain finite algebraic
consequences after the datum is supplied.  The continuum construction of
interfaces and junctions remains `op:continuum-gauging-interfaces`.

## Verification

- `tools/build_monograph.sh`
- Output: `monograph/tex/main.pdf`
- Page count: 2678
- The first build caught an overfull line in the new hypothesis.  The anomaly
  class was moved into displayed math, and the second build completed with a
  clean log scan.
