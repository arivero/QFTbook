# Build Audit: Issue 606 Conformal Nets

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Scope: issue #606 / Volume V Chapter 12 conformal-net depth pass.
- Substantive edits:
  - Added an operator-algebraic conformal-net section to
    `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`.
  - Defined interval nets, locality, covariance, positive energy, vacuum
    cyclicity, irreducibility, split property, strong additivity,
    complete rationality, and the `mu`-index.
  - Stated the complete-rational representation-category theorem and the
    Carpi--Kawahigashi--Longo--Weiner strongly-local-VOA theorem as precise
    quoted theorem boundaries.
  - Proved the Ising conformal-net `mu`-index check from the displayed
    quantum dimensions and added an open problem for unqualified VOA/net
    equivalence.
  - Extended `calculation-checks/cft_voa_modular_checks.py` to verify
    the Ising global-dimension / `S_{00}` / `mu`-index arithmetic.
  - Downloaded the CKLW arXiv TeX source into
    `references/02_2d_cft/conformal_nets_cklw_1503_01260/` for local
    theorem-boundary checking.
- Verification completed before commit:
  - `python3 calculation-checks/cft_voa_modular_checks.py`
  - `tools/run_calculation_checks.sh`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `git diff --check`
  - `tools/build_monograph.sh`
