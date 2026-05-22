# Volume II, Chapter 13 Dossier: Renormalized Operators And Minimal Subtraction

## Source Position

- Primary local source: second-sequence handwritten material, from the bottom
  of page 110 through page 118.
- Immediate predecessor: the 1PI renormalization group.
- Immediate successor in the source order: the stress-tensor trace and scale
  dependence.
- Role in the monograph: extend 1PI RG from couplings to local operator
  insertions, then introduce dimensional regularization and minimal
  subtraction as a coordinate system whose pole structure controls beta
  functions.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, bottom of page 110
  and pages 111--118; checked against rendered page images in
  `monograph/tex/build/source_visual_operators_ms/`.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`, the
  operator/MS block beginning after the 1PI RG discussion, used only as a
  comparison layer.
- `SRC-EXTERNAL`: standard dimensional-regularization and MS structure, with
  previous BPHZ/locality chapters supplying the perturbative locality
  controls.  No axiomatic framework is used as a foundation.

## Construction Task

The chapter must define:

- infinitesimal local deformations
  \(\delta S=\int \dd^Dx\,\sum_I\delta g_I O_I\);
- smooth compactly supported source deformations
  \(\delta S_\eta=\int\dd^Dx\,\eta_0^I(x)O_I(x)\), with constant sources as
  the coupling-deformation special case;
- the source-renormalization relation
  \(\eta_0^I(x)=\eta_\mu^J(x)N_{JI}(\mu)\);
- the relation between bare deformation coefficients \(\delta g_I\) and
  running deformation coefficients \(\delta g_I(\mu)\);
- the renormalized operator
  \([O_I]_\mu=\sum_J N_{IJ}(\mu)O_J\);
- the source-extended finite-regulator Wilsonian pushforward
  \(L_\Lambda[\phi;\eta_\Lambda]\) with a local differential source map
  \(\eta_0=\mathcal Z_\Lambda\eta_\Lambda\);
- the sign convention
  \(-\delta W/\delta\eta=\langle O\rangle\) for Euclidean sources coupled
  through the action;
- the Wilsonian composite representative
  \(\mathcal O_{\Lambda,A}^{\rm W}=\delta L_\Lambda/\delta\eta_\Lambda^A\)
  and its distinction from connected and 1PI insertion kernels;
- the source-extended connected-functional equality
  \(W_\Lambda^{\rm low}[J,\eta_\Lambda]
    =W_{\Lambda_0}[J,\eta_0(\eta_\Lambda)]\) at finite regulator;
- the 1PI insertion representative
  \(\mathcal O^\Gamma_{\Lambda,A}
    =-\delta\Gamma_\Lambda/\delta\eta_\Lambda^A\);
- a worked finite-regulator insertion example for
  \(O_m=\frac12\phi^2\) in scalar \(\phi^4\), including the covariance split
  of the insertion bubble, the Wilsonian insertion representative, the
  BPHZ normal-product subtraction, and the 1PI source-coordinate
  normalization condition;
- the full local Taylor expansion of the source coordinate map
  \(\eta_0=\mathcal Z_\Lambda(\eta_\Lambda)\) needed for multiple
  insertions and contact terms;
- the partition formula for multi-insertion connected distributions under a
  nonlinear local source-coordinate change;
- the two-insertion Wilsonian identity separating the connected product of
  one-insertion representatives from the second source derivative of the
  Wilsonian action;
- the corresponding 1PI source-Hessian identity showing the
  Legendre-transform subtraction by the low-field two-point function;
- the anomalous-dimension transformation law under scale-dependent
  source-coordinate changes,
  \(\widetilde\gamma=M\gamma M^{-1}-(\dd M/\dd t)M^{-1}\);
- the anomalous-dimension matrix
  \(\gamma_{IK}=\partial\beta_K/\partial g_I\) in this deformation
  convention;
- operator running and its diagonal/scaling form;
- the field operator as the special case governed by \(Z(\mu)\);
- the operator-insertion Callan--Symanzik equation derived from
  \(G_I^{(n)}=Z_\phi^{-n/2}N_{IJ}G_{0,J,\Lambda}^{(n)}\), with contact terms
  excluded from the noncoincident equation and described as local collision
  terms;
- the dimensional-regularization action in \(D=d-\epsilon\);
- engineering dimensions
  \([\phi]=(d-\epsilon-2)/2\),
  \([O_I]=d-\epsilon+\delta_I(\epsilon)\), and
  \([g_I^\epsilon]=-\delta_I(\epsilon)\);
- the MS coordinate definition
  \(g_I^\epsilon=\mu^{-\delta_I(\epsilon)}
   [\lambda_I+\sum_{n\ge1}\epsilon^{-n}K_I^{(n)}]\);
- the one-loop \(d=4\), \(\phi^4\) example that produces the
  \(3/(16\pi^2\epsilon)\) pole;
- the \(d-\epsilon\) beta function
  \(\beta_I^\epsilon=\dd\lambda_I/\dd\log\mu\);
- the Laurent expansion of \(\beta_I^\epsilon\) and the conclusion
  \(\beta_I^\epsilon=\beta_I(\lambda)+\epsilon\delta_I^{(1)}\lambda_I\);
- the recursive pole equations that determine \(K_I^{(n)}\) from
  \(\beta_I(\lambda)\).

## Claim Ledger

1. Renormalized local operators are defined by the response of the action to
   renormalized infinitesimal source deformations; constant sources recover
   coupling deformations.
2. The mixing matrix \(N_{IJ}(\mu)\) is fixed by the same beta functions that
   govern the couplings.
3. In the chosen convention,
   \(\dd N_{IJ}/\dd\log\mu=-\gamma_{IK}N_{KJ}\), with
   \(\gamma_{IK}=\partial\beta_K/\partial g_I\).
4. If \(\gamma\) is diagonal along the flow, operator running exponentiates;
   at a fixed point it becomes a power law.
5. The elementary field operator satisfies
   \([\phi]_\mu=Z(\mu)^{-1/2}\phi\) and
   \(\gamma_\phi=\frac12\dd\log Z/\dd\log\mu\).
6. At finite regulator, a source-extended Wilsonian action preserves
   connected low-momentum correlators with local-operator insertions after
   the local source-coordinate map is applied.
7. A Wilsonian composite insertion is the source derivative of the Wilsonian
   action; the corresponding 1PI insertion is obtained by low-field
   integration followed by Legendre transform.
8. In the mass-operator example, the full one-loop insertion bubble splits
   into high-high, low-low, and mixed covariance assignments.  The high-high
   part corrects the Wilsonian insertion, the low-low part is produced by the
   remaining low-field 1PI insertion, and the mixed part is represented by
   local source-coordinate data in the low-momentum expansion.
9. For multiple inserted operators, the finite-regulator chain rule for the
   full local source chart expresses renormalized distributions as a sum over
   partitions of the insertion labels.  The singleton partition gives the
   noncoincident operator mixing, while partitions with larger blocks are
   local distributions supported on collision diagonals.
10. Under scale-dependent finite changes of renormalized source coordinates,
   anomalous dimensions transform by the connection law
   \(\widetilde\gamma=M\gamma M^{-1}-(\dd M/\dd t)M^{-1}\).
11. The operator-insertion Callan--Symanzik equation follows by
   differentiating the renormalized insertion chart at fixed bare data.
12. Contact terms in inserted correlators are local distributions supported on
   collision diagonals and depend on the contact-term convention.
13. Minimal subtraction defines dimensionless couplings by retaining only pole
   terms in the relation between bare and renormalized couplings.
14. In four-dimensional scalar quartic theory, the one-loop MS relation is
   \(g^\epsilon=\mu^\epsilon[\lambda+3\lambda^2/(16\pi^2\epsilon)+O(\lambda^3)]\).
15. The \(\mu\)-independence of bare couplings constrains the Laurent expansion
   of \(\beta_I^\epsilon\).
16. Perturbative order counting implies
   \(\beta_I^{(m)}=0\) for \(m\ge2\) and
   \(\beta_I^{(1)}=\delta_I^{(1)}\lambda_I\).
17. The nonnegative epsilon structure of the MS beta function leaves the
    \(\epsilon^0\) beta function as the beta function of the target
    \(d\)-dimensional theory; the remaining pole coefficients are determined
    recursively, with the homogeneous-sector form reproducing the source
    equations involving
    \((1-\lambda_J\partial_{\lambda_J})K_I^{(n)}\).

## Figure Requirements

- Operator mixing matrix \(N_{IJ}\) and induced flow generated by
  \(\gamma_{IK}\).
- Field insertion special case showing that the running is the wavefunction
  normalization.
- Source-extended Wilsonian/operator bridge showing the path from bare
  sources to Wilsonian insertions, connected insertions, 1PI insertion
  kernels, and projected mixing data.
- Mass-operator insertion matching diagram showing the split of the one-loop
  insertion bubble into high-high, low-low, and mixed contributions and their
  images in the Wilsonian insertion, low-field 1PI insertion, and local
  source-coordinate map.
- Multi-insertion contact-coordinate diagram separating the linear source
  jet controlling noncoincident mixing from higher source jets supported on
  collision diagonals.
- Minimal-subtraction pole structure diagram.
- One-loop \(\phi^4\) MS subtraction diagram with the pole coefficient.
- Laurent/recursive structure figure showing how positive powers of
  \(\epsilon\) constrain \(\beta_I^\epsilon\) and nonpositive powers determine
  \(K_I^{(n)}\).

## Audit Notes

- No reader-facing source-page references.
- Do not collapse operator renormalization into a slogan about composite
  operators; define it through infinitesimal deformations.
- Keep stress-tensor trace material for the next chapter.
- State all index conventions for \(N_{IJ}\), \(\gamma_{IK}\), and
  \(K_I^{(n)}\).
- Make clear that \(\gamma_{IK}=\partial\beta_K/\partial g_I\) is the
  deformation-operator convention for the selected coordinate chart; arbitrary
  local operators require enlarging the chart or adding an independent mixing
  matrix.
- Operator-insertion Callan--Symanzik equations must be derived from the
  source/insertion renormalization chart, not quoted without proof.
- Separate noncoincident correlator equations from contact-term conventions.
- Keep the MS discussion as a coordinate construction, not as an ontological
  foundation.
- Keep Wilsonian composite representatives, connected insertions, and 1PI
  insertion kernels as separate objects connected by explicit maps.
- State the Euclidean source sign convention before using source derivatives.
- Treat scale-dependent source redefinitions as connection transformations
  for anomalous dimensions.
- 2026-05-22 source-certification pass: the handwritten pages from the bottom
  of page 110 through page 118 were checked end-to-end against the two local
  transcription layers.  The manuscript now includes the full derivative of
  \(\delta g_I=\delta g_J(\mu)N_{JI}\), the arbitrary-displacement argument
  leading to \(\dd N/\dd\log\mu=-\gamma N\), the field-operator
  \(Z^{-1/2}\) specialization, the \(d=4\ \phi^4\) one-loop MS pole
  \(3/(16\pi^2\epsilon)\), the positive-power constraints on
  \(\beta_I^\epsilon\), and both the general and homogeneous recursive pole
  equations.
- 2026-05-22 insertion-matching pass: added a worked finite-regulator
  source-bridge example for \(O_m=\phi^2/2\).  The manuscript now defines the
  insertion bubble \(\mathcal I_{A,B}(Q)\), splits it by covariance
  assignment, writes the Wilsonian mass insertion, writes the BPHZ normal
  product subtraction at \(\mathcal Q_\mu\), and derives the 1PI
  source-coordinate normalization condition.
- 2026-05-22 multi-insertion contact pass: added the full local Taylor
  expansion of the source coordinate chart, the partition formula for
  multiple connected insertions, the noncoincident/contact-term separation,
  the two-insertion Wilsonian identity, and the 1PI source-Hessian identity.
