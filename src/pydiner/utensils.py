"""
Utility functions.
"""
from collections import OrderedDict
from datetime import datetime
from itertools import islice, repeat, takewhile
from json import load as readjson
from pathlib import Path
from sys import stderr

REPO = Path(__file__).resolve().parent.parent.parent
WARNING = "\x1b[93m* ACHTUNG *\x1b[0m"


def achtung(*args, file=stderr):
    """ None: Print timestamp and error message(s) to STDERR. """
    print(clock(), WARNING, *args, file=file, flush=True)


def batcher(seq, n, joined=tuple, sliced=islice):
    """ Iterator[tuple]: Length-limited batches taken from iterable. """
    return takewhile(len, (joined(sliced(x, n)) for x in repeat(iter(seq))))


def clock(timespec="seconds"):
    """ str: UTC date and time and ISO format. """
    return datetime.utcnow().isoformat(sep=" ", timespec=timespec)


def distinct(seq):
    """ Iterator: Unique sequence elements in original order. """
    return iter(OrderedDict.fromkeys(seq))


def echo(*args, file=None):
    """ None: Print timestamp and log message(s) to STDOUT. """
    print(clock(), *args, file=file, flush=True)


def fullpath(path=""):
    """ Path: Expand relative paths and tildes. """
    return Path.cwd() / Path(path).expanduser()


def getparams(profile):
    """ dict, list, or None: Read parameters from JSON file if it exists. """
    path = (REPO / "etc" / profile).with_suffix(".json")
    if path.is_file():
        with open(path, "r") as f:
            return readjson(f)


def hello(obj):
    """ None: Print short description of a Python object. """
    print(obj.__name__, type(obj).__name__, obj.__doc__, sep="\n")


def iterlines(*paths):
    """ Iterator[str]: Read one or more text files lazily. """
    for path in paths:
        with open(path) as file:
            yield from file

