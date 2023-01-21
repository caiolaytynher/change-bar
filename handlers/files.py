import re
from pathlib import Path


def get_file_content(filepath: Path) -> str:
    with open(filepath, "r") as file:
        return "".join(file.readlines())


def update_file(filepath: Path, content: str):
    with open(filepath, "w") as file:
        file.write(content)


def apply_changes(
    content: str,
    replacements: list[tuple[str, str]],
) -> str:
    for target, replacement in replacements:
        pattern: re.Pattern[str] = re.compile(target)
        content = pattern.sub(replacement, content)

    return content
