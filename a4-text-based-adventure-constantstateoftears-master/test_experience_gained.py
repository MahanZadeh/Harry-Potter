from unittest import TestCase
from game import experience_gained
from unittest.mock import patch
import io


class TestExperienceGained(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exp_increases(self, mock_output):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        actual = experience_gained(character)
        expected = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 100, "damage": "",
                    "recovery_rate": "", "attack_probability": ""}
        self.assertEqual(actual, expected)

    @patch('game.character_info',
           return_value={"name": "", "HP": 20, "max_HP": 30, "class": "1", "lvl": 2, "exp": 300, "damage": "",
                         "recovery_rate": 5, "attack_probability": 5})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_increases_after_300_exp(self, mock_output, mock_character_info_update):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 200, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        actual = experience_gained(character)
        expected = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 2, "exp": 300, "damage": "",
                    "recovery_rate": "", "attack_probability": ""}
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_output_is_dictionary(self, mock_output):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        actual = experience_gained(character)
        self.assertTrue(type(actual) is dict)
