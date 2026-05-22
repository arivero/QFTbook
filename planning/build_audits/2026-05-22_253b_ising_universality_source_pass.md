# 2026-05-22 253b Ising Universality Source Audit

## Scope

- Source block: `references/253b lecture notes 2023.pdf`, pages 136--146.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, around the statistical
  Ising model and universality block.
- Additional comparison:
  `references/253b transcribed lecture notes.tex`, around the same source
  block.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter15_the_statistical_ising_model_and_universality.tex`.

## Source Content Checked

- The statistical Ising model as a spin system on a \(D\)-dimensional lattice
  in thermal equilibrium, including the \(D=2\) square-lattice picture,
  \(s_x=\pm1\), diagonal spin operators, and nearest-neighbor Hamiltonian.
- The explicit warning that the finite spin Hilbert space and Hamiltonian are
  not the Hilbert space and Hamiltonian of the emergent QFT.
- The Boltzmann distribution, partition function, maximum-entropy
  characterization, symmetric-rate entropy monotonicity statement, and thermal
  trace formula for spin correlators.
- The low-temperature two-fold ground-state degeneracy, spontaneous
  magnetization, disappearance of spontaneous magnetization above the Curie
  temperature, and long-distance spin-correlator regimes below, at, and above
  \(T_c\).
- The critical behavior
  \(f(r)\sim r^{-2\Delta_\sigma}\) and
  \(\xi(T)\sim |T-T_c|^{-\nu}\), with the quoted \(D=2\) and \(D=3\)
  values of \(\Delta_\sigma\) and \(\nu\).
- The near-critical scaling-limit formula for lattice spin correlators with
  \(L/\xi(T)\) held fixed and a spin-field renormalization factor.
- The critical \(m=0\) limit, the Ising fixed point/CFT identification, and
  the operator relations \(\sigma\leftrightarrow\phi\) and
  \(\varepsilon\leftrightarrow[\phi^2]\), including
  \(\Delta_\varepsilon=D-1/\nu\).
- The generalized continuous-spin Ising model with single-site potential
  \(P(s)\), the Euclidean lattice action
  \[
    S=\frac{\beta}{2}\sum_{\langle xy\rangle}(s_x-s_y)^2
      +\sum_x(P(s_x)-\beta D s_x^2),
  \]
  and the double-well potential picture.
- The Brillouin-zone Fourier transform, periodic momentum-space field,
  finite UV cutoff \(|k^\mu|\le\pi\), and small-momentum expansion of
  \(\sum_\mu|e^{ik_\mu}-1|^2\).
- The scalar long-distance action with continuum kinetic term,
  \(\mathbb Z_2\)-even potential, higher-derivative lattice-anisotropic terms,
  and finite non-Euclidean-invariant cutoff.
- The RG picture comparing continuum massless \(\phi^4\), the critical Ising
  lattice model, irrelevant Wilsonian deformations, mass/temperature
  deformations, and massive phases.
- The fixed-point statement that, in the scalar deformation sector after
  removing identity, descendants, and metric deformations, the relevant Ising
  directions are the spin field \(\sigma\) and energy field \(\varepsilon\).
- The irrelevance estimate \(u_I\mu^{\Delta_I-D}\to0\) for
  \(\Delta_I>D\), the temperature perturbation
  \(\int\dd^Dx\,u_t\varepsilon(x)\), the local relation
  \(u_t=c_T(T-T_c)+O((T-T_c)^2)\), and
  \(\nu=1/(D-\Delta_\varepsilon)\).

## Manuscript Changes

- Added a reconstruction caveat after the scaling-limit formula: the limit
  first defines Euclidean separated-point Schwinger functions, and a
  Lorentzian QFT Hilbert space is obtained only after reconstruction
  hypotheses; it is not the finite spin-trace space.
- Refined the relevant-operator statement so that the "only two" claim is
  explicitly about scalar action deformations after excluding identity,
  total derivatives, equation-of-motion descendants, and metric deformations.
- Improved the spin-correlator regime figure by giving curve labels white
  backgrounds after the rendered check showed labels too close to plotted
  curves.
- Confirmed that the lattice scalar path integral uses the Brillouin-zone
  cutoff and derivative expansion, with the \(k_\mu^4\) term represented by
  the corresponding higher-derivative operator.
- Updated the chapter dossier and the no-skip coverage register to mark this
  source block as certified.

## Rendered Check

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/253b_136_146-136.png` through `/tmp/253b_136_146-146.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_ising_cert-291.png` through `/tmp/qft_ising_cert-299.png`.
- Visual checks covered the finite ensemble/trace figure, correlator-regime
  figure, scaling-limit figure, generalized scalar path-integral figure, and
  universality/relevant-coordinate figure.  No cropped equations, overlapping
  labels, or missing source-level figure elements were found in the audited
  pages after the correlator-label adjustment.

## Verification

- `tools/build_monograph.sh` completed cleanly after the TeX edits.
- The strict monograph text audit inside the build completed cleanly.
- `tools/audit_monograph_text.sh` completed cleanly.
- `git diff --check` completed cleanly.

This promotes handwritten 253b pages 136--146 to certified coverage after the
statistical-Ising and universality source audit.
