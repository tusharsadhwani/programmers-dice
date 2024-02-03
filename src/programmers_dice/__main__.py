"""Support executing the CLI by doing `python -m programmers_dice`."""
from __future__ import annotations

from programmers_dice.cli import cli

if __name__ == "__main__":
    raise SystemExit(cli())
