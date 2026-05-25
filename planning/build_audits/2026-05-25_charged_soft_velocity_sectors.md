# 2026-05-25 Charged Soft Velocity-Sector Pass

GitHub issues: #527 and #528, on charged-sector Haag--Ruelle and LSZ with
Wilson-line or Coulombic dressings.

## Manuscript Change

Volume IV, Chapter 5 now contains a finite-cutoff soft coherent calculation
between the boosted Coulomb flux discussion and the charged-sector open
problem:

- the finite soft-photon one-particle space
  \(\mathfrak h_{\lambda,\Lambda}\) is defined with the photon phase-space
  measure and transverse polarization projector;
- the charged velocity profile \(F_{q,\mathbf v,\lambda,\Lambda}\) is derived
  from the worldline/Faddeev--Kulish eikonal denominator;
- Proposition `soft-coherent-velocity-separation` proves
  \[
    \|F_{q,\mathbf v,\lambda,\Lambda}
      -F_{q,\mathbf w,\lambda,\Lambda}\|^2
    =
    {q^2\over 2(2\pi)^3}\log{\Lambda\over\lambda}\,
    \mathcal A(\mathbf v,\mathbf w)
  \]
  with \(\mathcal A(\mathbf v,\mathbf w)\ge0\) and equality only for
  \(\mathbf v=\mathbf w\);
- the normalized coherent-vector overlap is then summed directly and shown to
  vanish as \(\lambda\downarrow0\) for distinct charged velocities.

## Boundary

This is not advertised as a complete massless-QED scattering theorem.  It is
the finite-Fock-space calculation that explains why the charged velocity and
flux label must be included in the asymptotic representation before a
Haag--Ruelle replacement can be formulated.

## Verification

- `python3 calculation-checks/charged_flux_dressing_checks.py` passed with
  `All charged flux and Wilson-line dressing checks passed.`
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with a clean final log scan.
- `pdfinfo monograph/tex/main.pdf` reports 1242 pages.
