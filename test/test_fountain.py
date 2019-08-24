"""
Example: Use doctest to test a module.
"""
import doctest

import pydiner


def test_fountain():
    assert not doctest.testmod(pydiner.fountain).failed
