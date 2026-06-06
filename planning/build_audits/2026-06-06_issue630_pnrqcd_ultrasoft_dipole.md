# Issue #630 pNRQCD ultrasoft dipole pass

## Target

Strengthen the QCD heavy-quark part of Volume II, Chapter 19 by moving the
pNRQCD discussion beyond a static-potential coordinate.  The target was the
fluctuation layer that makes weak-coupling pNRQCD a field-theoretic expansion:
singlet-octet chromoelectric dipole transitions, ultrasoft correlators, and
the residual data required before a potential-model spectrum is interpreted as
a QCD prediction.

## Manuscript Changes

- Added `ca:qcd-pnrqcd-ultrasoft-dipole-window` after the singlet/octet bilocal
  and tree Coulomb-potential construction.
- Stated the multipole parameter \(r\partial_{\rm us}\sim v_{\rm rel}\) and
  the leading singlet-octet chromoelectric dipole coupling in the chapter's
  trace-delta gauge-field normalization.
- Derived the tree octet color factor \(+1/N_c\) and the corresponding octet
  gap \(V_O^{(0)}-V_S^{(0)}=g^2N_c/(4\pi r)\).
- Wrote the ultrasoft second-order energy-shift coordinate using the octet
  Hamiltonian and an adjoint-Wilson-line chromoelectric correlator, with the
  width interpretation named when intermediate channels cross a physical cut.
- Explicitly listed the mass-scheme, matching-scale, correlator,
  counterterm, threshold, multipole, relativistic, and nonperturbative residual
  data needed for a controlled pNRQCD prediction.

## Companion Evidence

- Extended `calculation-checks/qcd_nrqcd_checks.py` with:
  - the trace-delta octet Coulomb gap check;
  - the weak-coupling multipole parameter \(r\partial_{\rm us}=v_{\rm rel}\);
  - a finite two-level singlet-octet model verifying the negative
    second-order ultrasoft shift;
  - a resolvent-denominator check for positive ultrasoft energy.
- Updated `calculation-checks/README.md` and the Chapter 19 dossier.

## Re-audit

This is a physics-depth pass rather than a tangential mathematics insertion.
The new material identifies the dynamical fluctuations that correct and can
broaden quarkonium levels; the static singlet potential is treated as one
coordinate inside the matched EFT, not as the full prediction.  The TeX edit
contains no issue, directive, or planning metadata.

## Verification

- `python3 -m py_compile calculation-checks/qcd_nrqcd_checks.py`
- `python3 calculation-checks/qcd_nrqcd_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_nrqcd`
- Focused Chapter 19 theorem-form, unnumbered-display-label,
  negative-scope, and style-density audits.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 calculation-checks/scet_factorization_checks.py` after refreshing
  shifted Ch19 textual factorization anchors.
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`
- `tools/build_monograph.sh` clean; regenerated `monograph/tex/main.pdf` at
  3411 pages.
