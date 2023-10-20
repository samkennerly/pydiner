"""
Example: Run all tests in a module.
"""
from .fixtures import all_tests, bad_result, clear_tmpdir
from . import test_utensils


def errors(module):
    """ int: Run all tests in module. Return number of failed tests. """
    modname = module.__name__

    tests = all_tests(module)
    errors = [ bad_result(x) for x in tests ]
    for t, e in zip(tests, errors):
        print(f"{modname}.{t.__name__}: {e}")

    nerrors = sum( 1 for v in errors if v is not None )
    print(f"{nerrors} errors in {modname}")

    return errors

if any(errors(test_utensils)):
    print("*** FAIL ***")
else:
    print("OK!")

clear_tmpdir()
