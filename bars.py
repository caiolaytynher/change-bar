from pathlib import Path
from subprocess import Popen

from handlers.files import update_file, apply_changes, get_file_content


def change_bar(bar: str):
    file_path: Path = Path.home() / ".config/qtile/config.py"
    file_content: str = get_file_content(file_path)
    new_file_content: str = apply_changes(
        content=file_content,
        replacements=[
            (
                r"components\.panels\.*\simport",
                f"components.panels.{bar} import",
            )
        ],
    )

    update_file(file_path, new_file_content)

    Popen(["/usr/bin/qtile", "cmd-obj", "-o", "cmd", "-f", "restart"])
