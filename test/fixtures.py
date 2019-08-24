"""
Example: Create test fixtures for test modules.
"""
import pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
TMPDIR = REPO/'tmp'

def cleartmp():
    if TMPDIR.exists():
        paths = TMPDIR.glob('**/*')
        paths = set( x if x.is_dir() else x.unlink() for x in paths )
        paths = set( x.rmdir() for x in paths if x is not None )
    else:
        TMPDIR.mkdir()

