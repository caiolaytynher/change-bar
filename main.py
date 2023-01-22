import sys

from bars import change_bar
from config import config


def main(args: list[str]):
    if len(args) > 1:
        bar: str = args[1]
    else:
        raise Exception("No argument was given.")

    if bar not in config.wallpapers[config.theme]:
        raise ValueError("Not a valid bar.")

    change_bar(bar, config)


if __name__ == "__main__":
    main(sys.argv)
