(* ::Package:: *)
(* Convention checks for gamma traces and anomaly normalizations.

   This is a plain Wolfram Language companion to gamma_trace_checks.py.
   It avoids Notebook-only structure so that both readers and agents can
   inspect it.  The four-dimensional matrices are the Weinberg-compatible
   mostly-plus matrices used in the stringbook spinor appendix and in the
   stringbook "gamma matrices.nb" notebook. *)

ClearAll["Global`*"];

id2 = IdentityMatrix[2];
zero2 = ConstantArray[0, {2, 2}];
sigma[1] = {{0, 1}, {1, 0}};
sigma[2] = {{0, -I}, {I, 0}};
sigma[3] = {{1, 0}, {0, -1}};

block[a_, b_, c_, d_] := ArrayFlatten[{{a, b}, {c, d}}];

gammaW[0] = -I block[zero2, id2, id2, zero2];
Do[
  gammaW[j] = -I block[zero2, sigma[j], -sigma[j], zero2],
  {j, 1, 3}
];

gammaWB[0] = block[zero2, id2, -id2, zero2];
Do[
  gammaWB[j] = block[zero2, sigma[j], sigma[j], zero2],
  {j, 1, 3}
];

eta = DiagonalMatrix[{-1, 1, 1, 1}];
id4 = IdentityMatrix[4];
zero4 = ConstantArray[0, {4, 4}];
uChiralPhase = block[id2, zero2, zero2, I id2];

eps[inds__Integer] := Module[{list = {inds}},
  If[Length[DeleteDuplicates[list]] < Length[list], 0, Signature[list + 1]]
];

assert[name_, statement_] := If[TrueQ[statement],
  Null,
  Print["FAILED: ", name];
  Throw[$Failed]
];

assertMatrix[name_, lhs_, rhs_] := assert[name, Simplify[lhs - rhs] == 0 lhs];

Do[
  assertMatrix[
    "Clifford " <> ToString[mu] <> ToString[nu],
    gammaW[mu].gammaW[nu] + gammaW[nu].gammaW[mu],
    2 eta[[mu + 1, nu + 1]] id4
  ],
  {mu, 0, 3}, {nu, 0, 3}
];

Do[
  assertMatrix[
    "Weinberg/Wess-Bagger phase " <> ToString[mu],
    gammaW[mu],
    uChiralPhase.gammaWB[mu].Inverse[uChiralPhase]
  ],
  {mu, 0, 3}
];

gamma5 = -I gammaW[0].gammaW[1].gammaW[2].gammaW[3];
assertMatrix["gamma5 squared", gamma5.gamma5, id4];
assertMatrix["gamma5 diagonal", gamma5, DiagonalMatrix[{1, 1, -1, -1}]];

Do[
  assertMatrix[
    "gamma5 anticommutes " <> ToString[mu],
    gamma5.gammaW[mu] + gammaW[mu].gamma5,
    zero4
  ],
  {mu, 0, 3}
];

Do[
  assert[
    "gamma5 trace " <> ToString[{mu, nu, rho, sig}],
    Simplify[
      Tr[gamma5.gammaW[mu].gammaW[nu].gammaW[rho].gammaW[sig]]
      == 4 I eps[mu, nu, rho, sig]
    ]
  ],
  {mu, 0, 3}, {nu, 0, 3}, {rho, 0, 3}, {sig, 0, 3}
];

gamma2[0] = I sigma[2];
gamma2[1] = sigma[1];
gamma2Chi = gamma2[0].gamma2[1];

Do[
  assert[
    "2D chirality trace " <> ToString[{nu, rho}],
    Simplify[Tr[gamma2[nu].gamma2Chi.gamma2[rho]] == 2 eps[rho, nu]]
  ],
  {nu, 0, 1}, {rho, 0, 1}
];

one = {{1}};
axialLeft = one;
axialRight = -one;
vector = one;
coeffWithoutHalf = Tr[axialLeft.(vector.vector + vector.vector)]
  - Tr[axialRight.(vector.vector + vector.vector)];
coeffWithHalf = coeffWithoutHalf/2;
assert["raw anticommutator gives four", coeffWithoutHalf == 4];
assert["mixed-anomaly coefficient gives two", coeffWithHalf == 2];

Print["All Wolfram Language gamma-trace and anomaly-normalization checks passed."];
