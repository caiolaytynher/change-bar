from pathlib import Path
from subprocess import Popen

from handle_files import update_file, apply_changes
from config import Config


def change_bar(bar: str, config: Config):
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
        new_file_content: str = apply_changes(
            content=file.read_text(), replacements=replacement
        )

        update_file(file, new_file_content)

    Popen(["/usr/bin/qtile", "cmd-obj", "-o", "cmd", "-f", "restart"])
    Popen(["/usr/bin/feh", "--bg-fill", config.wallpapers[config.theme][bar]])
