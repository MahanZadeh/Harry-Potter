from unittest import TestCase
from unittest.mock import patch
from game import monster_damage_stats


class TestMonsterDamage(TestCase):

    @patch('game.damage_generator', return_value=1)
    def test_monster_damage_lvl_1(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        test_monster = {"name": "Dudley Dursley", "HP": "", "damage": "", "attack_probability": 3,
                        "description": "He looks as petulant as ever"}
        monster_damage_stats(test_character, test_monster)
        expected = {"name": "Dudley Dursley", "HP": "", "damage": 1, "attack_probability": 3,
                    "description": "He looks as petulant as ever"}
        self.assertEqual(expected, test_monster)

    @patch('game.damage_generator', return_value=5)
    def test_monster_damage_lvl_2(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        test_monster = {"name": "Dudley Dursley", "HP": "", "damage": "", "attack_probability": 3,
                        "description": "He looks as petulant as ever"}
        monster_damage_stats(test_character, test_monster)
        expected = {"name": "Dudley Dursley", "HP": "", "damage": 5, "attack_probability": 3,
                    "description": "He looks as petulant as ever"}
        self.assertEqual(expected, test_monster)

    @patch('game.damage_generator', return_value=5)
    def test_monster_damage_lvl_3(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        test_monster = {"name": "Dudley Dursley", "HP": "", "damage": "", "attack_probability": 3,
                        "description": "He looks as petulant as ever"}
        monster_damage_stats(test_character, test_monster)
        expected = {"name": "Dudley Dursley", "HP": "", "damage": 5, "attack_probability": 3,
                    "description": "He looks as petulant as ever"}
        self.assertEqual(expected, test_monster)
