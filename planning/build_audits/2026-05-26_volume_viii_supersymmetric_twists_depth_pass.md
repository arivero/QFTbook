# 2026-05-26 Volume VIII Chapter 7 Supersymmetric Twists Depth Pass

Status: completed and pushed-ready.

## Scope

- Rewrote the supersymmetric twists chapter from a short overview into a
  proof-bearing development.
- Defined twisting as restriction of `Spin(d) x G_R` representations to the
  diagonal subgroup determined by a homomorphism `rho`.
- Developed the curved-manifold background construction through the induced
  R-symmetry bundle `P_R(M)`.
- Defined scalar twisting supercharges and the closure condition
  `Q^2 = gauge + flavor + Lie derivative`.
- Added a regulator-level twist datum, including anomaly, field/BV-space,
  integration-cycle, observable-algebra, and contact-term data.
- Proved the twisted metric-independence criterion from the regulated Ward
  identity and `Q`-exact metric response.
- Computed the four-dimensional `N=2` Donaldson-twist decomposition of
  supercharges into scalar, one-form, and self-dual two-form pieces.
- Decomposed the `N=2` vector multiplet into Donaldson-Witten differential
  forms.
- Proved off-shell closure of the Donaldson-Witten transformations:
  `Q^2=delta_{-phi}`.
- Added the Mathai-Quillen gauge-fermion term that localizes to `F_A^+=0`
  and linked it to the ASD deformation complex.
- Derived the Donaldson descent package from the universal equivariant
  curvature `F_A + psi + phi`.
- Added the two-dimensional `N=(2,2)` charge table identifying the A- and
  B-twist scalar supercharges.

## Calculation Check

- Added `calculation-checks/twisting_representation_checks.py`.
- The check verifies the `SU(2)` Clebsch-Gordan arithmetic behind the
  Donaldson twist, the dimensions of the twisted gaugino form fields, the
  two-dimensional A/B twist scalar-supercharge charge bookkeeping, and the
  Donaldson-Witten `Q^2=delta_{-phi}` closure ledger.

## Verification

- `python3 calculation-checks/twisting_representation_checks.py`
  passed with `All supersymmetric twisting representation checks passed.`
- `python3 -m py_compile calculation-checks/twisting_representation_checks.py`
  passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before this audit note was added.
- First `tools/build_monograph.sh` exposed hyperref bookmark warnings from
  math in section titles; the headings were fixed with `texorpdfstring`.
- Second `tools/build_monograph.sh` completed cleanly, including log scan.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1817`.
