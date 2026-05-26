# OS Reconstruction Corrected OS-II Proof Pass

Date: 2026-05-26

## Scope

- Reframed the OS-I error precisely as the false passage from separate
  one-variable Laplace continuations to a joint many-variable
  Fourier--Laplace transform.
- Added the corrected OS-II analytic theorem to
  `volume_iv/chapter02_osterwalder_schrader_reconstruction.tex`.
- Developed the proof through:
  - local one-gap semigroup continuation;
  - Malgrange--Zerner gluing;
  - the `A_N/P_N` induction;
  - Hilbert Taylor reconstruction of vector-valued analytic fields;
  - convex exhaustion of time-gap argument domains;
  - regularized positivity estimates from the linear-growth condition;
  - Banach-valued maximum-principle propagation of tube bounds.
- Added a strict harness rule distinguishing named mathematical inputs from
  QFT-specific bridge theorems, which must be derived in the monograph.

## Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full build completed with a clean final log scan.  The generated PDF is
`monograph/tex/main.pdf`, 1547 pages.
