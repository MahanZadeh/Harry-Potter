from unittest import TestCase
from unittest.mock import patch
from game import ravenclaw_damage


class TestRavenclawDamage(TestCase):

    @patch('game.damage_generator', return_value=5)
    def test_ravenclaw_damage_lvl_1(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = ravenclaw_damage(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 1, "exp": 0,
                    "damage": 5, "recovery_rate": '', "attack_probability": ''}
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=10)
    def test_ravenclaw_damage_lvl_2(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 2, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = ravenclaw_damage(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 2, "exp": 0,
                    "damage": 10, "recovery_rate": '', "attack_probability": ''}
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=15)
    def test_gryffindor_damage_lvl_3(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 3, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = ravenclaw_damage(test_character)
        expected = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "3", "lvl": 3, "exp": 0,
                    "damage": 15, "recovery_rate": '', "attack_probability": ''}
        self.assertEqual(expected, actual)
