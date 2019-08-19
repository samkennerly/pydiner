import datetime

import pydiner

def test_isonow():

    assert isinstance(pydiner.isonow(),str), "non-string output"

    now = datetime.datetime.utcnow
    delta = datetime.datetime.fromisoformat(pydiner.isonow()) - now()
    toolong = datetime.timedelta(seconds=1)

    assert abs(delta) < toolong, f"wrong time by >= {delta}"
