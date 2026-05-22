# Operator Source And Insertion Callan--Symanzik Audit

Date: 2026-05-22.

Development pass:

- Recast renormalized local operators as source-renormalized deformation
  operators using smooth compactly supported sources
  \(\eta_0^I(x)\), with constant sources as the coupling-deformation case.
- Made the matrix convention
  \(\eta_0^I=\eta_\mu^J N_{JI}\) explicit before defining
  \([O_I]_\mu=N_{IJ}O_J\).
- Clarified that the cotangent transformation law applies to operators dual to
  the selected coordinate chart; other local operators require an enlarged
  chart or an independent mixing matrix.
- Replaced the asserted operator-insertion Callan--Symanzik equation with a
  proposition derived from
  \(G_I^{(n)}=Z_\phi^{-n/2}N_{IJ}G_{0,J,\Lambda}^{(n)}\) at fixed bare data.
- Separated the noncoincident correlator equation from contact-term
  conventions supported on collision diagonals.
- Updated the chapter dossier with these requirements.

Verification:

- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- rendered and visually inspected the affected Chapter 33 pages of
  `/Users/xiyin/QFT/monograph/tex/main.pdf`

Result:

- All checks passed.
- The new source-renormalization definitions and proposition/proof block render
  cleanly.
