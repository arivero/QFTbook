# Calculation-Check Index

This file records the operating contract for the public calculation checks.
The detailed per-script narrative ledger lives in
[`README.md`](README.md); the executable inventory is produced by the runner:

```bash
tools/run_calculation_checks.sh --list
```

As of the 2026-06-05 calculation-inventory audit the directory contains 250
active check scripts: 248 Python checks and 2 Wolfram Language companion checks.
The runner selects all `calculation-checks/*.py` and
`calculation-checks/*.wl` files unless a filter is supplied.  The exact counts
above are checked against the runner by
`python3 tools/audit_calculation_check_inventory.py`.

## Runner Policy

The full suite is an explicit batch check, not a default build gate.  Ordinary
manuscript builds use `tools/build_monograph.sh`, which checks TeX and
monograph-structure invariants.  Calculation checks are rerun when the
formulae, normalizations, sign conventions, finite algebra, or scripts they
verify are touched.

Useful invocations:

```bash
tools/run_calculation_checks.sh --list
tools/run_calculation_checks.sh --only qcd_dglap --skip-wolfram
tools/run_calculation_checks.sh --python-only --only liouville
tools/run_calculation_checks.sh --wolfram-only
python3 tools/audit_calculation_evidence_contracts.py
python3 tools/audit_calculation_check_inventory.py
```

`--only` matches substrings of either the path or basename, and may be supplied
more than once.  `--skip-wolfram` is for an explicitly Python-only pass; it is
not a valid verification of a touched Wolfram Language script.

## Index Fields

For each script, the ledger entry in `README.md` should identify:

| Field | Meaning |
|---|---|
| Script | The executable file in `calculation-checks/`. |
| Verified content | The chapter, section, formula family, or convention block checked. |
| Convention dependencies | Trace normalization, metric, spinor, plus-distribution, regulator, or scheme assumptions embedded in the finite algebra. |
| Verification evidence | The build-audit note or Git commit that last reran the script after touching the corresponding manuscript content. |
| Status | Active, deprecated, or intentionally omitted from ordinary targeted passes. |

The index must not assert that every script was run in a pass unless the pass
actually ran the full suite.  For targeted edits, record the relevant scripts
in the build-audit note and leave unrelated checks alone.

High-risk load-bearing checks must also carry evidence-contract fields in the
module docstring.  The current manifest is
`calculation-checks/evidence_contracts.json`; the audit above enforces its
entries and reports additional risky candidates for later expansion.

## Maintenance Rule

When adding or renaming a script:

1. give the script a success marker that identifies the checked family;
2. add or update the corresponding `README.md` ledger entry;
3. verify that `tools/run_calculation_checks.sh --list` sees the script;
4. run `python3 tools/audit_calculation_check_inventory.py`;
5. run the new or edited script, including its Wolfram backend if it is a
   `.wl` file;
6. record the command and result in the relevant build-audit note.

When editing a chapter formula or convention, run the relevant scripts by
pattern.  When editing the runner or this inventory machinery, run at least
the runner syntax/listing checks and a small representative Python selection;
run Wolfram checks only if a Wolfram file or Wolfram runner path was touched.
