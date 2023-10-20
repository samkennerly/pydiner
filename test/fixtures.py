"""
Example test fixtures: constants, cleanup methods, etc.
"""
from pathlib import Path
from shutil import rmtree

REPO = Path(__file__).resolve().parent.parent
TMPDIR = REPO/"tmp"


def all_tests(module):
    """ list[callable]: All test methods (or callable objects) in a module. """
    tests = vars(module).items()
    tests = [ v for k,v in tests if k.lower().startswith("test_") and callable(v) ]

    return tests


def bad_result(meth):
    """ Exception or None: Error thrown by a method, if any. """
    try:
        meth()
    except Exception as err:
        return err


def clear_tmpdir():
    """ None: Create a clean temporary folder. """
    if TMPDIR.exists():
        rmtree(TMPDIR)

    TMPDIR.mkdir()
