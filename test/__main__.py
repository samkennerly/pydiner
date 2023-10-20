"""
Example: Run all tests in a module.
"""
from .fixtures import all_tests, bad_result, clear_tmpdir
from . import test_utensils

TEST_MODULES = (test_utensils, )


def errors(module):
    """ int: Run all tests in module. Return number of failed tests. """
    modname = module.__name__

    results = { x.__name__: bad_result(x) for x in all_tests(module) }
    for name, err in results.items():
        print(f"{modname}.{name}: {err}")

    errors = sum( 1 for v in results.values() if v is not None )
    print(f"\n{errors} errors in {modname}\n")

    return errors


print("Testing modules:", *TEST_MODULES, "", sep="\n")

clear_tmpdir()
nfails = sum( errors(x) for x in TEST_MODULES )

print(f"*** {nfails} FAILED TESTS ***") if nfails else print("OK!")
