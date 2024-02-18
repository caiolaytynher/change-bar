import re


def update_str(
    content: str,
    replacements: list[tuple[str, str]],
) -> str:
    for target, replacement in replacements:
        pattern: re.Pattern[str] = re.compile(target)
        content = pattern.sub(replacement, content)

    return content
