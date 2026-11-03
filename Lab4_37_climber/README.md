# Climber Lab 4
LAB4 REPOSITORY : https://github.com/bmeghana-14/37_climber_lab4
This repository contains the completed version of the assigned `SETAPESU26/37_climber` Pygame lab.

## Completed tasks

1. **Height-score bug fixed** — `self.height` is now a high-water mark using `max(...)`, so the HUD does not decrease after the player backtracks or falls.
2. **Platform colours** — platform colours gradually change with height.
3. **Moving platforms** — every third non-ground platform moves horizontally with a small oscillation speed.
4. **Coin collection effect** — collecting a coin creates a short sparkle burst at the collection point.

## Run

```bash
pip install pygame
python game.py
```

Controls: `A`/Left and `D`/Right to move, `Space`/`W`/Up to jump, `R` to restart.

