# Issue #257 Bloch--Nordsieck Limit-Order Pass

## Scope

- Oldest active GitHub issue: `#257`, on the inclusive probability discussion
  in
  `monograph/tex/volumes/volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex`.
- Required repair: state the order of operations in the Bloch--Nordsieck
  cancellation and prove that the cancellation is an inclusive, coefficientwise
  statement rather than a termwise fixed-photon-number statement.

## Content Added

- Renamed the opening definition to "Regulated resolution-inclusive transition
  probability" and wrote the regulated object as
  \(P^{(\mu)}_{\beta|\alpha}(E_T)\).
- Added a forward pointer that the regulator-free inclusive probability is an
  ordered limit, not the termwise fixed-\(N\) limit.
- Labeled the inclusive-probabilities section for cross-reference.
- Stated the order of construction:
  fix \(0<\mu<E_T<M\), compute in the regulated theory, form the inclusive
  detector-degenerate sum at fixed regulator, and only then remove \(\mu\).
- Introduced
  \(\ell_T(\mu)=\log(E_T/\mu)\) and
  \(\ell_M(\mu)=\log(M/\mu)\), and wrote the real \(N\)-photon contribution
  and virtual rate factor separately.
- Added the proposition "Coefficientwise Bloch--Nordsieck cancellation":
  at order \(A_{\beta\alpha}^L\), the sum over \(N=0,\ldots,L\) real photons
  together with the virtual powers gives
  \[
    \sum_{N=0}^{L}
    \frac{[-\ell_M(\mu)]^{L-N}}{(L-N)!}
    \frac{\ell_T(\mu)^N}{N!}
    =
    \frac{1}{L!}\left(\log\frac{E_T}{M}\right)^L.
  \]
- Added an explicit proof of the binomial cancellation before taking
  \(\mu\downarrow0\).
- Clarified that the exponentiated leading-soft expression is a resummation of
  coefficientwise cancellations and cannot be interpreted as a termwise
  fixed-photon-number regulator limit.
- Updated the chapter dossier claim ledger and audit notes.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
