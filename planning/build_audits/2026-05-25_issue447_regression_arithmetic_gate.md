# Issue #447 Regression Arithmetic Gate

## Scope

- GitHub issue #447 collected four coefficient/sign regressions from the
  earlier remediation pass:
  - the \(\pi^0\to2\gamma\) anomaly coefficient and the missing
    \(\{q,q\}=2q^2\) factor;
  - the \(x^3\) coefficient in the one-dimensional identity-block expansion
    about \(z=1/2\);
  - the stress-tensor source-functional sign in Volume III Chapters 1 and 3;
  - the sign conversion between Hermitian Lorentzian conformal charges and
    the radial \([P,K]\) algebra used in the unitarity-bound chapter.

## Resolution

- Added `calculation-checks/cft_anomaly_regression_checks.py` as a fast,
  finite arithmetic regression gate for all four items.
- The anomaly check verifies
  \(\operatorname{Tr}(T^3q^2)=1/6\),
  \(\operatorname{Tr}(T^3\{q,q\})=1/3\), and
  \(N_c\operatorname{Tr}(T^3\{q,q\})/16=1/16\) for \(N_c=3\), in the
  coefficient units \(e^2/(\pi^2 f_\pi)\).
- The identity-block check verifies that the cubic coefficient after extracting
  \(-\Delta_\phi2^{3-2\Delta_\phi}\) is
  \(\frac43(\Delta_\phi-1)(2\Delta_\phi-1)\), not the old
  \(\frac13(\Delta_\phi-1)(2\Delta_\phi-1)\).
- The stress-tensor check fixes the convention being tested: Volume III uses
  \(W=-\log Z\) and covariant metric variations
  \(\delta S=-\frac12\int\sqrt g\,T^{\mu\nu}\delta g_{\mu\nu}\), so
  \(\langle T^{\mu\nu}\rangle=-2g^{-1/2}\delta W/\delta g_{\mu\nu}\).
- The radial-algebra check verifies the map
  \(D_{\rm rad}=-iD_{\rm L}\), \(J_{\rm rad}=-iJ_{\rm L}\),
  \(P_{\rm rad}=iP_{\rm L}\), \(K_{\rm rad}=-iK_{\rm L}\), which sends
  \([P_{\rm L},K_{\rm L}]=2i(\delta D_{\rm L}-J_{\rm L})\) to
  \([P_{\rm rad},K_{\rm rad}]=-2(\delta D_{\rm rad}-J_{\rm rad})\).

## Verification

- `tools/run_calculation_checks.sh`

The run completed successfully, including the Wolfram backend probe and the
existing Wolfram gamma-trace check:

```text
All CFT/anomaly regression arithmetic checks passed.
All gamma-trace and anomaly-normalization checks passed.
All gauge-generator, color-factor, and Wilson-normalization checks passed.
All Wolfram Language gamma-trace and anomaly-normalization checks passed.
```
