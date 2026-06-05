#!/usr/bin/env python3
"""Evidence contract.

Target claims:
- Endpoint convolution, distributional pairing, zero-bin subtraction, finite
  scheme changes, RG transport, Wilson-line decoupling, Glauber diagnostics,
  the spectator-model color-entanglement obstruction to generalized TMD
  factorization, soft-drop scales, and massive-vector Sudakov areas obey the
  finite algebra stated in the jets/SCET chapter.
- The occurrence-level factorization ledger covers the declared
  process-level QCD/SCET, Regge, and Abelian soft-factorization occurrences
  through a source-derived manifest, classifies the main non-process homonyms,
  and keeps BMS non-global soft evolution separate from Glauber exchange.
- The regulated endpoint-region integral has a real fixed-order remainder
  bound, and unsubtracted or unpaired region splits fail as negative controls.
- A noncommuting finite measurement can detect a Glauber rotation, so a
  residual slot is not a proof of factorization.

Independent construction:
- All checks use finite distributions, rational matrices, exact polynomial
  integrals, or symbolic identities built independently of the manuscript
  prose.
- The endpoint-region expansion is checked by direct symbolic integration and
  by the Lipschitz remainder bound.
- The Glauber-breaking example is checked both as a concrete rational matrix
  model and as a symbolic two-state rotation formula.
- The spectator-model obstruction is checked by an independent finite SU(2)
  color-trace computation, eikonal delta-coefficient bookkeeping, a
  source-derived Rogers-Mulders model point, explicit hard-factor bounds, and
  a fixed-recoil positive-denominator transverse witness after analytic
  reduction of the two Glauber transverse integrations.
- The factorization occurrence audit mechanically scans the manuscript source
  for factorization labels, factorization-titled environments, captions,
  section/paragraph titles, and semantic prose windows around theorem-like
  environments, then checks independent TSV artifacts rather than a
  Python-owned occurrence list or self-attested review row.

Imported assumptions:
- The checks are finite-regulator or fixed-order algebraic tests of a proposed
  SCET/factorization datum.
- The endpoint integral is a one-dimensional Feynman-parameter endpoint model;
  it is not a continuum QCD theorem.
- The finite Glauber Hilbert space is a diagnostic model for measurement
  commutation, not a construction of the QCD Glauber region.
- The spectator-model check verifies the color/eikonal skeleton of the
  Rogers-Mulders mechanism and a compact auxiliary positive-denominator
  transverse nonvanishing datum; it does not treat the deformation as a
  gauge-theory regulator, prove regulator removal, or normalize an all-order
  hadronic cross section.

Negative controls:
- Naively double-counting the zero-bin leaves exactly the overlap term.
- A finite scheme change whose factors do not multiply to one changes the
  hard/jet/soft product.
- The unsubtracted hard endpoint integral diverges, and an unpaired
  intermediate split retains arbitrary split-scale dependence.
- A noncommuting measurement gives a nonzero Glauber remainder.
- Separate color-traced TMD factors have zero order-g single-loop anomaly
  while the cross-hadron two-gluon color trace is nonzero; a pointwise
  nonzero spectator integrand value is not accepted as an integrated
  nonvanishing proof.
- A source candidate absent from the manifest or textual-review TSV, a stale
  row absent from the corresponding source scan, or a semantic negative
  control missed by the prose-window scanner fails the occurrence-ledger
  check.

Scope boundary:
- This script verifies finite algebra, fixed-order endpoint expansion, and
  proof-obligation diagnostics.  It does not construct SCET, prove
  composite-operator existence, prove regulator removal, derive mode
  decompositions from QCD, or establish all-order factorization for a
  physical cross section.
"""

from __future__ import annotations

import csv
import math
import re
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Mapping

import sympy as sp
from sympy.integrals.quadrature import gauss_legendre

from check_utils import assert_leq as _assert_leq

Distribution = Mapping[Fraction, Fraction]

ROOT = Path(__file__).resolve().parents[1]

JETS_CHAPTER = (
    "monograph/tex/volumes/volume_ii/"
    "chapter19b_jets_ir_safe_observables_and_hadronization.tex"
)
QCD_CHAPTER = (
    "monograph/tex/volumes/volume_ii/"
    "chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex"
)
REGGE_CHAPTER = (
    "monograph/tex/volumes/volume_ii/"
    "chapter07_partial_waves_dispersion_relations_and_high_energy_bounds.tex"
)
QED_IR_CHAPTER = (
    "monograph/tex/volumes/volume_ii/"
    "chapter22_infrared_divergences_and_inclusive_qed.tex"
)

FACTORIZATION_MANIFEST = "planning/factorization_occurrence_manifest.tsv"
TEXTUAL_FACTORIZATION_REVIEW = "planning/factorization_textual_candidate_review.tsv"
FACTORIZATION_WORD = re.compile(r"factorization|factorized", re.IGNORECASE)
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
BEGIN_RE = re.compile(r"\\begin\{([^}]+)\}(?:\[([^\]]*)\])?")
TITLE_RE = re.compile(r"\\(section|subsection|subsubsection|paragraph)\*?\{([^{}]+)\}")
THEOREM_LIKE_ENVIRONMENTS = {
    "controlledapproximation",
    "definition",
    "example",
    "hypothesis",
    "lemma",
    "proposition",
    "remark",
    "theorem",
}
SEMANTIC_FACTORIZATION_PHRASES = (
    "factorization coordinate",
    "factorization statement",
    "factorization theorem",
    "factorized approximation",
)


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def read_repo_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def find_label_line(relative_path: str, label: str) -> int:
    pattern = re.compile(r"\\label\{" + re.escape(label) + r"\}")
    for line_number, line in enumerate(read_repo_text(relative_path).splitlines(), 1):
        if pattern.search(line):
            return line_number
    raise AssertionError(f"ledger inventory label {label!r} missing from {relative_path}")


def normalized_tex_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def slug_text(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "candidate"


def title_factorization_trigger(text: str) -> str | None:
    normalized = normalized_tex_text(text).lower()
    if FACTORIZATION_WORD.search(normalized):
        return "factorization"
    return semantic_factorization_trigger(text)


def semantic_factorization_trigger(text: str) -> str | None:
    normalized = normalized_tex_text(text).lower()
    for phrase in SEMANTIC_FACTORIZATION_PHRASES:
        if phrase in normalized:
            return phrase
    return None


def generated_textual_factorization_candidates_from_lines(
    relative_path: str, lines: list[str]
) -> dict[str, dict[str, str]]:
    candidates: dict[str, dict[str, str]] = {}

    def add_candidate(
        candidate_id: str,
        line_number: int,
        source_kind: str,
        trigger: str,
        linked_label: str = "",
    ) -> None:
        if candidate_id in candidates:
            return
        candidates[candidate_id] = {
            "source_path": relative_path,
            "line_anchor": f"L{line_number}",
            "source_kind": source_kind,
            "trigger": trigger,
            "linked_label": linked_label,
        }

    for line_number, line in enumerate(lines, 1):
        title_match = TITLE_RE.search(line)
        if not title_match:
            continue
        title_text = title_match.group(2)
        trigger = title_factorization_trigger(title_text)
        if not trigger:
            continue
        source_kind = f"{title_match.group(1)}-title"
        candidate_id = f"title:{relative_path}:L{line_number}:{slug_text(title_text)}"
        add_candidate(candidate_id, line_number, source_kind, trigger)

    for line_number, line in enumerate(lines, 1):
        begin_match = BEGIN_RE.search(line)
        if not begin_match:
            continue
        environment = begin_match.group(1)
        if environment not in THEOREM_LIKE_ENVIRONMENTS:
            continue
        end_re = re.compile(r"\\end\{" + re.escape(environment) + r"\}")
        end_index = min(len(lines), line_number + 220)
        body_labels: list[str] = []
        for index in range(line_number - 1, min(len(lines), line_number + 220)):
            body_labels.extend(LABEL_RE.findall(lines[index]))
            if end_re.search(lines[index]):
                end_index = index + 1
                break
        window_start = max(0, line_number - 33)
        window_end = min(len(lines), end_index + 32)
        trigger_line = 0
        trigger = ""
        for index in range(window_start, window_end):
            found_trigger = semantic_factorization_trigger(lines[index])
            if found_trigger:
                trigger_line = index + 1
                trigger = found_trigger
                break
        if not trigger:
            continue
        primary_label = body_labels[0] if body_labels else ""
        if primary_label:
            candidate_id = f"semantic:{primary_label}:{slug_text(trigger)}"
        else:
            candidate_id = f"semantic:{relative_path}:L{line_number}:{slug_text(trigger)}"
        add_candidate(candidate_id, trigger_line, "semantic-prose-window", trigger, primary_label)

    return candidates


def generated_textual_factorization_candidates() -> dict[str, dict[str, str]]:
    candidates: dict[str, dict[str, str]] = {}
    for path in sorted((ROOT / "monograph/tex").rglob("*.tex")):
        relative_path = str(path.relative_to(ROOT))
        lines = path.read_text(encoding="utf-8").splitlines()
        candidates.update(generated_textual_factorization_candidates_from_lines(relative_path, lines))
    return candidates


def generated_factorization_candidates() -> dict[tuple[str, str], set[str]]:
    candidates: dict[tuple[str, str], set[str]] = {}
    for path in sorted((ROOT / "monograph/tex").rglob("*.tex")):
        relative_path = str(path.relative_to(ROOT))
        lines = path.read_text(encoding="utf-8").splitlines()

        for line in lines:
            for label in LABEL_RE.findall(line):
                if FACTORIZATION_WORD.search(label):
                    candidates.setdefault((relative_path, label), set()).add("label")

        for line_number, line in enumerate(lines, 1):
            begin_match = BEGIN_RE.search(line)
            if not begin_match:
                continue
            environment, title = begin_match.groups()
            if not title or not FACTORIZATION_WORD.search(title):
                continue
            end_re = re.compile(r"\\end\{" + re.escape(environment) + r"\}")
            for candidate_line in lines[line_number - 1 :]:
                for label in LABEL_RE.findall(candidate_line):
                    candidates.setdefault((relative_path, label), set()).add("environment-title")
                if end_re.search(candidate_line):
                    break

        for line_number, line in enumerate(lines, 1):
            begin_match = BEGIN_RE.search(line)
            if not begin_match:
                continue
            environment = begin_match.group(1)
            if environment not in {"figure", "table"}:
                continue
            end_re = re.compile(r"\\end\{" + re.escape(environment) + r"\}")
            body_lines: list[str] = []
            labels: list[str] = []
            for candidate_line in lines[line_number - 1 : min(len(lines), line_number + 220)]:
                body_lines.append(candidate_line)
                labels.extend(LABEL_RE.findall(candidate_line))
                if end_re.search(candidate_line):
                    break
            body = "\n".join(body_lines)
            if "\\caption" in body and FACTORIZATION_WORD.search(body):
                for label in labels:
                    candidates.setdefault((relative_path, label), set()).add("caption")

    return candidates


def load_factorization_manifest() -> list[dict[str, str]]:
    manifest_path = ROOT / FACTORIZATION_MANIFEST
    with manifest_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    required = {"candidate_id", "source_path", "disposition", "ledger_key", "reason"}
    if not rows or set(rows[0]) != required:
        raise AssertionError("factorization occurrence manifest has unexpected columns")

    seen: set[tuple[str, str]] = set()
    for row in rows:
        key = (row["source_path"], row["candidate_id"])
        if key in seen:
            raise AssertionError(f"duplicate factorization manifest row {key!r}")
        seen.add(key)
        if row["disposition"] not in {"included", "grouped", "excluded"}:
            raise AssertionError(f"bad factorization disposition for {key!r}")
        if not row["ledger_key"] or not row["reason"]:
            raise AssertionError(f"manifest row {key!r} needs ledger_key and reason")
        if not row["candidate_id"].startswith("review:"):
            find_label_line(row["source_path"], row["candidate_id"])
    return rows


def load_textual_factorization_review() -> list[dict[str, str]]:
    review_path = ROOT / TEXTUAL_FACTORIZATION_REVIEW
    with review_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    required = {
        "candidate_id",
        "source_path",
        "line_anchor",
        "source_kind",
        "trigger",
        "disposition",
        "ledger_key",
        "reason",
    }
    if not rows or set(rows[0]) != required:
        raise AssertionError("factorization textual review has unexpected columns")
    seen: set[tuple[str, str]] = set()
    for row in rows:
        key = (row["source_path"], row["candidate_id"])
        if key in seen:
            raise AssertionError(f"duplicate textual factorization review row {key!r}")
        seen.add(key)
        if row["disposition"] not in {"included", "grouped", "excluded"}:
            raise AssertionError(f"bad textual factorization disposition for {key!r}")
        if not row["line_anchor"].startswith("L") or not row["line_anchor"][1:].isdigit():
            raise AssertionError(f"textual factorization row {key!r} needs an L-number line anchor")
        if not row["trigger"] or not row["ledger_key"] or not row["reason"]:
            raise AssertionError(f"textual factorization row {key!r} is incomplete")
        line_number = int(row["line_anchor"][1:])
        source_lines = read_repo_text(row["source_path"]).splitlines()
        if line_number < 1 or line_number > len(source_lines):
            raise AssertionError(f"textual factorization row {key!r} line anchor is outside the source")
    return rows


def factorization_ledger_block() -> str:
    text = read_repo_text(JETS_CHAPTER)
    start_marker = r"\paragraph{Occurrence-level claim-status ledger for factorization uses.}"
    end_marker = "Renormalization of the hard, jet, and soft functions gives evolution"
    try:
        start = text.index(start_marker)
        end = text.index(end_marker, start)
    except ValueError as exc:
        raise AssertionError("factorization occurrence ledger block was not found") from exc
    return text[start:end]


def check_factorization_occurrence_ledger_inventory() -> None:
    ledger = factorization_ledger_block()
    normalized_ledger = normalized_tex_text(ledger)
    manifest_rows = load_factorization_manifest()
    textual_rows = load_textual_factorization_review()

    generated = generated_factorization_candidates()
    textual_generated = generated_textual_factorization_candidates()
    textual_manifest_candidates = {
        (row["source_path"], row["ledger_key"])
        for row in textual_rows
        if row["disposition"] == "included"
        and row["ledger_key"]
        and not row["ledger_key"].startswith("text:")
    }
    for source_path, ledger_key in textual_manifest_candidates:
        find_label_line(source_path, ledger_key)
    manifest_candidates = {
        (row["source_path"], row["candidate_id"])
        for row in manifest_rows
    }
    generated_manifest_candidates = set(generated) | textual_manifest_candidates
    missing = sorted(generated_manifest_candidates - manifest_candidates)
    stale = sorted(manifest_candidates - generated_manifest_candidates)
    if missing:
        raise AssertionError(f"factorization source candidates lack manifest disposition: {missing}")
    if stale:
        raise AssertionError(f"factorization manifest rows are stale or no longer source-derived: {stale}")

    if any(row["candidate_id"].startswith("review:") for row in manifest_rows):
        raise AssertionError("textual factorization review must be source-derived, not a self-attested review row")

    textual_generated_keys = {
        (info["source_path"], candidate_id)
        for candidate_id, info in textual_generated.items()
    }
    textual_review_keys = {
        (row["source_path"], row["candidate_id"])
        for row in textual_rows
    }
    missing_textual = sorted(textual_generated_keys - textual_review_keys)
    stale_textual = sorted(textual_review_keys - textual_generated_keys)
    if missing_textual:
        raise AssertionError(f"textual factorization candidates lack review disposition: {missing_textual}")
    if stale_textual:
        raise AssertionError(f"textual factorization review rows are stale: {stale_textual}")

    for row in manifest_rows:
        candidate_id = row["candidate_id"]
        disposition = row["disposition"]
        ledger_key = row["ledger_key"]
        if disposition == "included":
            if candidate_id not in ledger:
                raise AssertionError(f"included factorization occurrence {candidate_id!r} missing from ledger")
            if ledger_key not in ledger:
                raise AssertionError(f"included factorization ledger key {ledger_key!r} missing from ledger")
        elif disposition == "grouped":
            if ledger_key not in ledger:
                raise AssertionError(f"grouped factorization ledger key {ledger_key!r} missing from ledger")
        elif disposition == "excluded":
            if ledger_key not in normalized_ledger:
                raise AssertionError(
                    f"excluded factorization category {ledger_key!r} missing from boundary prose"
                )

    for row in textual_rows:
        candidate_id = row["candidate_id"]
        info = textual_generated[candidate_id]
        for field in ("line_anchor", "source_kind", "trigger"):
            if row[field] != info[field]:
                raise AssertionError(
                    f"textual factorization row {candidate_id!r} has stale {field}: "
                    f"{row[field]!r} != {info[field]!r}"
                )
        disposition = row["disposition"]
        ledger_key = row["ledger_key"]
        if disposition == "included" and ledger_key not in ledger:
            raise AssertionError(f"included textual factorization key {ledger_key!r} missing from ledger")
        if disposition == "grouped" and ledger_key not in ledger:
            raise AssertionError(f"grouped textual factorization key {ledger_key!r} missing from ledger")
        if disposition == "excluded" and ledger_key not in normalized_ledger:
            raise AssertionError(
                f"excluded textual factorization category {ledger_key!r} missing from boundary prose"
            )

    negative_control_lines = [
        r"Nearby prose declares a factorization coordinate for a hadronic observable.",
        r"\begin{controlledapproximation}[Semantic trigger without lexical title]",
        r"\label{ca:semantic-negative-control}",
        r"This synthetic environment has no factorization word in its title.",
        r"\end{controlledapproximation}",
    ]
    negative_control = generated_textual_factorization_candidates_from_lines(
        "synthetic/negative_control.tex", negative_control_lines
    )
    if "semantic:ca:semantic-negative-control:factorization-coordinate" not in negative_control:
        raise AssertionError("semantic factorization negative control was not detected")

    if "Glauber: color correlations enter through the nonlinear dipole evolution" in normalized_ledger:
        raise AssertionError("non-global soft evolution was conflated with Glauber exchange")
    if "Glauber: no Glauber exchange is represented by this row" not in normalized_ledger:
        raise AssertionError("non-global row must explicitly separate BMS soft evolution from Glauber exchange")
    if "super-leading or hadron-hadron Glauber questions are separate coordinates" not in normalized_ledger:
        raise AssertionError("non-global row must keep super-leading/Glauber questions separate")

    issue_828_required = {
        "hyp:triple-regge-factorization-system",
        "eq:triple-regge-factorization-formula",
        "thm:weinberg-leading-soft-photon",
        "fig:volume-ii-soft-factorization",
        "eq:qcd-gpd-definition",
        "eq:qcd-endpoint-kernel-cusp-coefficient",
        "eq:qcd-large-spin-dglap-cusp",
    }
    missing_required = sorted(label for label in issue_828_required if label not in ledger)
    if missing_required:
        raise AssertionError(f"issue #828 required labels missing from ledger: {missing_required}")


def normalize(dist: Distribution) -> Fraction:
    return sum(dist.values(), Fraction(0))


def moment(dist: Distribution) -> Fraction:
    return sum(x * weight for x, weight in dist.items())


def signed_difference(left: Distribution, right: Distribution) -> dict[Fraction, Fraction]:
    keys = set(left) | set(right)
    return {key: left.get(key, Fraction(0)) - right.get(key, Fraction(0)) for key in keys}


def finite_pairing(dist: Distribution, test: Distribution) -> Fraction:
    return sum(weight * test.get(point, Fraction(0)) for point, weight in dist.items())


def total_variation(dist: Distribution) -> Fraction:
    return sum(abs(weight) for weight in dist.values())


def sup_norm(test: Distribution) -> Fraction:
    return max((abs(value) for value in test.values()), default=Fraction(0))


def endpoint_convolution(
    jet_n: Distribution,
    jet_barn: Distribution,
    soft: Distribution,
    q_hard: Fraction,
) -> dict[Fraction, Fraction]:
    out: dict[Fraction, Fraction] = defaultdict(Fraction)
    for s1, w1 in jet_n.items():
        for s2, w2 in jet_barn.items():
            for k, ws in soft.items():
                e = (s1 + s2) / (q_hard * q_hard) + k / q_hard
                out[e] += w1 * w2 * ws
    return dict(out)


def generating_transform(dist: Distribution, scale: Fraction) -> dict[Fraction, Fraction]:
    return {scale * x: weight for x, weight in dist.items()}


def multiply_transforms(*transforms: Mapping[Fraction, Fraction]) -> dict[Fraction, Fraction]:
    out: dict[Fraction, Fraction] = {Fraction(0): Fraction(1)}
    for transform in transforms:
        new_out: dict[Fraction, Fraction] = defaultdict(Fraction)
        for e1, w1 in out.items():
            for e2, w2 in transform.items():
                new_out[e1 + e2] += w1 * w2
        out = dict(new_out)
    return out


def check_event_shape_convolution() -> None:
    jet_n = {Fraction(1): Fraction(1, 3), Fraction(4): Fraction(2, 3)}
    jet_barn = {Fraction(2): Fraction(3, 5), Fraction(5): Fraction(2, 5)}
    soft = {Fraction(0): Fraction(1, 4), Fraction(3): Fraction(3, 4)}
    q_hard = Fraction(6)

    direct = endpoint_convolution(jet_n, jet_barn, soft, q_hard)
    transformed = multiply_transforms(
        generating_transform(jet_n, Fraction(1, q_hard * q_hard)),
        generating_transform(jet_barn, Fraction(1, q_hard * q_hard)),
        generating_transform(soft, Fraction(1, q_hard)),
    )
    assert_equal("endpoint convolution transform", direct, transformed)
    assert_equal("convolution normalization", normalize(direct), Fraction(1))

    expected_first_moment = (
        moment(jet_n) / (q_hard * q_hard)
        + moment(jet_barn) / (q_hard * q_hard)
        + moment(soft) / q_hard
    )
    assert_equal("endpoint first moment", moment(direct), expected_first_moment)


def check_distributional_factorization_remainder_bound() -> None:
    physical = {
        Fraction(0): Fraction(7, 15),
        Fraction(1, 4): Fraction(1, 5),
        Fraction(1, 2): Fraction(1, 6),
        Fraction(3, 4): Fraction(1, 6),
    }
    factorized = {
        Fraction(0): Fraction(1, 2),
        Fraction(1, 4): Fraction(1, 6),
        Fraction(1, 2): Fraction(1, 5),
        Fraction(3, 4): Fraction(2, 15),
    }
    remainder = signed_difference(physical, factorized)
    assert_equal("equal total weight in factorization model", normalize(remainder), Fraction(0))

    test = {
        Fraction(0): Fraction(3, 5),
        Fraction(1, 4): Fraction(-2, 7),
        Fraction(1, 2): Fraction(4, 9),
        Fraction(3, 4): Fraction(-5, 11),
    }
    pairing = finite_pairing(remainder, test)
    bound = total_variation(remainder) * sup_norm(test)
    _assert_leq("distributional remainder total-variation bound", abs(pairing), bound)

    sign_test = {
        point: Fraction(1) if weight > 0 else Fraction(-1) if weight < 0 else Fraction(0)
        for point, weight in remainder.items()
    }
    assert_equal("sharp total-variation dual pairing", finite_pairing(remainder, sign_test), total_variation(remainder))


def finite_zero_bin_sum(
    collinear: Mapping[str, Fraction],
    soft: Mapping[str, Fraction],
    overlap: Mapping[str, Fraction],
    test: Mapping[str, Fraction],
) -> Fraction:
    return (
        sum(weight * test[cell] for cell, weight in collinear.items())
        + sum(weight * test[cell] for cell, weight in soft.items())
        - sum(weight * test[cell] for cell, weight in overlap.items())
    )


def check_zero_bin_inclusion_exclusion() -> None:
    collinear = {"c": Fraction(5), "o1": Fraction(7), "o2": Fraction(11)}
    soft = {"s": Fraction(13), "o1": Fraction(7), "o2": Fraction(11)}
    overlap = {"o1": Fraction(7), "o2": Fraction(11)}
    test = {
        "c": Fraction(2, 3),
        "s": Fraction(3, 5),
        "o1": Fraction(5, 7),
        "o2": Fraction(7, 11),
    }
    matched = finite_zero_bin_sum(collinear, soft, overlap, test)
    unique_union = (
        collinear["c"] * test["c"]
        + soft["s"] * test["s"]
        + overlap["o1"] * test["o1"]
        + overlap["o2"] * test["o2"]
    )
    naive_double_count = sum(weight * test[cell] for cell, weight in collinear.items()) + sum(
        weight * test[cell] for cell, weight in soft.items()
    )
    assert_equal("finite zero-bin inclusion-exclusion", matched, unique_union)
    assert_equal(
        "naive overlap double count",
        naive_double_count - matched,
        sum(weight * test[cell] for cell, weight in overlap.items()),
    )


def check_zero_bin_scheme_reshuffling() -> None:
    collinear = {"c": Fraction(2), "o": Fraction(5)}
    soft = {"s": Fraction(7), "o": Fraction(5)}
    overlap = {"o": Fraction(5)}
    test = {"c": Fraction(3), "s": Fraction(4), "o": Fraction(11)}
    base = finite_zero_bin_sum(collinear, soft, overlap, test)

    delta = Fraction(13)
    collinear_shifted = {"c": collinear["c"], "o": collinear["o"]}
    soft_shifted = {"s": soft["s"], "o": soft["o"] + delta}
    overlap_shifted = {"o": overlap["o"] + delta}
    shifted = finite_zero_bin_sum(collinear_shifted, soft_shifted, overlap_shifted, test)
    assert_equal("paired zero-bin scheme reshuffling", shifted, base)


def check_regulated_endpoint_region_expansion() -> None:
    x = sp.symbols("x", positive=True)
    eps = sp.symbols("eps", positive=True)
    eta = sp.symbols("eta", positive=True)
    lam = sp.Rational(1, 7)
    f = 1 + 3 * x + 2 * x**2
    f0 = f.subs(x, 0)

    exact = sp.integrate(f / (x + lam), (x, 0, 1))
    endpoint = f0 * sp.log((1 + lam) / lam)
    hard = sp.integrate((f - f0) / x, (x, 0, 1))
    remainder = -lam * sp.integrate((f - f0) / (x * (x + lam)), (x, 0, 1))
    assert_equal(
        "regulated endpoint expansion identity",
        sp.simplify(exact - endpoint - hard - remainder),
        0,
    )

    lipschitz_bound = lam * sp.Rational(7) * sp.log((1 + lam) / lam)
    _assert_leq(
        "regulated endpoint Lipschitz remainder bound",
        float(abs(remainder.evalf())),
        float(lipschitz_bound.evalf()),
    )

    unsubtracted_hard = sp.integrate(f / x, (x, eps, 1))
    if sp.limit(unsubtracted_hard, eps, 0, dir="+") != sp.oo:
        raise AssertionError("unsubtracted endpoint hard integral should diverge")

    naive_split = f0 * sp.log(eta / lam) + sp.integrate(f / x, (x, eta, 1))
    split_derivative = sp.simplify(sp.diff(naive_split, eta))
    assert_equal("naive split-scale dependence", split_derivative, -2 * eta - 3)


def check_multiplicative_scheme_covariance() -> None:
    hard = Fraction(2, 3)
    jet_n = Fraction(5, 7)
    jet_barn = Fraction(11, 13)
    soft = Fraction(17, 19)
    base_product = hard * jet_n * jet_barn * soft

    r_h = Fraction(3, 5)
    r_n = Fraction(7, 11)
    r_barn = Fraction(13, 17)
    r_s = Fraction(1, 1) / (r_h * r_n * r_barn)
    assert_equal("multiplicative scheme product condition", r_h * r_n * r_barn * r_s, Fraction(1))

    shifted_product = (hard * r_h) * (jet_n * r_n) * (jet_barn * r_barn) * (soft * r_s)
    assert_equal("factorized product under finite scheme change", shifted_product, base_product)
    bad_shifted_product = (hard * r_h) * (jet_n * r_n) * (jet_barn * r_barn) * (soft * r_s * 2)
    if bad_shifted_product == base_product:
        raise AssertionError("unpaired finite scheme change should alter the factorized product")

    gamma_h = Fraction(5, 6)
    gamma_n = Fraction(-1, 3)
    gamma_barn = Fraction(7, 10)
    gamma_s = -gamma_h - gamma_n - gamma_barn
    assert_equal("unshifted anomalous-dimension consistency", gamma_h + gamma_n + gamma_barn + gamma_s, Fraction(0))

    dlog_r_h = Fraction(2, 7)
    dlog_r_n = Fraction(-3, 11)
    dlog_r_barn = Fraction(5, 13)
    dlog_r_s = -dlog_r_h - dlog_r_n - dlog_r_barn
    shifted_sum = (
        (gamma_h + dlog_r_h)
        + (gamma_n + dlog_r_n)
        + (gamma_barn + dlog_r_barn)
        + (gamma_s + dlog_r_s)
    )
    assert_equal("shifted anomalous-dimension consistency", shifted_sum, Fraction(0))


def integrate_piecewise(values: Mapping[tuple[Fraction, Fraction], Fraction], start: Fraction, end: Fraction) -> Fraction:
    if start == end:
        return Fraction(0)
    if start > end:
        return -integrate_piecewise(values, end, start)

    total = Fraction(0)
    for (left, right), value in values.items():
        overlap_left = max(start, left)
        overlap_right = min(end, right)
        if overlap_left < overlap_right:
            total += value * (overlap_right - overlap_left)
    return total


def check_rg_transport_common_scale_independence() -> None:
    intervals = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(2)), (Fraction(2), Fraction(3)))
    gamma_h = {intervals[0]: Fraction(3), intervals[1]: Fraction(-1), intervals[2]: Fraction(2)}
    gamma_j = {intervals[0]: Fraction(-2), intervals[1]: Fraction(4), intervals[2]: Fraction(1)}
    gamma_s = {interval: -gamma_h[interval] - 2 * gamma_j[interval] for interval in intervals}

    for interval in intervals:
        assert_equal(
            "pointwise SCET anomalous-dimension consistency",
            gamma_h[interval] + 2 * gamma_j[interval] + gamma_s[interval],
            Fraction(0),
        )

    natural_h = Fraction(0)
    natural_j = Fraction(1)
    natural_s = Fraction(2)

    def total_transport_exponent(common_scale: Fraction) -> Fraction:
        return (
            integrate_piecewise(gamma_h, natural_h, common_scale)
            + 2 * integrate_piecewise(gamma_j, natural_j, common_scale)
            + integrate_piecewise(gamma_s, natural_s, common_scale)
        )

    reference = total_transport_exponent(Fraction(2))
    assert_equal("RG transport to first common scale", reference, total_transport_exponent(Fraction(2)))
    assert_equal("RG transport independent of later common scale", reference, total_transport_exponent(Fraction(3)))

    shifted_gamma_h = {interval: gamma_h[interval] + Fraction(5) for interval in intervals}
    shifted_gamma_s = {interval: gamma_s[interval] - Fraction(5) for interval in intervals}
    shifted = (
        integrate_piecewise(shifted_gamma_h, natural_h, Fraction(3))
        + 2 * integrate_piecewise(gamma_j, natural_j, Fraction(3))
        + integrate_piecewise(shifted_gamma_s, natural_s, Fraction(3))
    )
    unshifted = total_transport_exponent(Fraction(3))
    assert_equal("paired hard-soft anomalous-dimension scheme shift", shifted, unshifted + Fraction(5) * (natural_s - natural_h))


def check_soft_drop_boundary_scales_and_rg_consistency() -> None:
    beta = 2
    rho = Fraction(1, 4096)
    z_cut = Fraction(1, 16)
    theta_star = Fraction(1, 4)
    z_star = Fraction(1, 256)

    assert_equal("soft-drop boundary mass equation", z_star * theta_star * theta_star, rho)
    assert_equal("soft-drop boundary grooming equation", z_cut * theta_star**beta, z_star)
    assert_equal("soft-drop boundary theta equation", theta_star ** (beta + 2), rho / z_cut)

    mu_j_squared = rho
    mu_cs_squared = rho * z_star
    assert_equal("soft-drop collinear-soft transverse scale", mu_cs_squared, z_star * mu_j_squared)
    if not mu_cs_squared < mu_j_squared:
        raise AssertionError("collinear-soft scale should lie below the collinear scale for z_star < 1")

    intervals = ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(2)), (Fraction(2), Fraction(4)))
    gamma_h = {intervals[0]: Fraction(4), intervals[1]: Fraction(-2), intervals[2]: Fraction(1)}
    gamma_g = {intervals[0]: Fraction(-3), intervals[1]: Fraction(5), intervals[2]: Fraction(2)}
    gamma_j = {intervals[0]: Fraction(1), intervals[1]: Fraction(1), intervals[2]: Fraction(-4)}
    gamma_cs = {
        interval: -gamma_h[interval] - gamma_g[interval] - gamma_j[interval]
        for interval in intervals
    }

    for interval in intervals:
        assert_equal(
            "soft-drop anomalous-dimension consistency",
            gamma_h[interval] + gamma_g[interval] + gamma_j[interval] + gamma_cs[interval],
            Fraction(0),
        )

    natural_h = Fraction(0)
    natural_g = Fraction(1)
    natural_j = Fraction(2)
    natural_cs = Fraction(2)

    def total_transport_exponent(common_scale: Fraction) -> Fraction:
        return (
            integrate_piecewise(gamma_h, natural_h, common_scale)
            + integrate_piecewise(gamma_g, natural_g, common_scale)
            + integrate_piecewise(gamma_j, natural_j, common_scale)
            + integrate_piecewise(gamma_cs, natural_cs, common_scale)
        )

    reference = total_transport_exponent(Fraction(2))
    assert_equal("soft-drop RG transport at first common scale", reference, total_transport_exponent(Fraction(2)))
    assert_equal("soft-drop RG transport independent of later common scale", reference, total_transport_exponent(Fraction(4)))


def check_soft_wilson_line_decoupling_identity() -> None:
    s = sp.symbols("s")
    a = sp.Rational(3, 2)
    connection = sp.Matrix([[0, a], [0, 0]])
    identity = sp.eye(2)
    # Nilpotency makes this exact polynomial Wilson line solve dY/ds = A Y.
    wilson = identity + s * connection
    field0 = sp.Matrix([1 + 2 * s + s**2, sp.Rational(1, 3) - s])

    lhs = sp.diff(wilson * field0, s) - connection * wilson * field0
    rhs = wilson * sp.diff(field0, s)
    assert_equal("finite BPS decoupling identity", sp.simplify(lhs - rhs), sp.zeros(2, 1))


def trace(matrix: sp.Matrix) -> sp.Rational:
    return sp.trace(matrix)


def frobenius_square(matrix: sp.Matrix) -> sp.Rational:
    return sp.trace(matrix.T * matrix)


def check_glauber_unitarity_diagnostic() -> None:
    unitary = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)], [sp.Rational(-4, 5), sp.Rational(3, 5)]])
    identity = sp.eye(2)
    assert_equal("finite Glauber unitary", unitary.T * unitary, identity)

    rho = sp.Matrix([[sp.Rational(2, 5), sp.Rational(1, 10)], [sp.Rational(1, 10), sp.Rational(3, 5)]])
    evolved = unitary * rho * unitary.T
    assert_equal("inclusive Glauber trace", trace(evolved), trace(rho))

    commuting_measurement = sp.Rational(7, 3) * identity
    assert_equal(
        "commuting Glauber measurement",
        trace(commuting_measurement * evolved),
        trace(commuting_measurement * rho),
    )

    noncommuting_measurement = sp.Matrix([[1, 0], [0, 0]])
    without_glauber = trace(noncommuting_measurement * rho)
    with_glauber = trace(noncommuting_measurement * evolved)
    if with_glauber == without_glauber:
        raise AssertionError("noncommuting measurement should detect the finite Glauber rotation")

    rotated_measurement_difference = unitary.T * noncommuting_measurement * unitary - noncommuting_measurement
    exact_remainder = with_glauber - without_glauber
    assert_equal(
        "Glauber remainder cyclic form",
        exact_remainder,
        trace(rotated_measurement_difference * rho),
    )

    # Exact finite-dimensional Cauchy-Schwarz check:
    # |Tr(A rho)|^2 <= Tr(A^T A) Tr(rho^T rho).  This is the rational
    # Hilbert-Schmidt version of the operator/trace-norm bound used in the text.
    lhs = exact_remainder * exact_remainder
    rhs = frobenius_square(rotated_measurement_difference) * frobenius_square(rho)
    if lhs > rhs:
        raise AssertionError(f"Glauber Hilbert-Schmidt remainder bound failed: {lhs} > {rhs}")


def check_symbolic_glauber_breaking_example() -> None:
    c, s, r1, r2 = sp.symbols("c s r1 r2")
    unitary = sp.Matrix([[c, s], [-s, c]])
    measurement = sp.Matrix([[1, 0], [0, 0]])
    rho = sp.diag(r1, r2)
    evolved = unitary * rho * unitary.T
    delta = sp.trace(measurement * evolved) - sp.trace(measurement * rho)
    delta_on_unit_circle = sp.simplify(delta.subs(c**2, 1 - s**2))
    assert_equal("symbolic finite Glauber breaking", delta_on_unit_circle, s**2 * (r2 - r1))

    concrete = delta_on_unit_circle.subs({s: sp.Rational(4, 5), r1: sp.Rational(1, 5), r2: sp.Rational(3, 5)})
    if concrete == 0:
        raise AssertionError("concrete Glauber-breaking negative control should be nonzero")


def check_spectator_model_color_entanglement() -> None:
    half = sp.Rational(1, 2)
    generators = [
        sp.Matrix([[0, half], [half, 0]]),
        sp.Matrix([[0, -sp.I * half], [sp.I * half, 0]]),
        sp.Matrix([[half, 0], [0, -half]]),
    ]

    for index, generator in enumerate(generators):
        assert_equal(
            f"SU(2) generator {index} trace",
            sp.simplify(trace(generator)),
            0,
        )

    for a, generator_a in enumerate(generators):
        for b, generator_b in enumerate(generators):
            expected = half if a == b else 0
            assert_equal(
                f"SU(2) trace normalization {a},{b}",
                sp.simplify(trace(generator_a * generator_b)),
                expected,
            )

    entangled_color = sp.simplify(
        sum(
            trace(generator_a * generator_b) * trace(generator_b * generator_a)
            for generator_a in generators
            for generator_b in generators
        )
    )
    assert_equal(
        "SU(2) cross-hadron entangled color factor",
        entangled_color,
        half * half * (2 * 2 - 1),
    )

    separate_single_loop_color = sp.simplify(
        sum(
            trace(generator_a) * trace(generator_b)
            for generator_a in generators
            for generator_b in generators
        )
    )
    assert_equal("separate TMD order-g anomaly vanishes", separate_single_loop_color, 0)
    if entangled_color == 0:
        raise AssertionError("cross-hadron two-gluon color factor should be nonzero")

    pi = sp.pi
    same_side_eikonal_delta = (-2 * sp.I * pi) * (-2 * sp.I * pi)
    same_side_spin_phase = -1
    opposite_side_eikonal_delta = (2 * sp.I * pi) * (-2 * sp.I * pi)
    opposite_side_spin_phase = 1
    assert_equal(
        "same-side eikonal plus spin sign",
        sp.simplify(same_side_eikonal_delta * same_side_spin_phase),
        4 * pi**2,
    )
    assert_equal(
        "opposite-side eikonal plus spin sign",
        sp.simplify(opposite_side_eikonal_delta * opposite_side_spin_phase),
        4 * pi**2,
    )
    assert_equal(
        "same/opposite Glauber terms add",
        sp.simplify(
            same_side_eikonal_delta * same_side_spin_phase
            + opposite_side_eikonal_delta * opposite_side_spin_phase
        ),
        8 * pi**2,
    )

    def eps_x(vector_y: float) -> float:
        # epsilon_perp(s, v) for s = xhat.
        return vector_y

    def rogers_mulders_mass_function(
        x: Fraction, hadron_mass: Fraction, quark_mass: Fraction, spectator_mass: Fraction
    ) -> Fraction:
        return (
            (1 - x) * quark_mass**2
            + x * spectator_mass**2
            - x * (1 - x) * hadron_mass**2
        )

    x1 = Fraction(1, 2)
    x2 = Fraction(1, 2)
    hadron_mass_1 = Fraction(1, 1)
    hadron_mass_2 = Fraction(6, 5)
    quark_mass_1 = Fraction(3, 4)
    quark_mass_2 = Fraction(4, 5)
    spectator_mass_1 = Fraction(7, 5)
    spectator_mass_2 = Fraction(3, 2)
    source_mass_1_squared = rogers_mulders_mass_function(
        x1, hadron_mass_1, quark_mass_1, spectator_mass_1
    )
    source_mass_2_squared = rogers_mulders_mass_function(
        x2, hadron_mass_2, quark_mass_2, spectator_mass_2
    )
    numerator_1 = hadron_mass_1 * (1 - x1) + spectator_mass_1
    numerator_2 = hadron_mass_2 * (1 - x2) + spectator_mass_2
    assert_equal("Rogers-Mulders L1^2 source mass", source_mass_1_squared, Fraction(809, 800))
    assert_equal("Rogers-Mulders L2^2 source mass", source_mass_2_squared, Fraction(217, 200))
    assert_equal("Rogers-Mulders spin numerator M1", numerator_1, Fraction(19, 10))
    assert_equal("Rogers-Mulders spin numerator M2", numerator_2, Fraction(21, 10))

    def lc_dot(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> float:
        return a[0] * b[1] + a[1] * b[0] - a[2] * b[2] - a[3] * b[3]

    def vector_add(
        a: tuple[float, float, float, float], b: tuple[float, float, float, float]
    ) -> tuple[float, float, float, float]:
        return tuple(left + right for left, right in zip(a, b))

    def vector_subtract(
        a: tuple[float, float, float, float], b: tuple[float, float, float, float]
    ) -> tuple[float, float, float, float]:
        return tuple(left - right for left, right in zip(a, b))

    hard_x1 = float(x1)
    hard_x2 = float(x2)
    hadronic_s = 148.0
    hard_boson_mass_squared = 2.0**2
    k3 = (2.5, 49.0 / 20.0, 3.5, 0.0)
    k4 = (2.5, 1.25, -2.5, 0.0)
    hard_lower_bound = (42.25**2) / (74.0 * 67.5**2)
    hard_upper_bound = (81.5**2) / (74.0 * 16.5**2)

    def rogers_mulders_hard_factor(k_x: float, k_y: float) -> float:
        k1 = (5.0, 0.0, k_x, k_y)
        k2 = (0.0, 37.0 / 10.0, 1.0 - k_x, -k_y)
        numerator = lc_dot(vector_add(k1, k3), vector_add(k2, k4))
        denominator = lc_dot(vector_subtract(k1, k3), vector_subtract(k1, k3)) - hard_boson_mass_squared
        if numerator <= 0.0 or denominator >= 0.0:
            raise AssertionError("chosen hard window should keep the Rogers-Mulders hard factor nonsingular")
        hard_factor = (numerator / denominator) ** 2 / (2.0 * hard_x1 * hard_x2 * hadronic_s)
        if not hard_lower_bound <= hard_factor <= hard_upper_bound:
            raise AssertionError("Rogers-Mulders hard factor escaped the declared compact-window bound")
        return hard_factor

    def gauss_nodes(n: int, left: float, right: float) -> list[tuple[float, float]]:
        nodes, weights = gauss_legendre(n, 30)
        midpoint = 0.5 * (left + right)
        half_width = 0.5 * (right - left)
        return [
            (midpoint + half_width * float(node), half_width * float(weight))
            for node, weight in zip(nodes, weights)
        ]

    def reduced_l_scalar(
        k_squared: float,
        deformation_mass_squared: float,
        source_mass_squared: float,
        feynman_nodes: list[tuple[float, float]],
    ) -> float:
        total = 0.0
        for z, weight in feynman_nodes:
            denominator = (
                z * deformation_mass_squared
                + (1.0 - z) * source_mass_squared
                + z * (1.0 - z) * k_squared
            )
            if denominator <= 0.0:
                raise AssertionError("Feynman-parameter denominator should be positive")
            total += weight * (1.0 - z) / denominator
        if total <= 0.0:
            raise AssertionError("positive-deformation transverse l integral should have positive scalar weight")
        return total

    def compact_positive_deformation_spectator_integral(k_order: int) -> float:
        q_x = 1.0
        q_y = 0.0
        transverse_window = 3.0
        deformation_mass_squared = float(Fraction(1, 9))
        mass_1_squared = float(source_mass_1_squared)
        mass_2_squared = float(source_mass_2_squared)
        source_numerator_product = float(numerator_1 * numerator_2)
        feynman_nodes = gauss_nodes(18, 0.0, 1.0)

        total = 0.0
        for k_x, weight_x in gauss_nodes(k_order, -transverse_window, transverse_window):
            for k_y, weight_y in gauss_nodes(k_order, -transverse_window, transverse_window):
                k_squared = k_x * k_x + k_y * k_y
                q_minus_k_squared = (q_x - k_x) ** 2 + (q_y - k_y) ** 2
                denominator = (k_squared + mass_1_squared) * (
                    q_minus_k_squared + mass_2_squared
                )
                l1_weight = reduced_l_scalar(
                    k_squared,
                    deformation_mass_squared,
                    mass_1_squared,
                    feynman_nodes,
                )
                l2_weight = reduced_l_scalar(
                    q_minus_k_squared,
                    deformation_mass_squared,
                    mass_2_squared,
                    feynman_nodes,
                )
                spin_projection = eps_x(k_y) * eps_x(q_y - k_y)
                if spin_projection > 0.0:
                    raise AssertionError("chosen double-spin projection should be sign-definite")
                total += (
                    weight_x
                    * weight_y
                    * rogers_mulders_hard_factor(k_x, k_y)
                    * source_numerator_product
                    * spin_projection
                    * l1_weight
                    * l2_weight
                    / (16.0 * math.pi**2 * denominator)
                )
        return total

    coarse_integral = compact_positive_deformation_spectator_integral(18)
    refined_integral = compact_positive_deformation_spectator_integral(26)
    quadrature_error_bound = 4.0 * abs(refined_integral - coarse_integral)
    if refined_integral + quadrature_error_bound >= 0.0:
        raise AssertionError("positive-deformation spectator witness is not sign-separated from zero")
    relative_gap = quadrature_error_bound / abs(refined_integral)
    if relative_gap > 0.01:
        raise AssertionError("positive-deformation spectator quadrature did not converge")


def massive_vector_sudakov_area(log_q2_over_m2: Fraction) -> Fraction:
    return log_q2_over_m2 * log_q2_over_m2 / 4


def check_massive_vector_sudakov_area() -> None:
    big_log = Fraction(6)
    # The chart is 0 < y < L and 0 < x < y/2.
    triangle_area = sum(
        Fraction(1, 4) * (right * right - left * left)
        for left, right in [(Fraction(0), big_log)]
    )
    assert_equal(
        "massive-vector Sudakov triangular area",
        triangle_area,
        massive_vector_sudakov_area(big_log),
    )

    alpha_times_c_over_pi = Fraction(5, 7)
    exponent = -alpha_times_c_over_pi * massive_vector_sudakov_area(big_log)
    assert_equal("massive-vector Sudakov exponent coefficient", exponent, Fraction(-45, 7))

    # Splitting the y interval checks additivity of the finite phase-space
    # integral before taking a continuum limit.
    pieces = [
        (Fraction(0), Fraction(2)),
        (Fraction(2), Fraction(5)),
        (Fraction(5), big_log),
    ]
    piecewise_area = sum(
        Fraction(1, 4) * (right * right - left * left)
        for left, right in pieces
    )
    assert_equal("piecewise massive-vector area", piecewise_area, massive_vector_sudakov_area(big_log))


def main() -> None:
    check_event_shape_convolution()
    check_distributional_factorization_remainder_bound()
    check_zero_bin_inclusion_exclusion()
    check_zero_bin_scheme_reshuffling()
    check_regulated_endpoint_region_expansion()
    check_multiplicative_scheme_covariance()
    check_rg_transport_common_scale_independence()
    check_soft_drop_boundary_scales_and_rg_consistency()
    check_soft_wilson_line_decoupling_identity()
    check_glauber_unitarity_diagnostic()
    check_symbolic_glauber_breaking_example()
    check_spectator_model_color_entanglement()
    check_massive_vector_sudakov_area()
    check_factorization_occurrence_ledger_inventory()
    print(
        "All SCET convolution, distributional-remainder, zero-bin, "
        "endpoint-expansion, scheme-covariance, RG-transport, soft-drop-scale, "
        "soft-Wilson-line, Glauber-unitarity/breaking, integrated "
        "spectator-model color-entanglement, massive-vector Sudakov, and "
        "occurrence-ledger checks passed."
    )


if __name__ == "__main__":
    main()
