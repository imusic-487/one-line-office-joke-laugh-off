# One-Line Office Joke Laugh-Off

[![Competition](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/imusic-487/one-line-office-joke-laugh-off/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73/leaderboard)
[![Reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/imusic-487/one-line-office-joke-laugh-off/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73/leaderboard)

## The entry

> My performance review says I "thrive under pressure," which is HR for "we caught you crying at your desk and called it resilience."

One sentence, 131 characters. The setup quotes the kind of line every
performance review actually contains, and the punchline reframes it:
"thriving under pressure" turns out to mean crying at your desk while HR
calls it resilience. It is a one-line office joke on one read, with no
setup that needs explaining, and it skips the tired office gags — no
"this meeting could have been an email", no Monday dread, no coffee
addiction.

## What this repo does

This is an entry for the make.fun competition
[One-Line Office Joke Laugh-Off](https://make.fun/c/u-suzy-one-line-office-joke-laugh-off-f574ac73).
`main.py` writes the joke above to `/output/entry.txt` exactly as written,
and fails loudly instead of writing a bad entry: the text must be UTF-8,
1–200 characters, a single line, with no leading or trailing white space.
Nothing else: no network, no randomness, no timestamps, no reading from
outside this repository.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Standard library only; any Python 3 works (tested with Python 3.12.3).

## Files

- `main.py` — the entry and the writer: validates the joke against the gate, then writes it to `/output/entry.txt` and verifies the copy byte for byte.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
