from unittest import TestCase
from unittest.mock import patch
from game import make_character
import io


class TestMakeCharacter(TestCase):

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '1'])
    def test_make_gryffindor_lvl_1(self, mock_input, mock_damage, mock_output, mock_sleep):
        actual = make_character()
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                    "damage": 2, "recovery_rate": 4, "attack_probability": 3}
        self.assertEqual(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.damage_generator', return_value=10)
    @patch('builtins.input', side_effect=['Max', '2'])
    def test_make_slytherin_lvl_1(self, mock_input, mock_damage, mock_output, mock_sleep):
        actual = make_character()
        expected = {"name": "Max", "HP": 20, "max_HP": 20, "class": "2", "lvl": 1, "exp": 0,
                    "damage": 10, "recovery_rate": 3, "attack_probability": 6}
        self.assertEqual(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '3'])
    def test_make_ravenclaw_lvl_1(self, mock_input, mock_damage, mock_output, mock_sleep):
        actual = make_character()
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 1, "exp": 0,
                    "damage": 2, "recovery_rate": 4, "attack_probability": 4}
        self.assertEqual(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '4'])
    def test_make_hufflepuff_lvl_1(self, mock_input, mock_damage, mock_output, mock_sleep):
        actual = make_character()
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "4", "lvl": 1, "exp": 0,
                    "damage": 2, "recovery_rate": 3, "attack_probability": 6}
        self.assertEqual(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '4'])
    def test_data_structure_of_make_character(self, mock_input, mock_damage, mock_output, mock_sleep):
        actual = make_character()
        self.assertTrue(type(actual) is dict)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.damage_generator', return_value=2)
    @patch('builtins.input', side_effect=['Mahan', '4'])
    def test_correct_dictionary_length(self, mock_input, mock_damage, mock_output, mock_sleep):
        actual = len(make_character())
        expected = 9
        self.assertEqual(actual, expected)
