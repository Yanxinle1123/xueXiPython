import unittest
from unittest import TestCase

from comm.common import value4


class Test(TestCase):
    def test_value4(self):
        self.assertEqual(value4("4"), 4)
        self.assertEqual(value4("4.0"), 4)

    def test_value4_str(self):
        print(value4("one"))
        self.assertEqual(value4("one"), "one")


if __name__ == "__main__":
    unittest.main()
