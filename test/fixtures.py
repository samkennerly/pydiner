"""
Example test fixtures: constants, cleanup methods, etc.
"""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TMPDIR = REPO / 'tmp'

def bigprint(*args):
    """ None: Fancy print function. """
    print("", 10 * '-', *args, "", sep="\n")
