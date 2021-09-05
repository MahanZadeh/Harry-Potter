from unittest import TestCase
from unittest.mock import patch
from game import room_descriptions


class TestRoomDescriptions(TestCase):

    @patch('random.choice', return_value="Gryffindor Common Room\n")
    def test_output_room_descriptions(self, random_string):
        expected_output = "Gryffindor Common Room\n"
        actual = room_descriptions()
        self.assertEqual(expected_output, actual)

    @patch('random.choice', return_value="Gryffindor Common Room\n")
    def test_output_is_string(self, random_string):
        actual = room_descriptions()
        self.assertTrue(type(actual) is str)
