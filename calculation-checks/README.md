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

- `banks_zaks_two_loop_checks.py`: exact rational checks for the Banks-Zaks
  two-loop beta-function conventions in the monograph's
  \(\operatorname{tr}_{\square}(t^a t^b)=\delta^{ab}\) normalization,
  including the conformal-window edge and leading \(\epsilon_{\rm BZ}\)
  fixed-point formulas.
- `bpst_instanton_normalization_checks.py`: finite algebra and radial-integral
  checks for the BPST instanton section, including self-duality of the
  't Hooft symbols, the quadratic \(\eta\)-symbol identity used in the
  curvature calculation, \(\int F^a_{\mu\nu}F^a_{\mu\nu}=32\pi^2\), \(Q=1\),
  and the conversion between the common half-trace action
  \(8\pi^2/g_{\rm ht}^2\) and the monograph trace-delta coupling
  \(4\pi^2/g_{\rm YM}^2\).
- `center_polyakov_checks.py`: finite center-phase checks for the thermal
  center-symmetry and Polyakov-loop section, including temporal-plaquette
  phase cancellation, Polyakov-loop \(N\)-ality, neutral pair correlators,
  center averaging of charged loops, and the static-source free-energy
  relation.
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
- `wilson_fisher_epsilon_checks.py`: exact rational arithmetic turning the
  two-loop \(N=1\) Wilson-Fisher pole coefficients into
  \(x_*\), \(\eta\), \(\gamma_{2*}\), \(y_t\), \(\nu\), and \(\omega\).
- `on_wilson_fisher_epsilon_checks.py`: exact rational arithmetic for the
  singlet \(O(N)\) Wilson-Fisher family, including the \(N=1\) reduction and
  the leading large-\(N\) scaling of \(u=Nx\).
- `schwinger_model_checks.py`: finite sign and normalization checks for the
  Schwinger-model chapter, including the two-dimensional current-duality
  convention, the algebraic elimination of the electric field, the
  anomaly-induced mass \(m_{\rm Sch}^2=e^2/\pi\), the screened static
  potential, and the periodicity of the massive-model string tension for
  integer probe charge.
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
