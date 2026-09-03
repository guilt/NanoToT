# NanoToT — Clone / Child Packer

[![GitHub](https://img.shields.io/badge/GitHub-guilt/NanoToT-181717?logo=github)](https://github.com/guilt/NanoToT)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![docs](https://img.shields.io/badge/docs-USER_GUIDE-0A66C2)](docs/USER_GUIDE.md)

Tiny is a markdown cache that can grow ears, a mouth, and borrowed eyes. If a sense is missing it says so. Port 11434. Files you can delete.

This is **not** a fourth brain. Clone = copy. Child = reset stage, soften
floats, keep distilled markdown, drop raw media.

```bash
python -m pip install -e ".[dev]"
make tests && make examples
nanotot pack     --src examples/tiny --out child/
nanotot child    --src examples/tiny --out baby/
nanotot child    --src examples/tiny --out baby/ --keep-eye-md --keep-ear-md
nanotot inspect  --src examples/tiny
```

`examples/tiny/` is a real organism tree you can pack today (core markdown +
an eye belief + an honest ear miss).

## The core idea

TinyToT already knows how to clone *itself* as a variant delta
(`tinytot-clone`). NanoToT packs an *organism tree* under `/tiny/`:

- `pack` copies core markdown + `ear/` + `eye/` + `howl/`
- `child` then resets `stage: baby`, `interactions: 0`, turns senses off,
  and deletes raw media (jpg / wav / latent)

## Capabilities

| Command | What it does |
|---|---|
| `pack` | copy the tree, keep media |
| `child` | pack + reset stage + drop media |
| `--keep-eye-md` / `--keep-ear-md` | keep distilled sidecars |
| `inspect` | stage + file counts |

## Quick start

```bash
git clone https://github.com/guilt/NanoToT.git
cd NanoToT && git checkout bananey
python -m pip install -e ".[dev]"
make tests && make examples
```

Until PyPI: `pip install "nanotot @ git+https://github.com/guilt/nanotot.git@bananey"`

## Documentation

| I want to... | Page |
|---|---|
| Get running in 5 minutes | [Getting Started](docs/source/getting_started.md) |
| Understand pack vs child | [User Guide](docs/USER_GUIDE.md) |
| Copy a tree | [How-To: Pack](docs/source/how_to/02_pack.md) |
| Make a baby | [How-To: Child](docs/source/how_to/03_child.md) |
| Look up a symbol | [API Reference](docs/source/api/README.md) |

## Development

```
make tests            pytest with coverage (gate ≥ 80%)
make examples         pack + child + inspect
make docs             regenerate API docs + Sphinx HTML
```

## Family

- [TinyToT](https://github.com/guilt/TinyToT) — `tinytot-clone` for the server itself
- [TinyHowl](https://github.com/guilt/TinyHowl) · [TinyEar](https://github.com/guilt/TinyEar) · [TinyEye](https://github.com/guilt/TinyEye)

## Links

- **GitHub**: [github.com/guilt/NanoToT](https://github.com/guilt/NanoToT)
- **Docs**: [USER_GUIDE](docs/USER_GUIDE.md) · [Getting started](docs/source/getting_started.md) · [API](docs/source/api/README.md)
- **TinyToT variants**: [How-To: Variants](https://github.com/guilt/TinyToT/blob/bananey/docs/source/how_to/11_variants.md)

## License

MIT — see [LICENSE.md](LICENSE.md).
