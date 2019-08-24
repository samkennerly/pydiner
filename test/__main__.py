"""
Example: Discover and run tests in each module.
"""

def test_all(module):
    print('',module.__name__,10*'-',sep='\n')
    for name,meth in vars(module).items():
        if name.startswith('test_'):
            print(name)
            meth()

print('Run',__file__)

from . import test_fountain
test_all(test_fountain)

from . import test_utensils
test_all(test_utensils)

from . import fixtures
fixtures.cleartmp()

print('\nExit',__file__)