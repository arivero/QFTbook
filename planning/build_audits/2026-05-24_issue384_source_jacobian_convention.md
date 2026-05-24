# Issue 384: Source Jacobian Convention Dependence

GitHub issue #384 flagged that the LSZ chapter displayed the connected
cumulant prefactor \(\ii^{-N}\) for the source convention
\(Z[J]=\langle T\exp(\ii\int J\phi)\rangle\), but did not state how the
prefactor changes if the source coupling is chosen with the opposite sign.

Edits made:

- Added the alternate source functional
  \[
    Z_-[J]=\langle T\exp(-\ii\int J\phi)\rangle .
  \]
- Displayed the corresponding connected-distribution extraction:
  \[
    G_N^{\rm conn}
    =
    \left.
    (-\ii)^{-N}
    \frac{\delta^N\log Z_-[J]}
         {\delta J(x_1)\cdots\delta J(x_N)}
    \right|_{J=0}
    =
    \left.
    \ii^N
    \frac{\delta^N\log Z_-[J]}
         {\delta J(x_1)\cdots\delta J(x_N)}
    \right|_{J=0}.
  \]
- Stated explicitly that the source-derivative Jacobian changes with the sign
  chosen in the source coupling, while the Green function does not.
- Updated the chapter dossier notation, claim ledger, and audit notes.

This pins the convention at the LSZ source-functional point so later Lorentzian
and Euclidean source-functional discussions can inherit it without sign drift.
