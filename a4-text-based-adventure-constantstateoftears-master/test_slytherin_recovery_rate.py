from unittest import TestCase
from game import slytherin_recovery_rate


class TestSlytherinRecoveryRate(TestCase):

    def test_update_character_dictionary_level_1(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        actual = slytherin_recovery_rate(character)
        expected = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 0, "damage": "",
                    "recovery_rate": 3, "attack_probability": ""}
        self.assertEqual(actual, expected)

    def test_update_character_dictionary_level_2(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 2, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        actual = slytherin_recovery_rate(character)
        expected = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 2, "exp": 0, "damage": "",
                    "recovery_rate": 4, "attack_probability": ""}
        self.assertEqual(actual, expected)

    def test_update_character_dictionary_level_3(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 3, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        actual = slytherin_recovery_rate(character)
        expected = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 3, "exp": 0, "damage": "",
                    "recovery_rate": 5, "attack_probability": ""}
        self.assertEqual(actual, expected)
