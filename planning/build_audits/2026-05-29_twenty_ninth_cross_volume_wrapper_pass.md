# Twenty-Ninth Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

## Purpose

Continue #691 by reading short proof candidates that survived the previous
strict queue.  This pass targeted correct calculations whose content belongs
in the main exposition but whose theorem-family wrappers overstated their
logical role.

## Demoted From Theorem-Family Form

- `Automorphism denominator from Wick pairings` is now a Wick-pairing
  bookkeeping paragraph.  The orbit-stabilizer count and the later tadpole
  symmetry-factor use remain explicit.
- `Pairing of positive-energy states` is now an index-pairing paragraph.  The
  cancellation of positive-energy supermultiplets and the zero-mode index
  formula remain.
- `Flavor parameter counting` is now a Standard Model flavor-coordinate
  paragraph.  The \(U(n)^3/U(1)_B\) count and CKM phase count remain.
- `Field-content exhaustion at dimension six` is now a finite
  field-content-enumeration paragraph.  The enumeration remains separated
  from the nontrivial operator-basis quotient.
- `Torus partition function of a finite orbifold` is now an orbifold-gauging
  formula paragraph.  The flat-bundle sum, finite gauge-volume factor, modular
  label action, and discrete-torsion cocycle condition remain.
- `Topological cancellation for \(D_{N,1}\)` is now a local anomaly-response
  cancellation paragraph.  The axial-anomaly phase and defect Hall-response
  cancellation remain, without presenting the local response calculation as a
  full theorem about the compact defect path integral.
- `Baryon susceptibilities are baryon-number cumulants` is now a
  finite-regulator cumulant paragraph.  The spectral-theorem reduction to an
  ordinary moment-generating function and the charge-conjugation parity
  consequence remain.
- `Exchange symmetry and the CFL tensor` is now a color-flavor tensor
  calculation paragraph.  The fermion-exchange sign, antisymmetric
  color/flavor matching, and diagonal \(SU(3)\) stabilizer remain.

## Guardrail Update

`tools/audit_theorem_form.py` now rejects the eight demoted titles if they are
reintroduced as theorem/proposition/lemma/corollary wrappers.

## Retained After Reading

The Fredholm-minor expansion, largest-time identity, Dijkgraaf--Witten
triangulation-independence argument, Bogomolny lower bound, Haag--Ruelle map
isometry, OS ordered-insertion closability, scalar unitarity bound,
Rayleigh--Ritz and gap-stable Ritz counting, transfer-matrix commutativity,
Hadamard-parametrix change isomorphism, finite Grassmann
reflection-positivity criterion, and projective dual-norm kernel criterion
remain theorem-family candidates for now.  These are compact because their
setup has already been built, but each packages a reusable analytic,
geometric, representation-theoretic, scattering, operator-domain, or
functional-analytic construction rather than a one-line substitution.

## Counts After This Pass

- Theorem/proposition/lemma/corollary environments: 547.
- Proof environments: 542.
- The remaining high-priority queue is still nonempty, but after this pass my
  estimate is closer to twelve to twenty-four wrappers that may still require
  demotion or reframing, with the wider second pass still capable of exposing
  softer cases.

## Verification

- Stale-label scan for the eight removed labels: clean.
- `python3 tools/audit_theorem_form.py`: clean.
- `tools/audit_negative_scope_prose.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 2580 pages.
