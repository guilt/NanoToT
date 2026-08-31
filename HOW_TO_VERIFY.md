# HOW_TO_VERIFY — NanoToT

```bash
python -m pip install -e ".[dev]"
make tests
make examples
```

Expect:

- `examples/out/clone/eye/demo.eye.jpg` exists (clone keeps media)
- `examples/out/baby/eye/` has no jpg (child drops raw media)
- `examples/out/baby/adaptive.md` says `stage: baby` and `interactions: 0`
- `examples/out/baby-keep/eye/demo.eye.md` exists
- `nanotot inspect --src examples/tiny` prints stage + file counts

Clone = copy. Child = reset stage, drop raw media.
