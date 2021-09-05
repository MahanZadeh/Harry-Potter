from unittest import TestCase
from unittest.mock import patch
from game import get_user_command


class TestGetUserCommand(TestCase):

    @patch('builtins.input', return_value="1")
    def test_get_user_command_direction(self, mock_input):
        situation = "direction"
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0,
                     "attack_probability": 0}
        actual = get_user_command(situation, character)
        expected = "1"
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='1')
    def test_get_user_command_run(self, mock_input):
        situation = "run"
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0,
                     "attack_probability": 0}
        actual = get_user_command(situation, character)
        expected = "1"
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='2')
    def test_get_user_command_fight(self, mock_input):
        situation = "fight"
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0,
                     "attack_probability": 0}
        actual = get_user_command(situation, character)
        expected = "2"
        self.assertEqual(actual, expected)


    @patch('builtins.input', return_value = '1')
    def test_get_user_command_run_mid_combat(self, mock_input):
        situation = "run_mid_combat"
        character = {"name": "Mahan", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0,
                     "attack_probability": 0}
        actual = get_user_command(situation, character)
        expected = "1"
        self.assertEqual(actual, expected)

