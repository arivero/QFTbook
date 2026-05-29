# Thirty-Fifth Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: continued Issue #691 proof-substance audit, with emphasis on
hypothesis-heavy statements and theorem-family environments whose proof body
does not carry the advertised mathematical load.

Changes made:

- Downgraded finite-regulator Euclidean convexity from theorem to proposition.
  The result is rigorous at finite positive Euclidean regulator, but the hard
  QFT input is the positivity assumption; the proof itself is Holder plus
  Legendre--Fenchel convexity.
- Demoted the planar \(\mathcal N=4\) two-site scalar mixing tensor from a
  proposition/proof to a convention-fixing one-loop derivation paragraph.  The
  paragraph now states explicitly that this is not a nonperturbative theorem
  and not a replacement for a full component-diagram listing.
- Demoted the pure-SYM BPS wall-tension formula from a proposition/proof to a
  square-completion derivation paragraph.  The new closing sentence separates
  the elementary effective-chart algebra from the nontrivial construction of
  the wall sector and central-charge datum.
- Demoted the Landau--Ginzburg quasihomogeneous charge/central-charge statement
  from a proposition/proof to an algebraic protected-data paragraph.  The text
  now says explicitly that the central-charge formula is a necessary
  anomaly-matching datum, not a proof of the infrared fixed point.
- Expanded the BV observable-differential proof by displaying the generated
  bracket identity, the odd-Jacobi square of \(\operatorname{ad}_S\), the
  cancellation of the Laplacian-bracket cross terms, and the final reduction to
  the QME Hamiltonian bracket.

Additional audit observations:

- The original 47 labels listed in Issue #691 no longer occur in the current
  TeX sources.
- The local \(P\)-\(Q\) bridge example in the planar-QSC chapter is no longer a
  proposition/proof wrapper.  It is recorded as a nontrivial local analytic
  assumption followed by algebraic consequences in prose, which is the right
  presentation for this hypothesis-heavy construction.

Current count after edits:

- theorem: 94
- proposition: 367
- lemma: 29
- corollary: 10
- proof: 495
- theorem-family total: 500

The immediate short-proof queue has fallen to 40 entries at or below 170 proof
tokens.  Most of the leading entries now look like compact but genuine
structural lemmas; the next audit pass should continue reading them in context
because a short proof is only a queue signal, not evidence of triviality.
