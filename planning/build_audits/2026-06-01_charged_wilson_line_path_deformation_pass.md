# Charged Wilson-Line Path-Deformation Pass

Date: 2026-06-01.

Scope:

- Advanced the charged Haag--Ruelle/LSZ work for GitHub issue #527 without
  closing the theorem-level problem.
- Replaced the compressed statement that a compact Wilson-line deformation
  multiplies a charged creator by a "neutral Wilson loop" with explicit
  abelian Stokes bookkeeping at finite regulator:
  \(\partial S_{\gamma',\gamma}=\gamma'_R-\gamma_R\) and
  \(\int_{\gamma'_R}A-\int_{\gamma_R}A=\int_{S_{\gamma',\gamma}}F\).
- Added the nonabelian infinitesimal parallel-transporter variation formula
  as a curvature insertion with fixed endpoint and fixed asymptotic ray.
- Recorded the conceptual separation between compact same-flux deformations,
  which are finite LSZ-coordinate changes, and asymptotic-ray changes, which
  change the charged infrared sector.

Calculation checks:

- Extended `calculation-checks/charged_flux_dressing_checks.py` with an exact
  rational finite Stokes check for two paths enclosing a compact surface.
- The check verifies that the Wilson-line exponent changes by the charge
  times the curvature flux and that this surface factor carries no endpoint
  gauge charge.

Status:

- This pass clarifies a necessary mechanism for the charged LSZ construction.
  It does not solve the full nonperturbative charged Haag--Ruelle theorem,
  whose missing large-time estimates and charged asymptotic representation
  theory remain open.
