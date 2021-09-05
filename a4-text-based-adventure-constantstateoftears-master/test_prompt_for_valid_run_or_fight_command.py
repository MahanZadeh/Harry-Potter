from unittest import TestCase
from unittest.mock import patch
from game import prompt_for_valid_run_or_fight_command


class TestPromptForValidRunOrFightCommand(TestCase):

    @patch('builtins.input', return_value="1")
    def test_prompt_for_valid_command_flee(self, mock_input):
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 0}
        expected = "1"
        actual = prompt_for_valid_run_or_fight_command(character)
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value="2")
    def test_prompt_for_valid_command_mid_combat_fight(self, mock_input):
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 0}
        expected = "2"
        actual = prompt_for_valid_run_or_fight_command(character)
        self.assertEqual(actual, expected)
