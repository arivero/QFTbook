# LSZ Wave-Packet Theorem Boundary

Date: 2026-05-22

Scope:
- Strengthened the logical boundary between Haag--Ruelle scattering and LSZ reduction in the first scattering block.

Improvements:
- Made the asymptotic Fock space, Haag--Ruelle wave operators, and scattering operator explicit before any LSZ formula:
  \[
  \Omega_{\mathrm{in}},\Omega_{\mathrm{out}}:\mathcal F_s(\mathcal H_1)\to\mathcal H,
  \qquad S=\Omega_{\mathrm{out}}^*\Omega_{\mathrm{in}}.
  \]
- Defined the positive-energy mass shell, field residue \(Z\), one-particle wave packets, and the Hilbert-space scattering matrix element used by the reduction theorem.
- Added a wave-packet LSZ theorem stating that the connected component of \(\langle F_{\rm out},S F_{\rm in}\rangle\) is obtained by external one-particle residue extraction from the connected time-ordered Green function after boundary-value smearing.
- Updated the chapter dossier so later development can rely on this theorem as a nonperturbative-to-Green-function bridge rather than as a perturbative definition of scattering.

Verification:
- Ran `tools/build_monograph.sh`; the monograph build and log scan completed cleanly.
- Rendered PDF pages 140--149, covering Chapter 17 pages 122--131, and visually inspected the new theorem page and the LSZ diagrams.
- The rendered theorem, mass-shell definitions, and diagrams are legible and stable on the page.

Next dependency:
- Cross sections and invariant amplitudes may use \(S\) and \(\mathcal M\) as quantities defined after Haag--Ruelle plus LSZ.
- Perturbative Feynman graphs for scattering remain downstream of this reduction theorem.
