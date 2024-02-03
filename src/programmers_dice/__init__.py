"""programmers-dice - Generates excuses for programmers."""
from __future__ import annotations

import random

EXCUSES = [
    "Clear your cache.",
    "Ctrl+Shift+R should fix it.",
    "Works for me.",
    "It runs locally.",
    "Let's order a pizza.",
    "That's a first.",
    "User error.",
    "Almost done...",
    "Can't reproduce.",
    "My wrist hurts.",
    "Try it now.",
    "It worked yesterday.",
    "It's a hack.",
    "Non standard behaviour.",
    "It's not that simple.",
    "It's a feature.",
    "Can't even curl it.",
    "IE6?!",
]

def roll(count: int) -> list[str]:
    """Returns a greeting."""
    return random.choices(EXCUSES, k=count)
