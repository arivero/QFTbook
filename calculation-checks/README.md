# Calculation Checks

This directory contains public-facing scripts that verify convention-sensitive
algebra used in the monograph.  They are not substitutes for the derivations
in the text; they are reproducible checks of signs, trace normalizations, and
finite algebraic reductions.

Plain text formats are preferred over notebook-only formats.  Mathematica
checks should be committed as Wolfram Language `.wl` files, with optional
notebooks generated from them when useful.  Computationally heavy checks
should be written in Python rather than Mathematica; Wolfram Language files in
this directory should stay lightweight and reader-readable.

Current checks:

- `cft_anomaly_regression_checks.py`: finite arithmetic checks for the
  issue-#447 regression class: the \(\pi^0\to2\gamma\) anticommutator factor,
  the \(4/3\) identity-block cubic coefficient, the \(W=-\log Z\)
  stress-tensor source sign, and the Lorentzian-to-radial \([P,K]\) sign.
- `gamma_trace_checks.py`: mostly-plus gamma-matrix conventions, \(\gamma_5\),
  the Weinberg/Wess-Bagger chiral phase comparison, the four-gamma trace, the
  two-dimensional chirality trace, and the anticommutator normalization used
  in the nonabelian anomaly coefficient.
- `gauge_convention_checks.py`: \(SU(N)\) Hermitian-generator normalization
  \(\operatorname{tr}(t^a t^b)=\delta^{ab}\), output-first structure
  constants, \(C_A=2N\), \(T_F=1\), \(C_F=(N^2-1)/N\), the coupling-coordinate
  conversion from the common half-trace convention, and the Wilson-plaquette
  factor giving \((4g_0^2)^{-1}\int\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\).
- `gamma_trace_checks.wl`: a Wolfram Language version of the same finite
  algebraic checks, adapted from the stringbook spinor appendix and
  `gamma matrices.nb` conventions without relying on `.nb` structure.

Run all available checks from the repository root with:

```bash
tools/run_calculation_checks.sh
```

For Wolfram Language checks, the runner requires a working batch backend when
any `.wl` files are present.  On the author's macOS installation the preferred
entrypoint is

```bash
/Applications/Wolfram.app/Contents/MacOS/WolframKernel -script calculation-checks/<file>.wl
```

The harness probes the selected backend before running checks, rejects `.wl`
files with arithmetic continuations that begin a line with `+`, `-`, `*`, or
`/`, and requires every Wolfram script to print a line of the form
`All Wolfram Language ... passed.`.  Set `QFT_SKIP_WOLFRAM=1` only for an
explicitly Python-only pass.  Set
`WOLFRAMKERNEL=/absolute/path/to/WolframKernel` or
`WOLFRAMSCRIPT=/absolute/path/to/wolframscript` to override executable paths.

Planned checks:

- dimensional-reduction triangle numerator reductions for the axial anomaly;
- background-field one-loop Yang--Mills heat-kernel coefficient bookkeeping;
- conformal-block normalization and Casimir-equation checks;
- superfield, supersymmetry-transformation, and spinor-index convention
  checks for later supersymmetric field-theory volumes;
- simple Feynman-parameter integrals appearing in one-loop examples.
