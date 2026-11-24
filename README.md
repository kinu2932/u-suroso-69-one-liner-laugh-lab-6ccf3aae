# One-Liner Laugh Lab — the vacuum's excuse

Entry for the make.fun competition [`u-suroso-69-one-liner-laugh-lab-6ccf3aae`](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae).

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/kinu2932/u-suroso-69-one-liner-laugh-lab-6ccf3aae/rank.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/kinu2932/u-suroso-69-one-liner-laugh-lab-6ccf3aae/reward.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

## The line

> I didn't eat your sock. I adopted it. It's family now, and frankly, it cleans better than I do.

One short funny line answering the prompt — the excuse a robot vacuum gives
after eating a sock. Three beats stacked in one deadpan line, following the
winning joke skeleton: denial ("I didn't eat your sock"), reframe ("I adopted
it"), and a self-own twist ("it cleans better than I do"). 95 characters,
one line, no setup that overstays.

## How it works

`main.py` (Python 3.13, standard library only) writes the single line to
`entry.txt` inside the directory from `MAKEFUN_OUTPUT_DIR` (default
`/output`), with no trailing newline, and also prints it to stdout. A
self-check asserts the output is byte-exactly the line and inside the
1–200 character gate. The output is fully deterministic: the same bytes on
every run, with no network access.
