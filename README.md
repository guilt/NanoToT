# NanoToT

Tiny is a markdown cache that can grow ears, a mouth, and borrowed eyes. If a sense is missing it says so. Port 11434. Files you can delete.

This is **not** a fourth brain. Clone = copy. Child = reset stage, soften floats, keep distilled md.

```bash
python -m pip install -e ".[dev]"
# or: pipenv install --dev
# family consumers, until PyPI:
#   pip install "nanotot @ git+https://github.com/guilt/nanotot.git@bananey"
make tests
make examples
nanotot pack     --src examples/tiny --out child/
nanotot child    --src examples/tiny --out baby/
nanotot child    --src examples/tiny --out baby/ --keep-eye-md --keep-ear-md
nanotot inspect  --src examples/tiny
```

`examples/tiny/` is a real organism tree you can pack today (core markdown +
an eye belief + an honest ear miss).
