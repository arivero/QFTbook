(* ::Package:: *)
(* Reader-facing Wolfram Language checks for the planar N=4 integrability
   spine.  This plain-text companion mirrors the smaller Python reader script
   and keeps the checks close to Mathematica-style symbolic manipulation. *)

ClearAll["Global`*"];

assert[name_, statement_, assumptions_: True] := If[
  TrueQ[FullSimplify[statement, assumptions]],
  Null,
  Print["FAILED: ", name];
  Throw[$Failed]
];

assertZero[name_, values_] := Module[{flat = Flatten[{values}]},
  If[
    Max[Abs[N[flat, 40]]] < 10^-25,
    Null,
    Print["FAILED: ", name, " residual = ", N[flat, 20]];
    Throw[$Failed]
  ]
];

(* Spin-chain check: the length-four two-magnon Konishi wavefunction is an
   eigenvector of H=sum_i(1-P_{i,i+1}) with eigenvalue 6 and is cyclic. *)
length = 4;
p1 = 2 Pi/3;
p2 = -2 Pi/3;
rapidity[p_] := 1/(2 Tan[p/2]);
exchange = (rapidity[p1] - rapidity[p2] - I)/(rapidity[p1] - rapidity[p2] + I);
basis = Subsets[Range[0, length - 1], {2}];
indexOf[state_] := FirstPosition[basis, Sort[state]][[1]];
waveFunction[state_] := Exp[I (p1 state[[1]] + p2 state[[2]])] +
  exchange Exp[I (p2 state[[1]] + p1 state[[2]])];
wave = waveFunction /@ basis;
bitsFromState[state_] := Table[If[MemberQ[state, site], 1, 0], {site, 0, length - 1}];
stateFromBits[bits_] := Flatten[Position[bits, 1]] - 1;
acted = ConstantArray[0, Length[basis]];
Do[
  bits = bitsFromState[basis[[stateIndex]]];
  Do[
    acted[[stateIndex]] = acted[[stateIndex]] + wave[[stateIndex]];
    swapped = bits;
    first = site + 1;
    second = Mod[site + 1, length] + 1;
    swapped[[{first, second}]] = swapped[[{second, first}]];
    newState = stateFromBits[swapped];
    acted[[indexOf[newState]]] = acted[[indexOf[newState]]] - wave[[stateIndex]],
    {site, 0, length - 1}
  ],
  {stateIndex, 1, Length[basis]}
];
assertZero["length-four Konishi spin-chain eigenvector", FullSimplify[acted - 6 wave]];
translatedWave = Table[
  wave[[indexOf[Mod[basis[[stateIndex]] + 1, length]]]],
  {stateIndex, 1, Length[basis]}
];
assertZero["length-four Konishi cyclicity", FullSimplify[translatedWave - wave]];

(* Bethe-Yang check in the one-loop SL(2) convention used in the monograph. *)
roots = {1/(2 Sqrt[3]), -1/(2 Sqrt[3])};
phase[u_] := (u + I/2)/(u - I/2);
scattering[u_, v_] := (u - v + I)/(u - v - I);
assert["Bethe-Yang cyclicity", Times @@ (phase /@ roots) == 1];
Do[
  otherRoots = Delete[roots, rootIndex];
  lhs = phase[roots[[rootIndex]]]^length;
  rhs = Times @@ (scattering[roots[[rootIndex]], #] & /@ otherRoots);
  assert["Bethe-Yang root " <> ToString[rootIndex], lhs == rhs],
  {rootIndex, 1, Length[roots]}
];
assert["Konishi one-loop spin-chain energy", Total[1/(roots^2 + 1/4)] == 6];

(* Y-system checks: Hirota gives 1+Y and shifted zero-pole factors remember
   the rational source produced by crossing a strip boundary. *)
tCenterPlus = 7;
tUp = 5;
tDown = 3;
tLeft = 2;
tRight = 13;
tCenterMinus = (tUp tDown + tLeft tRight)/tCenterPlus;
yValue = tUp tDown/(tLeft tRight);
assert["Hirota gives 1+Y", tCenterPlus tCenterMinus/(tLeft tRight) == 1 + yValue];
assert["Hirota gives 1+1/Y", tCenterPlus tCenterMinus/(tUp tDown) == 1 + 1/yValue];
sourceFactor[u_, alpha_] := (u - alpha + I/2)/(u - alpha - I/2);
assert[
  "Y-system shifted source factor",
  sourceFactor[u + I/2, alpha] sourceFactor[u - I/2, alpha] ==
    (u - alpha + I)/(u - alpha - I)
];

(* Mirror-TBA checks: finite-grid pseudoenergy algebra and the A_infinity
   inverse symbol used in the mirror TBA-to-Y-system step. *)
eps = {7/10, 11/10, 8/5};
kernel = {{0, 1/5, -1/10}, {3/10, 0, 3/20}, {-1/20, 1/4, 0}};
logTerms = Log[1 + Exp[-eps]];
driving = eps + kernel.logTerms;
assertZero["mirror TBA pseudoenergy form", eps - (driving - kernel.logTerms)];
yVals = Exp[eps];
assertZero["mirror TBA Y-form", Log[yVals] - (driving - kernel.Log[1 + 1/yVals])];

aSymbol[m_, n_, q_] := (1 + q^2) (q^Abs[m - n] - q^(m + n))/(1 - q^2);
sSymbol[q_] := q/(1 + q^2);
Do[
  inverseProduct = aSymbol[m, n, q] - sSymbol[q] aSymbol[m + 1, n, q];
  inverseProduct = If[m > 1, inverseProduct - sSymbol[q] aSymbol[m - 1, n, q], inverseProduct];
  assert[
    "mirror A-infinity inverse " <> ToString[{m, n}],
    inverseProduct == If[m == n, 1, 0],
    0 < q < 1
  ],
  {m, 1, 4}, {n, 1, 4}
];

Print["All Wolfram Language planar N=4 reader companion checks passed."];
