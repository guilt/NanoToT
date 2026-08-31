from __future__ import annotations
import shutil
from pathlib import Path

CORE_MD = ("personality.md", "memories.md", "episodes.md", "relationships.md", "adaptive.md", "status.md")
MEDIA_EXT = {".jpg", ".jpeg", ".png", ".wav", ".opus", ".pt", ".adpcm", ".gif"}

def pack(src: Path, out: Path) -> Path:
    out.mkdir(parents=True, exist_ok=True)
    for name in CORE_MD:
        p = src / name
        if p.exists():
            shutil.copy2(p, out / name)
    for folder in ("ear", "eye"):
        d = src / folder
        if d.exists():
            shutil.copytree(d, out / folder, dirs_exist_ok=True)
    return out

def _soften_adaptive(text: str) -> str:
    out, saw_stage = [], False
    for line in text.splitlines():
        if line.startswith("stage:"):
            out.append("stage: baby"); saw_stage = True
        elif line.startswith("interactions:"):
            out.append("interactions: 0")
        else:
            out.append(line)
    if not saw_stage:
        out.insert(0, "stage: baby")
    return "\n".join(out) + "\n"

def child(src: Path, out: Path, keep_eye_md: bool = False) -> Path:
    pack(src, out)
    adaptive = out / "adaptive.md"
    if adaptive.exists():
        adaptive.write_text(_soften_adaptive(adaptive.read_text(encoding="utf-8")), encoding="utf-8")
    else:
        adaptive.write_text("---\nstage: baby\ninteractions: 0\nhowl: off\near: off\neye: off\n---\n", encoding="utf-8")
    for media in list(out.rglob("*")):
        if media.is_file() and media.suffix.lower() in MEDIA_EXT:
            media.unlink()
    if not keep_eye_md and (out / "eye").exists():
        for p in (out / "eye").glob("*.md"):
            p.unlink()
    return out
