import unittest
from unittest.mock import patch
from game import attack_description


class TestAttackDescription(unittest.TestCase):

    @patch('random.choice', return_value="Your spell proves ineffectual")
    def test_correct_message_returned_when_character_damage_less_than_five(self, mock_string):
        character_damage = 4
        actual = attack_description(character_damage)
        expected = "Your spell proves ineffectual"
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value="Now you are wizarding!")
    def test_correct_message_returned_when_character_damage_between_five_and_fifteen(self, mock_string):
        character_damage = 10
        actual = attack_description(character_damage)
        expected = "Now you are wizarding!"
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value="You land a powerful blow")
    def test_correct_message_returned_when_character_damage_more_than_fifteen(self, mock_string):
        character_damage = 15
        actual = attack_description(character_damage)
        expected = "You land a powerful blow"
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value="You land a powerful blow")
    def test_message_is_string(self, mock_string):
        character_damage = 15
        actual = attack_description(character_damage)
        self.assertTrue(type(actual) is str)
