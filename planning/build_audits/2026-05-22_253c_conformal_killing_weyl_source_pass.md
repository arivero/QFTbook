# 2026-05-22 253c Conformal Killing and Weyl Coupling Pass

## Scope

Checked handwritten 253c pp. 7--18 against the compiled CFT chapters.  The
source visual trace was rendered to:

- `monograph/tex/build/source_visual_trace/253c_trace-007.png`
- `monograph/tex/build/source_visual_trace/253c_trace-008.png`
- `monograph/tex/build/source_visual_trace/253c_trace-009.png`
- `monograph/tex/build/source_visual_trace/253c_trace-010.png`
- `monograph/tex/build/source_visual_trace/253c_trace-011.png`
- `monograph/tex/build/source_visual_trace/253c_trace-012.png`
- `monograph/tex/build/source_visual_trace/253c_trace-013.png`
- `monograph/tex/build/source_visual_trace/253c_trace-014.png`
- `monograph/tex/build/source_visual_trace/253c_trace-015.png`
- `monograph/tex/build/source_visual_trace/253c_trace-016.png`
- `monograph/tex/build/source_visual_trace/253c_trace-017.png`
- `monograph/tex/build/source_visual_trace/253c_trace-018.png`

## Manuscript Changes

Updated:

- `monograph/tex/volumes/volume_iii/chapter02_conformal_killing_vectors_and_the_conformal_group.tex`
- `monograph/tex/volumes/volume_iii/chapter03_stress_tensor_weyl_structure_and_improvement.tex`

The revised material now includes:

- the conformal Killing current \(J^\mu_\epsilon=T^\mu{}_\nu\epsilon^\nu\)
  and the derivation of its conservation from stress-tensor symmetry,
  conservation, tracelessness, and the conformal Killing equation;
- the Lorentzian charge
  \(Q_\epsilon(\Sigma)=\int_\Sigma d\sigma\,n_\mu T^\mu{}_\nu\epsilon^\nu\)
  on a spacelike Cauchy surface, with the Stokes-theorem argument for
  surface independence;
- the \(D\ge3\) conformal Killing vector solution
  \(a^\mu+\omega^\mu{}_\nu x^\nu+\lambda x^\mu
    +c^\mu x^2-2(c\cdot x)x^\mu\);
- the charge commutator
  \([Q_{\epsilon_1},Q_{\epsilon_2}]=-\ii Q_{[\epsilon_1,\epsilon_2]}\) with
  the vector-field bracket and the contact-term/domain qualification;
- finite conformal maps as diffeomorphisms with
  \(\partial_\mu f^\rho\partial_\nu f^\sigma\delta_{\rho\sigma}
    =\Omega_f^2\delta_{\mu\nu}\), the composition rule for \(\Omega\), the
  Euclidean inversion check, and the special conformal transformation
  \(x^\mu\mapsto (x^\mu+c^\mu x^2)/(1+2c\cdot x+c^2x^2)\);
- the stress-tensor convention based on variation with respect to
  \(g^{\mu\nu}\), the small-metric perturbation insertion
  \(\exp[-\frac12\int \delta g^{\mu\nu}T_{\mu\nu}]\), and the role of
  coincident stress-tensor contact terms;
- the Weyl variation, trace condition, and anomaly qualification;
- the detailed conformally coupled scalar derivation, including the
  \(S_0+aS_1\) curvature term, the flat metric variation of \(S_1\), the
  improvement contribution to \(T_{\mu\nu}\), the trace calculation, and
  \(a=\xi_\ast=(D-2)/(4(D-1))\).

## Visual Audit

Rendered manuscript physical PDF pages 422--432 to
`/tmp/qft_cft_ckv_weyl_phys2-422.png`--`/tmp/qft_cft_ckv_weyl_phys2-431.png`
and `/tmp/qft_cft_weyl_tail-432.png`.

The source figures were rewritten as TikZ figures rather than embedded from
the handwritten pages:

- Figure 49.1: spacelike slice, future timelike normal, and conformal charge.
- Figure 49.3: Euclidean inversion with the unit sphere and the radial image
  \(I(x)=x/x^2\).
- Figure 50.1: curvature-coupling path from the flat scalar action to the
  improved traceless stress tensor.

No handwritten PDF page is embedded in the manuscript.

## Verification

Ran:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
tools/audit_monograph_text.sh
git diff --check
```

The PDF build completed successfully, the strict reader-facing text audit
passed, and `git diff --check` reported no whitespace errors.
