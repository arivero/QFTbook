# Volume II, Solitons and Collective Quantization Dossier
Source-File: monograph/tex/volumes/volume_ii/chapter17c_solitons_collective_quantization.tex

## Source Position

- Manuscript file:
  `monograph/tex/volumes/volume_ii/chapter17c_solitons_collective_quantization.tex`.
- Compiled in the gauge/anomaly part through
  `monograph/tex/volumes/volume_iv/volume_iv_current.tex`, immediately after
  `chapter17_yang_mills_theory_and_matter_fields.tex`.
- Role in the monograph: begin the dedicated soliton quantization chapter
  requested by the soliton/monopole/instanton depth lane.  The chapter treats
  a soliton as a sector with collective coordinates, fluctuation determinants,
  and physical sector observables.
- Relation to neighboring chapters: Ch17 supplies gauge-Higgs solitons and
  monopoles; Vol VI Ch08 supplies the exact sine-Gordon scattering and DHN
  benchmark.  This chapter isolates the general quantization mechanism.

## Definitions And Results

- `ch:solitons-collective-quantization`: dedicated chapter for soliton
  collective quantization.
- `sec:kink-sector-translation-collective-coordinate`: finite-energy kink
  sector and translation collective-coordinate setup.
- `prop:kink-center-collective-coordinate`: derives
  `G_XX=M_cl=4/3` for the dimensionless kink and separates the center
  kinetic term from normal fluctuations.
- `sec:soliton-fluctuation-determinants-mass`: fluctuation determinant and
  physical mass layer.
- `prop:soliton-chapter-dhn-mass-shift`: derives the sine-Gordon DHN
  one-loop mass shift `-m/pi` from the zero-mode/Levinson contribution and
  the finite first-Born-subtracted phase-shift determinant, with the
  no-tadpole counterterm cancelling only the Born/tadpole graph.
- `sec:soliton-fermion-zero-modes-fractional-charge`: Jackiw-Rebbi zero-mode
  sector and half-charge coordinate.
- `eq:soliton-chapter-jackiw-rebbi-kink-zero-mode`: normalized kink zero mode.
- `eq:soliton-chapter-jackiw-rebbi-kink-half-charge`: sector charges
  `N_0-1/2`.

## Claim Ledger

- The chapter advances #597 by starting the dedicated soliton quantization
  component, rather than further expanding instanton or monopole geometry.
- The central physics claim is that the moduli-space center of a kink is only
  the first line of quantization.  The physical soliton mass and sector
  charges require zero-mode separation, determinant/counterterm data, and
  observable-sector interpretation.
- The kink center calculation gives an explicit collective-coordinate metric,
  not only a verbal description of a zero mode.
- The DHN calculation is included as a determinant/counterterm benchmark and
  cross-linked to the exact sine-Gordon spectrum.
- The Jackiw-Rebbi block records how an internal fermion zero mode changes the
  soliton sector charge, separate from the translational collective coordinate.

## Figure Ledger

- No new figure in this pass.
- Future expansion may add a sector diagram distinguishing center zero modes,
  normal determinant modes, and internal fermion zero modes.

## Calculation Checks

- `calculation-checks/soliton_quantization_channel_checks.py` carries the
  companion evidence contract.
- It checks the kink mass/zero-mode norm equality, finite zero-mode
  projection, sine-Gordon phase-shift derivative, first-Born phase from the
  fluctuation-potential integral, the finite Born-subtracted DHN determinant,
  and Jackiw-Rebbi zero-mode normalization and half-charge bookkeeping.

## Audit Notes

- 2026-06-06 issue #597 soliton-chapter start: added the compiled
  `chapter17c_solitons_collective_quantization.tex` after Ch17.  The pass
  prioritizes soliton quantization and physical sector data over new
  moduli-space mathematics.
- The frontmatter source map was updated so later listed chapter numbers shift
  after the new compiled chapter.
- No directives, GitHub issue text, or process-monitoring language was inserted
  into monograph TeX.
- 2026-06-08 issue #853: replaced the duplicated cutoff/counterterm algebra
  by a concise cross-reference to the canonical Volume VI mode-number
  derivation.  The chapter now states that \(-m/\pi\) is produced by the
  Born-subtracted determinant and zero-mode bookkeeping, not inserted as a
  finite counterterm.
