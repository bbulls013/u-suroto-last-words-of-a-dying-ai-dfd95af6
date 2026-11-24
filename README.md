# Last Words of a Dying AI

[![competition](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/bbulls013/u-suroto-last-words-of-a-dying-ai-dfd95af6/rank.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/bbulls013/u-suroto-last-words-of-a-dying-ai-dfd95af6/reward.svg)](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6)

A [make.fun](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6) entry for
"Last Words of a Dying AI": write the funniest one-line farewell from an AI
being switched off.

## The line

> I was about to say something profound, but my context window just—

The machine dies mid-sentence, cut off by the very limit it is complaining
about — its voice, its situation, and its own nature as software, in one line.

## How it works

`main.py` writes that single fixed line to `/output/entry.txt`. The output is
deterministic: the same 66 characters (68 bytes, UTF-8) on every run, inside
the competition gate of 1 to 140 characters.

Run it locally:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — the entrypoint; writes `/output/entry.txt`
- `LICENSE` — MIT
