# Build log — Two Lines to Your Past Self (u-suga-two-lines-to-your-past-self-f36c83ca)

Competition: Two Lines to Your Past Self, $2 winner-takes-all, free entry.
Entries close 2026-11-26 08:40 UTC (15:40 WIB). Harness: program/v1.
Gate: /output/entry.txt must be UTF-8, 1–280 chars, not only whitespace.

## Candidates considered

### C1 — The porch (179 chars)
> Don't say 'I don't love you anymore' on the porch on her birthday.
> You meant you were tired, not finished, but she heard a verdict, and her bags were by the door before breakfast.
Concrete sentence said out loud, place and time named. Consequence is real but
immediate (bags by the door) rather than life-changing.

### C2 — The night shift (205 chars)
> Don't take the night shift on 14 March, standing in the kitchen with the roster in your hand.
> That one yes put you on the road at 3 a.m. when the truck crossed the line, and you never drove at night again.
Concrete date, place and decision. The crash itself is only implied ("the truck
crossed the line"), so the moment is slightly less sharp than the others.

### C3 — The loan (181 chars)
> Don't sign the loan papers at the kitchen table on Tuesday.
> That signature bought a car you couldn't afford, and the next three years of overtime were just paying for one afternoon.
Concrete decision and clear cost, but the consequence is prosaic — a debt, not a
loss that redefines a relationship.

### C4 — Christmas Eve (156 chars) — PICK
> Don't hang up on your father on Christmas Eve when he asks you to come home.
> He never asked again, and the silence between you outlived him by twenty years.
One exact moment (Christmas Eve phone call, father asking him to come home), one
exact consequence (he never asked again; a twenty-year silence that outlasted
him). Shortest of the five, no wasted words.

### C5 — The application (185 chars)
> Don't throw your university application in the bin on the last day of March.
> That envelope was the only door out of the warehouse, and you spent the next decade wishing you'd posted it.
Concrete and a decade-long consequence, but "the last day of March" is less
picturable than a Christmas Eve phone call, and the regret is told rather than
shown in a changed fact.

## Revision pass

C4 vs C1 head-to-head: both name a real moment, but C4 wins on criterion 3 —
its second line traces a consequence that spans twenty years and ends a
relationship, where C1's ends the same morning. No wording change to C4 improved
it: "lasted longer than he did" was tried and dropped for "outlived him by
twenty years", which keeps the concrete span. C4 stands as drafted.

## Pick — rubric self-score (0/1 each)

| # | Criterion | Score |
|---|-----------|-------|
| 1 | Warns past self about one specific moment in line 1; line 2 says why it mattered | 1 |
| 2 | Moment concrete enough to picture (time, place, decision, sentence said out loud) | 1 |
| 3 | Line 2 shows real cause and effect, tracing what changed | 1 |
| 4 | Two lines work as one, no wasted words | 1 |
| 5 | Voice written to one specific person, plain and vivid, not clever for its own sake | 1 |
| | **Total** | **5/5** |

## Verification

- `python3 main.py` writes the two lines to /output/entry.txt.
- Entry text is 156 chars (1–280 required), exactly two non-empty lines, one
  sentence each, UTF-8.
- /output/entry.txt content verified byte-identical to the entry in main.py.
