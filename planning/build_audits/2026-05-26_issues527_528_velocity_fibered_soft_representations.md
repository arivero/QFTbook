# 2026-05-26 Issues #527/#528 Velocity-Fibered Soft Representation Pass

GitHub issues: #527 and #528, concerning charged-sector Haag--Ruelle/LSZ with
Wilson-line or Coulombic dressings.

## Manuscript Changes

Volume IV, Chapter 5 now adds a representation-theoretic scaffold for the
charged soft sectors that a future nonperturbative Haag--Ruelle theorem must
use.

- The pass explicitly restricts the dressed charged Haag--Ruelle/LSZ problem
  to nonconfining charged sectors with finite-energy physical charged
  asymptotic data.  In a confining phase, colored Wilson-line operators do not
  define charged particle asymptotic states; ordinary Haag--Ruelle theory
  applies instead to isolated neutral hadron or glueball shells.
- The chapter defines an infrared-regular photon test space
  \(\mathfrak h_{\rm reg}\subset\mathfrak h_{0,\Lambda}\) by requiring the
  limiting soft phase
  \[
    \ell_{\mathbf v}(f)
    =
    \lim_{\lambda\downarrow0}
    \sigma(F_{q,\mathbf v,\lambda,\Lambda},f)
  \]
  to exist.
- It defines the velocity-labelled soft state
  \[
    \omega_{\mathbf v}(W(f))
    =
    e^{i\ell_{\mathbf v}(f)}e^{-\|f\|^2/2}
  \]
  on the infrared-regular Weyl algebra.
- It constructs the direct-integral soft representation
  \(\mathcal H^{\rm soft}_{q,\nu}
    =\int^\oplus_{B_1(0)}\mathcal H_{\mathbf v}\,d\nu(\mathbf v)\).
- Proposition `prop:soft-weyl-algebra-preserves-velocity-fibers` proves that
  the soft photon Weyl algebra acts fiberwise and commutes with velocity
  projections.  Matrix elements between disjoint velocity-support sectors
  therefore vanish for all soft Weyl algebra elements.

This is not presented as the full charged Haag--Ruelle theorem.  It is a
closed structural theorem identifying the representation-theoretic target:
momentum-changing charged scattering dynamics must include charged-sector
operators beyond the soft photon Weyl algebra.

## Verification

Completed before commit:

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build completed cleanly and produced
`monograph/tex/main.pdf` with 1767 pages.
