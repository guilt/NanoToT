# Getting Started with NanoToT

```bash
python -m pip install -e ".[dev]"
make tests && make examples
nanotot inspect --src examples/tiny
```

Expect `examples/out/clone` to keep the demo JPEG and `examples/out/baby` to drop it.

See [HOW_TO_VERIFY.md](../../HOW_TO_VERIFY.md).
