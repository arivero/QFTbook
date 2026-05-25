# Issue #443 Sheet-Definition Order

## Scope

- GitHub issue #443: first/second-sheet terminology was defined in the later
  analyticity chapter but used earlier in the bound-state, resonance, and
  Bethe--Salpeter chapters.

## Resolution

- Added `def:stable-channel-sheet-convention` to the bound-state chapter
  before the first "first-sheet pole" use.
- The definition states:
  - the first sheet is the stable-channel analytic germ reached from the
    Feynman physical upper-edge boundary value;
  - a below-threshold first-sheet point is reached without crossing the
    threshold cut;
  - the adjacent second sheet relative to a channel is obtained by continuing
    through that channel cut, equivalently by changing the sign of a local
    threshold square root;
  - in multichannel problems the crossed channel cuts must be specified.
- Updated the resonance and Bethe--Salpeter chapters to reference the earlier
  definition.
- The later analyticity chapter now explicitly says that it develops the
  convention already introduced in the bound-state chapter.

## Verification Target

The active text should no longer require a reader to wait until the
analyticity chapter before the sheet terminology has been defined.
