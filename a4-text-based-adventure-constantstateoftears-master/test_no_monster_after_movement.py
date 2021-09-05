from unittest import TestCase
from game import no_monster_after_movement


class Test(TestCase):

    def test_healing_HP_less_than_difference_between_maxHP_and_HP(self):
        character = {"name": "", "HP": 15, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0, "damage": "",
             "recovery_rate": 4, "attack_probability": ""}
        expected = {"name": "", "HP": 19, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0, "damage": "",
             "recovery_rate": 4, "attack_probability": ""}
        actual = no_monster_after_movement(character)
        self.assertEqual(expected, actual)

    def test_healing_HP_more_than_difference_between_maxHP_and_HP(self):
        character = {"name": "", "HP": 17, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0, "damage": "",
             "recovery_rate": 5, "attack_probability": ""}
        expected = {"name": "", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0, "damage": "",
             "recovery_rate": 5, "attack_probability": ""}
        actual = no_monster_after_movement(character)
        self.assertEqual(expected, actual)

    def test_healing_HP_when_HP_equal_maxHP(self):
        character = {"name": "", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0, "damage": "",
             "recovery_rate": 4, "attack_probability": ""}
        expected = {"name": "", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0, "damage": "",
             "recovery_rate": 4, "attack_probability": ""}
        actual = no_monster_after_movement(character)
        self.assertEqual(expected, actual)


