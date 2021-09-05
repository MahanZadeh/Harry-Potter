from unittest import TestCase
from unittest.mock import patch
from game import character_emotional_descriptions


class TestCharacterEmotionalDescription(TestCase):

    @patch('random.choice', return_value="stare with indifference at the signed corpse of\n")
    def test_output_character_emotional_descriptions(self, random_number):
        expected_output = "stare with indifference at the signed corpse of\n"
        actual = character_emotional_descriptions()
        self.assertEqual(expected_output, actual)

    @patch('random.choice', return_value="stare with indifference at the signed corpse of\n")
    def test_output_is_string(self, random_number):
        actual = character_emotional_descriptions()
        self.assertTrue(type(actual) is str)
