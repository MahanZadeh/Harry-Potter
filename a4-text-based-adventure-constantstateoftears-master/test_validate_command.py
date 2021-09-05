from unittest import TestCase
from game import validate_command


class TestValidateCommand(TestCase):

    def test_going_right_when_at_starting_location(self):
        location = [0, 0]
        command = "2"
        actual = validate_command(command, location)
        expected = "2"
        self.assertEqual(actual, expected)

    def test_going_left_when_at_starting_location(self):
        location = [0, 0]
        command = "1"
        actual = validate_command(command, location)
        expected = "not valid"
        self.assertEqual(actual, expected)

    def test_going_up_when_at_starting_location(self):
        location = [0, 0]
        command = "4"
        actual = validate_command(command, location)
        expected = "not valid"
        self.assertEqual(actual, expected)

    def test_going_down_when_at_starting_location(self):
        location = [0, 0]
        command = "3"
        actual = validate_command(command, location)
        expected = "3"
        self.assertEqual(actual, expected)

    def test_when_command_is_quit(self):
        location = [0, 0]
        command = "quit"
        actual = validate_command(command, location)
        expected = "quit"
        self.assertEqual(actual, expected)

    def test_when_command_at_random_coordinates(self):
        location = [5, 10]
        command = "3"
        actual = validate_command(command, location)
        expected = "3"
        self.assertEqual(actual, expected)
