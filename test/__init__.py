"""
Help `python -m unittest` discover test modules.

The unittest framework replaces simple statements like:
>>> assert 0 != 1

with vastly more impressive boilerplate like:
>>> import unittest
>>> class TestSanity(unittest.TestCase):
...
...    def test_unity(self):
...        self.assertNotEqual(0,1)
...
... if __name__ == '__main__':
...    unittest.main()

and several dozen camelCase method names to memorize, including (but not limited
to! See the tables below for more assert methods...):

self.assertEqual(a, b)
self.assertNotEqual(a, b)
self.assertTrue(x)
self.assertFalse(x)
self.assertIs(a, b)
self.assertIsNot(a, b)
self.assertIsNone(x)
self.assertIsNotNone(x)
self.assertIn(a, b)
self.assertNotIn(a, b)
self.assertIsInstance(a, b)
self.assertNotIsInstance(a, b)

It is also possible to check the production of exceptions, warnings, and log
messages using the following methods:

self.assertRaises(exc, fun, *args, **kwds)
self.assertRaisesRegex(exc, r, fun, *args, **kwds)
self.assertWarns(warn, fun, *args, **kwds)
self.assertWarnsRegex(warn, r, fun, *args, **kwds)
self.assertLogs(logger, level)

There are also other methods used to perform more specific checks, such as:

self.assertAlmostEqual(a, b)
self.assertNotAlmostEqual(a, b)
self.assertGreater(a, b)
self.assertGreaterEqual(a, b)
self.assertLess(a, b)
self.assertLessEqual(a, b)
self.assertRegex(s, r)
self.assertNotRegex(s, r)
self.assertCountEqual(a, b)

The list of type-specific methods automatically used by assertEqual() are
summarized in the following table. Note that it’s usually not necessary to
invoke these methods directly, but there's no way to be certain!

self.assertMultiLineEqual(a, b)
self.assertSequenceEqual(a, b)
self.assertListEqual(a, b)
self.assertTupleEqual(a, b)
self.assertSetEqual(a, b)
self.assertDictEqual(a, b)

There are, of course, many more methods, some of which are deprecated. The
unittest module provides a rich set of tools for constructing and running tests.
Remember to call self.setUp() and self.tearDown() to prepare test fixtures!
"""
