"""
Example: Discover and run tests in each module.
"""
from .fixtures import TMPDIR, bigprint, cleartmp, errors
from . import test_utensils

cleartmp()

failed = dict()
failed.update(errors(test_utensils))
bigprint(**failed)
print(f"{len(failed)} FAILURES" if failed else "OK")

cleartmp()
TMPDIR.rmdir()
