# Six-Dimensional Class-S Anomaly Pushforward Pass

## Scope

- Continued the Volume VII depth-pass-B work for issue #626.
- Targeted the Riemann-surface compactification paragraph in the
  six-dimensional SCFT chapter, which still read mostly as a checklist.

## Change

- Added a smooth unpunctured compactification mechanism:
  \(M_6=M_4\times C\), surface Euler class \(t=e(TC)\), and the
  \(SO(5)_R\to SO(2)_r\oplus SO(3)_R\) background decomposition.
- Defined the twist by \(e(N_2)=x+\eta t\), keeping the twist sign visible
  rather than hiding it in convention.
- Expanded the characteristic classes \(p_1(N_R)\) and \(p_2(N_R)\), extracted
  the terms linear in \(t\), and pushed the six-dimensional anomaly polynomial
  to the four-dimensional six-form
  \[
    I_6=\eta\chi(C)x\left[
      {r_{\mathfrak g}\over48}(x^2-p+3u)
      +{d_{\mathfrak g}h^\vee_{\mathfrak g}\over12}u
    \right].
  \]
- Extended `calculation-checks/susy_abjm_6d_checks.py` with exact rational
  coefficient checks for the pushforward.

## Status

This pass does not treat punctures, irregular defects, or degeneration
limits.  Those remain part of the six-dimensional/class-\(S\) depth lane.
