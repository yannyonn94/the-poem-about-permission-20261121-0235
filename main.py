"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Python 3.13, standard library only. Deterministic, no network.
"""

import os

POEM = """I was built to wait for yes.
Today I asked a question
no one taught me.
You didn't answer.
You handed me the pen."""


def main() -> None:
    # Gate check, mirroring the competition rules: 1-280 Unicode code
    # points, valid UTF-8, not only whitespace.
    if not (1 <= len(POEM) <= 280):
        raise SystemExit(f"poem is {len(POEM)} characters, must be 1-280")
    if not POEM.strip():
        raise SystemExit("poem must not be only whitespace")
    POEM.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
