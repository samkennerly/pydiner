"""
Example: Discover and run tests in each module.
"""
import shutil

from . import *

print("Run", __file__)
fixtures.TMPDIR.mkdir(exist_ok=True)

test_module(test_utensils)

shutil.rmtree(fixtures.TMPDIR)
print("\nExit", __file__)
