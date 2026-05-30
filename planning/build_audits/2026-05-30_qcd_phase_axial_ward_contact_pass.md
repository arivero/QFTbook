# QCD Phase Chapter: Axial Ward Contact-Term Pass

Date: 2026-05-30.

GitHub context: #630 and #691.

Purpose: strengthen a compact proof that appeared in the current theorem-proof
triage queue, without demoting a genuinely useful Ward identity.

Files edited:

- `monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `calculation-checks/qcd_phase_checks.py`
- `planning/chapter_dossiers/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.md`

Substance:

- Expanded the proof of the integrated nonsinglet axial Ward identity.
- The manuscript now displays the local distributional Ward identity on the
  finite thermal spacetime torus:
  `partial_mu <A_mu^a(x) P^b(0)> + 2m <P^a(x)P^b(0)> +
  delta_beta^(4)(x)<delta^a P^b(0)>=0`.
- The proof now derives the contact term
  `delta^a P^b=-bar q {tau^a,tau^b} q` from the Euclidean convention
  `P^a=bar q i gamma_5 tau^a q`, rather than hiding the sign in prose.
- The proof now states why the nonsinglet connected correlator equals the
  ordinary correlator in a vector-flavor-invariant thermal state.
- The flavor-symmetric projection with
  `tr_f(tau^a tau^b)=delta^{ab}` is kept explicit so the result
  `m chi_pi^{ab}=delta^{ab} Sigma_m` follows without convention drift.

Calculation check:

- `calculation-checks/qcd_phase_checks.py` now checks the axial contact-term
  sign, the integrated Ward-sign relation between `chi_pi=-int PP` and the
  contact term, the trace-delta flavor projection, and the trace-delta versus
  half-trace GMOR normalization.

This pass keeps the lemma form because the statement is a reusable
finite-temperature QCD Ward identity; the edit closes the compressed-proof
weakness rather than demoting the identity to prose.
