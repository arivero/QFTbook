# Issue #469 Audit: 't Hooft Anomaly Matching As A Calculational Tool

## Scope

GitHub issue #469 reported that anomaly matching was present only as a
structural remark and that the manuscript did not yet develop 't Hooft anomaly
matching as a calculational constraint on infrared phases, with worked QCD
examples.

## Manuscript Changes

- Added `\section{'t Hooft Anomaly Matching as an Infrared Constraint}` to
  `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`,
  immediately after the Wess--Zumino--Witten construction and before the
  electromagnetic specialization.
- Stated the matching procedure as a four-step background-field test:
  specify the exact symmetry/backgrounds, compute the UV cocycle, list the
  possible IR responses, and compare cocycle classes modulo local
  counterterms.
- Recast the QCD WZW coefficient as a worked anomaly-matching calculation:
  the UV left-flavor anomaly has coefficient \(N_c/(48\pi^2)\), a level-\(n\)
  WZW term has coefficient \(n/(48\pi^2)\), and matching for arbitrary
  background and parameter forces \(n=N_c\).
- Made explicit that a purely two-derivative pion sigma model, or a unique
  trivial gapped unbroken chiral phase with no topological/invertible response,
  fails the UV anomaly test.
- Added the caveat that an unbroken phase is not excluded if it contains
  massless composite fermions or a topological/invertible sector carrying the
  same background cocycle.
- Added the vector-subgroup calculation:
  the left and right Dirac components give equal and opposite contributions to
  the vector flavor anomaly, so \(SU(N_f)_V\) is anomaly-free.
- Separated the status of Vafa--Witten vector alignment from anomaly matching:
  positivity/limits select the vector-aligned condensate under their
  hypotheses, while matching fixes the WZW response of the broken axial
  directions.

## Calculation Checks

- Added `calculation-checks/anomaly_matching_wzw_checks.py`.
- The script verifies:
  - matching \(N_c/(48\pi^2)\) with \(n/(48\pi^2)\) forces \(n=N_c\);
  - vector flavor anomaly cancellation between the two chiral components of a
    Dirac quark;
  - \(\operatorname{Tr}(T^3\{q,q\})=1/3\) and the \(N_c=3\)
    \(\pi^0\gamma\gamma\) coefficient \(e^2/(16\pi^2 f_\pi)\).

## Verification Plan

- Run the new calculation check directly.
- Run `git diff --check`.
- Run the monograph text and dossier audits.
- Build the monograph and inspect the pages containing the new section.

## Verification Results

- `python3 calculation-checks/anomaly_matching_wzw_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` completed with clean log scan.
- `pdfinfo monograph/tex/main.pdf` reports 866 pages.
- Rendered physical PDF pages 744--746 with `pdftoppm` and inspected the
  pages containing section 51.16; the heading, enumerated matching procedure,
  WZW-level matching formulae, vector-cancellation formula, and transition to
  the electromagnetic specialization are legible and non-overlapping.
