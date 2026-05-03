"""
Write a program that creates a text file named stichi.txt in the current directory
and writes the following poem into it (using print or write).

We walk through the years like steps.
No need to whine that our ascent is hard.
If we suddenly don't find a new step —
The way back is always a moment.
"""

with open("stichi.txt", "wt", encoding="utf-8") as fl:
    s = """We walk through the years like steps.
No need to whine that our ascent is hard.
If we suddenly don't find a new step —
The way back is always a moment."""
    print(s, file=fl, end='')