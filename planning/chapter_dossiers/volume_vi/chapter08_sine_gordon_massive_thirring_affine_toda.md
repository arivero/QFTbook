# Chapter 08: Sine-Gordon, Massive Thirring, And Affine Toda Theories

## Source Position

Volume VI now turns from general integrable machinery to concrete model
families.  This chapter supplies the first exact examples before the later
`O(N)`, Gross-Neveu, and integrable sigma-model chapter.

## Notation Inventory

- `A_UV`, `O_pert`, `lambda`, `Q`, `S`, `F`: UV algebra, perturbing
  coordinate, coupling, conserved charges, scattering data, and form factors.
- `varphi`, `beta`, `mu`: sine-Gordon field, coupling, and potential
  coordinate.
- `Q_top`: sine-Gordon topological charge.
- `xi`, `M_s`, `B_n`, `m_n`: sine-Gordon coupling parameter, soliton mass,
  breather label, and breather mass.
- `lambda`, `V`, `S_min`, `b(theta)`, `c(theta)`: inverse sine-Gordon
  coupling parameter, soliton/antisoliton charge doublet, minimal scalar
  factor, and transmission/reflection amplitudes in the exact soliton
  S-matrix.
- `F_a(theta)`, `S_mn(theta)`: neutral scalar breather block and minimal
  diagonal breather-breather scattering amplitude.
- `psi`, `g_T`: massive Thirring fermion and current-current coupling.
- `g`, `alpha_i`, `theta`, `n_i`: Lie algebra, roots, highest root, and
  affine Dynkin labels in affine Toda theory.

## Claim Ledger

- Defines an integrable model family as matched UV, perturbing, conserved,
  scattering, and form-factor data.
- Fixes sine-Gordon normalization, topological charge, and the attractive
  regime spectrum.
- Derives the breather mass formula from relativistic bound-state kinematics.
- Displays the exact soliton/antisoliton two-state S-matrix datum, separates
  the matrix part from the minimal scalar factor, proves matrix unitarity, and
  derives the physical-strip pole locations that give the breather masses.
- Corrects the lightest-breather pole discussion by separating the direct
  \(B_1B_1\to B_2\) pole from its crossed-channel image.
- Defines the neutral block \(F_a(\theta)\), proves unitarity, crossing, pole
  locations, and residue signs, and uses it to display the minimal
  breather-breather amplitudes.
- Proves that the direct pole of \(S_{mn}\) gives the mass of \(B_{m+n}\)
  whenever \((m+n)\xi<1\).
- States the massive Thirring equivalence in Coleman's coupling convention.
- Defines affine Toda action data and derives the classical mass matrix from
  the affine-root potential.

## Calculation Checks

- `calculation-checks/sine_gordon_smatrix_checks.py` verifies the matrix
  unitarity, free-fermion point, soliton-breather pole kinematics,
  lightest-breather direct and crossed poles, neutral-block residue signs, and
  breather-breather fusion mass formulae.

## Figure Ledger

No figure is included in this pass.  Future figures should include the
sine-Gordon periodic potential with soliton sectors, the soliton-antisoliton
bound-state pole in the rapidity strip, and affine Dynkin diagrams for the
first simply-laced examples.
