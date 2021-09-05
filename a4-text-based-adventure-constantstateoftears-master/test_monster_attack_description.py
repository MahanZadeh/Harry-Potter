import unittest
from unittest.mock import patch
from game import monster_attack_description


class TestAttackDescription(unittest.TestCase):

    @patch('random.choice', return_value="You feel a slight pang of pain")
    def test_correct_message_returned_when_character_damage_less_than_five(self, mock_string):
        character_damage = 4
        actual = monster_attack_description(character_damage)
        expected = "You feel a slight pang of pain"
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value="Your ears start to ring and your mouth feels numb")
    def test_correct_message_returned_when_character_damage_between_five_and_eight(self, mock_string):
        character_damage = 7
        actual = monster_attack_description(character_damage)
        expected = "Your ears start to ring and your mouth feels numb"
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value="You feel excruciating, unbelievable pain")
    def test_correct_message_returned_when_character_damage_more_than_eight(self, mock_string):
        character_damage = 8
        actual = monster_attack_description(character_damage)
        expected = "You feel excruciating, unbelievable pain"
        self.assertEqual(actual, expected)

    @patch('random.choice', return_value="You scream: ARGGGHHHHHHHHH THE PAIN")
    def test_message_is_string(self, mock_string):
        character_damage = 15
        actual = monster_attack_description(character_damage)
        self.assertTrue(type(actual) is str)
