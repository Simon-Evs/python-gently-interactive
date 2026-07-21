# Python Programming Exercises

## Learn Python by solving exercises in interactive notebooks

### Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and [marimo](https://marimo.io/) for interactive notebooks.

```bash
# Install dependencies
uv sync

# Open the notebook
uv run marimo edit notebooks/exercises.py
```

### How it works

Each notebook contains ~10 exercises. For each exercise you get:

1. **Description** — what to implement
2. **Code cell** — write your solution here
3. **Tests** — shows ✅ or ❌ as you work
4. **Hints** — locked by default, unlockable with a code

### Hint system

Use the slider at the top of the notebook to set your hint level:

| Level | What you see |
|-------|-------------|
| 0 | Nothing — hints hidden |
| 1 | Conceptual nudge |
| 2 | Detailed approach |
| 3 | Full solution code |

### Project Structure

```
notebooks/exercises.py  — Interactive exercise notebook (start here)
pyproject.toml          — Project config and dependencies
```

### Exercises

Exercises are adapted from [Python Programming Exercises, Gently Explained](https://inventwithpython.com/pythongently/) by Al Sweigart, licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

1) Hello World
2) Temperature Conversion
3) Odd & Even
4) Area & Volume
5) Fizz Buzz
6) Ordinal Suffix
7) ASCII Table
8) Read Write File
9) Chess Square Colour
10) Find & Replace
11) Hours, Minutes, Seconds
12) Smallest & Biggest
13) Sum & Product
14) Average
15) Median
16) Mode
17) Dice Roll
18) Buy 8 Get 1 Free
19) Password Generator
20) Leap Year
21) Validate Date
22) Rock, Paper, Scissors
23) 99 Bottles of Beer
24) Every 15 Minutes
25) Multiplication Table
26) Handshakes
27) Rectangle Drawing
28) Border Drawing
29) Pyramid Drawing
30) 3D Box Drawing
31) Convert Integers To Strings
32) Convert Strings To Integers
33) Comma-Formatted Numbers
34) Uppercase Letters
35) Title Case
36) Reverse String
37) Change Maker
38) Random Shuffle
39) Collatz Sequence
40) Merging Two Sorted Lists
41) ROT 13 Encryption
42) Bubble Sort

### License

This project is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). You are free to share and adapt this material for non-commercial purposes, as long as you give attribution and share under the same license.
