# Split/Nuclearity Normality Mechanism Pass

Date: 2026-05-31

GitHub issue: #695, foundational reconstruction/AQFT proof debt.

## Scope

Volume IV, Chapter 4 already contained the free-Fock phase-space benchmark and
the split-product-state construction.  The remaining local gap was the
intermediate normality mechanism: a nuclear Banach-space map is not, by
itself, a proof that the multiplication representation of separated local
von Neumann algebras extends normally to the spatial tensor product.

## Change

The nuclearity-to-split discussion now distinguishes three layers:

- Banach nuclearity of
  \(\Theta_{\beta,\mathcal O}(A)=e^{-\beta H}A\Omega\), which gives a
  summable vector expansion of the energy-damped local unit ball.
- Normal separated functionals on
  \(\mathcal M_1\bar\otimes\mathcal M_2'\), which are the objects needed by
  the Doplicher--Longo split criterion.
- The QFT estimates using the positive collar, locality, and the spectral
  condition to convert energy-damped nuclear expansions into limits of
  separated normal functionals.

The text explicitly warns that the coefficient functionals in an arbitrary
Banach nuclear decomposition need not be normal.  Thus the quoted theorem
remains an honest theorem boundary, while the analytic object whose proof must
be supplied is now visible in the manuscript.

## Calculation Check

Added `calculation-checks/split_nuclearity_normality_checks.py`.  It verifies:

- normal product-state extension through a tensor density matrix;
- positivity of the product state on \(C^*C\);
- reconstruction of a finite-rank nuclear map from separated coefficients;
- the separated bilinear expansion
  \(\langle\eta,B'\Theta(A)\rangle
    =\sum_j \ell_j(A)\langle\eta,B'\xi_j\rangle\).

This is a finite diagnostic, not a proof of the infinite-dimensional split
theorem.

## Verification

Targeted verification for this pass:

- `python3 calculation-checks/split_nuclearity_normality_checks.py`
- `python3 -m py_compile calculation-checks/split_nuclearity_normality_checks.py`
- `tools/run_calculation_checks.sh --list`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
