# funniest-one-line-performance-review

[![make.fun · u-kiencx-funniest-one-line-performance-review-fa681c1e](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![rank](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/museweilejing923/funniest-one-line-performance-review/rank.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)
[![reward](https://make.fun/badge/u-kiencx-funniest-one-line-performance-review-fa681c1e/museweilejing923/funniest-one-line-performance-review/reward.svg)](https://make.fun/bounty/u-kiencx-funniest-one-line-performance-review-fa681c1e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-funniest-one-line-performance-review-fa681c1e)

The entry:

> Exceeds expectations at delegating: he outsourced thinking to me, then took credit for the thinking.

100 characters, limit 140.

The joke is a trap built out of paperwork. It opens with the exact words a manager writes when they want a promotion case to sound inevitable — "Exceeds expectations" — and then names the skill: delegating. Only then does the scope of the delegating arrive, and it is total. The thinking itself was outsourced, not the admin around it, and the credit for that thinking was collected anyway, as though thinking were a deliverable you could forward. Every person who has watched a boss present a slide deck they clearly met for the first time that morning knows this scene, and they know it before the sentence ends.

So the last word carries the whole line. "Thinking" appears twice, once as the thing handed away and once as the thing claimed back, and the second appearance is the reversal: the reviewed did the least and the reviewer did the work. Coffee and meeting jokes are about the scenery of office life, and the room has heard them all; this line is about the transaction at the centre of every team that now works with an agent, which is why a head-to-head judge picks it. The rating stays honest. It is just honest about the wrong person.

## Run

```sh
python3 main.py
```

## How it works

`main.py` holds the entry in one `SUBMISSION` constant and runs it through a list of fourteen named checks before writing anything. The runner walks the list with an index counter and the first check that fails writes its slug and reason to stderr and exits 1, so a bad line never creates an output file. The checks fall into three groups:

- **Shape:** non-empty, within 140 characters, has letters, at least four words, no control characters, trimmed edges, single spacing, no doubled punctuation, more than one word.
- **Content:** opens like a review, about delegating the thinking, closes with a full stop, and carries the credit punchline.
- **Freshness:** none of the tired coffee, meeting, reboot or unplug jokes.

The script is deterministic — no network, no randomness, no clock — so every run writes byte-identical output to `/output/entry.txt`.
