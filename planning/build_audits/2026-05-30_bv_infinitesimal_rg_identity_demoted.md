# BV infinitesimal RG identity demotion

Date: 2026-05-30.

Target:
- GitHub issue #691, anti-wrapper audit for theorem-family statements whose
  proofs are only elementary consequences of definitions.

Files touched:
- `monograph/tex/volumes/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.tex`
- `planning/chapter_dossiers/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.md`

Change:
- Demoted the former lemma `Infinitesimal BV RG preserves the QME`.
- Preserved the actual identities
  `partial_t rho_t = Delta_{1/2}(R_t rho_t)`,
  `partial_t Delta_{1/2} rho_t = 0`, and
  `partial_t S_t = (S_t,R_t)-i hbar Delta R_t`.
- Reframed the passage as a named derivation: the nontrivial mathematical
  claim is the construction of a BV-compatible infinitesimal velocity
  `R_t` from a finite regulator or finite pushforward.  Once that datum is
  present, QME preservation is the cohomological tangent identity
  `Delta_{1/2}^2=0`, not a theorem-family result.

Rationale:
- The previous lemma/proof was correct but overpackaged.  It risked giving the
  reader the false impression that the short nilpotency calculation was the
  hard part of gauge-compatible Wilsonian RG.  The revised text places the
  burden where it belongs: on the finite BV pushforward or regulator scheme
  that supplies the odd generator and half-density data.

