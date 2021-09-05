from unittest import TestCase
from game import hufflepuff_attack_probability


class TestHufflepuffAttackProbability(TestCase):

    def test_update_attack_probability_level_1(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        character['lvl'] = 1
        actual = hufflepuff_attack_probability(character)
        expected = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 0, "damage": "",
                    "recovery_rate": "", "attack_probability": 6}
        self.assertEqual(actual, expected)

    def test_update_attack_probability_level_2(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 2, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        character['lvl'] = 2
        actual = hufflepuff_attack_probability(character)
        expected = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 2, "exp": 0, "damage": "",
                    "recovery_rate": "", "attack_probability": 7}
        self.assertEqual(actual, expected)

    def test_update_attack_probability_level_3(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 3, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        character['lvl'] = 3
        actual = hufflepuff_attack_probability(character)
        expected = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 3, "exp": 0, "damage": "",
                    "recovery_rate": "", "attack_probability": 8}
        self.assertEqual(actual, expected)

    def test_partial_character_dictionary(self):
        character = {"attack_probability": "", "lvl": 1}
        character['lvl'] = 1
        actual = hufflepuff_attack_probability(character)
        expected = {"attack_probability": 6, "lvl": 1}
        self.assertEqual(actual, expected)
