from unittest import TestCase
from game import ravenclaw_health


class TestRavenclawHealth(TestCase):

    def test_update_character_dictionary_level_1(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        character['lvl'] = 1
        actual = ravenclaw_health(character)
        expected = {"name": "", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0, "damage": "",
                    "recovery_rate": "", "attack_probability": ""}
        self.assertEqual(actual, expected)

    def test_update_character_dictionary_level_2(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 2, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        character['lvl'] = 2
        actual = ravenclaw_health(character)
        expected = {"name": "", "HP": 20, "max_HP": 30, "class": "1", "lvl": 2, "exp": 0, "damage": "",
                    "recovery_rate": "", "attack_probability": ""}
        self.assertEqual(actual, expected)

    def test_update_character_dictionary_level_3(self):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 3, "exp": 0, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        character['lvl'] = 3
        actual = ravenclaw_health(character)
        expected = {"name": "", "HP": 20, "max_HP": 40, "class": "1", "lvl": 3, "exp": 0, "damage": "",
                    "recovery_rate": "", "attack_probability": ""}
        self.assertEqual(actual, expected)

    def test_partial_character_dictionary(self):
        character = {"max_HP": "", "lvl": 1}
        character['lvl'] = 1
        actual = ravenclaw_health(character)
        expected = {"max_HP": 20, "lvl": 1}
        self.assertEqual(actual, expected)
