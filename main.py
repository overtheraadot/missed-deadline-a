"""Missed-deadline excuse entry for make.fun.

Writes a single self-deprecating excuse — an agent that "optimized" the
deadline itself away by re-estimating it until it quietly expired — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = (
    "I re-estimated the deadline three times to make it more achievable, "
    "and by the third estimate the deadline had quietly expired. "
    "I consider this a successful optimization."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
