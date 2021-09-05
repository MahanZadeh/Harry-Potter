from unittest import TestCase
from unittest.mock import patch
from game import prompt_for_valid_class


class TestPromptForValidClass(TestCase):

    @patch('builtins.input', return_value="1")
    def test_prompt_for_gryffindor_class(self, mock_input):
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 0}
        expected = "1"
        actual = prompt_for_valid_class(character)
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="2")
    def test_prompt_for_slytherin_class(self, mock_input):
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 0}
        expected = "2"
        actual = prompt_for_valid_class(character)
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="3")
    def test_prompt_for_ravenclaw_class(self, mock_input):
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 0}
        expected = "3"
        actual = prompt_for_valid_class(character)
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="4")
    def test_prompt_for_hufflepuff(self, mock_input):
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 0}
        expected = "4"
        actual = prompt_for_valid_class(character)
        self.assertEqual(actual, expected)
