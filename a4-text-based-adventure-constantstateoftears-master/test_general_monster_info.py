from unittest import TestCase
from unittest.mock import patch
from game import general_monster_info



class TestGeneralMonsterInfo(TestCase):

    @patch('game.damage_generator', return_value=1)
    def test_general_monster_info(self, mock_damage):
        test_character = {"name": "Mahan", "HP": 20, "max_HP": 20, "class": "1", "lvl": 1, "exp": 0,
                          "damage": "", "recovery_rate": "", "attack_probability": ""}
        test_monster = {"name": "Dudley Dursley", "HP": "", "damage": "", "attack_probability": 3,
                        "description": "He looks as petulant as ever"}
        general_monster_info(test_character, test_monster)
        expected = {"name": "Dudley Dursley", "HP": 20, "damage": 1, "attack_probability": 3,
                    "description": "He looks as petulant as ever"}
        self.assertEqual(expected, test_monster)