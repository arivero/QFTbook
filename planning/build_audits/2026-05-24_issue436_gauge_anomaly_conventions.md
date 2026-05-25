# Issue #436 Gauge And Anomaly Convention Pass

## Scope

- GitHub issue #436: inconsistent structure-constant index placement.
- Expanded user directive: audit non-Abelian gauge coupling and generator
  conventions, including anomaly normalizations, against the stringbook
  spinor/anomaly conventions.

## Convention Fixed

- The active monograph convention is output-first:
  \([t^a,t^b]=\ii f^c{}_{ab}t^c\).
- The default fundamental trace convention is
  \(\operatorname{tr}_{\square}(t^a t^b)=\delta^{ab}\).
- The Yang--Mills coupling coordinate is defined by
  \(-\frac1{4g_{\mathrm{YM}}^2}\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})\).
- Trace-lowered structure constants are
  \(f_{abc}:=-\ii\operatorname{tr}(t^a[t^b,t^c])\), with raising and lowering
  performed by the displayed trace pairing.

## Manuscript Changes

- Chapter 17 now states the output-first convention, trace-lowered constants,
  and the \(1/(4g_{\mathrm{YM}}^2)\) matrix-trace kinetic normalization.
- Chapter 17b now uses the same trace normalization in the Wilson lattice
  action, with \(\beta=N/g_0^2\) in the monograph convention and a local
  remark explaining the common half-trace \(\beta=2N/g_0^2\) coordinate.
  The smooth-plaquette expansion now explicitly accounts for
  \(\sum_{\mu<\nu}\) versus the full ordered \(\mu,\nu\) contraction, giving
  \((4g_0^2)^{-1}\int\operatorname{tr}F_{\mu\nu}F_{\mu\nu}\).
- Chapter 18 now states the condensed gauge-algebra kernel
  \(f^{(a,x)}{}_{(b,y)(c,z)}\) without introducing a second raising
  convention.
- Chapter 24 was rechecked against the issue report: its BV formulas use the
  same output-first convention \(f^a{}_{bc}\), and the minimal Yang--Mills BV
  action now explicitly references
  \([t^a,t^b]=\ii f^c{}_{ab}t^c\) before writing
  \(sc^a=-\frac12 f^a{}_{bc}c^bc^c\).  The condensed notation
  \(C^\gamma{}_{\alpha\beta}=f^\gamma{}_{\alpha\beta}\) is the corresponding
  abstract-index form rather than a second placement convention.
- Chapter 19 now defines \(C_A,T_R,C_R\) in the monograph trace convention:
  for \(SU(N_c)\), \(C_A=2N_c\), \(T_F=1\), and
  \(C_F=(N_c^2-1)/N_c\).  The one-loop QCD beta function is correspondingly
  \(\beta(g)=-(11N_c-2N_f)g^3/(24\pi^2)+O(g^5)\) for fundamental quarks in
  the coupling coordinate of the monograph.
- Chapter 20 now reminds the reader of the same Hermitian gauge convention
  before the non-Abelian anomaly discussion.  The mixed non-Abelian anomaly
  coefficient now includes the missing factor
  \(\frac12\operatorname{tr}(T^A\{t^a,t^b\})\), so the Abelian Dirac axial
  specialization returns \(1/(16\pi^2)\epsilon FF\).
- Appendix A now states the two-dimensional trace identity in the exact
  momentum-index order used by the anomaly calculation:
  \(\operatorname{tr}(\gamma^\nu\gamma\gamma^\rho)=2\epsilon^{\rho\nu}\).
- Chapter 21 was checked for the only active half-trace generator convention:
  its \(T^a\) are flavor generators for the chiral target, not color gauge
  generators.  The chapter now says this explicitly before using
  \(T^a=\sigma^a/2\) in the pion normalization.

## Calculation Checks

- Added public calculation checks in `calculation-checks/`:
  - `gauge_convention_checks.py` verifies the default \(SU(2)\) basis
    \(t^a=\sigma^a/\sqrt2\), \(SU(N)\) trace-delta generators, the doubled
    \(C_A,T_F,C_F\) constants in the monograph coupling coordinate, and the
    Wilson plaquette factor.
  - `gamma_trace_checks.py` checks the stringbook-compatible Weinberg
    mostly-plus gamma matrices, \(\gamma_5\), the Wess--Bagger chiral phase
    comparison, the four-dimensional \(\gamma_5\) trace, the two-dimensional
    chirality trace, and the anticommutator factor in the mixed anomaly.
  - `gamma_trace_checks.wl` provides the same finite symbolic checks in an
    agent-readable Wolfram Language file rather than a notebook-only format.
- Added `tools/run_calculation_checks.sh`, including the macOS app-bundled
  Wolfram executable path
  `/Applications/Wolfram.app/Contents/MacOS/wolframscript`.
- The harness now records that heavy or numerical checks should be Python
  scripts, while Wolfram Language checks are lightweight reader-facing
  symbolic convention checks.

## Searches

- Active manuscript and dossier searches outside this audit record no longer
  find the old raised-pair structure-constant notation.
- No active hits remain for the old
  \(\frac1{2g_{\mathrm{YM}}^2}\operatorname{tr}(F^2)\) kinetic convention or
  for \(\frac1{2g_R^2}\operatorname{tr}(F_{\mu\nu}F_{\mu\nu})\) in the lattice
  Symanzik action.
- Half-trace normalization appears only in local explanatory remarks that
  explicitly identify it as an alternate convention.
- Active text has no uses of the standard half-trace numerical QCD constants
  as the monograph's own \(C_A,T_F,C_F\) convention.

## Verification

- `env QFT_SKIP_WOLFRAM=1 tools/run_calculation_checks.sh`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 787 pages.
