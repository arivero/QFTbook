# Issue #475 Audit: ANEC And Conformal Collider Bounds

## Scope

GitHub issue #475 requested a substantive CFT-volume treatment of the averaged
null energy condition, the modern modular/causality derivations, and the
Hofman--Maldacena conformal-collider bounds.

## Manuscript Changes

- Expanded `chapter10_light_ray_operators_and_energy_correlators.tex` with a
  dedicated `ANEC and Conformal Collider Bounds` section.
- Defined the transversely smeared ANEC quadratic form
  \(\mathcal A_n(\varphi)\) on \(N_n=n^\perp/\mathbb R n\), rather than using
  an unsmeared null integral as an ordinary operator.
- Stated the Lorentzian CFT hypotheses for ANEC positivity: unitarity,
  unique vacuum, spectrum condition, stress tensor as a Wightman
  distribution, finite-energy domain, and the analyticity/growth assumptions
  needed for the light transform.
- Added the modular-Hamiltonian proof mechanism through null-cut regions,
  the local null-cut modular Hamiltonian, relative-entropy monotonicity, and
  the cancellation that leaves the full null integral of \(T_{++}\).
- Added the Lorentzian-causality proof mechanism through the Regge
  light-cone continuation of a normalized four-point function and the sign of
  the stress-tensor light-transform discontinuity.
- Connected ANEC positivity to positivity of the detector distribution on
  \(S^{D-2}\) and hence to the finite-dimensional stress-tensor-state
  Hofman--Maldacena inequalities.

## Calculation Checks

- Added `calculation-checks/conformal_collider_checks.py`.
- The script checks:
  - the \(S^2\) angular averages \(\langle n_i n_j\rangle=\delta_{ij}/3\)
    and the \(2/15\) traceless rank-four contraction;
  - the helicity \(2,1,0\) ratios that give
    \(1-t_2/3-2t_4/15\),
    \(1+t_2/6-2t_4/15\), and
    \(1+t_2/3+8t_4/15\);
  - the vanishing of the integrated \(t_2,t_4\) deformations, which preserves
    total energy \(Q\).

## Verification Plan

- Run `python3 calculation-checks/conformal_collider_checks.py`.
- Run `git diff --check`.
- Run the monograph text and dossier audits.
- Build the monograph and inspect the rendered pages of the revised chapter.

## Verification Results

- `python3 calculation-checks/conformal_collider_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed with a clean log scan after correcting an
  overfull line in the causality paragraph and replacing an inappropriate
  bra-ket macro in the modular derivation by explicit expectation brackets.
- `pdfinfo monograph/tex/main.pdf` reported 875 pages.
- Rendered and inspected physical PDF pages 862--865, covering the chapter
  opening, the detector/null-line definitions, the ANEC theorem boundary, the
  modular and causality derivations, and the beginning of the
  Hofman--Maldacena bounds section.
