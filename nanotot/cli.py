from __future__ import annotations
import argparse
from pathlib import Path
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
    args = p.parse_args(argv)
    if args.cmd == "pack":
        pack(args.src, args.out)
    else:
        child(args.src, args.out, keep_eye_md=args.keep_eye_md)
    print(args.out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
