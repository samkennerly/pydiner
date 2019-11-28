"""
Example test fixtures: constants, cleanup methods, etc.
"""
from pathlib import Path
from shutil import rmtree

REPO = Path(__file__).resolve().parent.parent
TMPDIR = REPO / 'tmp'

def all_tests(testmodule):
    for name, obj in vars(testmodule).items():
        if name.startswith('test_') and callable(obj):
            yield name, obj

def bigprint(**kwargs):
    """ None: Fancy print function for key:value pairs. """
    for k,v in kwargs.items():
        print(f"{k}: {repr(v)}")

def cleartmp():
    """ None: Delete and recreate temporary folder. """
    if TMPDIR.exists():
        rmtree(TMPDIR)

    TMPDIR.mkdir()

def do(meth):
    """ None or Exception: There is no try. """
    try:
        meth()
    except Exception as err:
        return err

def errors(module):
    modname = module.__name__
    errors = ( (k, do(v)) for k,v in all_tests(module) )
    errors = ( (k, v) for k,v in errors if v is not None )

    return { f"{modname}.{name}":err for name, err in errors }





