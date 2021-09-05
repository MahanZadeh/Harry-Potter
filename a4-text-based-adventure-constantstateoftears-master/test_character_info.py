from unittest import TestCase
from game import character_info
from unittest.mock import patch


class TestCharacterInfo(TestCase):

    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '1'])
    def test_make_gryffindor(self, mock_input, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = character_info(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                    "damage": 2, "recovery_rate": 4, "attack_probability": 3}
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=10)
    @patch('builtins.input', side_effect=['Max', '2'])
    def test_make_slytherin(self, mock_input, mock_damage):
        test_character = {"name": "Max", "HP": 20, "max_HP": "", "class": "2", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = character_info(test_character)
        expected = {"name": "Max", "HP": 20, "max_HP": 20, "class": "2", "lvl": 1, "exp": 0,
                    "damage": 10, "recovery_rate": 3, "attack_probability": 6}
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '3'])
    def test_make_ravenclaw(self, mock_input, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = character_info(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 1, "exp": 0,
                    "damage": 2, "recovery_rate": 4, "attack_probability": 4}
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '3'])
    def test_make_hufflepuff(self, mock_input, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "4", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = character_info(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "4", "lvl": 1, "exp": 0,
                    "damage": 2, "recovery_rate": 3, "attack_probability": 6}
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '4'])
    def test_data_structure_of_make_character(self, mock_input, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "4", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = character_info(test_character)
        self.assertTrue(type(actual) is dict)

    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '4'])
    def test_correct_dictionary_length(self, mock_input, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "4", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = len(character_info(test_character))
        expected = 9
        self.assertEqual(actual, expected)
