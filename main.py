"""Rejected Olympic Sports: one funny single-line sport.

The program writes exactly one line of text to /output/entry.txt.
Pure Python standard library only. The line is a made-up event a
broadcaster would have to announce with a straight face: two athletes
apologising over the same bump until politeness itself gets penalised.
"""

import os

LINE = (
    "Competitive Apologising: two athletes keep saying sorry for the "
    "same collision until the judges disqualify them both for politeness."
)


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 200, len(text)
    assert "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
