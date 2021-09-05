from unittest import TestCase
from unittest.mock import patch
from game import choice_of_monsters


class TestChoiceOfMonsters(TestCase):

    @patch('game.damage_generator', return_value=1)
    @patch('random.choice', return_value={"name": "Dudley Dursley", "HP": "", "damage": "", "attack_probability": 3,
                                          "description": "He looks as petulant as ever"})
    def test_monster_dictionary_is_correctly_generated(self, mock_monster, mock_damage):
        character_test = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        expected = {"name": "Dudley Dursley", "HP": 20, "damage": 1, "attack_probability": 3,
                    "description": "He looks as petulant as ever"}
        actual = choice_of_monsters(character_test)
        self.assertEqual(expected, actual)

    @patch('game.damage_generator', return_value=1)
    @patch('random.choice', return_value={"name": "Dudley Dursley", "HP": "", "damage": "", "attack_probability": 3,
                                          "description": "He looks as petulant as ever"})
    def test_monster_dictionary_is_a_dictionary(self, mock_monster, mock_damage):
        character_test = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = choice_of_monsters(character_test)
        self.assertTrue(type(actual) is dict)

    @patch('game.damage_generator', return_value=1)
    @patch('random.choice', return_value={"name": "Dudley Dursley", "HP": "", "damage": "", "attack_probability": 3,
                                          "description": "He looks as petulant as ever"})
    def test_monster_dictionary_has_five_keys(self, mock_monster, mock_damage):
        character_test = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        actual = len(choice_of_monsters(character_test))
        expected = 5
        self.assertEqual(actual, expected)
