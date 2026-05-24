# Issue #256 QED Charged Infraparticle Pass

## Scope

- Oldest active GitHub issue: `#256`, on the asymptotic Hilbert-space
  discussion in
  `monograph/tex/volumes/volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex`.
- Required repair: state that charged sectors of four-dimensional QED are not
  ordinary charged-particle Fock sectors, name Buchholz's theorem and related
  infraparticle constructions, and explain that the Faddeev--Kulish dressing
  changes representation when the infrared cutoff is removed.

## Content Added

- Added a new section, "Charged Asymptotic Sectors and Infraparticles."
- Defined the large-radius smeared electric flux
  \[
    \Phi_R(f)=\int_{S^2}d\Omega\,R^2 f(\mathbf n)n_iE^i(0,R\mathbf n)
  \]
  and its limiting flux functional \(\Phi_\infty(f)\).
- Explained from locality and Gauss' law that limiting electric flux is
  superselected; the constant test function gives total electric charge and
  nonconstant test functions record angular Coulomb-field data.
- Stated the Buchholz infraparticle obstruction: nonzero abelian gauge charge
  is incompatible with a sharp Wigner mass-shell particle sector, and charged
  particle weights with different velocities carry different asymptotic flux
  data.
- Named Buchholz, Fröhlich--Morchio--Strocchi, Faddeev--Kulish, and
  Buchholz--Dybalski in a reader-facing footnote.
- Added the boosted Coulomb angular flux density
  \[
    \mathcal E_{g,\mathbf v}(\mathbf n)
    =
    \frac{g}{4\pi}
    \frac{1-|\mathbf v|^2}{(1-\mathbf v\cdot\mathbf n)^2}.
  \]
- Computed the one-photon Hilbert norm of the leading soft profile:
  \[
    \|f_p\|_\gamma^2
    \sim
    C(p,g)\int_0^\Lambda \frac{d\omega}{\omega},
  \]
  showing that the zero-cutoff Faddeev--Kulish cloud is not a photon-Fock
  vector.
- Updated the dressed-state paragraph to say explicitly that finite-cutoff
  \(\mathcal W_p\) is a Fock Weyl operator, while removing the cutoff is the
  representation-changing step.
- Updated the chapter dossier.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
