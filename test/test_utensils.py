"""
Example: Use assert statements to test a module.
"""
import datetime
import io
import pathlib

import pydiner
from . import fixtures


def test_batcher():
    n, maxlen = 10, 3
    testvals = list(range(n))
    batches = [testvals[i : i + maxlen] for i in range(0, n, maxlen)]
    output = pydiner.batcher(testvals, maxlen, batch=list)

    assert list(output) == batches


def test_distinct():
    assert "".join(pydiner.distinct("spam" * 100)) == "spam"


def test_fullpath():
    absolute = "/spam"
    relative = "spam/eggs.txt"

    assert pydiner.fullpath(absolute) == pathlib.Path(absolute)
    assert pydiner.fullpath(relative) == pathlib.Path.cwd() / relative


def test_genlines():
    folder = fixtures.TMPDIR
    lines = [f"{i} spam\n" for i in range(10)]
    paths = [folder / f"spam{i}.txt" for i in range(3)]

    fixtures.cleartmp()
    for path in paths:
        with open(path, "w") as f:
            f.writelines(lines)

    lines = len(paths) * lines
    output = pydiner.genlines(*paths)

    assert list(output) == lines


def test_isonow():
    now = datetime.datetime.utcnow()
    stamped = datetime.datetime.fromisoformat(pydiner.isonow())
    longtime = datetime.timedelta(seconds=1)

    assert abs(stamped - now) < longtime


def test_loggers():
    methods = pydiner.achtung, pydiner.echo
    inputs = ["How about a nice game of", __file__, "?"]
    outstr = " ".join(map(str, inputs)) + "\n"

    for meth in methods:
        with io.StringIO() as stream:
            meth(*inputs, file=stream)
            assert stream.getvalue().endswith(outstr)
