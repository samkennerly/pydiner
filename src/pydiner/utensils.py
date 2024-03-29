"""
Utility functions.
"""
from collections import OrderedDict
from datetime import UTC, datetime
from itertools import islice, repeat, takewhile
from json import load as readjson
from pathlib import Path
from sys import stderr

# Absolute path to this repository
REPO = Path(__file__).resolve().parent.parent.parent


def achtung(*args, file=stderr):
    """None: Print timestamp and error message(s) to STDERR."""
    echo("\x1b[93m* WARNING *\x1b[0m", *args, file=file)


def batched(seq, n, joined=tuple, sliced=islice):
    """Iterator[tuple]: Length-limited batches taken from iterable."""
    return takewhile(len, (joined(sliced(x, n)) for x in repeat(iter(seq))))


def clock(timespec="seconds"):
    """str: UTC date and time in ISO format."""
    return datetime.now(UTC).isoformat(sep=" ", timespec=timespec)[:19]


def distinct(seq):
    """Iterator: Unique sequence elements in original order."""
    return iter(OrderedDict.fromkeys(seq))


def echo(*args, file=None):
    """None: Print timestamp and log message(s) to STDOUT."""
    print(clock(), *args, file=file, flush=True)


def fullpath(path=""):
    """Path: Expand relative paths and tildes."""
    return Path.cwd() / Path(path).expanduser()


def getparams(profile, **kwargs):
    """dict: kwargs, but with default values from a pre-saved profile."""
    profile = Path(profile).with_suffix(".json")

    with open(profile) as file:
        params = readjson(file)

    return {**params, **kwargs}


def hello(obj):
    """None: Print short description of a Python object."""
    print(obj.__name__, type(obj).__name__, obj.__doc__, sep="\n")


def iterlines(*paths):
    """Iterator[str]: Read one or more text files lazily."""
    for path in paths:
        with open(path) as file:
            yield from file


# Copyright © 2023 Sam Kennerly
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
