# 2026-05-31 EEC Asymptotic Multiplication-Model Pass

Scope: `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`,
`planning/chapter_dossiers/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_dis.md`,
and `calculation-checks/energy_correlator_sum_rule_checks.py`.

Motivation: GitHub issue #519 asks for a nonperturbative detector-observable
foundation for energy correlators rather than a purely perturbative
calorimeter discussion.  Earlier passes had introduced stress-tensor flux
limits, finite-event measures, eventwise EEC sum rules, endpoint perturbation
theory, and light-ray OPE bookkeeping.  The remaining local gap was the
operator-theoretic bridge between the spectral action on outgoing hadrons and
products of smeared detectors, especially the status of coincident-detector
contact terms.

Substantive change:

- Added an asymptotic direct-integral model for the outgoing hadronic
  scattering representation.  In this model a smeared detector is the
  multiplication operator with symbol
  \(m_f(Y)=\sum_{r\in Y}p_r^0f(\widehat{\mathbf p}_r)\).
- Made self-adjointness for real test functions, positivity for nonnegative
  test functions, the Hamiltonian domain bound
  \(|m_f|\leq\|f\|_\infty E_{\rm tot}\), and the common product-domain
  statement consequences of the direct-integral spectral theorem.
- Spelled out that detector products are product measures
  \(\mu_X^{\otimes k}\), so diagonal contact strata are part of the
  observable.  Removing them is a separate measurement prescription.
- Kept the nonperturbative stress-tensor flux construction as the hard open
  problem: the flux limit must be shown to agree with the multiplication model
  under outgoing scattering wave operators.

Calculation check:

- Expanded `energy_correlator_sum_rule_checks.py` beyond zeroth/first EEC
  moments.  It now checks the finite-event multiplication algebra, the
  detector norm bound, constant-detector total-energy identity, and equality
  between detector products and product-measure pairings, including diagonal
  contact weights.

Status: This pass strengthens the nonperturbative detector foundation but does
not close issue #519.  The full issue still requires a genuine all-order
renormalized light-ray OPE/mixing theorem, endpoint matching beyond the
displayed leading structures, and the modern high-loop/frontier energy-flow
program.
