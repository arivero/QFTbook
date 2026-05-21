#!/usr/bin/env python3
"""Generate the QFT monograph volume/chapter skeleton.

This script is intentionally conservative: it creates missing chapter files and
regenerates volume include files, but it never overwrites an existing chapter.
Substantive writing should happen directly in the relevant chapter file.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "monograph" / "tex"


VOLUMES = [
    (
        "volume_i",
        "Fields, Green Functions, And Scattering",
        [
            "What Is Quantum Field Theory?",
            "Quantum Mechanics, Relativity, And Locality",
            "Local Field Operators, Poincare Covariance, And Microcausality",
            "Lagrangian Formalism And Quantum-Mechanical Path Integrals",
            "Correlation Functions, Wick Rotation, And Gaussian Integrals",
            "Relativistic Scalar Fields And Canonical Quantization",
            "Symmetries, Noether Theorem, And Stress Tensors",
            "Scalar Path Integrals And Euclidean Green Functions",
            "Kallen-Lehmann Spectral Representation And Particle Content",
            "Perturbative Green Functions And Feynman Graphs",
            "Lorentzian Green Functions And Analytic Continuation",
            "Haag-Ruelle Scattering Theory",
            "LSZ Reduction And The S-Matrix",
            "Cross Sections, Partial Waves, And Unitarity",
            "Massive Particles With Spin",
            "Spinor Fields, Fermionic Statistics, And Grassmann Path Integrals",
            "Massless Particles, Helicity, And Gauge Redundancy",
            "Maxwell Theory, Constraints, And Gauge Fixing",
            "Quantum Electrodynamics And External States",
            "QED Renormalization And Electromagnetic Form Factors",
        ],
    ),
    (
        "volume_ii",
        "Scattering, Renormalization, And Gauge Dynamics",
        [
            "Recap Of Local QFT, Spectral Data, And Path Integrals",
            "The S-Matrix And LSZ Revisited",
            "Bound States From Exchange Amplitudes",
            "Unstable Particles, Self-Energies, And Resonances",
            "Composite Bound States And Bethe-Salpeter Amplitudes",
            "Analyticity, Crossing, And Landau Singularities",
            "Partial Waves, Dispersion Relations, And High-Energy Bounds",
            "Renormalizability And Local Counterterms",
            "Subdivergences And BPHZ Subtractions",
            "Renormalization Group And Running Couplings",
            "The 1PI Renormalization Group",
            "Renormalized Operators And Minimal Subtraction",
            "Stress-Tensor Trace, Scale Invariance, And Conformal Currents",
            "The Wilson-Fisher Fixed Point And Scaling Operators",
            "The Statistical Ising Model And Universality",
            "Wilsonian Effective Field Theory",
            "Yang-Mills Theory And Matter Fields",
            "Gauge Fixing, Ghosts, And BRST Cohomology",
            "QCD Renormalization, Asymptotic Freedom, And DIS",
            "Chiral Axial Anomalies",
            "Global Anomalies, Spontaneous Symmetry Breaking, And Pions",
            "Infrared Divergences And Inclusive QED",
            "Generating Functionals And The 1PI Effective Action",
        ],
    ),
    (
        "volume_iii",
        "Conformal Field Theory",
        [
            "What Is Conformal Field Theory?",
            "The Ising Fixed Point And Critical Universality",
            "Conformal Symmetry And Conformal Killing Vectors",
            "The Conformal Group And Finite Transformations",
            "Conformal Versus Weyl Invariance",
            "Basic Consequences Of Conformal Symmetry",
            "State-Operator Correspondence",
            "Conformally Coupled Scalars And Local Operators On The Cylinder",
            "Ward Identities And Conformal Charges",
            "Representations Of The Conformal Algebra And Primary Operators",
            "Finite Transformations Of Primary Fields",
            "Consequences Of Unitarity And Unitarity Bounds",
            "Conformal Correlation Functions And Frames",
            "The BPZ Inner Product And Spinning Two-Point Functions",
            "Three-Point And Four-Point Functions",
            "The Operator Product Expansion",
            "Conformal Blocks And Crossing",
            "Projective Lightcone Formalism",
            "Bootstrap Bounds And Numerical Bootstrap",
            "A Survey Of Conformal Field Theories",
            "Two-Dimensional CFT And The Virasoro Algebra",
            "Modular Invariance, Weyl Anomaly, And Sewing",
            "Four-Dimensional Superconformal Field Theory",
            "Large-N Expansion And Spin Chains",
        ],
    ),
    (
        "volume_iv",
        "Mathematical Frameworks And Nonperturbative Definition",
        [
            "Wightman Reconstruction And Its Limits",
            "Euclidean QFT And Osterwalder-Schrader Reconstruction",
            "Algebraic QFT And Local Nets Of Observables",
            "Perturbative AQFT, BRST, And BV Formalism",
            "Factorization Algebras And Perturbative QFT",
            "Lattice Regularization And Continuum Limits",
            "Reflection Positivity And Euclidean Measures",
            "Constructive QFT: What Has Been Built",
            "Statistical Field Theory And Critical Phenomena",
            "Phases Of Quantum Field Theory",
            "Spontaneous Symmetry Breaking In Infinite Systems",
            "Mass Gap, Confinement, And Nonperturbative Dynamics",
            "Nonlinear Sigma Models",
            "Topological Terms And Theta Angles",
            "Defects, Interfaces, And Boundary Conditions",
            "Nonperturbative RG And Functional Methods",
        ],
    ),
    (
        "volume_v",
        "Exact Structures, Dualities, And Extended Operators",
        [
            "Global Forms Of Gauge Groups And Higher-Form Symmetries",
            "Wilson, 't Hooft, And Disorder Operators",
            "Generalized Symmetries And Anomaly Inflow",
            "Non-Invertible Symmetries And Categorical Structures",
            "Boundary And Defect QFT",
            "Boundary And Defect CFT",
            "Supersymmetry And Superconformal Symmetry",
            "Supersymmetric Localization",
            "Topological Twists",
            "Topological Quantum Field Theory",
            "Vertex Operator Algebras And Chiral Algebras",
            "Rational CFT And Modular Tensor Categories",
            "Duality As Equivalence, Correspondence, And Emergence",
            "Large-N Methods Beyond The Leading Expansion",
            "Integrability And Spin Chains",
            "Resurgence, Semiclassics, Solitons, And Instantons",
            "Asymptotic Expansions And Large-Order Structure",
        ],
    ),
    (
        "volume_vi",
        "Frontiers And Interfaces",
        [
            "QFT In Curved Spacetime",
            "Entanglement, Modular Theory, And Relative Entropy",
            "Holography And Large-N QFT",
            "Quantum Gravity Constraints On QFT",
            "Scattering Amplitudes And On-Shell Methods",
            "Celestial And Asymptotic Structures",
            "Higher Symmetries, Defects, And Extended Operators",
            "Strings As Two-Dimensional QFT And Beyond",
            "Quantum Error Correction And Emergent Spacetime",
            "Higher Categories And Extended Field Theory",
            "Mathematical Formalization Programs",
            "Open Problems In The Foundations Of QFT",
        ],
    ),
]

ROMAN = ["I", "II", "III", "IV", "V", "VI"]

VOLUME_SOURCE_NOTES = {
    "volume_i": (
        "The order here is structural: local quantum physics, path-integral "
        r"Green functions, early K\"allen--Lehmann spectral representation, "
        "Haag--Ruelle scattering, LSZ, and only then perturbative S-matrix "
        "calculations."
    ),
    "volume_ii": (
        "This chapter continues from the nonperturbative S-matrix/LSZ setup "
        "before using "
        "scattering amplitudes, renormalization, RG, gauge theory, anomalies, "
        "and effective actions."
    ),
    "volume_iii": (
        "The conformal-field-theory sequence is structural: fixed points, "
        "conformal symmetry, state-operator correspondence, Ward identities, "
        "representations, correlators, OPE, blocks, bootstrap, 2d CFT, modular "
        "structure, supersymmetry, and large-N."
    ),
    "volume_iv": (
        "This chapter is a mathematical deepening layer. It clarifies "
        "foundations and nonperturbative definition without replacing the "
        "constructive order of the main text."
    ),
    "volume_v": (
        "This chapter is an exact-structure and extended-operator expansion "
        "built after the core construction. It may import modern machinery only "
        "after the relevant physical structures have appeared."
    ),
    "volume_vi": (
        "This chapter is a frontier interface chapter. It should state open "
        "problems honestly and connect them back to the spine rather than "
        "presenting frontier language as a replacement for foundations."
    ),
}

GENERATED_MARKERS = (
    "This chapter is part of the generated monograph skeleton",
    "Draft scaffold for a lecture-spine chapter",
    "Draft scaffold for a structural chapter",
)


def slug(title: str) -> str:
    if title == "What Is Quantum Field Theory?":
        return "what_is_qft"
    s = title.lower()
    s = s.replace("'t hooft", "t-hooft")
    s = s.replace("qft", "qft").replace("lsz", "lsz").replace("brst", "brst")
    s = s.replace("bv", "bv").replace("qed", "qed").replace("qcd", "qcd")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def tex_title(title: str) -> str:
    lowered = (
        title.replace("And", "and")
        .replace("Of", "of")
        .replace(" In ", " in ")
        .replace(" The ", " the ")
        .replace(" A ", " a ")
        .replace(" As ", " as ")
        .replace(" To ", " to ")
        .replace(" Versus ", " versus ")
    )
    return (
        lowered.replace("Kallen-Lehmann", r"K\"allen--Lehmann")
        .replace("Haag-Ruelle", "Haag--Ruelle")
        .replace("Wilson-Fisher", "Wilson--Fisher")
        .replace("Yang-Mills", "Yang--Mills")
        .replace("Bethe-Salpeter", "Bethe--Salpeter")
        .replace("Osterwalder-Schrader", "Osterwalder--Schrader")
        .replace("Faddeev-Popov", "Faddeev--Popov")
    )


def label_for(volume: str, number: int) -> str:
    return f"ch:{volume.replace('_', '-')}-{number:02d}"


def chapter_stub(volume: str, number: int, title: str) -> str:
    return f"""\\chapter{{{tex_title(title)}}}
\\label{{{label_for(volume, number)}}}

\\section{{Program}}

{VOLUME_SOURCE_NOTES[volume]}

The chapter must identify which statements are definitions, constructions,
regulated claims, perturbative claims, or nonperturbative claims. External
literature may sharpen hypotheses and references, but it does not determine the
conceptual order.

"""


def should_overwrite_generated(path: Path) -> bool:
    if not path.exists():
        return True
    text = path.read_text(encoding="utf-8")
    return any(marker in text for marker in GENERATED_MARKERS)


def main() -> None:
    volume_root = TEX / "volumes"
    for volume_index, (volume, part_title, chapters) in enumerate(VOLUMES):
        vdir = volume_root / volume
        vdir.mkdir(parents=True, exist_ok=True)

        inputs = []
        for index, title in enumerate(chapters, start=1):
            filename = f"chapter{index:02d}_{slug(title)}.tex"
            path = vdir / filename
            if should_overwrite_generated(path):
                path.write_text(chapter_stub(volume, index, title), encoding="utf-8")
            inputs.append(filename[:-4])

        volume_file = vdir / f"{volume}.tex"
        volume_heading = f"Volume {ROMAN[volume_index]}. {tex_title(part_title)}"
        hprefix = f"vol{ROMAN[volume_index]}"
        lines = [
            f"\\part{{{volume_heading}}}",
            "\\setcounter{chapter}{0}",
            f"\\renewcommand{{\\theHchapter}}{{{hprefix}.\\arabic{{chapter}}}}",
            f"\\renewcommand{{\\theHsection}}{{{hprefix}.\\arabic{{chapter}}.\\arabic{{section}}}}",
            f"\\renewcommand{{\\theHsubsection}}{{{hprefix}.\\arabic{{chapter}}.\\arabic{{section}}.\\arabic{{subsection}}}}",
            "",
        ]
        for input_name in inputs:
            lines.append(f"\\input{{volumes/{volume}/{input_name}}}")
        lines.append("")
        volume_file.write_text("\n".join(lines), encoding="utf-8")

    print(f"Generated skeleton under {volume_root}")


if __name__ == "__main__":
    main()
