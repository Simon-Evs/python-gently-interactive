# Python Gently Interactive

## Learn Python by solving exercises in an interactive notebook

### Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and [marimo](https://marimo.io/) for the interactive notebook.

```bash
# Install dependencies
uv sync

# Open the notebook (edit mode - you can write and save your solutions)
uv run marimo edit notebooks/exercises.py

# Reset - clear all your answers and start fresh
cp notebooks/.exercises_template.py notebooks/exercises.py
```

### How it works

The notebook contains 42 exercises. For each exercise you get:

1. **Description** — what to implement, with a link to the full explanation
2. **Code cell** — write your solution here
3. **Tests** — shows ✅ or ❌ as you work
4. **Hints** — controlled by a slider at the top of the notebook

### Hint system

Use the slider at the top of the notebook to set your hint level:

| Level | What you see |
|-------|-------------|
| 0 | No hints |
| 1 | Conceptual nudge |
| 2 | Detailed approach |
| 3 | Full solution code |

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
