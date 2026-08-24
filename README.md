# Gym Tracker

A command-line gym tracker built in Python to log workouts, track sets/reps/weight, 
and review workout history over time.

## Features
- Log a workout session with multiple exercises, each with sets, reps, and weight
- View past workout history
- Input validation to prevent crashes from invalid input
- Persistent storage using JSON — your data is saved between runs

## How to run
```bash
python main.py
```
No external dependencies — built entirely with Python's standard library (`json`, `datetime`).

## Roadmap
- [ ] Merge sessions logged on the same day
- [ ] Track personal bests per exercise
- [ ] Split into multiple files for better structure
- [ ] Refactor data model to use classes

## What I learned
Built as a learning project to practice core Python concepts: functions, file I/O, 
data structures (nested dicts/lists), input validation, and Git/GitHub workflows 
(branching, pull requests, resolving a lost commit via `git reflog`).
