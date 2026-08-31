#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

CORE_MD = (
    "personality.md",
    "memories.md",
    "episodes.md",
    "relationships.md",
    "adaptive.md",
    "status.md",
)


def pack(src: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    for name in CORE_MD:
        p = src / name
        if p.exists():
            shutil.copy2(p, out / name)
    for folder in ("ear", "eye"):
        d = src / folder
        if d.exists():
            shutil.copytree(d, out / folder, dirs_exist_ok=True)


def _soften_adaptive(text: str) -> str:
    out = []
    for line in text.splitlines():
        if line.startswith("stage:"):
            out.append("stage: baby")
        elif line.startswith("interactions:"):
            out.append("interactions: 0")
        else:
            out.append(line)
    if "stage:" not in text:
        out.insert(0, "stage: baby")
    return "\n".join(out) + "\n"


def child(src: Path, out: Path, keep_eye_md: bool = False) -> None:
    pack(src, out)
    adaptive = out / "adaptive.md"
    if adaptive.exists():
        adaptive.write_text(_soften_adaptive(adaptive.read_text(encoding="utf-8")), encoding="utf-8")
    else:
        adaptive.write_text(
            "---\nstage: baby\ninteractions: 0\nhowl: off\near: off\neye: off\n---\n",
            encoding="utf-8",
        )
    for media in out.rglob("*"):
        if media.suffix.lower() in {".jpg", ".jpeg", ".png", ".wav", ".opus", ".pt", ".adpcm"}:
            media.unlink()
    if not keep_eye_md:
        for p in list((out / "eye").glob("*.md")) if (out / "eye").exists() else []:
            p.unlink()


def main() -> int:
    p = argparse.ArgumentParser(prog="nanotot")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("pack", "child"):
        s = sub.add_parser(name)
        s.add_argument("--src", type=Path, required=True)
        s.add_argument("--out", type=Path, required=True)
        if name == "child":
            s.add_argument("--keep-eye-md", action="store_true")
    args = p.parse_args()
    if args.cmd == "pack":
        pack(args.src, args.out)
    else:
        child(args.src, args.out, keep_eye_md=args.keep_eye_md)
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
