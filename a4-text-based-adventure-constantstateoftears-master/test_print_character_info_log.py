from unittest import TestCase
from game import print_character_info_log
from unittest.mock import patch
import io


class TestPrintCharacterInfoLog(TestCase):

    @patch('game.room_descriptions', return_value="gryffindor common room\n")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_info_log_correctly(self, mock_output, mock_room_desc):
        character = {"name": "", "HP": 20, "max_HP": "", "class": "1", "lvl": 1, "exp": 100, "damage": "",
                     "recovery_rate": "", "attack_probability": ""}
        print_character_info_log(character)
        actual_output = mock_output.getvalue()
        expected_output = (" Location: gryffindor common room\n\n"
                           " Health: 20\n"
                           " Level: 1\n"
                           " XP: 100\n")
        self.assertEqual(actual_output, expected_output)
