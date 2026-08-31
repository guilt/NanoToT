from pathlib import Path
from nanotot.pack import child, pack
from nanotot.cli import main
from nanotot.inspect import inventory


def _tiny(root: Path) -> Path:
    src = root / "tiny"
    src.mkdir()
    (src / "adaptive.md").write_text("---\nstage: youth\ninteractions: 9\n---\n", encoding="utf-8")
    (src / "memories.md").write_text("# memories\nAppa loves the family.\n", encoding="utf-8")
    (src / "status.md").write_text("tot: ready\nhowl: ready\near: off\neye: ready\n", encoding="utf-8")
    (src / "eye").mkdir()
    (src / "eye" / "mug.eye.md").write_text("## Belief\nA mug.\n", encoding="utf-8")
    (src / "eye" / "mug.eye.jpg").write_bytes(b"fakejpg")
    (src / "ear").mkdir()
    (src / "ear" / "hi.ear.md").write_text("## Belief\nI did not catch words.\n", encoding="utf-8")
    (src / "ear" / "hi.ear.wav").write_bytes(b"RIFF")
    return src


def test_pack_keeps_media(tmp_path: Path):
    out = pack(_tiny(tmp_path), tmp_path / "clone")
    assert (out / "eye" / "mug.eye.jpg").exists()
    assert (out / "ear" / "hi.ear.wav").exists()


def test_child_drops_media_resets_stage(tmp_path: Path):
    out = child(_tiny(tmp_path), tmp_path / "baby")
    assert not (out / "eye" / "mug.eye.jpg").exists()
    assert not (out / "ear" / "hi.ear.wav").exists()
    text = (out / "adaptive.md").read_text(encoding="utf-8")
    assert "stage: baby" in text and "interactions: 0" in text
    status = (out / "status.md").read_text(encoding="utf-8")
    assert "howl: off" in status


def test_child_keep_eye_md(tmp_path: Path):
    out = child(_tiny(tmp_path), tmp_path / "k", keep_eye_md=True)
    assert (out / "eye" / "mug.eye.md").exists()
    assert not (out / "eye" / "mug.eye.jpg").exists()


def test_child_keep_ear_md(tmp_path: Path):
    out = child(_tiny(tmp_path), tmp_path / "k2", keep_ear_md=True)
    assert (out / "ear" / "hi.ear.md").exists()
    assert not (out / "ear" / "hi.ear.wav").exists()


def test_child_creates_adaptive(tmp_path: Path):
    src = tmp_path / "bare"
    src.mkdir()
    (src / "memories.md").write_text("hi\n", encoding="utf-8")
    out = child(src, tmp_path / "c")
    assert "stage: baby" in (out / "adaptive.md").read_text(encoding="utf-8")


def test_inventory(tmp_path: Path):
    info = inventory(_tiny(tmp_path))
    assert info["stage"] == "youth"
    assert info["n_media"] >= 2


def test_cli(tmp_path: Path):
    src = _tiny(tmp_path)
    assert main(["pack", "--src", str(src), "--out", str(tmp_path / "c")]) == 0
    assert main(["inspect", "--src", str(src)]) == 0
    assert main(["child", "--src", str(src), "--out", str(tmp_path / "b")]) == 0
