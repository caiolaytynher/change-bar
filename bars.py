from pathlib import Path
from subprocess import Popen

from file_updating import update_str
from config import Config


def apply_changes(bar: str, config: Config):
    files: list[Path] = [
        Path.home() / ".config/qtile/config.py",
        Path.home() / ".config/qtile/components/groups.py",
        Path.home() / ".config/qtile/scripts/autostart.sh",
        Path.home() / ".config/picom/picom.conf",
    ]

    replacements: list[list[tuple[str, str]]] = [
        [
            (
                r"components\.panels\..*\simport",
                f"components.panels.{bar} import",
            )
        ],
        [
            (
                r"\"border_focus\":\stheme\..*,",
                '"border_focus": theme.accent,'
                if bar == "vibrant"
                else '"border_focus": theme.contrast[3],',
            )
        ],
        [
            (
                r"feh\s--bg-fill\s.*",
                f"feh --bg-fill {config.wallpapers[config.theme][bar]}",
            )
        ],
        [
            (
                r"corner-radius\s=\s.*;",
                "corner-radius = 0;"
                if bar == "utility"
                else "corner-radius = 10;",
            )
        ],
    ]

    for file, replacement in zip(files, replacements):
        file.write_text(
            update_str(content=file.read_text(), replacements=replacement)
        )

    Popen(["/usr/bin/qtile", "cmd-obj", "-o", "cmd", "-f", "restart"])
    Popen(["/usr/bin/feh", "--bg-fill", config.wallpapers[config.theme][bar]])
