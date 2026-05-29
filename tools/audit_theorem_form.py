#!/usr/bin/env python3
"""Audit theorem-family headings and proof-environment placement.

This is deliberately narrow.  It catches theorem/proposition/lemma/corollary
titles of the form "X is not Y" or "X does not prove Y", which should usually
be a remark or status paragraph unless a genuine counterexample or obstruction
is being proved.  It also rejects a proof environment attached directly to a
definition, since convention checks and definitional consequences must be
written in prose or stated as separate theorem-family claims.

It does not try to judge proof quality; it flags presentation patterns that
create fake-looking proofs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "monograph" / "tex" / "volumes"

THEOREM_ENV_RE = re.compile(
    r"\\begin\{(theorem|proposition|lemma|corollary)\}(?:\[([^\]]*)\])?",
)

STATEMENT_ENV_RE = re.compile(
    r"\\begin\{(assumption|hypothesis|theorem|proposition|lemma|corollary)\}(?:\[([^\]]*)\])?",
)

REVIEWED_ASSUMPTION_THEOREM_NEIGHBORS = {
    (
        "volume_ii/chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex",
        "Higher-dimensional angular tube",
        "proposition",
        r"Conditional angular counting in \(D\) spacetime dimensions",
    ),
    (
        "volume_ii/chapter15_the_statistical_ising_model_and_universality.tex",
        "Separated spin scaling limit",
        "proposition",
        "Ferromagnetic nearest-neighbor models are reflection positive",
    ),
    (
        "volume_ii/chapter16_wilsonian_effective_field_theory.tex",
        "Finite-order BPHZ--Wilsonian matching estimates",
        "theorem",
        "Finite-order BPHZ--Wilsonian matching",
    ),
    (
        "volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex",
        "Leading-logarithmic dipole/BFKL evolution setup",
        "proposition",
        "Mellin eigenvalue of the leading BFKL kernel",
    ),
    (
        "volume_iii/chapter05_conformal_charges_and_ward_identities.tex",
        "Vacuum and large-boundary behavior",
        "proposition",
        "Local conformal-current Ward identity",
    ),
    (
        "volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex",
        "Small-circle affine-Toda input",
        "proposition",
        "Local index of a nondegenerate chiral critical point",
    ),
    (
        "volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex",
        "Large-spin BES scaling regime",
        "proposition",
        "Zhukovsky Fourier transform",
    ),
    (
        "volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex",
        r"Weak-coupling regularity of the \(SL(2)\) QSC",
        "lemma",
        "Half-integer digamma primitive",
    ),
    (
        "volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex",
        "Field-theoretic matching to the Gieseker integral",
        "theorem",
        "Planar circular Wilson loop from the Gaussian model",
    ),
    (
        "volume_xi/chapter09_stochastic_quantization_singular_spde.tex",
        r"\(\Phi^4_2\) stochastic-quantization assembly inputs on the torus",
        "theorem",
        r"\(\Phi^4_2\) stochastic-quantization assembly on the torus",
    ),
}

NEGATIVE_SCOPE_TITLE_RE = re.compile(
    r"\b("
    r"does not|do not|is not|are not|cannot|"
    r"not a|not an|not the|not supply|not imply|not prove|no baseline"
    r")\b",
    re.IGNORECASE,
)

CALCULATION_WRAPPER_TITLE_RE = re.compile(
    r"\b("
    r"check|checks|bookkeeping|"
    r"One-loop tadpole self-energy and cutoff growth|"
    r"Two-loop sunset insertion|"
    r"One-loop pole shift and mass-coordinate prescription|"
    r"Tree-level .*phi.* amplitude after LSZ|"
    r"Representative QED Feynman rules|"
    r"Tree-level Compton hard kernel|"
    r"One-instanton test of the ADS numerator and denominator|"
    r"Pure-SYM one-instanton zero-mode test|"
    r"Constant-seed covering-count test|"
    r"Leading Konishi wrapping integral|"
    r"One-loop dimension from the weak QSC|"
    r"Finite-cutoff local counterterm calculation|"
    r"Mass-source and Konishi identities in massive SQCD|"
    r"BES equation from the large-spin ABA|"
    r"Collapsed-cut digamma package|"
    r"Small-spin QSC slope|"
    r"Local intertwining and block-unitarity constraints|"
    r"Single level-III nesting step|"
    r"Weak limit of the rank-one ABA orientation|"
    r"Covariance of the free scalar field|"
    r"Finite-dimensional Gaussian source functional|"
    r"Infinitesimal translation covariance|"
    r"Cauchy data determine the free solution|"
    r"Infinitesimal stress-tensor transformation|"
    r"Schwarzian cocycle|"
    r"Inversion of scalar and spin primaries|"
    r"Positivity of the finite principal-value matrix|"
    r"Integer-power extrapolation with explicit weights|"
    r"Largest-time cancellation|"
    r"Source-response kernel from .* differentiation|"
    r"Finite closed-time-path constraints|"
    r"Finite trace constraints|"
    r"comparison algebra|"
    r"finite algebra of .*comparisons|"
    r"exact finite.*GEVP extraction|"
    r"Richardson cancellation|"
    r"(?:finite )?normal Gaussian factor|"
    r"Fixed-point formula in the .*S\\^2.* model|"
    r"localization deformation identity|"
    r"two-dimensional Wess--Zumino action|"
    r"free scalar thermal Green function|"
    r"BCFW shift preserves|"
    r"spectral extraction of the finite-lattice static energy|"
    r"Airy transform of a cubic grand potential|"
    r"Hirota factorization in the one-row T-gauge|"
    r"Veneziano residue and finite-spin exchange|"
    r"ambient transformations and Poincare-patch formulae|"
    r"rank-one conifold quotient|"
    r"Rank-one ABJM sphere integral|"
    r"Leading phase-space coefficient|"
    r"connected Green functions are source cumulants|"
    r"little-group translations are polarization shifts|"
    r"identification with .*so|"
    r"Einstein-cylinder cover|"
    r"First QED term|"
    r"Exact heat-bath detailed balance|"
    r"Euler--Lagrange equation for a scalar field|"
    r"Schwartz triple and weak delta kernels|"
    r"Null-translation matrices|"
    r"Inversion is conformal|"
    r"GKO coset stress tensor and central charge|"
    r"Regulated meaning of the configuration path integral|"
    r"Universal-cover necessity|"
    r"Noncoincident insertions and contact coordinates|"
    r"\\(SU\\(2\\)\\) subgroups generate \\(SU\\(3\\)\\)|"
    r"Projective-channel unitarity identities|"
    r"Large-\\(N\\) glueball width counting|"
    r"Leading connected four-point Green function|"
    r"Covariance of Wightman distributions|"
    r"Isotony and graded locality for polynomial field algebras|"
    r"First variational identity|"
    r"First-order Noether charges as phase-space generators|"
    r"Canonical stress tensor from translations|"
    r"Gaussian elimination of quadratic momenta|"
    r"Gaussian functional source identity|"
    r"Gaussian integration by parts|"
    r"Stress tensor of a real scalar field|"
    r"Minimal scalar Hilbert tensor|"
    r"Euclidean boundary value gives the time-ordered function|"
    r"Heisenberg field and invariant mass-shell normalization|"
    r"Two-body phase-space reduction in four dimensions|"
    r"Free Dirac propagator as Feynman inverse|"
    r"Maxwell action and Euler--Lagrange equation|"
    r"Connected scattering kernels|"
    r"Finite-regulator Gaussian pushforward|"
    r"Legendre Hessian identity|"
    r"Yang--Mills variation in the trace-form convention|"
    r"Callan--Symanzik equation|"
    r"Insertion Callan--Symanzik equation|"
    r"Shifted representation and tadpole condition|"
    r"Functional Schwinger--Dyson identity|"
    r"Simple-pole Stokes jump|"
    r"Factorial moment in a running-coupling model|"
    r"BPST sector in the trace-delta convention|"
    r"Shallow .*S.*wave bound-state effective-range chart|"
    r"Support test by multiplication|"
    r"Associativity of the ZF creation algebra|"
    r"Finite-channel convergence criterion|"
    r"Verlinde formula from modular diagonalization|"
    r"Reflection positivity under split local interactions|"
    r"Closedness of reflection positivity|"
    r"Linear finite-scale tuning exponents|"
    r"\\(Q\\)-exact deformation independence|"
    r"Associativity from the splitting axiom|"
    r"Continuum flow preserves Chern--Weil charge|"
    r"Holomorphic decoupling equation|"
    r"Holomorphic scale matching across a massive threshold|"
    r"Gauss-law annihilation of gauge charge|"
    r"Kernel bounds imply stochastic coordinate moments|"
    r"Surface selection by Haar projection|"
    r"Ward identity from diffeomorphism covariance|"
    r"Screening equivalence of center-sensitive charges|"
    r"Gauge equivalence of Cartan surface singularities|"
    r"Tree Compton cross-section functional|"
    r"Drell--Yan leading-power kinematics|"
    r"Leading soft Wilson-line decoupling identity|"
    r"Tree-level singlet color factor|"
    r"Color factor of one-gluon exchange between two quarks|"
    r"Dyson resummation of exact two-point insertions|"
    r"NSVZ beta function as a coordinate identity|"
    r"Saturated pure-SYM Berezin coefficient|"
    r"Level-one descendant Gram positivity|"
    r"Two-dimensional conformal Killing fields|"
    r"Spectral meaning of the horizon functional|"
    r"Conformal Borel map for one negative cut|"
    r"Static spin and flavor symmetry|"
    r"Gauge invariance of the dipole matrix element|"
    r"Detector positivity from ANEC|"
    r"Displacement criterion|"
    r"Finite unitarity model for Glauber cancellation|"
    r"Conformal covariance of the transverse kernel|"
    r"Stress-tensor insertion from a small metric perturbation|"
    r"Dual net and the Haag-duality gap|"
    r"Mass-shell support of free solutions|"
    r"Axial-gauge quadratic inverse|"
    r"Covariant-gauge quadratic inverse|"
    r"Functoriality of finite Berezin pushforward|"
    r"Octet and decuplet first-order mass relations|"
    r"Heavy-baryon spin average removes the chromomagnetic coordinate|"
    r"Free residual dispersion and the kinetic operator|"
    r"Gauge invariance of the spatial bilocal|"
    r"Gauge invariance of the subtracted TMD operator|"
    r"Scheme covariance of finite matching kernels|"
    r"Euclidean recursion preserves the Clifford relations|"
    r"Curvature covariance and gauge-invariant densities|"
    r"Auxiliary .*D.*field elimination|"
    r"Gauge invariance and .*F.*term equations|"
    r"Tree-level GIM diagonality|"
    r"IRC safety of generalized|"
    r"Witten--Veneziano mass formula|"
    r"Component RTT relation|"
    r"Determinantal solution of the QQ-system|"
    r"Hirota from Pluecker identities|"
    r"Baxter product wavefunctions|"
    r"Field-strength matrix element descends to the helicity line|"
    r"Auxiliary-vector polarization projector|"
    r"Nilpotency from the master equation|"
    r"Origin of the finite-density sign problem|"
    r"Supercharge decomposition in the Donaldson twist|"
    r"Pointwise energy identity|"
    r"Power counting for .*Phi|"
    r"Cutoff behavior of the tadpole|"
    r"Scalar one-point selection rule|"
    r"Principal-chiral Lax equivalence|"
    r"Vertex OPE and scaling dimension|"
    r"Constant-map A-model algebra|"
    r"Descent of Wilson charges|"
    r"Homological invariance of descended observables|"
    r"Connected-manifold formula|"
    r"Pair-of-pants selection rule|"
    r"Residual quotient symmetry after normal-subgroup gauging|"
    r"Finite condensate criterion|"
    r"Finite condensate confinement criterion|"
    r"Gauge-Higgs analytic corridor|"
    r"Condensate branches and source normalization|"
    r"SQCD specialization of the NSVZ coordinate relation|"
    r"VY glueball superpotential|"
    r"Uniqueness of the quantum modification|"
    r"KW local conformal manifold from rank one|"
    r"SQCD central charges and free-field comparison|"
    r"Affine-Toda critical-point count|"
    r"Pure .*index and condensate relation|"
    r"KW .*F.*term equations|"
    r"Cascade rank step|"
    r"Elementary .*BF_2.* boundary states|"
    r"ADHM dimension count|"
    r"One-box fixed points from the tangent character|"
    r"Parity criterion for .*SU|"
    r".*N=4.*pure.*N=2.*matching|"
    r".*N=4.*pure.*N=1.*matching|"
    r"Five-dimensional coupling convention|"
    r"Unpunctured class-.*S.* Coulomb-base dimension|"
    r"Hexagon scalar Watson factor|"
    r"Weak and strong expansions of .*B.*lambda|"
    r"Pentagon OPE from the defect spectral resolution|"
    r"Finite .*SU.*heat-bath.*overrelaxation invariance|"
    r"Parity and the opposite levels|"
    r"Abelian Chern--Simons boundary algebra|"
    r"Quadratic Chern--Simons action in light-cone gauge|"
    r"Light-cone Chern--Simons current kernel|"
    r"Planar color reduction of the light-cone kernel|"
    r"KW anomaly and superpotential .*R.*charge|"
    r"Compact scalar radius inversion|"
    r"Coulomb critical equation|"
    r"Jacobian quotient from the .*B.*type differential|"
    r"Conditional determination by complete .*data|"
    r"Separated universality|"
    r"Local universality from RG coordinates|"
    r"Conditional .*universality|"
    r"Detailed balance for the finite Ising Metropolis chain|"
    r"Detailed balance for the finite .*Z_2.* gauge chain|"
    r"Finite .*SU\\(3\\).* subgroup-update invariance|"
    r"HMC Metropolis correction at finite regulator|"
    r"Exact finite-.*N.* variance identity|"
    r"Finite-volume phase-reweighting variance bound|"
    r"Leading strong-coupling tube in pure Yang--Mills|"
    r"One-loop Polyakov-holonomy potential|"
    r"Static HTL polarization and Debye mass|"
    r"Clogston scale in the controlled two-species model|"
    r"HDL magnetic leading-log gap equation|"
    r"CFL Higgs screening mass matrix|"
    r"Fermi-surface measure and density of states|"
    r"Leading logarithmic cold dense quark self-energy|"
    r"Correlated delete-one-block jackknife for smooth ratios"
    r"|Collins--Soper consistency"
    r"|Retarded boundary value and sign convention"
    r"|GMOR as a pole-saturation consequence"
    r"|Heat-kernel smoothing estimate"
    r"|Finite functional exclusion certificate"
    r"|Positivity criterion for a BRST doublet sector"
    r"|Coefficientwise perturbation at fixed regulator"
    r"|Descendant transformation laws from primary data"
    r"|Bulk gluing gives the anomaly line"
    r"|Wess--Zumino consistency for Weyl anomalies"
    r"|Two-point Feynman prescription from ordered tubes"
    r"|Isolated shell as a one-particle subrepresentation"
    r"|Euclidean long-time projection to a gapped ground state"
    r"|Endpoint screening bounds the static energy"
    r"|Diffeomorphism Ward identity for metric stress tensors"
    r"|Positivity of the switched detector response"
    r"|Conditional finite-coordinate Wilsonian continuum limit"
    r"|Two-winding expansion of the vacuum energy"
    r"|Crossing scalar convention algebra"
    r"|Mirror-TBA node and source inventory"
    r"|Finite-chain ABA--Q--SoV comparison, scoped form"
    r"|Matrix unitarity and the breather pole locations"
    r"|Soliton--breather unitarity, crossing, and pole locations"
    r"|Gross--Neveu scalar unitarity identity"
    r"|Principal-chiral scalar unitarity identity"
    r"|Neutral scalar block"
    r"|Fermi exchange from the Mandelstam line"
    r"|Supersphere Ricci coefficient"
    r"|Projective-supermodel one-loop identity"
    r"|Constant-curvature radius flow"
    r"|Cigar central charge, weights, and spin"
    r"|Curvature of the sausage target"
    r"|Closure under one-loop Ricci flow"
    r"|Integrated sausage Ricci trajectory"
    r"|RG time versus Hamilton Ricci flow"
    r"|One-loop Weyl identities for the bell and cigar"
    r"|Well-defined chamber extension"
    r"|Three-particle consistency"
    r"|Exact-sequence proof of an operator .*TQ.* relation"
    r"|Finite-chain SoV reduction under simple-spectrum hypotheses"
    r"|Finite-sector model convergence from coordinate estimates"
    r"|Negative-sector model convergence from scale-summed coordinates"
    r"|Trace sum rule"
    r"|Form-factor version of the trace sum rule"
    r"|Finite-volume golden-rule limit"
    r"|Two-particle decay width in .*1\\+1.* dimensions"
    r"|Linear potential in the induced two-dimensional gauge sector"
    r"|Zhukovsky form of the dispersion"
    r"|Zhukovsky monodromy along the crossing path"
    r"|Dressing unitarity from charge antisymmetry"
    r"|DHM pole lattice and admissible local continuations"
    r"|Local crossing of the BES phase"
    r"|Jump data from the Cauchy transform"
    r"|Mirror Zhukovsky sheet parametrization"
    r"|One auxiliary wing of the Y-system"
    r"|Data lost by the .*s.*kernel inverse"
    r"|Konishi weak-density rationalization"
    r"|Pole structure of the Konishi weak density"
    r"|Magic-sheet continuation of the one-row gauge"
    r"|Fermionic product and central-row telescope"
    r"|Fermionic-node asymptotics"
    r"|Local T-hook algebra behind the .*P.*mu.* bridge"
    r"|Dimension exponent of .*mu"
    r"|Dual .*Q.*omega.* transport"
    r"|Large-.*u.* power balance"
    r"|Large-.*u.* characteristic determinant"
    r"|Large-.*u.* coefficient products"
    r"|Weak .*P.*mu.* elimination before the Baxter equation"
    r"|.*T.*gauge compatibility with the magic row"
    r"|Consistency of the .*P.*mu.* discontinuity"
    r"|Monodromy recursion for .*mu"
    r"|Unimodular .*P.*Q.* bridge"
    r"|Finite-density ABA counting equation"
    r"|Associativity of finite defect fusion"
    r"|Origin of the Wick coefficients"
    r"|Finite Gibbs traces are KMS"
    r"|Finite-volume spectral detailed balance"
    r"|Weyl variation of the .*R.*2.* counterterm"
    r"|Finite-volume graded-trace identity"
    r"|Finite-volume symmetry basis versus cluster branches"
    r"|Conformal anomaly coefficients"
    r"|Pure .*SU\\(2\\).* one-instanton coefficient"
    r"|Coefficient of abelian inflow"
    r"|Cardy boundary fields from fusion"
    r"|Mass decoupling from .*N_f=N_c\\+1.* to .*N_f=N_c"
    r"|Magnetic .*R.*charge and NSVZ consistency"
    r"|KS .*R.*anomaly remnant"
    r"|Radial Higgs cutoff in the ADS instanton patch"
    r"|Action groupoid cardinality"
    r"|Wrapped strings and Coulomb-branch masses"
    r"|Riemann--Roch count for Hitchin differentials"
    r"|Degree sum for a simple Lie algebra"
    r"|Ising net .*mu.*index and DHR fusion"
    r"|Finite large-.*K.* fit with an explicit remainder amplifier"
    r"|Cardy solution for the diagonal invariant"
    r"|Operator implementation of spectral flow"
    r"|Shear and sound poles"
    r"|Thermal susceptibility integrals"
    r"|Index of the anti-self-dual complex"
    r"|Index of the monopole deformation problem"
    r"|Monopole condensation from the local .*F.*terms"
    r"|Non-abelian Chern--Simons auxiliary elimination"
    r"|Wilson lifting of the naive species"
    r"|Overlap operator satisfies Ginsparg--Wilson"
    r"|Overlap index as spectral asymmetry"
    r"|Peierls bracket from the pAQFT star commutator"
    r"|Lifting a projected RG zero"
    r"|Level-two Liouville null vector"
    r"|Dual level-two null vector and BPZ equation"
    r"|Equivariance of polar link projection"
    r"|Stout smearing is a smooth gauge-covariant link map"
    r"|Borel transform of the subtracted dispersion kernel"
    r"|Partial-wave unitarity circle"
    r"|Tree-level high-density quark action"
    r"|Fermionic trace endpoint signs"
    r"|Harmonic supersymmetric oscillator index"
    r"|Large-field EFT expansion requires a field-domain hypothesis"
    r"|Adjacent spacelike exchange in Wightman functions"
    r"|Charge algebra from the vector-field bracket"
    r"|Global conformal Ward identity from surface deformation"
    r"|K-S data give OS Schwinger functions on flat space"
    r"|Flat-space comparison with OS Schwinger functions"
    r"|Local source-coordinate changes produce contact terms"
    r"|QED as the Abelian Faddeev--Popov specialization"
    r"|Surface deformation of a conserved conformal charge"
    r"|Finite-volume gauge averaging"
    r"|Slab derivation of the gauging-interface fusion"
    r"|Polynomial free-field wedge algebra"
    r"|KW beta-function rank count"
    r"|Rank-one abelian quotient"
    r"|Local descent as the infinitesimal limit of inflow"
    r"|Uniqueness of an admissible angular-momentum interpolation"
    r"|Free Reggeon diffusion kernel"
    r"|Two-Reggeon cut in the free diffusion model"
    r"|Higgs-patch collective-coordinate calculation"
    r"|Yukawa-lifting Berezin determinant on the Higgs patch"
    r"|Electric-magnetic anomaly matching"
    r"|IRC classification of soft-drop outputs"
    r"|Classical chambers for the hypersurface GLSM"
    r")\b",
    re.IGNORECASE,
)


def main() -> int:
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*.tex")):
        text = path.read_text(encoding="utf-8")
        for match in THEOREM_ENV_RE.finditer(text):
            title = match.group(2) or ""
            if not title:
                continue
            if NEGATIVE_SCOPE_TITLE_RE.search(title):
                line = text.count("\n", 0, match.start()) + 1
                failures.append(f"{path}:{line}: {match.group(1)} [{title}]")
            if CALCULATION_WRAPPER_TITLE_RE.search(title):
                line = text.count("\n", 0, match.start()) + 1
                failures.append(
                    f"{path}:{line}: calculation-only wrapper {match.group(1)} [{title}]"
                )

        lines = text.splitlines()
        for idx, line_text in enumerate(lines):
            proof_match = re.search(r"\\begin\{proof\}(?:\[([^\]]*)\])?", line_text)
            if not proof_match:
                continue
            prev = idx - 1
            while prev >= 0 and not lines[prev].strip():
                prev -= 1
            prev_text = lines[prev].strip() if prev >= 0 else ""
            forbidden_statement_endings = {
                r"\end{definition}": "definition",
                r"\end{controlledapproximation}": "controlled approximation",
                r"\end{quotedtheorem}": "quoted theorem",
            }
            if prev_text in forbidden_statement_endings:
                failures.append(
                    f"{path}:{idx + 1}: proof environment follows a "
                    f"{forbidden_statement_endings[prev_text]}"
                )
            if (
                proof_match.group(1) is None
                and prev_text
                and prev_text
                not in {
                    r"\end{theorem}",
                    r"\end{proposition}",
                    r"\end{lemma}",
                    r"\end{corollary}",
                }
            ):
                failures.append(
                    f"{path}:{idx + 1}: unnamed proof is not attached directly "
                    "to a theorem-family statement"
                )

        statements: list[tuple[int, str, str]] = []
        for idx, line_text in enumerate(lines, 1):
            if match := STATEMENT_ENV_RE.search(line_text):
                statements.append((idx, match.group(1), match.group(2) or ""))

        relpath = str(path.relative_to(ROOT))
        for current, following in zip(statements, statements[1:]):
            line, env, title = current
            next_line, next_env, next_title = following
            if env not in {"assumption", "hypothesis"} or next_env not in {
                "theorem",
                "proposition",
                "lemma",
                "corollary",
            }:
                continue
            if next_line - line > 140:
                continue
            key = (relpath, title, next_env, next_title)
            if key in REVIEWED_ASSUMPTION_THEOREM_NEIGHBORS:
                continue
            failures.append(
                f"{path}:{line}: {env} [{title}] is followed {next_line - line} "
                f"lines later by {next_env} [{next_title}]; read the substance and "
                "demote, separate, or add a reviewed exception"
            )

    if failures:
        print("Theorem-form audit failures:", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print("Theorem-form audit clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
