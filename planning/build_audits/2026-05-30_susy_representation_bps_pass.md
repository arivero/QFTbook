# SUSY Representation BPS And Central-Charge Pass

Date: 2026-05-30

Related issue: #691

## Scope

This pass continued the semantic theorem/proposition audit in Volume VII,
Chapter 1.  The goal was not to demote every compact representation-theory
statement, but to separate convention bookkeeping from genuine positivity
content.

## Changes

- Demoted `Central-charge tensor structure` from proposition/proof form to a
  paragraph-level derivation.  Its content is the Lorentz tensor decomposition
  of two left Weyl spinors, the HLS exclusion of extra spacetime-tensor
  charges, combined-index antisymmetry, and the graded Jacobi identity for
  internal invariance.  That material remains explicit, but no longer appears
  as an independent proposition under the quoted HLS theorem.
- Fixed the central-charge normalization in the chapter to
  \[
    \{Q^I_\alpha,Q^J_\beta\}=2\epsilon_{\alpha\beta}Z^{IJ}.
  \]
  This is the normalization needed for the stated BPS inequality
  \(m\ge z_s\) when \(z_s\) is a singular value of \(Z\).
- Strengthened `Rest-frame BPS bound from singular values` rather than
  demoting it.  The proof now states the skew Takagi normal form, displays the
  Hermitian anticommutator block
  \[
    2\begin{pmatrix}m&z_s\\ z_s&m\end{pmatrix},
  \]
  constructs the combinations \(R_\pm\), derives the eigenvalues
  \(2(m\pm z_s)\), and separates the representation-theoretic shortening
  criterion from the dynamical question of whether a QFT contains saturating
  states.

## Harness And Dossier

- `tools/audit_theorem_form.py` now rejects reintroducing `Central-charge tensor
  structure` as a theorem-family wrapper.
- The Volume VII, Chapter 1 dossier records the \(2\epsilon Z\) convention and
  the strengthened BPS block proof.
- `calculation-checks/susy_representation_checks.py` had its central-charge
  symmetry comment updated to match the normalization; the executable checks
  already used the \(2(m\pm z)\) positivity eigenvalues.

## Status

Issue #691 remains open.  This pass removed one proposition wrapper and
strengthened one retained proposition whose proof carries actual Hilbert-space
positivity content.
