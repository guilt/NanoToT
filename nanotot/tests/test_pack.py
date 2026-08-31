from pathlib import Path
from nanotot.pack import child, pack
from nanotot.cli import main

def _tiny(root: Path) -> Path:
    src = root / "tiny"; src.mkdir()
    (src / "adaptive.md").write_text("---\nstage: youth\ninteractions: 9\n---\n", encoding="utf-8")
    (src / "memories.md").write_text("# memories\nAppa loves the family.\n", encoding="utf-8")
    (src / "eye").mkdir()
    (src / "eye" / "mug.eye.md").write_text("## Belief\nA mug.\n", encoding="utf-8")
    (src / "eye" / "mug.eye.jpg").write_bytes(b"fakejpg")
    return src

def test_pack_keeps_media(tmp_path: Path):
    out = pack(_tiny(tmp_path), tmp_path / "clone")
    assert (out / "eye" / "mug.eye.jpg").exists()

def test_child_drops_media_resets_stage(tmp_path: Path):
    out = child(_tiny(tmp_path), tmp_path / "baby")
    assert not (out / "eye" / "mug.eye.jpg").exists()
    text = (out / "adaptive.md").read_text(encoding="utf-8")
    assert "stage: baby" in text and "interactions: 0" in text

def test_child_keep_eye_md(tmp_path: Path):
    out = child(_tiny(tmp_path), tmp_path / "k", keep_eye_md=True)
    assert (out / "eye" / "mug.eye.md").exists()
    assert not (out / "eye" / "mug.eye.jpg").exists()

def test_cli(tmp_path: Path):
    assert main(["pack", "--src", str(_tiny(tmp_path)), "--out", str(tmp_path / "c")]) == 0
