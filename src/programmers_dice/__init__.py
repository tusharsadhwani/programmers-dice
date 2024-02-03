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
    "The code is compiling, it will work soon.",
    "I think it's a cosmic ray issue.",
    "It's a feature, not a bug, I swear.",
    "The documentation is clearly mistaken.",
    "I'm not a magician, I can't fix everything.",
    "I'm not a psychic, I can't predict everything.",
    "It's a feature, the users just don't know it.",
    "I'm pretty sure the code is haunted.",
    "I think the code is allergic to Tuesdays.",
    "I'm not a mind reader, I need more info.",
    "I'm not a miracle worker, I'm just a programmer.",
    "It's a case of parallel universe interference.",
]


def roll(count: int) -> list[str]:
    """Returns a greeting."""
    return random.choices(EXCUSES, k=count)
