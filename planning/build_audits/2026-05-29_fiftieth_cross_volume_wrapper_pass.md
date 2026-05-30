# Fiftieth Cross-Volume Wrapper Pass

Date: 2026-05-29

Purpose: continue issue #691 after checkpoint `04e1a4cf` by reading another
batch of compact proposition proofs and separating genuine theorem-level
machinery from examples and support lemmas.

## Demoted Or Re-ranked

- Volume II, Chapter 7:
  `Tempered distributions with unbounded representatives` is now an example.
  It is a constructed counterexample showing that temperedness does not imply a
  pointwise polynomial bound for a chosen representative.
- Volume III, Chapter 8:
  `Scalar three-point kinematics` is now a lemma.  The three-point form is a
  reusable conformal-kinematic support fact rather than proposition-level
  structure.
- Volume XI, Chapter 9:
  `Smooth enhanced-noise energy estimate` is now a lemma.  It is a PDE energy
  estimate supporting the stochastic-quantization assembly.
- Volume XI, Chapter 9:
  `Nelson stability implies normalized \(L^q\) density bounds` is now a
  lemma.  It is the measure-estimate step converting Nelson exponential
  stability into cutoff-uniform density bounds.
- Volume XII, Chapter 2:
  `Leading Hadamard transport equation` is now a lemma.  It is the leading
  transport identity for the point-splitting parametrix.
- Volume XII, Chapter 9:
  `Transport equation for \(U\)` is now a lemma.  It is the microlocal
  Hadamard-parametrix support identity \(U=\Delta^{1/2}\).

## Harness Update

`tools/audit_theorem_form.py` now rejects recurrence of the constructed
tempered-distribution counterexample as a theorem-family wrapper.  The
transport and estimate items remain allowed as lemmas: their rank is support
machinery, not proposition/theorem structure.

## Retained After Reading

The pass reread and retained several nearby compact items: the
Kallen--Lehmann representation, spectral-pole statements, the conformal
Killing-vector classification, conformal-collider inequalities, the
Kontsevich--Segal one-dimensional semigroup reconstruction, the pAQFT change
of Hadamard parametrix, and McKean--Singer.  Their proofs are compact because
they rely on earlier established machinery, not because they are merely
decorative substitutions.

## Remaining Work

The remaining queue still contains proposition/theorem statements whose rank
can only be judged by reading the full local development: local nets,
anomaly-obstruction statements, integrability algebra, BV pushforwards,
constructive RG, microlocal extension, and localization.  This issue remains
open.
