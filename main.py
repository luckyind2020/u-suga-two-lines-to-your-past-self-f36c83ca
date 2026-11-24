"""Two Lines to Your Past Self — entry runner.

Reads the two-line entry from entry.txt and prints it, one line per line.
"""

import os


def load_entry(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as handle:
        lines = [line.rstrip("\n") for line in handle if line.strip()]
    if len(lines) != 2:
        raise ValueError(f"expected exactly two lines, found {len(lines)}")
    return lines


def entry_path() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main() -> None:
    for line in load_entry(entry_path()):
        print(line)


if __name__ == "__main__":
    main()
