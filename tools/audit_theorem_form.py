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
    r"finite normal Gaussian factor|"
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
    r"Tree Compton cross-section functional|"
    r"Dyson resummation of exact two-point insertions|"
    r"Two-dimensional conformal Killing fields|"
    r"Spectral meaning of the horizon functional|"
    r"Conformal Borel map for one negative cut|"
    r"Static spin and flavor symmetry|"
    r"Gauge invariance of the dipole matrix element|"
    r"Stress-tensor insertion from a small metric perturbation|"
    r"Dual net and the Haag-duality gap|"
    r"Mass-shell support of free solutions|"
    r"Functoriality of finite Berezin pushforward|"
    r"Octet and decuplet first-order mass relations|"
    r"Free residual dispersion and the kinetic operator|"
    r"Gauge invariance of the spatial bilocal|"
    r"Gauge invariance of the subtracted TMD operator|"
    r"Euclidean recursion preserves the Clifford relations|"
    r"Tree-level GIM diagonality|"
    r"IRC safety of generalized|"
    r"Component RTT relation|"
    r"Determinantal solution of the QQ-system|"
    r"Hirota from Pluecker identities|"
    r"Baxter product wavefunctions|"
    r"Field-strength matrix element descends to the helicity line|"
    r"Auxiliary-vector polarization projector|"
    r"Nilpotency from the master equation|"
    r"Origin of the finite-density sign problem|"
    r"Supercharge decomposition in the Donaldson twist|"
    r"Power counting for .*Phi|"
    r"Cutoff behavior of the tadpole|"
    r"Scalar one-point selection rule|"
    r"Principal-chiral Lax equivalence|"
    r"Vertex OPE and scaling dimension|"
    r"Constant-map A-model algebra|"
    r"Descent of Wilson charges|"
    r"Connected-manifold formula|"
    r"Pair-of-pants selection rule|"
    r"Residual quotient symmetry after normal-subgroup gauging|"
    r"Finite condensate criterion|"
    r"Finite condensate confinement criterion|"
    r"Elementary .*BF_2.* boundary states|"
    r"ADHM dimension count|"
    r"One-box fixed points from the tangent character|"
    r"Parity criterion for .*SU|"
    r".*N=4.*pure.*N=2.*matching|"
    r".*N=4.*pure.*N=1.*matching|"
    r"Finite .*SU.*heat-bath.*overrelaxation invariance|"
    r"Parity and the opposite levels|"
    r"Abelian Chern--Simons boundary algebra|"
    r"KW anomaly and superpotential .*R.*charge|"
    r"Conditional determination by complete .*data|"
    r"Separated universality|"
    r"Local universality from RG coordinates|"
    r"Conditional .*universality|"
    r"Detailed balance for the finite Ising Metropolis chain|"
    r"Detailed balance for the finite .*Z_2.* gauge chain|"
    r"Finite .*SU\\(3\\).* subgroup-update invariance|"
    r"HMC Metropolis correction at finite regulator|"
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
    r"|Curvature of the sausage target"
    r"|Closure under one-loop Ricci flow"
    r"|Integrated sausage Ricci trajectory"
    r"|Well-defined chamber extension"
    r"|Three-particle consistency"
    r"|Exact-sequence proof of an operator .*TQ.* relation"
    r"|Finite-chain SoV reduction under simple-spectrum hypotheses"
    r"|Trace sum rule"
    r"|Form-factor version of the trace sum rule"
    r"|Finite-volume golden-rule limit"
    r"|Two-particle decay width in .*1\\+1.* dimensions"
    r"|Linear potential in the induced two-dimensional gauge sector"
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
