from unittest import TestCase
from game import monster_health_stats


class TestMonsterHealthStats(TestCase):

    def test_monster_health_when_character_lvl_1(self):
        character = {"name": "", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 4, "attack_probability": ""}
        monster = {"name": "Peter Pettigrew", "HP": "", "damage": "", "attack_probability": 5,
                   "description": "I thought I smelt a rat."}
        expected = {"name": "Peter Pettigrew", "HP": 20, "damage": "", "attack_probability": 5,
                    "description": "I thought I smelt a rat."}
        monster_health_stats(character, monster)
        actual = monster["HP"]
        self.assertEqual(actual, expected["HP"])

    def test_monster_health_when_character_lvl_2(self):
        character = {"name": "", "HP": 20, "max_HP": 20, "class": "1", "lvl": 2, "exp": 0, "damage": "",
                     "recovery_rate": 4, "attack_probability": ""}
        monster = {"name": "A Death Eater", "HP": "", "damage": "", "attack_probability": 6,
                   "description": "Why couldn't it have been a Pasta-Eater instead?"}
        expected = {"name": "A Death Eater", "HP": 25, "damage": "", "attack_probability": 6,
                    "description": "Why couldn't it have been a Pasta-Eater instead?"}
        monster_health_stats(character, monster)
        actual = monster["HP"]
        self.assertEqual(actual, expected["HP"])

    def test_monster_health_when_character_lvl_3(self):
        character = {"name": "", "HP": 20, "max_HP": 20, "class": "1", "lvl": 3, "exp": 0, "damage": "",
                     "recovery_rate": 4, "attack_probability": ""}
        monster = {"name": "A Death Eater", "HP": "", "damage": "", "attack_probability": 6,
                   "description": "Why couldn't it have been a Pasta-Eater instead?"}
        expected = {"name": "A Death Eater", "HP": 30, "damage": "", "attack_probability": 6,
                    "description": "Why couldn't it have been a Pasta-Eater instead?"}
        monster_health_stats(character, monster)
        actual = monster["HP"]
        self.assertEqual(actual, expected["HP"])
