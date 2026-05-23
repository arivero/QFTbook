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

Some source chapters under `monograph/tex/volumes/volume_iv/` are included in
compiled Volumes I and II.  A dedicated `planning/chapter_dossiers/volume_iv/`
directory has not yet been created; until it is, their planning status is
tracked through the manifest-level planning files.
