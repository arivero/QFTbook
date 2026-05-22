# 2026-05-22 253b Bound States, Partial Waves, and Resonance Opening Audit

## Source Block

- Handwritten source: `references/253b lecture notes 2023.pdf`, pp. 13--18.
- Rendered trace checked:
  - `monograph/tex/build/source_visual_trace/253b_trace-013.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-014.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-015.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-016.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-017.png`
  - `monograph/tex/build/source_visual_trace/253b_trace-018.png`
- Monograph homes:
  - `monograph/tex/volumes/volume_ii/chapter03_bound_states_from_exchange_amplitudes.tex`
  - `monograph/tex/volumes/volume_i/chapter14_cross_sections_partial_waves_and_unitarity.tex`
  - `monograph/tex/volumes/volume_ii/chapter04_unstable_particles_self_energies_and_resonances.tex`

## Verification Notes

- The one-dimensional scattering convention is now explicit:
  \(\psi_k^{\rm in}\sim e^{-ikx}+S(k)e^{ikx}\) and
  \(\psi_k^{\rm out}=S(k)^{-1}\psi_k^{\rm in}\).
- The bound-state analytic continuation follows the handwritten argument:
  at \(k=i\alpha\), the growing coefficient is \(S(i\alpha)^{-1}\), so a
  pole of \(S(k)\) on the positive imaginary axis gives a normalizable
  bound-state solution.
- A short-range potential figure was added to match the source-page picture
  before the existing \(k\)- and \(E_{\rm nr}\)-plane pole diagram.
- The relativistic partial-wave normalization from the source is now stated
  in Volume II, including the delta-normalized partial-wave state,
  \(\mathcal N(E)=(2E/(k\omega_1\omega_2))^{1/2}\) for identical scalar
  bosons, the even-\(\ell\) restriction, and the elastic component
  \(S_\ell(E)\).
- The scalar-QED spin-one channel example is included as a pole-and-residue
  statement: the scalar-antiscalar numerator is proportional to
  \(4k^2P_1(\cos\theta)\).
- The above-threshold opening in the resonance chapter now separates the
  tree-level real-axis pole from the exact physical-axis partial wave, whose
  boundedness follows from unitarity. The resonance is stated as a pole of
  the analytic continuation through the threshold cut.
- The one-dimensional resonance discussion now records the source-page
  point that purely outgoing flux with uniform time decay is not a
  normalizable Hilbert-space eigenvector.

## Checks

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/build_monograph.sh`: passed; compiled
  `monograph/tex/main.pdf` at 425 pages with clean log scan.
- Targeted PDF render passed for the changed bound-state and resonance pages:
  `pdftoppm -png -f 176 -l 180 -r 170 monograph/tex/main.pdf
  /tmp/qft_253b_bound_resonance_final`.
