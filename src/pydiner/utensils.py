"""
General-purpose utility functions.
"""
from collections import OrderedDict
from datetime import datetime
from itertools import islice, repeat, takewhile
from json import load as readjson
from pathlib import Path
from sys import stderr

REPO = Path(__file__).resolve().parents[2]

def achtung(*args,file=stderr):
    """ None: Print timestamp and error message(s) to STDERR. """
    print(isonow(),'\x1b[93mERROR',*args,'\x1b[0m',file=file,flush=True)

def batcher(seq,maxlen,batch=tuple,taker=islice):
    """ Iterator[tuple]: Length-limited batches taken from iterable. """
    return takewhile(len,( batch(taker(x,maxlen)) for x in repeat(iter(seq)) ))

def config(profile):
    """ dict: Read configuration file for selected profile. """
    path = (REPO/'etc'/profile).with_suffix('.json')
    with open(path,'r') as f:
        return readjson(f)

def distinct(seq):
    """ Iterator: Unique sequence elements in original order. """
    return iter(OrderedDict.fromkeys(seq))

def echo(*args,file=None):
    """ None: Print timestamp and log message(s) to STDOUT. """
    print(isonow(),*args,file=file,flush=True)

def fullpath(path=''):
    """ Path: Expand relative paths and tildes. """
    return Path.cwd()/Path(path).expanduser()

def genlines(*paths):
    """ Iterator[str]: Read lines from text file(s). """
    for path in paths:
        with open(path) as lines:
            yield from lines

def hello(obj):
    """ None: Print short description of a Python object. """
    print(type(obj).__name__,obj.__doc__ or 'No docstring!',sep='\n')

def isonow(sep='T',timespec='seconds'):
    """ str: UTC date and time in ISO format. """
    return datetime.utcnow().isoformat(sep=sep,timespec=timespec)
