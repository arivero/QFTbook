# Reeh--Schlieder Tube-Sign and Boundary-Uniqueness Pass

Scope: Volume IV, Chapter 3, the Reeh--Schlieder theorem for weakly additive
vacuum nets.

Finding:

- The proof used the spectral integral
  `F_A(a)=<psi,U(a)A Omega>` correctly, but described the holomorphic
  continuation as `a+i b`, `b in V_+`.  With the monograph's mostly-plus
  convention and `U(a)=int exp(i a.p) dE(p)`, positive energy gives damping
  in the tube `M-i V_+`, not `M+i V_+`.
- The proof also compressed the boundary-uniqueness step into a phrase,
  even though the step is the analytic engine of the theorem.

Edit:

- Added Lemma `lem:positive-energy-tube-uniqueness`.
- The lemma proves holomorphy of finite positive-energy spectral matrix
  coefficients in `M-i V_+`, continuity of the real boundary value, and
  propagation of an open real-edge zero to the whole real edge using the
  distributional edge-of-the-wedge theorem.
- Updated the Reeh--Schlieder proof to invoke the lemma directly.
- Updated Figure `fig:reeh-schlieder-cyclicity` and its caption so the
  schematic tube is labelled as `M-i V_+` and the vertical coordinate is tube
  depth rather than the literal imaginary coordinate.
- Updated the chapter dossier with the new notation and claim ledger entries.

Follow-up sign sweep:

- The same convention mismatch was present in Volume IV, Chapter 1's
  Wightman tube-analyticity section and Figure `fig:wightman-tube-analyticity`.
- That section now defines the mostly-plus forward tube as
  `z_j = xi_j - i eta_j`, `eta_j in V_+`, and the figure labels the vertical
  coordinate as tube depth rather than `Im z in V_+`.
- The Chapter 1 dossier now records this convention explicitly.

Status:

- This strengthens issue #695 by making a foundational analytic step and a
  convention-sensitive tube sign explicit at the theorem's point of use.
- It does not close #695; the broader quoted-theorem proof-debt lane still
  includes other AQFT structural inputs and examples.
