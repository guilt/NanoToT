from __future__ import annotations

import argparse
from pathlib import Path

from .inspect import inventory, render_inventory
from .pack import child, pack


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="nanotot")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("pack", "child"):
        s = sub.add_parser(name)
        s.add_argument("--src", type=Path, required=True)
        s.add_argument("--out", type=Path, required=True)
        if name == "child":
            s.add_argument("--keep-eye-md", action="store_true")
            s.add_argument("--keep-ear-md", action="store_true")
    ins = sub.add_parser("inspect")
    ins.add_argument("--src", type=Path, required=True)
    args = p.parse_args(argv)
    if args.cmd == "pack":
        pack(args.src, args.out)
        print(args.out)
    elif args.cmd == "child":
        child(args.src, args.out, keep_eye_md=args.keep_eye_md, keep_ear_md=args.keep_ear_md)
        print(args.out)
    else:
        print(render_inventory(inventory(args.src)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
