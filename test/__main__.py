"""
Example: Discover and run tests in each module.
"""
from . import fixtures, test_fountain, test_utensils


def test_all(module):
    print("", module.__name__, 10 * "-", sep="\n")
    for name, meth in vars(module).items():
        if name.startswith("test_"):
            print(name)
            meth()


print("Run", __file__)

test_all(test_fountain)
test_all(test_utensils)
fixtures.cleartmp()

print("\nExit", __file__)
