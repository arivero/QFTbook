# 2026-05-30 WZW Level Dequoted

## Scope

GitHub issue: #696, anomaly quoted-theorem proof debt.

The QCD Wess--Zumino--Witten level matching statement in Volume II,
Chapter 21 was still in a `quotedtheorem` environment even though the
manuscript already fixed the flavor trace convention and displayed the
descent coefficient comparison.  That made a QFT anomaly conclusion look like
an imported black box.

## Change

- Removed `qthm:wzw-anomaly-matching`.
- Rewrote the passage as "WZW level matching from the flavor descent
  coefficient."
- The text now states explicitly that the equality \(n=N_c\) is the
  coefficient matching between:
  - \(N_c\) color copies of the left-handed quark flavor anomaly in the
    half-trace convention \(\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab}\);
  - the unit-level gauged WZW variation normalized by the five-dimensional
    Wess--Zumino functional.
- The higher powers of the background field are described as fixed by
  Wess--Zumino consistency inside the same local cocycle class, up to local
  counterterms, rather than as independent assumptions.
- Cross-references in the CFL anomaly-matching discussion now point to the
  local WZW level-matching argument/equation rather than to a quoted theorem.

## Remaining Boundary

The full term-by-term gauged WZW functional is still not expanded in this
chapter.  The chapter uses the defining variation and the neutral-pion
two-photon coefficient.  Issue #696 remains open for finite \(SU(2)\) global
anomaly phases, determinant/Pfaffian-line holonomy, APS/eta bridges, and other
anomaly theorem-boundary blocks.
