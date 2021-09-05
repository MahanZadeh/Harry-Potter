from unittest import TestCase
from unittest.mock import patch
from game import monster_emotional_descriptions


class TestMonsterEmotionalDescription(TestCase):

    @patch('random.choice', return_value="an irate\n")
    def test_output_character_emotional_descriptions(self, random_message):
        expected_output = "an irate\n"
        actual = monster_emotional_descriptions()
        self.assertEqual(expected_output, actual)

    @patch('random.choice', return_value="an irate\n")
    def test_output_is_a_string(self, random_message):
        actual = monster_emotional_descriptions()
        self.assertTrue(type(actual) is str)
