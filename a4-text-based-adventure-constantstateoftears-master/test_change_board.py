from unittest import TestCase
from game import change_board


class TestChangeBoard(TestCase):

    def test_value_of_current_location_key_updates_correctly(self):
        current_location = [2, 2]
        board = {(0, 0): False, (2, 2): False}
        change_board(current_location, board)
        expected = {(0, 0): False, (2, 2): True}
        self.assertEqual(board, expected)

    def test_value_of_current_location_key_does_not_change_when_already_true(self):
        current_location = [0, 0]
        board = {(0, 0): True, (2, 2): False}
        change_board(current_location, board)
        expected = {(0, 0): True, (2, 2): False}
        self.assertEqual(board, expected)

    def test_all_keys_remain_tuples(self):
        current_location = [2, 2]
        board = {(0, 0): False, (2, 2): False}
        change_board(current_location, board)
        for keys in board.keys():
            self.assertTrue(type(keys) is tuple)

    def test_all_values_remain_booleans(self):
        current_location = [2, 2]
        board = {(0, 0): False, (2, 2): False}
        change_board(current_location, board)
        for values in board.values():
            self.assertTrue(type(values) is bool)

    def test_elements_of_keys_are_integers(self):
        current_location = [2, 2]
        board = {(0, 0): False, (2, 2): False}
        change_board(current_location, board)
        for keys in board.keys():
            for elements in keys:
                self.assertTrue(type(elements) is int)
