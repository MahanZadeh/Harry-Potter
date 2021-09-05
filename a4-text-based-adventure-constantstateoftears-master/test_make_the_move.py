from unittest import TestCase
from game import make_the_move


class TestMakeTheMove(TestCase):

    def test_move_at_zero_zero_coordinates_going_right(self):
        location = [0, 0]
        command = "2"
        expected = [1, 0]
        actual = make_the_move(command, location)
        self.assertEqual(expected, actual)

    def test_move_at_zero_zero_coordinates_going_down(self):
        location = [0, 0]
        command = "3"
        expected = [0, 1]
        actual = make_the_move(command, location)
        self.assertEqual(expected, actual)

    def test_move_at_arbitrary_location_going_left(self):
        location = [15, 21]
        command = "1"
        expected = [14, 21]
        actual = make_the_move(command, location)
        self.assertEqual(expected, actual)

    def test_move_at_arbitrary_location_going_le(self):
        location = [7, 19]
        command = "4"
        expected = [7, 18]
        actual = make_the_move(command, location)
        self.assertEqual(expected, actual)
