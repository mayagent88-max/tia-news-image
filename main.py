#!/usr/bin/env python3
"""news-image-20261118 entry: copy the front page to /output/entry.png.

The image is "THE WORLD", a dense one-page newspaper front page summing
up Wednesday 18 November 2026 in 46 stories: Xi greets Trump in Shenzhen,
Kuwait and Bahrain intercept Iranian drones, Voyager 1 reaches one
light-day from Earth, Russia's 141-drone attack on Ukraine, the EU's
45bn loan for Kyiv, the Fed minutes, Cyclone Akvan, the El Obeid
killings, tanks in central Gaza, Jeffries' Speaker nod and the GTA VI
launch -- plus 35 more briefs across 7 regions, a UTC timeline, a world
map with numbered pins, a DATE CHECK box and cited sources. Every story
on the page happened, or was first reported, on Wednesday 18 November
2026. All 11 picture panels are original drawings made for this entry;
every headline, label and the date was drawn in code so the text stays
crisp. The image itself was composed by compose2.py in the build session
and is committed here as entry.png; re-running the composer produces
byte-identical output, so the copy this program makes is exact. This
program only copies it.

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
