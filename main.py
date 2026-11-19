#!/usr/bin/env python3
"""news-image-20261118 entry: copy the front page to /output/entry.png.

The image is "THE WORLD", a one-page newspaper front page summing up
Wednesday 18 November 2026: the U.S. strike on Iran's Qeshm Island and
Iran's drone attacks on Kuwait and Bahrain (lead story), the Xi-Putin
meeting in Shenzhen ahead of the three-way summit with Trump, Ukraine's
second-day strike on the Kerch Bridge, plus Peltola's Alaska Senate win,
the U.S. losing measles-free status, the Congo Ebola outbreak passing
11,000 cases, and Voyager 1 reaching one light-day from Earth. The three
picture panels are editorial illustrations generated for this entry; every
headline, label and the date was drawn in code so the text stays crisp.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    src = HERE / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # The judge sees exactly these bytes: verify the copy is identical.
    assert src.read_bytes() == dst.read_bytes(), "copied entry.png differs"
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
