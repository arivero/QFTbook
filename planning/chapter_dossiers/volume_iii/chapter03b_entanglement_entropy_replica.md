# Volume V, Chapter 55 Dossier: Entanglement Entropy And The Replica Method

## Logical Role

- Role in the monograph: give the first self-contained CFT treatment of
  spatial entanglement, the replica construction, and the universal interval
  and ball formulas.
- Immediate predecessor: stress tensor, Weyl structure, and trace anomalies.
- Immediate successor: radial quantization and the state--operator map.

## Definitions And Results

The chapter establishes:

- regulated reduced density matrices \(\rho_{A,\epsilon}\), Renyi entropies
  \(S_n(A;\epsilon)\), and von Neumann entropy \(S_A(\epsilon)\), with explicit
  warnings about continuum factorization, gauge constraints, and
  regulator-dependent area terms;
- modular Hamiltonian \(K_A=-\log\rho_A\) and the entanglement first law
  \(\delta S_A=\operatorname{Tr}(\delta\rho_AK_A)\);
- the replica identity
  \(\operatorname{Tr}\rho_A^n=Z[M_n(A)]/Z[M_1]^n\) and
  \(S_A=(n\partial_n-1)W_n|_{n=1}\), with the analytic continuation in \(n\)
  stated as an assumption;
- the local conical-defect geometry near a smooth entangling surface and the
  role of entangling-surface counterterms;
- the two-dimensional single-interval derivation from the uniformizing map,
  the Schwarzian stress-tensor transformation, twist dimensions
  \(h_n=\bar h_n=c_{2d}(n-1/n)/24\), and
  \(S=(c_{2d}/3)\log(L/\epsilon)+\hbox{constant}\);
- conformal-map descendants for an interval on a circle and an interval at
  finite temperature;
- the conformal map from the causal diamond of a ball to
  \(\mathbb R\times\mathbb H^{D-1}\), the local ball modular Hamiltonian, and
  the hyperbolic-cylinder thermal partition-function formula;
- the universal ball entropy
  \(S_{\rm univ}=(-1)^{D/2-1}4a_D\log(R/\epsilon)\) for even \(D\), and
  \(S_{\rm univ}=(-1)^{(D-1)/2}F_D\) for odd \(D\), with \(a_2=c_{2d}/12\),
  \(a_4=a_{\rm W}\), and \(F_D=-\log|Z(S^D)|\).

## Claims To Verify

1. Entropy statements must distinguish regulator-dependent area terms from
   universal logarithmic or finite CFT data.
2. The replica formula uses a normalized reduced density matrix; the ratio
   \(Z[M_n]/Z[M_1]^n\) is essential.
3. The analytic continuation away from positive integer \(n\) is an extra
   hypothesis, not a purely formal consequence of the integer replicas.
4. The two-dimensional twist dimension must use the total stress tensor of
   the replicated theory, giving \(h_n=c_{2d}(n-1/n)/24\).
5. The ball modular Hamiltonian is local only for vacuum balls and half-spaces;
   generic regions require the replica defect or nonlocal modular operator.
6. The signs in the universal ball formula must reproduce
   \(+(c_{2d}/3)\log(R/\epsilon)\) in \(D=2\), \(-4a_{\rm W}\log(R/\epsilon)\)
   in \(D=4\), and \(-F_3\) in \(D=3\).

## Figures

- No figure is currently required; the causal-diamond to hyperbolic-cylinder
  map is given by explicit coordinates.

## Checks

- 2026-05-25 issue #474 pass: added the dedicated entanglement/replica chapter
  and calculation checks for the two-dimensional twist derivative, replica
  entropy sign, and universal ball-entropy sign conventions.
