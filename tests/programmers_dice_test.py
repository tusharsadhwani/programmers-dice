from programmers_dice import EXCUSES, roll


def test_roll() -> None:
    """Tests roll() from the package."""
    excuses = roll(3)
    assert len(excuses) == 3
    assert all(excuse in EXCUSES for excuse in excuses)
