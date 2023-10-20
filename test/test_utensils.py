"""
Tests for the 'utensils' module
"""
from datetime import UTC, datetime, timedelta
from io import StringIO
from pathlib import Path

import pydiner
from .fixtures import TMPDIR


def test_batched(nseq=100, nbatch=23, joined=list):
    seq = joined(range(nseq))
    subseqs = [seq[i : i + nbatch] for i in range(0, nseq, nbatch)]
    batches = pydiner.batched(seq, nbatch, joined=joined)

    assert joined(batches) == subseqs, "value mismatch"


def test_clock(maxerr=timedelta(seconds=1)):
    now = datetime.now(tz=UTC)
    stamped = datetime.fromisoformat(pydiner.clock()).astimezone(UTC)

    assert abs(stamped - now) < maxerr, f"timestamps off by more than {maxerr}"


def test_distinct(n=1000, seq="spam", joined="".join):
    seq = joined(seq)
    vals = pydiner.distinct(n * seq)

    assert joined(vals) == seq, "value mismatch"


def test_fullpath():
    absolute = "/spam"
    relative = "spam/eggs.txt"

    assert pydiner.fullpath(absolute) == Path(absolute), "bad absolute path"
    assert pydiner.fullpath(relative) == Path.cwd() / relative, "bad relative path"


def test_iterlines(nfiles=3, nlines=10):
    folder = TMPDIR

    lines = [f"{i} spam\n" for i in range(nlines)]
    paths = [folder / f"spam{i}.txt" for i in range(nfiles)]
    for path in paths:
        with open(path, "w") as f:
            f.writelines(lines)

    output = pydiner.iterlines(*paths)

    assert list(output) == (nfiles * lines), "value mismatch"


def test_loggers():
    inputs = ["How about a nice game of", __file__, "?"]
    outstr = " ".join(str(x) for x in inputs) + "\n"

    for meth in (pydiner.achtung, pydiner.echo):
        with StringIO() as stream:
            meth(*inputs, file=stream)
            assert stream.getvalue().endswith(outstr), "value mismatch"
