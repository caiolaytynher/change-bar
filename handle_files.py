import re
from pathlib import Path


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
