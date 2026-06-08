# Issue #885 Connection/Canonical Debye-HTL Audit

## Scope

- Volume X, Chapter 7 thermal gauge screening.
- Volume X, Chapter 12 QCD HTL/Linde subsection.
- `calculation-checks/thermal_screening_checks.py` and check inventory.
- Chapter dossiers for the touched chapters.

## Physics Repair

- Reserved `mathcal A_mu` for the connection and `a_mu=mathcal A_mu/g` for the
  canonical HTL source.
- Made the Debye conversion explicit:
  connection-source curvature `chi=m_D^2/g^2`, canonical-source polarization
  `m_D^2`.
- Rewrote the HTL auxiliary-field response as a canonical-source derivation
  with `D_a=partial+g[a,.]`, `f_i0`, and `j_a`.
- Carried the conversion through EQCD kinetic/mass terms, the static
  propagator normalization, `g_3^2=g^2T`, induced currents, and Polyakov
  holonomy `P exp(int mathcal A_0)=P exp(g int a_0)`.
- Chapter 12 now treats its HTL block as the QCD-notation application of the
  Chapter 7 canonical bridge.

## Regression Guard

`thermal_screening_checks.py` now checks the finite algebra under
`mathcal A=ga` for:

- quadratic kinetic term;
- Debye mass term;
- 1PI kernel;
- four-dimensional and EQCD static propagator normalizations;
- induced source-current conversion;
- holonomy exponent.

## Re-Audit Notes

- Scope stayed on physical response normalization rather than adding tangential
  mathematical infrastructure.
- The chapter prose emphasizes source variations, propagators, currents, and
  holonomies because those affect physical amplitudes and response functions.
- Directives and process notes remain in planning files, not monograph TeX.
