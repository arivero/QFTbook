Issue #844/#630 EEC benchmark-window audit
==========================================

Scope
-----

- Target: Volume II Chapter 19, analytic EEC benchmark comparison.
- Companion: `calculation-checks/energy_correlator_light_ray_ope_checks.py`.
- Issues: #844 claim-architecture consolidation and #630 QCD rigor uplift.

Quality audit
-------------

- The edit keeps the block as a controlled approximation because it has a
  declared finite detector-test window and a displayed residual bound.  It
  removes the reader-facing `ledger` title because the physics claim is a
  benchmark comparison in a measured detector topology.
- The monograph now states that source row, total-rate normalization, and
  angular-variable pushforward are part of the physical comparison.  A result
  tabulated in `z=(1-zeta)/2` must be paired with the pulled-back detector test,
  and a vector-current benchmark is not automatically a Higgs-source benchmark.
- The companion adds exact finite negative controls for the two remaining weak
  spots: using the wrong angular variable and using the wrong source row.  This
  turns the comparison into an observable test rather than another named
  architecture surface.
- Planning and issue-audit language stays here and in the dossier, not in the
  TeX chapter.
