# 2026-05-30 Liouville Stringbook Derivation Check

## Scope

- Reviewed the local stringbook source
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  especially the Liouville CFT appendix around `\label{liouvillecftsec}` and
  the \(c=25\) ZZ/FZZT boundary-state discussion.
- Compared the current monograph Liouville chapter against the stringbook
  conventions for the scattering-normalized fields \(V_P\), the two-point
  normalization \(\pi\delta(P-P')\), the \(P\)-basis DOZZ representative, the
  reflection phase \(S(P)\), and the special \(b=1\) FZZT normalization.

## Edits

- Tightened the probabilistic zero-mode reduction by spelling out the
  normalization map \(\gamma=2b\) and
  \(\alpha_i^{\mathrm{prob}}=2\alpha_i\) for
  \(V_{\alpha_i}=\mathopen{:}\exp(2\alpha_i\phi)\mathclose{:}\).
- Replaced the imprecise post-Girsanov expectation with the negative moment
  of the explicit GMC functional \(Z_g\), with deterministic Green-function
  and gamma-function factors kept outside the expectation.
- Added the reflection-phase extraction from the pole
  \(\epsilon=Q/2+i(P_1+P_2+P_3)\) of the scattering-normalized DOZZ constant,
  including both the \(\Upsilon_b\)-ratio and gamma-ratio forms of \(S(P)\).
- Recorded in the chapter dossier that the stringbook \(c=25\) FZZT formula
  is being used as a special-normalization check, while the monograph keeps
  the general-\(b\) boundary bootstrap normalization explicit.

## Remaining Boundary

- The full boundary Liouville sewing construction remains an open problem in
  the chapter.  The present pass checked the normalization spine but did not
  turn the FZZT/ZZ bootstrap formulas into a complete functorial boundary
  theory.
