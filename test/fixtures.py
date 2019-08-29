"""
Example: Create test fixtures for test modules.
"""
import pathlib

TMPDIR = pathlib.Path(__file__).parent.resolve() / "tmp"


def cleartmp():
    if TMPDIR.exists():
        print("Clear", TMPDIR)
        paths = TMPDIR.glob("**/*")
        paths = set(x if x.is_dir() else x.unlink() for x in paths)
        paths = set(x.rmdir() for x in paths if x is not None)
    else:
        print("mkdir", TMPDIR)
        TMPDIR.mkdir()
