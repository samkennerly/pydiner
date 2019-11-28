"""
Test frameworks might need this file to discover tests.
"""
from . import fixtures
from . import test_utensils

def test_module(module):
    """ None: Run all tests in module. """
    fixtures.bigprint(module.__name__)
    for name, obj in vars(module).items():
        if name.startswith("test_") and callable(obj):
            obj()
