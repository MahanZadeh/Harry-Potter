from unittest import TestCase
from unittest.mock import patch
from game import determine_the_high_roller


class TestDetermineTheHighRoller(TestCase):

    @patch('random.randint', side_effect=[5, 9])
    def test_dictionary_updates_when_starting_values_are_zero(self, random_output):
        dice_result = {"hero": 0, "monster": 0}
        character = {"name": "", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0,
                     "attack_probability": 4}
        monster = {"name": "A Death Eater", "HP": 25, "damage": "", "attack_probability": 6,
                   "description": "Why couldn't it have been a Pasta-Eater instead?"}
        actual = determine_the_high_roller(dice_result, character, monster)
        expected = {"hero": 5, "monster": 9}
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[5, 9])
    def test_dictionary_does_not_update_if_dice_result_is_the_same(self, random_output):
        dice_result = {"hero": 10, "monster": 12}
        character = {"name": "", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 4}
        monster = {"name": "A Death Eater", "HP": 25, "damage": "", "attack_probability": 6,
                   "description": "Why couldn't it have been a Pasta-Eater instead?"}
        actual = determine_the_high_roller(dice_result, character, monster)
        expected = {"hero": 10, "monster": 12}
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[5, 9])
    def test_dictionary_has_two_keys(self, random_output):
        dice_result = {"hero": 10, "monster": 12}
        character = {"name": "", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 4}
        monster = {"name": "A Death Eater", "HP": 25, "damage": "", "attack_probability": 6,
                   "description": "Why couldn't it have been a Pasta-Eater instead?"}
        actual = len(determine_the_high_roller(dice_result, character, monster))
        expected = 2
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[5, 9])
    def test_dictionary_values_are_integers(self, random_output):
        dice_result = {"hero": 10, "monster": 12}
        character = {"name": "", "HP": 20, "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "",
                     "recovery_rate": 0, "attack_probability": 4}
        monster = {"name": "A Death Eater", "HP": 25, "damage": "", "attack_probability": 6,
                   "description": "Why couldn't it have been a Pasta-Eater instead?"}
        actual = determine_the_high_roller(dice_result, character, monster)
        for values in actual.values():
            self.assertTrue(type(values) is int)
