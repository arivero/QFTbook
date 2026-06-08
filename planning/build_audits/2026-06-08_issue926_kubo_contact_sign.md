# Issue #926 Kubo Contact-Sign Audit

## Scope

- Target chapter: `monograph/tex/volumes/volume_x/chapter04_spectral_functions_kubo_transport.tex`.
- Issue repaired: use one contact-term sign in the general source-response
  kernel and the conductivity response kernel.

## Substance Audit

- The chapter now defines the full source derivative as
  \(\mathcal K^{\rm full}_{AB}=-G^{R,\rm comm}_{AB}+C^{\rm resp}_{AB}\).
  The contact \(C^{\rm resp}\) is the local term in the full response
  derivative, not a sign-free decoration.
- The conductivity section now defines
  \(K^{\rm cond}_{ij}=-\mathcal K^{\rm full}_{ij}
  =G^{R,\rm comm}_{J_iJ_j}-C^{\rm resp}_{ij}\) from
  \(\langle J_i\rangle=-K^{\rm cond}_{ij}A_j^{\rm ext}\).
- A finite minimally coupled charged oscillator supplies the regulated
  diamagnetic example:
  \(H(A)=(p-qA)^2/(2m)+m\Omega^2x^2/2\),
  \(J(A)=qp/m-q^2A/m\), and \(C^{\rm resp}_{JJ}=-q^2/m\).  Its static
  paramagnetic retarded kernel is \(-q^2/m\), so both the full static response
  and the conductivity static kernel cancel.  The real contact leaves the
  nonzero-frequency commutator spectral part unchanged.
- The calculation check now includes a negative control: using the wrong
  contact sign leaves a nonzero static conductivity kernel, which would create
  a spurious \(1/\omega\) contribution in \(\sigma(\omega)\).

## Physics-Depth Reaudit

- The pass is physics-facing rather than formal: it repairs the static
  response and diamagnetic seagull bookkeeping that controls gauge Ward
  identities, Euclidean zero modes, and the Drude/regular conductivity split.
- No directive or process note was added to reader-facing TeX; process
  tracking stays in this audit note and the chapter dossier.

## Verification

- Passed: `python3 calculation-checks/thermal_kubo_checks.py`.
- Passed: focused style/dossier/evidence audits:
  `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_x/chapter04_spectral_functions_kubo_transport.tex --fail`,
  `bash tools/audit_chapter_dossiers.sh`,
  `python3 tools/audit_calculation_evidence_contracts.py`,
  `python3 tools/audit_calculation_check_inventory.py`, and
  `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_x/chapter04_spectral_functions_kubo_transport.tex`.
- Passed: `tools/run_calculation_checks.sh --python-only`.
- Passed: `tools/build_monograph.sh`.
