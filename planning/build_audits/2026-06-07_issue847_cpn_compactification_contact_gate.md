# Issue #847: CP degree-one compactification/contact gate

## Change

Added a finite compactification/contact gate to the Volume VII Chapter 09
degree-one `P^{N-1}` instanton discussion.

The monograph now separates the bulk evaluation-form Berezin Jacobian from the
stable-map boundary and local source-contact data.  For the representatives
`p_0=[1:0:...]`, `p_1=[0:1:...]`, and `h=X_1-X_0`, the three degree-one
boundary indicators are computed:

- the two point insertions collide on a contracted component;
- the hyperplane insertion collides with `p_0`;
- the hyperplane insertion collides with `p_1`.

All three vanish in the canonical separated-evaluation convention, and the
contact counterterms are explicitly set to zero in that retained chart.  The
same block records how point collisions, a hyperplane through a point, or
nonzero source-contact counterterms change the retained coefficient unless the
boundary/contact convention is transported.

## Companion

Added `check_degree_one_cpn_compactification_contact_gate()` to
`calculation-checks/susy_2d_lg_glsm_checks.py`.

The finite check verifies:

- separated representatives avoid the three compactification boundary strata;
- the retained compactified integral is the unit line count;
- point-collision and hyperplane-through-point mutations change the compactified
  integral;
- nonzero local contact counterterms shift the degree-one coefficient;
- omitting the contact residual underbudgets the comparison before a mirror
  residue is used.

README, evidence-contract, and Chapter 09 dossier metadata were updated.

## Re-audit

This is physics-depth progress on the direct A-model instanton measure side,
not a moduli-space-only annex.  It adds a concrete compactification/contact
piece to the fluctuation-and-measure bridge that the user explicitly asked to
prioritize over Hori-Vafa residue inheritance.

It is still a finite retained-window gate.  It does not prove the continuum
GLSM vortex regulator limit, derive the full nonzero-mode determinant, identify
the complete original-to-mirror operator map, prove uniform boundary estimates,
or close #847.  It should therefore remain labelled as a direct-measure
improvement and not as a full Hori-Vafa derivation.
