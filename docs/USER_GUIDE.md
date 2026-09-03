# NanoToT User Guide

## Where to start

| I want to... | Section |
|---|---|
| Copy a tree | [Pack](#pack) |
| Make a baby | [Child](#child) |
| See what is in a tree | [Inspect](#inspect) |

---

## Pack

```bash
nanotot pack --src examples/tiny --out /tmp/clone
```

Copies `personality.md`, `memories.md`, `episodes.md`, `relationships.md`,
`adaptive.md`, `status.md`, and any `ear/` `eye/` `howl/` folders. Media stays.

---

## Child

```bash
nanotot child --src examples/tiny --out /tmp/baby
nanotot child --src examples/tiny --out /tmp/baby-keep --keep-eye-md --keep-ear-md
```

After pack: `stage: baby`, `interactions: 0`, senses `off`, raw media deleted.
Sidecar markdown dropped unless `--keep-*-md`.

---

## Inspect

```bash
nanotot inspect --src examples/tiny
```

Prints stage and counts. Not a fourth brain — `ls` plus a few flags.
