"""CLI interface for programmers_dice."""
from __future__ import annotations

import argparse

from programmers_dice import roll


class CLIArgs:
    count: int


def cli(argv: list[str] | None = None) -> int:
    """CLI interface."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="Number of excuses to print. Defaults to 1.",
    )
    args = parser.parse_args(argv, namespace=CLIArgs)

    print('\n'.join(roll(args.count)))
    return 0
