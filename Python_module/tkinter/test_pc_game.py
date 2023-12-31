import unittest
from unittest import TestCase

import pytest

from Python_module.tkinter import pc_game
from Python_module.tkinter.pc_game import add_fixed_list


class TestPcGame(TestCase):
    def test_add_fixed_list(self):
        global key_color_index
        text_list = [1, 2, 3, 4, 5]
        self.assertEqual(add_fixed_list(text_list, 6, 5), [6, 2, 3, 4, 5])
        self.assertEqual(add_fixed_list(text_list, 7, 5), [6, 7, 3, 4, 5])
        pc_game.key_color_index = 0


@pytest.mark.parametrize("value,value1,value2,expected", [
    ([], '1', 5, ['1']),
    (['6', 2, 3, 4, 5], 7, 5, [7, 2, 3, 4, 5]),
    ([1], '1', 5, [1, '1']),
])
def test_add_fixed_list(value, value1, value2, expected):
    assert add_fixed_list(value, value1, value2) == expected


if __name__ == "__main__":
    unittest.main()
