from itertools import count

FIZZ, BUZZ, START, STOP, STEP = (3, 5, 1, 101, 1)


class Fountain:
    """
    Sliceable infinite FizzBuzz. Mostly useless.
    Example of using generators for lazy evaluation.
    The classic FizzBuzz problem is described here:

    https://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail/
    https://blog.codinghorror.com/why-cant-programmers-program/
    https://imranontech.com/2007/01/24/

    ---- Caution ----

    Never list(), tuple(), or set() a Fountain!
    Expressions like list(forever) will never return.
    https://en.wikipedia.org/wiki/Halting_problem

    ---- Examples ----

    Create a Fountain:
    >>> soda = Fountain(fizz=2,buzz=3)
    >>> soda
    Fountain(fizz=2,buzz=3)

    Get values one at a time:
    >>> soda[12]
    'FizzBuzz'
    >>> soda[-3]
    'Buzz'
    >>> soda[6_000_000_000_000_000]
    'FizzBuzz'

    Slicing a Fountain returns a tuple of strings, except...
    >>> soda[:6]
    ('FizzBuzz', '1', 'Fizz', 'Buzz', 'Fizz', '5')
    >>> soda[-6:0]
    ('FizzBuzz', '-5', 'Fizz', 'Buzz', 'Fizz', '-1')
    >>> soda[100:0:-13]
    ('Fizz', 'Buzz', 'Fizz', '61', 'FizzBuzz', '35', 'Fizz', 'Buzz')
    >>> soda[1_000_000_000_001:6_000_000_000_000:1_000_000_000_000]
    ('1000000000001', 'Buzz', '3000000000001', '4000000000001', 'Buzz')

    Slicing until "the end" is not possible.
    >>> soda[1:]
    Traceback (most recent call last):
    ...
    ValueError: endless slice

    Calling a Fountain returns a generator:
    >>> afew = soda(start=10,stop=2,step=-1)
    >>> type(afew)
    <class 'generator'>
    >>> ' '.join(afew)
    'Fizz Buzz Fizz 7 FizzBuzz 5 Fizz Buzz'
    >>> ' '.join(afew)
    ''

    Calling with stop=None returns an endless generator:
    >>> forever = soda(start=1,stop=None)
    >>> next(forever)
    '1'
    >>> [ next(forever) for x in range(5) ]
    ['Fizz', 'Buzz', 'Fizz', '5', 'FizzBuzz']

    Iterating over a Fountain is possible, but be careful.
    This loop is safe, but soda[9001] is much faster:
    >>> for i,x in enumerate(soda):
    ...     if i > 9000:
    ...         break
    >>> x
    '9001'

    This is the big difference between a Fountain and Sequence:
    >>> len(soda)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: FizzBuzz forever
    """

    def __init__(self, fizz=FIZZ, buzz=BUZZ):
        self.fizz = int(fizz)
        self.buzz = int(buzz)

    shape = property(lambda self: (self.fizz, self.buzz))

    def __bool__(self):
        """ bool: Hard-coded to avoid any __len__ calls. """
        return True

    def __call__(self, start=START, stop=STOP, step=STEP):
        """ Iterator[str]: Generate values for selected range. """
        fizz, buzz = self.fizz, self.buzz

        ints = count(start, step) if stop is None else range(start, stop, step)
        for i in ints:
            yield ("Fizz" * (not i % fizz) + "Buzz" * (not i % buzz)) or str(i)

    def __getitem__(self, i):
        """ str or Tuple[str,...]: Value(s) at selected index or slice. """

        if not isinstance(i, slice):
            return next(self(i, None, 1))

        start, stop, step = i.start or 0, i.stop, i.step or 1
        if stop is None:
            raise ValueError("endless slice")

        return tuple(self(start, stop, step))

    def __iter__(self):
        """ Iterator[str]: Values from 0 to forever. """
        return self(0, None, 1)

    def __len__(self):
        """ None: Raise error because math.inf is not an int. """
        raise ZeroDivisionError("FizzBuzz forever")

    def __repr__(self):
        """ str: Reproducible representation. """
        return f"{type(self).__name__}(fizz={self.fizz},buzz={self.buzz})"

    def __reversed__(self):
        """ Iterator[str]: Values from 0 to minus forever. """
        return self(0, None, -1)
