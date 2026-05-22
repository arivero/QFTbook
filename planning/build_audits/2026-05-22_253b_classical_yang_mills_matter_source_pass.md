# 2026-05-22 253b Classical Yang--Mills And Matter Source Pass

## Scope

- Source block: handwritten 253b pages 157--168.
- Manuscript target:
  `monograph/tex/volumes/volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`.
- Comparison layers:
  `transcription/tex/253b/scattering_rg_qcd.tex` and
  `references/253b transcribed lecture notes.tex`.

## Source Items Checked

- Local gauge potential \(A_{a\mu}\), Hermitian generators \(t^a\), and
  \([t^a,t^b]=i f^{ab}{}_{c}t^c\).
- Infinitesimal law
  \(\delta A_\mu=\partial_\mu\zeta-i[A_\mu,\zeta]\) and component law
  \(\delta A^a_\mu=\partial_\mu\zeta^a+f^{bc}{}_{a}A^b_\mu\zeta^c\).
- Finite law
  \(A_\mu'=gA_\mu g^{-1}+i g\partial_\mu g^{-1}\) with
  \(g=\exp(i\zeta_a t^a)\), plus the BCH and adjoint-action closure
  identities.
- Curvature
  \(F_{\mu\nu}=i[\partial_\mu-iA_\mu,\partial_\nu-iA_\nu]\) and covariance
  \(F'_{\mu\nu}=gF_{\mu\nu}g^{-1}\).
- Invariant trace, including the source cyclicity identity
  \(\operatorname{tr}([t^a,t^b]t^c)=\operatorname{tr}(t^a[t^b,t^c])\),
  \(f^{abc}=f^{ab}{}_{e}\kappa^{ec}\), and complete antisymmetry.
- Yang--Mills action normalization, positive invariant quadratic form, compact
  reductive gauge algebra, \(SU(2)\) and \(SU(N)\) examples.
- \(D=4\) \(\theta\)-term: parity/time-reversal odd, locally a total
  derivative, no local perturbative vertex around the trivial sector, and
  nonzero contribution on finite-action topological sectors.
- Matter representations, fundamental, anti-fundamental, adjoint, covariant
  derivative, QCD quark indices, Hermitian scalar/pseudoscalar mass matrices,
  and chiral mass matrix notation.

## Manuscript Changes

- Added the source-level trace cyclicity equation before the conjugation
  invariance of the trace.
- Expanded the positivity/classification statement to name the abelian factors
  and compact simple Cartan types \(A,B,C,D,E,F,G\).
- Stated explicitly that the \(\theta\)-density does not modify local
  Euler--Lagrange equations under fixed-boundary variation, while preserving
  the nonperturbative topological-sector caveat.
- Added the finite anti-fundamental convention
  \(\rho_{\overline{\square}}(g)=g^*\) and the corresponding generator
  \(t_{\overline{\square}}^a=-(t^a)^*\).
- Added and render-checked a new \(SU(N)\) representation/QCD-index figure.

## Verification

- Built the full manuscript with `tools/build_monograph.sh`.
- Ran the strict text audit with `tools/audit_monograph_text.sh`.
- Ran `git diff --check`.
- Rendered the source pages with:
  `pdftoppm -png -f 157 -l 168 -r 180 'references/253b lecture notes 2023.pdf' /tmp/253b_157_168`.
- Rendered the manuscript chapter region with:
  `pdftoppm -png -f 346 -l 356 -r 170 monograph/tex/main.pdf /tmp/qft_ym_cert2`.
- After adjusting the representation figure, render-checked page 352 at
  `/tmp/qft_ym_repfig_fix2-352.png`; no overlaps or clipped figure labels
  remain.
