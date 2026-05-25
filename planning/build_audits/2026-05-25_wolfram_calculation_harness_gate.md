# Wolfram Calculation Harness Gate

## Scope

- Tightened the public calculation-check harness after discovering that the
  earlier `wolframscript -file` path could stall before executing even
  elementary local code on the active macOS installation.
- The failure mode meant that a Mathematica/Wolfram check could appear to be
  covered by the repository script while the actual Wolfram backend had not
  been successfully exercised.

## Harness Changes

- `tools/run_calculation_checks.sh` now enumerates Python and Wolfram checks
  explicitly.
- If `.wl` checks exist, the runner requires a working Wolfram backend unless
  `QFT_SKIP_WOLFRAM=1` is explicitly set for a Python-only pass.
- The preferred backend is `WolframKernel -script`; `wolframscript -file`
  remains only as a fallback when the kernel entrypoint is unavailable.
- Before running any `.wl` file, the runner executes a generated local probe
  script and requires the marker `QFT_WOLFRAM_BACKEND_PROBE_OK`.
- The runner rejects `.wl` files with arithmetic continuations whose first
  nonspace token is `+`, `-`, `*`, or `/`, since that pattern can be parsed as
  a new statement by `wolframscript -file`.
- Each `.wl` check must print a success line of the form
  `All Wolfram Language ... passed.`; absence of this marker is a harness
  failure even if the process exits with status zero.

## Agent Rule

When a commit introduces or edits a `.wl` check or the calculation-check
runner, the verification note must name the actual Wolfram backend used and
record the emitted Wolfram success marker.  A missing `wolframscript` on
`PATH`, a skipped Wolfram pass, or a Python-only pass is not a verification of
a Wolfram Language file.
