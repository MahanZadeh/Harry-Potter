from unittest import TestCase
from unittest.mock import patch
from game import hufflepuff_damage


class TestHufflepuffDamage(TestCase):

    @patch('game.damage_generator', return_value=2)
    def test_hufflepuff_damage_lvl_1(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = hufflepuff_damage(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                    "damage": 2, "recovery_rate": '', "attack_probability": ''}
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=10)
    def test_hufflepuff_damage_lvl_2(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 2, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = hufflepuff_damage(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 2, "exp": 0,
                    "damage": 10, "recovery_rate": '', "attack_probability": ''}
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=15)
    def test_hufflepuff_damage_lvl_3(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 3, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = hufflepuff_damage(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 3, "exp": 0,
                    "damage": 15, "recovery_rate": '', "attack_probability": ''}
        self.assertEqual(expected, actual)
