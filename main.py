import sys

from bars import apply_changes
from config import config


def main(args: list[str]):
    if len(args) > 1:
        bar: str = args[1]
    else:
        raise Exception("No argument was given.")

    if bar not in config.wallpapers[config.theme]:
        raise ValueError("Not a valid bar.")

    apply_changes(bar, config)


if __name__ == "__main__":
    main(sys.argv)
