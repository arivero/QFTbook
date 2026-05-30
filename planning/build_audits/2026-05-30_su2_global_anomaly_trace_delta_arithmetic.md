# 2026-05-30 SU(2) Global Anomaly Trace-Delta Arithmetic

## Target

- GitHub issue #696, anomaly quoted-theorem proof-debt cluster.
- File:
  `monograph/tex/volumes/volume_xii/chapter07_eta_invariants_global_anomalies.tex`.

## Finding

The Witten \(SU(2)\) global-anomaly section correctly kept the
five-dimensional mod-two index theorem as quoted global-analysis input, but
the representation-theoretic normalization in the theorem statement was too
compressed.  The reader should not have to infer how the monograph's
trace-delta convention turns the spin-\(j\) representation into the integer
\(T_\Delta(R_j)=n(n+1)(n+2)/6\), nor which part of the anomaly criterion is
ordinary finite-dimensional arithmetic rather than the quoted index theorem.

## Change

- Added a `Trace-delta normalization in the SU(2) representation ring`
  paragraph after the quoted mod-two index theorem.
- Derived
  \[
    \operatorname{tr}_{R_j}(J_aJ_b)
    =
    \frac13j(j+1)(2j+1)\delta_{ab}
  \]
  from the \(J_3\)-weight sum.
- Converted to the monograph convention \(t_a=\sqrt2 J_a\), obtaining
  \[
    T_\Delta(R_j)=\frac23j(j+1)(2j+1)
    =\frac{n(n+1)(n+2)}6,\qquad n=2j .
  \]
- Derived the parity criterion \(T_\Delta(R_j)\) odd iff
  \(2j\equiv1\pmod4\), using \(\binom{n+2}{3}\) modulo two.
- Updated the chapter dossier.

## Status

This pass does not prove the five-dimensional real mod-two index theorem.
It narrows the quoted-theorem boundary: the remaining external input is the
mapping-torus index equality, while the trace convention and parity criterion
are now derived in the manuscript.
