"""Read an organism tree. Not a fourth brain — just ls + a few flags."""
from __future__ import annotations

from pathlib import Path

CORE_MD = (
    "personality.md",
    "memories.md",
    "episodes.md",
    "relationships.md",
    "adaptive.md",
    "status.md",
)


def read_stage(root: Path) -> str:
    adaptive = root / "adaptive.md"
    if not adaptive.exists():
        return "unknown"
    for line in adaptive.read_text(encoding="utf-8").splitlines():
        if line.startswith("stage:"):
            return line.split(":", 1)[1].strip()
    return "unknown"


def inventory(root: Path) -> dict:
    root = Path(root)
    files = [p for p in root.rglob("*") if p.is_file()]
    return {
        "root": str(root),
        "stage": read_stage(root),
        "core": {name: (root / name).exists() for name in CORE_MD},
        "n_files": len(files),
        "n_eye_md": len(list(root.glob("eye/*.eye.md"))) + len(list((root / "eye").glob("*.md"))) if (root / "eye").exists() else 0,
        "n_ear_md": len(list((root / "ear").glob("*.md"))) if (root / "ear").exists() else 0,
        "n_media": sum(
            1
            for p in files
            if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".wav", ".opus", ".pt", ".adpcm", ".gif"}
        ),
    }


def render_inventory(info: dict) -> str:
    lines = [
        f"root: {info['root']}",
        f"stage: {info['stage']}",
        f"files: {info['n_files']}",
        f"eye_md: {info['n_eye_md']}",
        f"ear_md: {info['n_ear_md']}",
        f"media: {info['n_media']}",
        "core:",
    ]
    for name, ok in info["core"].items():
        lines.append(f"  {name}: {'yes' if ok else 'missing'}")
    return "\n".join(lines) + "\n"
