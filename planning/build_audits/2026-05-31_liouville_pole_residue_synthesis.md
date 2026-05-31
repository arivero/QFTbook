# Liouville Pole-Residue Synthesis Pass

Date: 2026-05-31

Scope:
- `monograph/tex/volumes/volume_v/chapter13_liouville_cft.tex`
- `planning/chapter_dossiers/volume_v/chapter13_liouville_cft.md`

Purpose:
- Address GitHub issue #702 by making explicit the logical mechanism that
  connects the Seiberg domain, the weak-coupling zero-mode divergence,
  Coulomb-gas screening integrals, and the dual \(b\leftrightarrow b^{-1}\)
  screening family.

Mathematical change:
- Added a new subsection, "Pole-Residue Structure of Liouville Correlators",
  before the BPZ/degenerate-screening block.
- Introduced
  \[
    \varepsilon_\Sigma(\boldsymbol\alpha)
    =
    \sum_i\alpha_i-\frac Q2\chi(\Sigma)
  \]
  as the constant-mode convergence coordinate.
- Identified the Seiberg-domain condition
  \(\operatorname{Re}\varepsilon_\Sigma>0\) with convergence of the
  \(\phi_0\to-\infty\) zero-mode tail.
- Explained that the meromorphic correlator has pole hyperplanes
  \(\varepsilon_\Sigma=-Nb\) whose residues are represented by
  \(N\) insertions of \(V_b\), and dual pole hyperplanes
  \(\varepsilon_\Sigma=-\widehat N/b\) represented by
  \(\widehat N\) insertions of \(V_{1/b}\).
- Rewrote the \(C_-(\alpha)\) screening lemma so the one-screening integral
  is described as the residue at the single-screening pole, with higher
  screenings assigned to distinct pole hyperplanes.
- Rewrote the dual-screening lemma so \(V_{1/b}\) is the
  \(b\leftrightarrow b^{-1}\) residue family of the DOZZ meromorphic
  correlator, with \(\widetilde\mu\) as a dual-residue normalization.

Formula preservation:
- No displayed numerical constants or gamma-function formulae were changed.
- The Dotsenko-Fateev beta integral, \(C_-(\alpha)\),
  \(\widetilde C_-(\alpha)\), the reflection phase, and the DOZZ formula
  are untouched.

Verification:
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `python3 calculation-checks/liouville_bpz_checks.py`
- `git diff --check`
- `tools/build_monograph.sh`
