# 2026-05-22 253a Relativistic Particles And Locality Source Pass

## Source Block

- Primary source: `references/253a lectures 2022.pdf`, pp. 3--9.
- Rendered source images inspected:
  - `/tmp/253a_003_009-003.png`
  - `/tmp/253a_003_009-004.png`
  - `/tmp/253a_003_009-005.png`
  - `/tmp/253a_003_009-006.png`
  - `/tmp/253a_003_009-007.png`
  - `/tmp/253a_003_009-008.png`
  - `/tmp/253a_003_009-009.png`
- Operational transcription cross-check:
  - `transcription/tex/253a/foundations.tex`

## Source Content Checked

- Free relativistic particle Hilbert space, vacuum, sharp one-particle states,
  and noninteracting multi-particle states.
- Creation and annihilation operators, delta normalization, and free
  Hamiltonian \(H_0\).
- Formal interacting Hamiltonian \(H=H_0+H_{\mathrm{int}}\) and the need to
  impose the Poincare algebra and locality as part of the same construction.
- Causality light-cone figure and the exclusion of spacelike signaling.
- Local field operators \(\widehat\phi(x)\), with \(x^\mu\) as spacetime
  parameters rather than operators.
- Poincare transformation \(x\mapsto\Lambda x+a\), unitary implementation,
  group law, infinitesimal generators, and Lie algebra.
- Microcausality \([\widehat\phi(x),\widehat\phi(y)]=0\) for
  \((x-y)^2>0\).
- Free scalar field construction, invariant mass-shell measure, commutator
  calculation, Lorentz-frame reduction to equal time, and odd-integrand
  argument.
- Interacting-theory postulates: Hilbert space, Poincare symmetry,
  Poincare-invariant vacuum, and local fields obeying covariance and
  microcausality.

## Manuscript Changes

- `monograph/tex/volumes/volume_i/chapter02_quantum_mechanics_relativity_and_locality.tex`
  - Added the Poincare group law and unitary representation law.
  - Added the source noncovariant creation/annihilation normalization
    \(\mathfrak a_{\vec p}\), sharp momentum kets, and the corresponding
    \(H_0,\vec P_0\).
  - Added a positive formulation of the formal \(H_0+H_{\mathrm{int}}\)
    interaction question, tying Hamiltonian kernels to boosts and locality.
  - Added `fig:causal-lightcone-local-operation`, then adjusted labels after a
    rendered check.
  - Added the noncovariant free-field formula and a covariance verification
    from second quantization of the one-particle representation.
- `monograph/tex/volumes/volume_i/chapter03_local_field_operators_poincare_covariance_and_microcausality.tex`
  - Added the explicit convention that the point \(x\) in \(\widehat\Phi_A(x)\)
    is a spacetime label, not a Hilbert-space operator.
- Planning ledgers and chapter dossiers updated.

## Verification Run

- `tools/build_monograph.sh`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `git diff --check`: clean.
- Rendered manuscript pages inspected:
  - `/tmp/qft_253a_003_009_cert-048.png`: source normalization and formal
    interaction material.
  - `/tmp/qft_253a_003_009_cert2-049.png`: causal light-cone figure after
    label adjustment.
  - `/tmp/qft_253a_003_009_cert2-050.png`: noncovariant free-field formula,
    covariance verification, and microcausality derivation.
  - `/tmp/qft_253a_003_009_cert2-051.png`: field-coordinate convention in
    Chapter 3.
