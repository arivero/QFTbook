# Projected-Current Hydrodynamic Closure Pass

Date: 2026-05-31

Scope:

- `monograph/tex/volumes/volume_x/chapter04_spectral_functions_kubo_transport.tex`
- `planning/chapter_dossiers/volume_x/chapter04_spectral_functions_kubo_transport.md`

Issue lane:

- GitHub #703, hydrodynamic theorem-status expansion.

Audit finding:

- The chapter already separated finite-regulator Mori-Zwanzig algebra from
  hydrodynamic closure, but the closure boundary was compressed into a short
  paragraph.  The missing material was the exact limiting datum needed before
  one can honestly speak of a diffusion pole.

Change:

- Added a subsection `The Closure Datum Behind a Diffusion Pole`.
- Stated a projected-current hydrodynamic closure hypothesis: thermodynamic
  convergence of projected kernels, existence and regularity of the Laplace
  transform after Drude/zero-mode subtraction, decoupling of the initial-force
  term, and nonsingular charge susceptibility.
- Derived the Laplace-space slow-density equation and the diffusive pole
  \(z=-k^2\lambda+o(k^2)\), equivalently
  \(\omega=-i\lambda k^2+o(k^2)\), from the closed memory equation.
- Derived the Einstein relation \(\Sigma=D\chi\) as the comparison between
  the same limiting kernel written in density and current coordinates.

Verification:

- Run the strict text, theorem-form, unnumbered-label, dossier, and full build
  audits before commit.
