# Chapter Dossiers

The dossier directories are keyed to the historical on-disk chapter source
directories under `monograph/tex/volumes/`, not to the compiled volume numbers.
The compiled volume order is defined by the `volume_*_current.tex` manifests;
do not infer compiled placement from a dossier path alone.

| Dossier directory | On-disk chapter source directory | Current compiled-volume placement |
| --- | --- | --- |
| `volume_i/` | `monograph/tex/volumes/volume_i/` | Chapters drawn into compiled Volumes I, II, and IV |
| `volume_ii/` | `monograph/tex/volumes/volume_ii/` | Chapters drawn into compiled Volumes II, III, and IV |
| `volume_iii/` | `monograph/tex/volumes/volume_iii/` | Chapters drawn into compiled Volume V, the CFT volume |

Thus the dossiers for compiled Volume V currently live under
`planning/chapter_dossiers/volume_iii/`, because the CFT source chapters live
under `monograph/tex/volumes/volume_iii/`.  If a future reorganization renames
the dossier directories by compiled volume, this README and
`planning/README.md` must be updated in the same change.

Within a dossier directory, filename prefixes are not a reliable unique
chapter key.  Some were assigned from the source-note sequence before later
manifest reordering.  The known collision in `volume_ii/` is:

| Dossier | Reason for prefix |
| --- | --- |
| `chapter18_classical_yang_mills_matter.md` | Historical source-order dossier for classical Yang-Mills theory and matter, following Wilsonian effective actions in the 253b sequence |
| `chapter18_gauge_fixing_ghosts_brst.md` | Dossier keyed to the current on-disk chapter file `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex` |

Use the dossier heading, the `Source Position` block, and the current manifest
files to identify the intended chapter; do not use the numeric filename prefix
alone as a database key.

Some source chapters under `monograph/tex/volumes/volume_iv/` are included in
compiled Volumes I and II.  A dedicated `planning/chapter_dossiers/volume_iv/`
directory has not yet been created; until it is, their planning status is
tracked through the manifest-level planning files.
