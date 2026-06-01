# Contributing

Notes on Quantum Field Theory is an open-source scholarly project. Pull
requests are welcome, but every proposed change must be reviewed and approved
by Xi Yin or by a maintainer explicitly designated by Xi Yin before it is
merged.

## Standards for Manuscript Contributions

Manuscript changes should preserve the monograph's central standard: precise
definitions, stated assumptions, logically sound arguments, and self-contained
derivations for QFT-specific claims whenever feasible. Do not introduce
slogans, unsupported folklore, fake theorem/proof wrappers, or references to
standard literature as substitutes for the argument needed in the text.

When a contribution uses external literature, it should identify the relevant
source and rederive or check the mathematical and physical content needed by
the monograph. Downloaded reference files, extracted text, and private notes
should remain local unless the repository owner explicitly approves committing
them with compatible license terms.

## Standards for Code Contributions

Executable checks and scripts should be deterministic, documented at the point
of use, and fast enough for local verification unless their purpose genuinely
requires a longer computation. If a script verifies a convention or calculation
used in the monograph, the corresponding manuscript passage should point to the
check or the calculation dossier should record the connection.

## Pull Request Expectations

Each pull request should state its mathematical or physical scope, list the
files changed, and report the relevant local verification commands. This
repository intentionally does not use a GitHub CI gate; verification is run
locally by contributors and maintainers.

By contributing, you agree that manuscript and scholarly-content contributions
are licensed under CC BY 4.0 and code contributions are licensed under MIT,
unless a file states otherwise.
