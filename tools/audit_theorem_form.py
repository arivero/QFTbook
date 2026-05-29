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
    r"|Large-.*u.* power balance"
    r"|Large-.*u.* characteristic determinant"
    r"|Large-.*u.* coefficient products"
    r"|Weak .*P.*mu.* elimination before the Baxter equation"
    r"|.*T.*gauge compatibility with the magic row"
    r"|Consistency of the .*P.*mu.* discontinuity"
    r"|Monodromy recursion for .*mu"
    r"|Unimodular .*P.*Q.* bridge"
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
            if not re.search(r"\\begin\{proof\}", line_text):
                continue
            prev = idx - 1
            while prev >= 0 and not lines[prev].strip():
                prev -= 1
            if prev >= 0 and lines[prev].strip() == r"\end{definition}":
                failures.append(
                    f"{path}:{idx + 1}: proof environment follows a definition"
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
