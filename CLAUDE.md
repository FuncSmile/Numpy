# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a personal learning repository of NumPy tutorial scripts (Python 3.x), organized as a numbered sequence of lessons. Each lesson lives in its own directory and contains a single `Main.py` that is meant to be run directly to observe printed output — there are no tests, no package structure, and no build system.

## Environment

- A virtualenv lives in `Env/` (created via `python -m venv`, Python 3.13, based on `C:\laragon\bin\python\python-3.13`). It is gitignored.
- Activate it before running scripts:
  - PowerShell: `.\Env\Scripts\Activate.ps1`
- Run a lesson script with the venv's interpreter, e.g.: `.\Env\Scripts\python.exe .\01-How-to-create-array\Main.py`
- The only third-party dependency is `numpy`, installed into `Env`. There is no requirements.txt — if numpy is missing, install with `.\Env\Scripts\pip.exe install numpy`.

## Structure and conventions

- Lessons are directories named `NN-topic-name` (e.g. `00-intro`, `01-How-to-create-array`, `02-aritmatika-operation`), numbered in the order they should be studied/run. Each contains one `Main.py`.
- Scripts follow a consistent pattern: `import numpy as np`, often `os.system('cls')` at the top to clear the terminal, then a series of small demonstrations each followed by a `print(f"...")` showing the result. New lessons should follow this same demonstrate-and-print style rather than being restructured into functions/modules.
- Comments in scripts are frequently written in Indonesian (mixed with English) — match the existing tone when editing these files rather than converting everything to English.
- When adding a new lesson, create a new `NN-topic-name/Main.py` following the existing numbering and style rather than appending to an existing lesson file.
