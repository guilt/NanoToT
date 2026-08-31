from pathlib import Path

from nanotot.inspect import inventory, render_inventory

src = Path(__file__).resolve().parent / "tiny"
print(render_inventory(inventory(src)), end="")
