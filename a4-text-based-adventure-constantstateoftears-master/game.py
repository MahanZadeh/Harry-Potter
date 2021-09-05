import random
import itertools
import time


def ENCOUNTER_MONSTER_PROBABILITY() -> int:
    """Generate a number representing the percent chance of a monster encounter.

    :return: number representing percent chance of monster encounter
    """
    return 20


def WIDTH_OF_BOARD() -> int:
    """Generate number representing the width of game board.

    :return: number representing width of game board
    """
    return 25


def HEIGHT_OF_BOARD() -> int:
    """Generate number representing the height of game board.

    :return: number representing height of game board
    """
    return 25


def STARTING_LOCATION() -> list:
    """

    :return:
    """
    return [0, 0]


def FINAL_BOSS_LOCATION() -> list:
    """

    :return:
    """
    return [24, 24]


def MAX_LEVEL() -> int:
    """Generate a number representing the maximum level attainable for hero in game.

    :return: number representing maximum attainable level of hero
    """
    return 3


def GRYFFINDOR_BASE_DAMAGE_LVL_1() -> int:
    """Generate a number representing the base amount of damage that the class of Gryffindor can preform at level one.

    :return: number representing base amount of damage that the Gryffindor class can preform at level one
    """
    return 8


def GRYFFINDOR_MAX_DAMAGE_LVL_1() -> int:
    """Generate a number representing the max amount of damage that the class of Gryffindor can preform at level one.

    :return: number representing max amount of damage that the Gryffindor class can preform at level one
    """
    return 20


def GRYFFINDOR_BASE_DAMAGE_LVL_2() -> int:
    """Generate a number representing the base amount of damage that the class of Gryffindor can preform at level two.

    :return: number representing base amount of damage that the Gryffindor class can preform at level two
    """
    return 12


def GRYFFINDOR_MAX_DAMAGE_LVL_2() -> int:
    """Generate a number representing the max amount of damage that the class of Gryffindor can preform at level two.

    :return: number representing max amount of damage that the Gryffindor class can preform at level one
    """
    return 24


def GRYFFINDOR_BASE_DAMAGE_LVL_3() -> int:
    """Generate a number representing the base amount of damage that the class of Gryffindor can preform at level two.

    :return: number representing base amount of damage that the Gryffindor class can preform at level two
    """
    return 16


def GRYFFINDOR_MAX_DAMAGE_LVL_3() -> int:
    """Generate a number representing the max amount of damage that the class of Gryffindor can preform at level three.

    :return: number representing max amount of damage that the Gryffindor class can preform at level three
    """
    return 30


def GRYFFINDOR_MAX_HP_LVL_1() -> int:
    """Generate a number representing max_HP for the class of Gryffindor at level one.

    :return: number representing max_HP at level one for the class of Gryffindor
    """
    return 20


def GRYFFINDOR_MAX_HP_LVL_2() -> int:
    """Generate a number representing max_HP for the class of Gryffindor at level two.

    :return: number representing max_HP at level two for the class of Gryffindor
    """
    return 30


def GRYFFINDOR_MAX_HP_LVL_3() -> int:
    """Generate a number representing max_HP for the class of Gryffindor at level three.

    :return: number representing max_HP at level three for the class of Gryffindor
    """
    return 50


def GRYFFINDOR_RECOVERY_RATE_LVL_1() -> int:
    """Generate a number representing the class of Gryffindor's recovery rate at level one.

    :return: number representing Gyffindor's recovery rate at level one
    """
    return 4


def GRYFFINDOR_RECOVERY_RATE_LVL_2() -> int:
    """Generate a number representing the class of Gryffindor's recovery rate at level two.

    :return: number representing Gryffindor's recovery rate at level two
    """
    return 5


def GRYFFINDOR_RECOVERY_RATE_LVL_3() -> int:
    """Generate a number representing the class of Gryffindor's recovery rate at level three.

    :return: number representing Gryffindor's recovery rate at level three
    """
    return 6


def GRYFFINDOR_ATTACK_PROBABILITY_LVL_1() -> int:
    """Generate a number representing attack probability for the class of Gryffindor at level one.

    :return: number representing Gryffindor's attack probability at level one
    """
    return 3


def GRYFFINDOR_ATTACK_PROBABILITY_LVL_2() -> int:
    """Generate a number representing attack probability for the class of Gryffindor at level two.

    :return: number representing Gryffindor's attack probability at level two
    """
    return 5


def GRYFFINDOR_ATTACK_PROBABILITY_LVL_3() -> int:
    """Generate a number representing attack probability for the class of Gryffindor at level three.

    :return: number representing Gryffindor's attack probability at level three
    """
    return 6


def SLYTHERIN_BASE_DAMAGE_LVL_1() -> int:
    """Generate a number representing the base amount of damage that the class of Slytherin can preform at level one.

    :return: number representing base amount of damage that the Slytherin class can preform at level one
    """
    return 8


def SLYTHERIN_MAX_DAMAGE_LVL_1() -> int:
    """Generate a number representing the max amount of damage that the class of Slytherin can preform at level one.

    :return: number representing max amount of damage that the Slytherin class can preform at level one
    """
    return 12


def SLYTHERIN_BASE_DAMAGE_LVL_2() -> int:
    """Generate a number representing the base amount of damage that the class of Slytherin can preform at level two.

    :return: number representing base amount of damage that the Slytherin class can preform at level two
    """
    return 10


def SLYTHERIN_MAX_DAMAGE_LVL_2() -> int:
    """Generate a number representing the max amount of damage that the class of Slytherin can preform at level two.

    :return: number representing max amount of damage that the Slytherin class can preform at level one
    """
    return 16


def SLYTHERIN_BASE_DAMAGE_LVL_3() -> int:
    """Generate a number representing the base amount of damage that the class of Slytherin can preform at level three.

    :return: number representing base amount of damage that the Slytherin class can preform at level three
    """
    return 14


def SLYTHERIN_MAX_DAMAGE_LVL_3() -> int:
    """Generate a number representing the max amount of damage that the class of Slytherin can preform at level three.

    :return: number representing max amount of damage that the Slytherin class can preform at level three
    """
    return 21


def SLYTHERIN_MAX_HP_LVL_1() -> int:
    """Generate a number representing max_HP for the class of Slytherin at level one.

    :return: number representing max_HP for the class of Slytherin at level one
    """
    return 20


def SLYTHERIN_MAX_HP_LVL_2() -> int:
    """Generate a number representing max_HP for the class of Slytherin at level two.

    :return: a number representing max_HP for the class of Slytherin at level two
    """
    return 25


def SLYTHERIN_MAX_HP_LVL_3() -> int:
    """Generate a number representing max_HP for the class of Slytherin at level three.

    :return: a number representing max_HP for the class of Slytherin at level three
    """
    return 30


def SLYTHERIN_ATTACK_PROBABILITY_LVL_1() -> int:
    """Generate a number representing attack probability for the class of Slytherin at level one.

    :return: number representing Slytherin's attack probability at level one
    """
    return 6


def SLYTHERIN_ATTACK_PROBABILITY_LVL_2() -> int:
    """Generate a number representing attack probability for the class of Slytherin at level two.

    :return: number representing Slytherin's attack probability at level two
    """
    return 7


def SLYTHERIN_ATTACK_PROBABILITY_LVL_3() -> int:
    """Generate a number representing attack probability for the class of Slytherin at level two.

    :return: number representing Slytherin's attack probability at level two
    """
    return 8


def SLYTHERIN_RECOVERY_RATE_LVL_1() -> int:
    """Generate a number representing the class of Slytherin's recovery rate at level one.

    :return: number representing Slytherin's recovery rate at level one
    """
    return 3


def SLYTHERIN_RECOVERY_RATE_LVL_2() -> int:
    """Generate a number representing the class of Slytherin's recovery rate at level two.

    :return: number representing Slytherin's recovery rate at level two
    """
    return 4


def SLYTHERIN_RECOVERY_RATE_LVL_3() -> int:
    """Generate a number representing the class of Slytherin's recovery rate at level three.

    :return: number representing Slytherin's recovery rate at level three
    """
    return 5


def RAVENCLAW_BASE_DAMAGE_LVL_1() -> int:
    """Generate a number representing the base amount of damage that the class of Ravenclaw can deal at level one.

    :return: number representing base amount of damage that the Ravenclaw class can deal at level one
    """
    return 5


def RAVENCLAW_MAX_DAMAGE_LVL_1() -> int:
    """Generate a number representing the max amount of damage that the class of Ravenclaw can deal at level one.

    :return: number representing max amount of damage that the Ravenclaw class can deal at level one
    """
    return 20


def RAVENCLAW_BASE_DAMAGE_LVL_2() -> int:
    """Generate a number representing the base amount of damage that the class of Ravenclaw can deal at level one.

    :return: number representing base amount of damage that the Ravenclaw class can deal at level one
    """
    return 8


def RAVENCLAW_MAX_DAMAGE_LVL_2() -> int:
    """Generate a number representing the max amount of damage that the class of Ravenclaw can deal at level two.

    :return: number representing max amount of damage that the Ravenclaw class can deal at level two
    """
    return 30


def RAVENCLAW_BASE_DAMAGE_LVL_3() -> int:
    """Generate a number representing the base amount of damage that the class of Ravenclaw can deal at level three.

    :return: number representing base amount of damage that the Ravenclaw class can deal at level three
    """
    return 10


def RAVENCLAW_MAX_DAMAGE_LVL_3() -> int:
    """Generate a number representing the max amount of damage that the class of Ravenclaw can deal at level three.

    :return: number representing max amount of damage that the Ravenclaw class can deal at level three
    """
    return 35


def RAVENCLAW_MAX_HP_LVL_1() -> int:
    """Generate a number representing max_HP for the class of Ravenclaw at level one.

    :return: number representing max_HP for the class of Ravenclaw at level one
    """
    return 20


def RAVENCLAW_MAX_HP_LVL_2() -> int:
    """Generate a number representing max_HP for the class of Ravenclaw at level two.

    :return: number representing max_HP for the class of Ravenclaw at level two
    """
    return 30


def RAVENCLAW_MAX_HP_LVL_3() -> int:
    """Generate a number representing max_HP for the class of Ravenclaw at level three.

    :return: number representing max_HP for the class of Ravenclaw at level three
    """
    return 40


def RAVENCLAW_RECOVERY_RATE_LVL_1() -> int:
    """Generate a number representing the class of Ravenclaw's recovery rate at level one.

    :return: number representing Ravenclaw's recovery rate at level one
    """
    return 4


def RAVENCLAW_RECOVERY_RATE_LVL_2() -> int:
    """Generate a number representing the class of Ravenclaw's recovery rate at level two.

    :return: number representing Ravenclaw's recovery rate at level two
    """
    return 5


def RAVENCLAW_RECOVERY_RATE_LVL_3() -> int:
    """Generate a number representing the class of Ravenclaw's recovery rate at level three.

    :return: number representing Ravenclaw's recovery rate at level three
    """
    return 5


def RAVENCLAW_ATTACK_PROBABILITY_LVL_1() -> int:
    """Generate a number representing attack probability for the class of Ravenclaw at level one.

    :return: number representing Ravenclaw's attack probability at level one
    """
    return 4


def RAVENCLAW_ATTACK_PROBABILITY_LVL_2() -> int:
    """Generate a number representing attack probability for the class of Ravenclaw at level two.

    :return: number representing Ravenclaw's attack probability at level two
    """
    return 5


def RAVENCLAW_ATTACK_PROBABILITY_LVL_3() -> int:
    """Generate a number representing attack probability for the class of Ravenclaw at level three.

    :return: number representing Ravenclaw's attack probability at level three
    """
    return 6


def HUFFLEPUFF_BASE_DAMAGE_LVL_1() -> int:
    """Generate a number representing the base amount of damage that the class of Hufflepuff can deal at level one.

    :return: number representing base amount of damage that the Hufflepuff class can deal at level one
    """
    return 10


def HUFFLEPUFF_MAX_DAMAGE_LVL_1() -> int:
    """Generate a number representing the max amount of damage that the class of Hufflepuff can deal at level one.

    :return: number representing max amount of damage that the Hufflepuff class can deal at level one
    """
    return 15


def HUFFLEPUFF_BASE_DAMAGE_LVL_2() -> int:
    """Generate a number representing the base amount of damage that the class of Hufflepuff can deal at level two.

    :return: number representing base amount of damage that the Hufflepuff class can deal at level two
    """
    return 15


def HUFFLEPUFF_MAX_DAMAGE_LVL_2() -> int:
    """Generate a number representing the max amount of damage that the class of Hufflepuff can deal at level two.

    :return: number representing max amount of damage that the Hufflepuff class can deal at level two
    """
    return 20


def HUFFLEPUFF_BASE_DAMAGE_LVL_3() -> int:
    """Generate a number representing the base amount of damage that the class of Hufflepuff can deal at level three.

    :return: number representing base amount of damage that the Hufflepuff class can deal at level three
    """
    return 20


def HUFFLEPUFF_MAX_DAMAGE_LVL_3() -> int:
    """Generate a number representing the max amount of damage that the class of Hufflepuff can deal at level three.

    :return: number representing max amount of damage that the Hufflepuff class can deal at level three
    """
    return 26


def HUFFLEPUFF_MAX_HP_LVL_1() -> int:
    """Generate a number representing max_HP for the class of Hufflepuff at level one.

    :return: number representing max_HP for the class of Hufflepuff at level one
    """
    return 20


def HUFFLEPUFF_MAX_HP_LVL_2() -> int:
    """Generate a number representing max_HP for the class of Hufflepuff at level two.

    :return: number representing max_HP for the class of Hufflepuff at level two
    """
    return 30


def HUFFLEPUFF_MAX_HP_LVL_3() -> int:
    """Generate a number representing max_HP for the class of Hufflepuff at level two.

    :return: number representing max_HP for the class of Hufflepuff at level two
    """
    return 35


def HUFFLEPUFF_RECOVERY_RATE_LVL_1() -> int:
    """Generate a number representing the class of Hufflepuff's recovery rate at level one.

    :return: number representing Hufflepuff's recovery rate at level one
    """
    return 3


def HUFFLEPUFF_RECOVERY_RATE_LVL_2() -> int:
    """Generate a number representing the class of Hufflepuff's recovery rate at level two.

    :return: number representing Hufflepuff's recovery rate at level two
    """
    return 4


def HUFFLEPUFF_RECOVERY_RATE_LVL_3() -> int:
    """Generate a number representing the class of Hufflepuff's recovery rate at level three.

    :return: number representing Hufflepuff's recovery rate at level three
    """
    return 6


def HUFFLEPUFF_ATTACK_PROBABILITY_LVL_1() -> int:
    """Generate a number representing attack probability for the class of Hufflepuff at level one.

    :return: number representing Hufflepuff's attack probability at level one
    """
    return 6


def HUFFLEPUFF_ATTACK_PROBABILITY_LVL_2() -> int:
    """Generate a number representing attack probability for the class of Hufflepuff at level two.

    :return: number representing Hufflepuff's attack probability at level two
    """
    return 7


def HUFFLEPUFF_ATTACK_PROBABILITY_LVL_3() -> int:
    """Generate a number representing attack probability for the class of Hufflepuff at level three.

    :return: number representing Hufflepuff's attack probability at level three
    """
    return 8


def MONSTER_BASE_DAMAGE_LVL_1() -> int:
    """Generate a number representing the base amount of damage a monster can deal at level one.

    :return: a number representing the base amount of damage a monster can deal at level one
    """
    return 1


def MONSTER_MAX_DAMAGE_LVL_1() -> int:
    """Generate a number representing the max amount of damage a monster can deal at level one.

    :return: a number representing the max amount of damage a monster can deal at level one
    """
    return 10


def MONSTER_BASE_DAMAGE_LVL_2() -> int:
    """Generate a number representing the base amount of damage a monster can deal at level two.

    :return: a number representing the base amount of damage a monster can deal at level two
    """
    return 5


def MONSTER_MAX_DAMAGE_LVL_2() -> int:
    """Generate a number representing the max amount of damage a monster can deal at level two.

    :return: a number representing the max amount of damage a monster can deal at level two
    """
    return 15


def MONSTER_BASE_DAMAGE_LVL_3() -> int:
    """Generate a number representing the base amount of damage a monster can deal at level three.

    :return: a number representing the base amount of damage a monster can deal at level three
    """
    return 5


def MONSTER_MAX_DAMAGE_LVL_3() -> int:
    """Generate a number representing the max amount of damage a monster can deal at level three.

    :return: a number representing the max amount of damage a monster can deal at level three
    """
    return 20


def MONSTER_HEALTH_LVL_1() -> int:
    """Generate a number representing the health points of a monster at level one.

    :return: a number representing the health points of a monster at level one
    """
    return 20


def MONSTER_HEALTH_LVL_2() -> int:
    """Generate a number representing the health points of a monster at level two.

    :return: a number representing the health points of a monster at level two
    """
    return 25


def MONSTER_HEALTH_LVL_3() -> int:
    """Generate a number representing the health points of a monster at level three.

    :return: a number representing the health points of a monster at level three
    """
    return 30


def make_character() -> dict:
    """Create character stats in the form of a dictionary.

    :return: character stats in the form of a dictionary
    """
    character = {"name": input("Sorting Hat: MMMHMM A muggle? But a powerful one. What is your name?"), "HP": 20,
                 "max_HP": "", "class": "", "lvl": 1, "exp": 0, "damage": "", "recovery_rate": 0,
                 "attack_probability": 0}
    character["class"] = get_user_command("class", character)
    character_info(character)
    return character


def damage_generator(base_attack: int, max_attack: int) -> ():
    """Generate a random attack damage number.

    :param base_attack: an integer
    :param max_attack: an integer
    :precondition base_attack: base_attack must be a positive integer less than max_attack
    :precondition max_attack: max_attack must be a positive integer greater than base_attack
    :return: a random positive integer representing the character's damage stat
    """

    def damage():
        """ Generate a random number between base_attack and max_attack.

        :return: a psuedo-random number in range of base_attack and max_attack
        """
        return random.randint(base_attack, max_attack)

    return damage


def character_info(character: dict) -> dict:
    """Update the character dictionary based on the player's chosen class.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character dictionary based on the player's chosen class
    :return: Updated character dictionary based on the player's chosen class
    """
    if character['class'] == "1":
        return gryffindor_info(character)
    elif character['class'] == "2":
        return slytherin_info(character)
    elif character['class'] == "3":
        return ravenclaw_info(character)
    elif character['class'] == "4":
        return hufflepuff_info(character)


def gryffindor_info(character: dict) -> dict:
    """Adjust character stats based on gryffindor class' specifications.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character dictionary with gryffindor stats
    :return: adjusted character stats based on gryffindor class' specifications
    """
    gryffindor_damage(character)
    gryffindor_health(character)
    gryffindor_recovery_rate(character)
    gryffindor_attack_probability(character)
    return character


def gryffindor_damage(character: dict) -> dict:
    """Adjust character damage stats for the class of Gryffindor determined by character["lvl"] key.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character damage with gryffindor's specifications
    :return: adjusted character damage with a function that generates a psuedo-random number, determined by
            character["lvl"] key
    """
    if character['lvl'] == 1:
        character['damage'] = damage_generator(GRYFFINDOR_BASE_DAMAGE_LVL_1(), GRYFFINDOR_MAX_DAMAGE_LVL_1())
    elif character['lvl'] == 2:
        character['damage'] = damage_generator(GRYFFINDOR_BASE_DAMAGE_LVL_2(), GRYFFINDOR_MAX_DAMAGE_LVL_2())
    elif character['lvl'] == 3:
        character['damage'] = damage_generator(GRYFFINDOR_BASE_DAMAGE_LVL_3(), GRYFFINDOR_MAX_DAMAGE_LVL_3())
    return character


def gryffindor_health(character: dict) -> dict:
    """Update gryffindor character's max_HP based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character health  with gryffindor stats
    :return: character stats with updated max_HP based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_health(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_health(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': 30, 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_health(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': 50, 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}
    """
    if character['lvl'] == 1:
        character['max_HP'] = GRYFFINDOR_MAX_HP_LVL_1()
    elif character['lvl'] == 2:
        character['max_HP'] = GRYFFINDOR_MAX_HP_LVL_2()
    elif character['lvl'] == 3:
        character['max_HP'] = GRYFFINDOR_MAX_HP_LVL_3()
    return character


def gryffindor_recovery_rate(character: dict) -> dict:
    """Update gryffindor character's recovery_rate based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's recovery_rate with gryffindor stats
    :return: character stats with updated recovery_rate based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_recovery_rate(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 4,\
 'attack_probability': 0}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_recovery_rate(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 5,\
 'attack_probability': 0}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_recovery_rate(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 6,\
 'attack_probability': 0}
    """
    if character['lvl'] == 1:
        character['recovery_rate'] = GRYFFINDOR_RECOVERY_RATE_LVL_1()
    elif character['lvl'] == 2:
        character['recovery_rate'] = GRYFFINDOR_RECOVERY_RATE_LVL_2()
    elif character['lvl'] == 3:
        character['recovery_rate'] = GRYFFINDOR_RECOVERY_RATE_LVL_3()
    return character


def gryffindor_attack_probability(character: dict) -> dict:
    """Update gryffindor character's recovery_rate based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's attack_probability with gryffindor stats
    :return: character stats with updated recovery_rate based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_attack_probability(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 3}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_attack_probability(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 5}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> gryffindor_attack_probability(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 6}
    """
    if character['lvl'] == 1:
        character['attack_probability'] = GRYFFINDOR_ATTACK_PROBABILITY_LVL_1()
    elif character['lvl'] == 2:
        character['attack_probability'] = GRYFFINDOR_ATTACK_PROBABILITY_LVL_2()
    elif character['lvl'] == 3:
        character['attack_probability'] = GRYFFINDOR_ATTACK_PROBABILITY_LVL_3()
    return character


def slytherin_info(character: dict) -> dict:
    """Adjust character stats based on slytherin class' specifications.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character dictionary with slytherin's stats
    :return: adjusted character stats based on slytherin class' specifications
    """
    slytherin_damage(character)
    slytherin_health(character)
    slytherin_attack_probability(character)
    slytherin_recovery_rate(character)
    return character


def slytherin_damage(character: dict) -> dict:
    """Adjust character damage stats for the class of Slytherin determined by character["lvl"] key.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's damage with slytherin's stats
    :return: adjusted character damage with a function that generates a psuedo-random number, determined by
            character["lvl"] key
    """
    if character['lvl'] == 1:
        character['damage'] = damage_generator(SLYTHERIN_BASE_DAMAGE_LVL_1(), SLYTHERIN_MAX_DAMAGE_LVL_1())
    elif character['lvl'] == 2:
        character['damage'] = damage_generator(SLYTHERIN_BASE_DAMAGE_LVL_2(), SLYTHERIN_MAX_DAMAGE_LVL_2())
    elif character['lvl'] == 3:
        character['damage'] = damage_generator(SLYTHERIN_BASE_DAMAGE_LVL_3(), SLYTHERIN_MAX_DAMAGE_LVL_3())
    return character


def slytherin_health(character: dict) -> dict:
    """Update slytherin character's max_HP based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's health with slytherin's stats
    :return: character stats with updated max_HP based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_health(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_health(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': 25, 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_health(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': 30, 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}
    """
    if character['lvl'] == 1:
        character['max_HP'] = SLYTHERIN_MAX_HP_LVL_1()
    elif character['lvl'] == 2:
        character['max_HP'] = SLYTHERIN_MAX_HP_LVL_2()
    elif character['lvl'] == 3:
        character['max_HP'] = SLYTHERIN_MAX_HP_LVL_3()
    return character


def slytherin_attack_probability(character: dict) -> dict:
    """Update slytherin character's recovery_rate based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's attack_probabilty with slytherin's stats
    :return: character stats with updated recovery_rate based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_attack_probability(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 6}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_attack_probability(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 7}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_attack_probability(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 8}
    """
    if character['lvl'] == 1:
        character['attack_probability'] = SLYTHERIN_ATTACK_PROBABILITY_LVL_1()
    elif character['lvl'] == 2:
        character['attack_probability'] = SLYTHERIN_ATTACK_PROBABILITY_LVL_2()
    elif character['lvl'] == 3:
        character['attack_probability'] = SLYTHERIN_ATTACK_PROBABILITY_LVL_3()
    return character


def slytherin_recovery_rate(character: dict) -> dict:
    """Update slytherin character's recovery_rate based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's recovery rate with slytherin's stats
    :return: character stats with updated recovery_rate based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_recovery_rate(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 3,\
 'attack_probability': 0}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_recovery_rate(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 4,\
 'attack_probability': 0}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> slytherin_recovery_rate(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 5,\
 'attack_probability': 0}
    """
    if character['lvl'] == 1:
        character['recovery_rate'] = SLYTHERIN_RECOVERY_RATE_LVL_1()
    elif character['lvl'] == 2:
        character['recovery_rate'] = SLYTHERIN_RECOVERY_RATE_LVL_2()
    elif character['lvl'] == 3:
        character['recovery_rate'] = SLYTHERIN_RECOVERY_RATE_LVL_3()
    return character


def ravenclaw_info(character: dict) -> dict:
    """Adjust character stats based on gryffindor class' specifications.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character dictionary with ravenclaw's stats
    :return: adjusted character stats based on ravenclaw's class' specifications
    """
    ravenclaw_damage(character)
    ravenclaw_health(character)
    ravenclaw_recovery_rate(character)
    ravenclaw_attack_probability(character)
    return character


def ravenclaw_damage(character: dict) -> dict:
    """Adjust character damage stats for the class of Ravenclaw determined by character["lvl"] key.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's damage with ravenclaw's stats
    :return: adjusted character damage with a function that generates a psuedo-random number, determined by
            character["lvl"] key
    """

    if character['lvl'] == 1:
        character['damage'] = damage_generator(RAVENCLAW_BASE_DAMAGE_LVL_1(), RAVENCLAW_MAX_DAMAGE_LVL_1())
    elif character['lvl'] == 2:
        character['damage'] = damage_generator(RAVENCLAW_BASE_DAMAGE_LVL_2(), RAVENCLAW_MAX_DAMAGE_LVL_2())
    elif character['lvl'] == 3:
        character['damage'] = damage_generator(RAVENCLAW_BASE_DAMAGE_LVL_3(), RAVENCLAW_MAX_DAMAGE_LVL_3())
    return character


def ravenclaw_health(character: dict) -> dict:
    """Update ravenclaw character's max_HP based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's health with ravenclaw's stats
    :return: character stats with updated max_HP based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> ravenclaw_health(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> ravenclaw_health(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': 30, 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> ravenclaw_health(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': 40, 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}
    """
    if character['lvl'] == 1:
        character['max_HP'] = RAVENCLAW_MAX_HP_LVL_1()
    elif character['lvl'] == 2:
        character['max_HP'] = RAVENCLAW_MAX_HP_LVL_2()
    elif character['lvl'] == 3:
        character['max_HP'] = RAVENCLAW_MAX_HP_LVL_3()
    return character


def ravenclaw_recovery_rate(character: dict) -> dict:
    """Update ravenclaw character's recovery_rate based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's recover_rate with ravenclaw's stats
    :return: character stats with updated recovery_rate based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> ravenclaw_recovery_rate(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 4,\
 'attack_probability': 0}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 4, 'attack_probability': 0}
    >>> ravenclaw_recovery_rate(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 5,\
 'attack_probability': 0}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> ravenclaw_recovery_rate(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 5,\
 'attack_probability': 0}
    """
    if character['lvl'] == 1:
        character['recovery_rate'] = RAVENCLAW_RECOVERY_RATE_LVL_1()
    elif character['lvl'] == 2:
        character['recovery_rate'] = RAVENCLAW_RECOVERY_RATE_LVL_2()
    elif character['lvl'] == 3:
        character['recovery_rate'] = RAVENCLAW_RECOVERY_RATE_LVL_3()
    return character


def ravenclaw_attack_probability(character: dict) -> dict:
    """Update ravenclaw character's recovery_rate based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's attack_probabilty with ravenclaw's stats
    :return: character stats with updated recovery_rate based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> ravenclaw_attack_probability(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 4}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> ravenclaw_attack_probability(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 5}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> ravenclaw_attack_probability(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 6}
    """
    if character['lvl'] == 1:
        character['attack_probability'] = RAVENCLAW_ATTACK_PROBABILITY_LVL_1()
    elif character['lvl'] == 2:
        character['attack_probability'] = RAVENCLAW_ATTACK_PROBABILITY_LVL_2()
    elif character['lvl'] == 3:
        character['attack_probability'] = RAVENCLAW_ATTACK_PROBABILITY_LVL_3()
    return character


def hufflepuff_info(character: dict) -> dict:
    """Adjust character stats based on gryffindor class' specifications.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character dictionary with hufflepuff's stats
    :return: adjusted character stats based on hufflepuff class' specifications
    """
    hufflepuff_damage(character)
    hufflepuff_health(character)
    hufflepuff_recovery_rate(character)
    hufflepuff_attack_probability(character)
    return character


def hufflepuff_damage(character: dict) -> dict:
    """Adjust character damage stats for the class of Gryffindor determined by character["lvl"] key.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's damage with hufflepuff's stats
    :return: adjusted character damage with a function that generates a psuedo-random number, determined by
    character["lvl"] key
    """
    if character['lvl'] == 1:
        character['damage'] = damage_generator(HUFFLEPUFF_BASE_DAMAGE_LVL_1(), HUFFLEPUFF_MAX_DAMAGE_LVL_2())
    elif character['lvl'] == 2:
        character['damage'] = damage_generator(HUFFLEPUFF_BASE_DAMAGE_LVL_2(), HUFFLEPUFF_MAX_DAMAGE_LVL_2())
    elif character['lvl'] == 3:
        character['damage'] = damage_generator(HUFFLEPUFF_BASE_DAMAGE_LVL_3(), HUFFLEPUFF_MAX_DAMAGE_LVL_3())
    return character


def hufflepuff_health(character: dict) -> dict:
    """Update hufflepuff character's max_HP based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's health with hufflepuff's stats
    :return: character stats with updated max_HP based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_health(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_health(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': 30, 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_health(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': 35, 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 0}
    """
    if character['lvl'] == 1:
        character['max_HP'] = HUFFLEPUFF_MAX_HP_LVL_1()
    elif character['lvl'] == 2:
        character['max_HP'] = HUFFLEPUFF_MAX_HP_LVL_2()
    elif character['lvl'] == 3:
        character['max_HP'] = HUFFLEPUFF_MAX_HP_LVL_3()
    return character


def hufflepuff_recovery_rate(character: dict) -> dict:
    """Update hufflepuff character's recovery_rate based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's recovery_rate with hufflepuff's stats
    :return: character stats with updated recovery_rate based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_recovery_rate(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 3,\
 'attack_probability': 0}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_recovery_rate(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 4,\
 'attack_probability': 0}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_recovery_rate(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 6,\
 'attack_probability': 0}
    """
    if character['lvl'] == 1:
        character['recovery_rate'] = HUFFLEPUFF_RECOVERY_RATE_LVL_1()
    elif character['lvl'] == 2:
        character['recovery_rate'] = HUFFLEPUFF_RECOVERY_RATE_LVL_2()
    elif character['lvl'] == 3:
        character['recovery_rate'] = HUFFLEPUFF_RECOVERY_RATE_LVL_3()
    return character


def hufflepuff_attack_probability(character: dict) -> dict:
    """Update hufflepuff character's recovery_rate based on their level.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly updates the character's attack_probabilty with hufflepuff's stats
    :return: character stats with updated recovery_rate based on their level

    >>> test_character_lvl_1 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_attack_probability(test_character_lvl_1)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 6}

    >>> test_character_lvl_2 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_attack_probability(test_character_lvl_2)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 2, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 7}

    >>> test_character_lvl_3 = {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 0, 'attack_probability': 0}
    >>> hufflepuff_attack_probability(test_character_lvl_3)
    {'name': '', 'HP': 20, 'max_HP': '', 'class': '', 'lvl': 3, 'exp': 0, 'damage': '', 'recovery_rate': 0,\
 'attack_probability': 8}
    """
    if character['lvl'] == 1:
        character['attack_probability'] = HUFFLEPUFF_ATTACK_PROBABILITY_LVL_1()
    elif character['lvl'] == 2:
        character['attack_probability'] = HUFFLEPUFF_ATTACK_PROBABILITY_LVL_2()
    elif character['lvl'] == 3:
        character['attack_probability'] = HUFFLEPUFF_ATTACK_PROBABILITY_LVL_3()
    return character


def get_user_command(situation: str, character: dict):
    """Prompt a valid command from the player based on the situation.

    :param situation: a string
    :param character: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :precondition situation: must be one of these three strings (direction, run, run_mid_combat)
    :precondition character: must be a dictionary of the player's information, it must include a "name" key whose value
     is the player's name
    :postcondition: depending on the situation, prompts the player to provide a valid command in the game
    :return: a valid command
    """
    if situation == "direction":
        return prompt_for_valid_direction(character)
    elif situation == "run":
        return prompt_for_valid_run_or_fight_command(character)
    elif situation == "run_mid_combat":
        return prompt_for_valid_run_or_fight_command_mid_combat(character)
    else:
        return prompt_for_valid_class(character)


def prompt_for_valid_direction(character: dict) -> str:
    """Prompt a valid direction from the player.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: solicits a valid directional or quit command from the player
    :return: a valid direction or a quit command
    """
    input_list = [(index, element) for index, element in enumerate(["left", "right", "down", "up"], 1)]
    command = input(f"Which way do you want to go {character['name']}? {input_list}): ").lower().strip()
    while command not in ["1", "2", "3", "4", "quit"]:
        command = input(f"I don't understand. Which way do you wish to go, {character['name']}?: ").lower().strip()
    return command


def prompt_for_valid_run_or_fight_command_mid_combat(character: dict) -> str:
    """Prompt the player to run or fight mid combat.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: solicits a valid run or fight command from the player
    :return: a valid run or fight command
    """
    input_list = [(index, element) for index, element in enumerate(["run", "fight"], 1)]
    command = input(
        f"The battle still rages, {character['name']},"
        f" you have the chance to flee!\n {input_list}?").lower().strip()
    while command not in ["1", "2"]:
        command = input(f"You don't have all day!!!{input_list}?").lower().strip()
    return command


def prompt_for_valid_run_or_fight_command(character: dict) -> str:
    """Prompt the player to run or fight before a combat round.

     :param character: a dictionary
     :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
     :postcondition: solicits a valid run or fight command from the player
     :return: a valid run or fight command
     """
    input_list = [(index, element) for index, element in enumerate(["run", "fight"], 1)]
    command = input(
        f"Someone approaches! Will you stay and fight {character['name']}\n {input_list}?").lower().strip()
    while command not in ["1", "2"]:
        command = input(f"The footsteps of an unknown opponent draw closer!"
                        f"What say you...{input_list}?").lower().strip()
    return command


def prompt_for_valid_class(character: dict) -> str:
    """Prompt the player to choose their class-type.

     :param character: a dictionary
     :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
     following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
     :postcondition: solicits a a class type ("gryffindor", "slytherin", "ravenclaw", or "hufflepuff") from the player
     :return: a valid class
     """
    input_list = [(index, element) for index, element in
                  enumerate(["gryffindor", "slytherin", "ravenclaw", "hufflepuff"], 1)]
    print(f"Well, this is quite a pickle. Usually I can tell someone's correct house nearly right away")
    time.sleep(4)
    print(f"But you, {character['name']}, are different. I sense great courage within you. But I also sense"
          f" a great evil and darkness. So please tell me, which House calls out to you?\n"
          f"To guide you, I will offer you a summary of each house.\n")
    time.sleep(8)
    print(f"The students of Gryffindor are the warriors of Hogwarts, dealing great damage through combative spells.\n"
          f"They are able to recover from even the most deadly blows.\n")
    time.sleep(6)
    print(f"Slytherin students are like snakes, eating away at their enemies with gradual damage, sly tactics and"
          f" toxic potions.\n")
    time.sleep(6)
    print(f"Those in Ravenclaw can cast powerful spells, but due to the complexity of these attacks they"
          f" can sometimes miss their mark.\n")
    time.sleep(5)
    print(f"Although often overlooked, Hufflepuff students are still powerful, combining potions and magic,"
          f" they deal reliable and consistent damage.\n"
          f"So tell me, {character['name']}, where do you belong?")
    command = input(f"{input_list}): ").lower().strip()
    while command not in ["1", "2", "3", "4"]:
        command = input(f"That's not a House! Which House speaks to you? {character['name']}?: ").lower().strip()
    return command


def outcomes_of_moving(character: dict) -> dict:
    """Update the character's stats based on the outcome of their move.

    This function determines whether a monster will appear or not, and if it does, it provides the player with the
    option to flee or combat the monster. In the end, it will return the character's updated HP

    :param character: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage",
    "recovery_rate", "attack_probability")
    :precondition output: output must be a list of relevant print-messages to notify the player of the progression of
    the game
    :postcondition: correctly updates the player's stats based on the outcome of their move
    :return: character's updated stats based on the outcome of their move
    """
    if random.randint(1, 100) >= ENCOUNTER_MONSTER_PROBABILITY():
        print(f"The coast is clear.")
        no_monster_after_movement(character)
    else:
        print(f"Who's that lurking in the shadows?")
        encounter_monster(character)
    return character


def no_monster_after_movement(character: dict):
    """Update the character's HP when no monster appears after moving.

    :param character: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition output: output must be a list of relevant print-messages to notify the player of the progression of
    the game
    :postcondition: correctly updates the character's HP after they move and do not face a monster
    :return: character's updated HP after they move and do not face a monster

    >>> test_character = {'name': '', 'HP': 15, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 3, 'attack_probability': 0}
    >>> no_monster_after_movement(test_character)
    {'name': '', 'HP': 18, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 3,\
 'attack_probability': 0}

    >>> test_character = {'name': '', 'HP': 19, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 3, 'attack_probability': 0}
    >>> no_monster_after_movement(test_character)
    {'name': '', 'HP': 20, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 3,\
 'attack_probability': 0}

    >>> test_character = {'name': '', 'HP': 20, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 3, 'attack_probability': 0}
    >>> no_monster_after_movement(test_character)
    {'name': '', 'HP': 20, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '', 'recovery_rate': 3,\
 'attack_probability': 0}
    """
    if character["HP"] <= character["max_HP"] - character["recovery_rate"]:
        character["HP"] += character["recovery_rate"]
    else:
        character["HP"] = character["max_HP"]
    return character


def validate_command(command: str, current_location: list) -> str:
    """Validate player's command.

    :param command: a string
    :param current_location: a list
    :precondition command: must be a string in ["1", "2", "3", "4", "quit"]
    :precondition current_location: must be a list with two numerical elements corresponding to the x, y coordinates of
     the player on the grid
    :postcondition: correctly determines if the player's command is valid based on their current_location
    :return: a string indicating if the player's command is a valid one or not

    >>> validate_command("1", [0, 0])
    'not valid'
    >>> validate_command("2", [4, 2])
    '2'
    >>> validate_command("3", [2, 4])
    '3'
    >>> validate_command("4", [4, 0])
    'not valid'
    >>> validate_command("1", [2, 2])
    '1'
    >>> validate_command("2", [2, 2])
    '2'
    >>> validate_command("3", [2, 2])
    '3'
    >>> validate_command("4", [2, 2])
    '4'
    >>> validate_command("quit", [3, 4])
    'quit'
    """
    if command == "1" and (current_location[0] - 1) in range(0, WIDTH_OF_BOARD()):
        return command
    elif command == "2" and (current_location[0] + 1) in range(0, WIDTH_OF_BOARD()):
        return command
    elif command == "3" and (current_location[1] + 1) in range(0, HEIGHT_OF_BOARD()):
        return command
    elif command == "4" and (current_location[1] - 1) in range(0, HEIGHT_OF_BOARD()):
        return command
    elif command == "quit":
        return command
    else:
        return "not valid"


def make_the_move(valid_move, current_location: list) -> list:
    """Update player's position.

    :param valid_move: a string
    :param current_location: a list
    :precondition valid_move: must be a string in ["1", "2", "3", "4"]
    :precondition current_location: must be a list with two numerical elements corresponding to the y, x coordinates of
                                    the player on the grid
    :postcondition: correctly updates the player's location on the grid
    :return: the player's updated location on the grid

    >>> make_the_move("1", [2, 3])
    [1, 3]
    >>> make_the_move("2", [0, 0])
    [1, 0]
    >>> make_the_move("3",[1, 2])
    [1, 3]
    >>> make_the_move("4", [2, 3])
    [2, 2]
    >>> make_the_move("1", [0, 0])
    [-1, 0]
    >>> make_the_move("3", [2, 4])
    [2, 5]
    """
    if valid_move == "1":
        current_location[0] -= 1
    elif valid_move == "2":
        current_location[0] += 1
    elif valid_move == "3":
        current_location[1] += 1
    elif valid_move == "4":
        current_location[1] -= 1
    return current_location


def monster_damage_stats(character: dict, monster: dict):
    """Assign different levels of monster-damage based on the player's character level.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition monster: monster must be a dictionary where the keys are the attributes of the player. It must have
    the following keys ("name", "HP", "damage", "damage", "attack_probability")
    :postcondition: correctly modifies the monster's damage stat based on the character's level
    """
    if character["lvl"] == 1:
        monster["damage"] = damage_generator(MONSTER_BASE_DAMAGE_LVL_1(), MONSTER_MAX_DAMAGE_LVL_1())
    if character["lvl"] == 2:
        monster["damage"] = damage_generator(MONSTER_BASE_DAMAGE_LVL_1(), MONSTER_MAX_DAMAGE_LVL_2())
    if character["lvl"] == 3:
        monster["damage"] = damage_generator(MONSTER_BASE_DAMAGE_LVL_3(), MONSTER_MAX_DAMAGE_LVL_3())


def monster_health_stats(character: dict, monster: dict):
    """Assign different levels of monster-HP based on the player's character level.

    :param character: a dictionary
    :param monster: a dictionry
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition monster: monster must be a dictionary where the keys are the attributes of the player. It must have
    the following keys ("name", "HP", "damage", "damage", "attack_probability")
    :postcondition: correctly modifies the monster's HP stat based on the character's level

    >>> test_character_lvl_1 = {'name': '', 'HP': 15, 'max_HP': 20, 'class': '', 'lvl': 1, 'exp': 0, 'damage': '',\
     'recovery_rate': 3, 'attack_probability': 0}
    >>> test_monster = {'name': 'Dudley Dursley', 'HP': '', 'damage': '', 'attack_probability': 3,\
    "description": "He looks as petulant as ever"}
    >>> monster_health_stats(test_character_lvl_1, test_monster)
    >>> test_monster
    {'name': 'Dudley Dursley', 'HP': 20, 'damage': '', 'attack_probability': 3,\
 'description': 'He looks as petulant as ever'}

    >>> test_character_lvl_2 = {'name': '', 'HP': 15, 'max_HP': 20, 'class': '', 'lvl': 2, 'exp': 0, 'damage': '',\
     'recovery_rate': 3, 'attack_probability': 0}
    >>> test_monster = {'name': 'Dudley Dursley', 'HP': '', 'damage': '', 'attack_probability': 3,\
    "description": "He looks as petulant as ever"}
    >>> monster_health_stats(test_character_lvl_2, test_monster)
    >>> test_monster
    {'name': 'Dudley Dursley', 'HP': 25, 'damage': '', 'attack_probability': 3,\
 'description': 'He looks as petulant as ever'}

    >>> test_character_lvl_3 = {'name': '', 'HP': 15, 'max_HP': 20, 'class': '', 'lvl': 3, 'exp': 0, 'damage': '',\
     'recovery_rate': 3, 'attack_probability': 0}
    >>> test_monster = {'name': 'Dudley Dursley', 'HP': '', 'damage': '', 'attack_probability': 3,\
    "description": "He looks as petulant as ever"}
    >>> monster_health_stats(test_character_lvl_3, test_monster)
    >>> test_monster
    {'name': 'Dudley Dursley', 'HP': 30, 'damage': '', 'attack_probability': 3,\
 'description': 'He looks as petulant as ever'}
    """
    if character["lvl"] == 1:
        monster["HP"] = MONSTER_HEALTH_LVL_1()
    if character["lvl"] == 2:
        monster["HP"] = MONSTER_HEALTH_LVL_2()
    if character["lvl"] == 3:
        monster["HP"] = MONSTER_HEALTH_LVL_3()


def general_monster_info(character: dict, monster: dict) -> dict:
    """Modify monster's damage and health stats based on the character's level.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player.
    It must have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition monster: monster must be a dictionary where the keys are the attributes of the player. It must have
    the following keys ("name", "HP", "damage", "damage", "attack_probability")
    :postcondition: correctly modifies the monster' health and damage stats based on the character's level
    :return: an updated monster dictionary, determined by character level
    """
    monster_damage_stats(character, monster)
    monster_health_stats(character, monster)
    return monster


def choice_of_monsters(character: dict) -> dict:
    """Provide a random monster.

    :return: a randomly chosen monster dictionary
    """
    monster_one = {"name": "Dudley Dursley", "HP": "", "damage": "", "attack_probability": 3,
                   "description": "He looks as petulant as ever"}
    monster_two = {"name": "A Death Eater", "HP": "", "damage": "", "attack_probability": 6,
                   "description": "Why couldn't it have been a Pasta-Eater instead?"}
    monster_three = {"name": "Barty Crouch Jr.", "HP": "", "damage": "", "attack_probability": 5,
                     "description": "That's not Madeye Moody"}
    monster_four = {"name": "Bellatrix Lestrange", "HP": "", "damage": "", "attack_probability": 5,
                    "description": "Although she's totally evil, she's also totally my type"}
    monster_five = {"name": "Professor Snape", "HP": "", "damage": "", "attack_probability": 4,
                    "description": "How does this hack have a teaching position?"}
    monster_six = {"name": "Draco Malfoy", "HP": "", "damage": "", "attack_probability": 3,
                   "description": "Why is his hair always slicked back?"}
    monster_seven = {"name": "Aunt Marge", "HP": "", "damage": "", "attack_probability": 4,
                     "description": "Time for some payback!"}
    monster_eight = {"name": "Peter Pettigrew", "HP": "", "damage": "", "attack_probability": 5,
                     "description": "I thought I smelt a rat."}
    monster_nine = {"name": "Gilderoy Lockhart", "HP": "", "damage": "", "attack_probability": 6,
                    "description": "I want to hate him, but he's just too damn hunky."}
    monster_ten = {"name": "Aragog", "HP": "", "damage": "", "attack_probability": 7,
                   "description": "A GIANT SPIDER???"}

    list_of_monsters = [monster_one, monster_two, monster_three, monster_four, monster_five, monster_six, monster_seven,
                        monster_eight, monster_nine, monster_ten]
    selected_monster = random.choice(list_of_monsters)
    general_monster_info(character, selected_monster)
    return selected_monster


def determine_the_high_roller(dice_result: dict, character: dict, monster) -> dict:
    """Determine the high dice roller at the beginning of each combat round.

    :param dice_result: a dictionary
    :param character: a dictionary
    :param monster: a dictionary
    :precondition dice_result: must be a dictionary with two key-value pairs {"hero": 0, "monster": 0}
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition monster: monster must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "damage", "damage", "attack_probability")
    :postcondition: correctly updates the dice_result dictionary with the result of the hero and monster's dice rolls
    :return: updated dice_result dictionary
    """
    while dice_result["hero"] == dice_result["monster"]:
        dice_result["hero"] = random.randint(1, character["attack_probability"])
        dice_result["monster"] = random.randint(1, monster["attack_probability"])
    return dice_result


def attack_description(character_damage: int) -> str:
    """Provide a descriptive statement during combat based on damage dealt

    :param character_damage: an integer
    :precondition: character_damage must be an integer
    :postcondition: a randomly chosen description based on damage dealt
    :return: a descriptive statement during combat, based on damage dealt
    """
    low_level_damage = ["Your spell proves ineffectual", "You stumble over the words of your spell",
                        "Your spell is weak, maybe the Sorting Hat was wrong about you!",
                        "You mispronounce 'Avada Kedavra', nothing significant happens",
                        "Are you a wizard or magician?"]
    mid_level_damage = ["Your spell hits the mark!", "Now you are wizarding!",
                        "You hear a satisfying thud as your spell hits your opponent",
                        "You scream: Wingardium Leviosa. Propelling your opponent across the room",
                        "You wish all those muggles back home could see you now",
                        "If only class included this much violence"]
    high_level_damage = ["You land a powerful blow", "A violent stream of light propels from your wand",
                         "Your incantation proves powerful!",
                         "You scream 'Avada Kedavra', pale light streams from your wand"]

    if character_damage <= 5:
        return random.choice(low_level_damage)
    elif character_damage <= 15:
        return random.choice(mid_level_damage)
    elif character_damage > 15:
        return random.choice(high_level_damage)


def monster_attack_description(monster_damage: int) -> str:
    """Provide a descriptive statement during combat based on damage dealt by monster

    :param monster_damage: an integer
    :precondition: monster_damage must be an integer
    :postcondition: a randomly chosen description based on damage dealt by monster
    :return: a descriptive statement during combat, based on damage dealt by monster
    """
    low_level_damage = ["You feel a slight pang of pain", "A strange numbing sensation spreads through your body",
                        "You think to yourself: Is this the worst they can do?",
                        "A weak spell pings off your head", "Was that even a spell? You don't feel much of any pain.",
                        "Your opponent yells: Expelliarmus. Yet, they fail to disarm you."]
    mid_level_damage = ["Your ears start to ring and your mouth feels numb",
                        "You think: if this is wizarding, it sure hurts",
                        "A spell whizzes into your chest", "You keel over gasping for breath",
                        "Your opponent mumbles a strange spell.",
                        "Your opponent casts 'Obliviate' and suddenly you forget who you are!"]
    high_level_damage = ["You feel excruciating, unbelievable pain", "You crave the sweet relief of death",
                         "You scream: ARGGGHHHHHHHHH THE PAIN",
                         "You longingly think of the muggle life you've left behind",
                         "Your heart sinks as you hear your opponent scream: AVADA KEDAVRA"]

    if monster_damage <= 5:
        return random.choice(low_level_damage)
    elif monster_damage <= 8:
        return random.choice(mid_level_damage)
    elif monster_damage > 8:
        return random.choice(high_level_damage)


def character_deals_damage(character: dict, monster: dict) -> dict:
    """Reduce monster's HP based on the character's damage.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition character: must be a dictionary of the character's stats
    :precondition monster: must be a dictionary of the monster's stats
    :postcondition: correctly updates the monster's HP based on the character's damage
    :return: updated monster dictionary after taking damage
    """
    character_attack = character["damage"]()
    monster["HP"] -= character_attack
    if monster["HP"] <= 0:
        monster["HP"] = 0
    print(f'\n{attack_description(character_attack)}')
    time.sleep(2)
    print(f'You deal {character_attack} damage')
    time.sleep(2)
    print(f'{monster["name"]} HP: {monster["HP"]} \n')
    time.sleep(2)
    return monster


def monster_deals_damage(character: dict, monster: dict) -> dict:
    """Reduce character's HP based on the character's damage.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition monster: monster must be a dictionary where the keys are the attributes of the player. It must have
    the following keys ("name", "HP", "damage", "damage", "attack_probability")
    :postcondition: correctly updates the character's HP based on the monster's damage
    :return: updated character dictionary after taking damage
    """
    monster_attack = monster["damage"]()
    character["HP"] -= monster_attack
    if character["HP"] <= 0:
        character["HP"] = 0
    print(f'\n{monster["name"]} strikes you, dealing {monster_attack} damage.')
    time.sleep(2)
    print(f'{monster_attack_description(monster_attack)}')
    time.sleep(2)
    print(f'Your Health: {character["HP"]} \n')
    time.sleep(2)
    return character


def character_emotional_descriptions() -> str:
    """Provide a randomly chosen emotion that prints after a completed combat round.

    :return: a randomly chosen emotional state
    """

    vengeful_emotions = ["stare with indifference at the signed corpse of", "spit with disgust on the bruised body of",
                         "smirk with satisfaction, as you stand over",
                         "laugh triumphantly at the badly beaten figure of",
                         "feel a slight pang of regret, as you examine the remains of",
                         "weep silently as you realize you are a murderer and have killed:",
                         "overlook the wreckage. You can't even recognize the remains of:",
                         "think, perhaps, you should have gone to grad school instead of murdering:"]
    return random.choice(vengeful_emotions)


def monster_emotional_descriptions() -> str:
    """Provide a randomly chosen emotion of the monster.

    :return: a randomly chosen emotional state
    """
    emotions = ["an irate", "a disgusted", "a perturbed", "a weeping", "a bloody", "a dazed", "an inconsolable",
                "an angry", "a cackling", "a disapproving", "a hesitant", "a depressed", 'an indignant']
    return random.choice(emotions)


def experience_gained(character: dict) -> dict:
    """Update character's experience and level.

    :param character: a dictionary
    :precondition: character must be a dictionary of the player's stats. It should include at least two key-value pairs
    of "exp" and "lvl"
    :postcondition: correctly updates the character's experience and level
    :return: updated character's dictionary
    """
    character["exp"] += 100
    if character["exp"] >= 300:
        character["lvl"] = int(character["exp"] / 300) + 1
        character_info(character)
    elif character["lvl"] >= MAX_LEVEL():
        character["lvl"] = 3

    if character["exp"] == 300:
        print(f"Dumbledore: Congratulations, {character['name']}! Your wizarding mastery has increased, "
              f"You can now cast spells like a second year student.")
    elif character["exp"] == 600:
        print(f"Dumbledore: Congratulations, {character['name']}! Your wizarding mastery has increased, "
              f"You can now cast spells like a three year student.")

    return character


def encounter_monster(character: dict) -> dict:
    """Determine the outcome of encountering a monster after having moved.

    :param character: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :postcondition: correctly updates the character's stats (i.e., HP, exp, lvl) after encountering a monster
    :return: updated dictionary of the character's stats based on the outcome of their encounter with the monster
    """
    run_or_fight = get_user_command("run", character)
    monster = choice_of_monsters(character)
    monster_fleeing = False
    print(f'You see {monster_emotional_descriptions()} {monster["name"]}, '
          f'and think to yourself: {monster["description"]}')
    while character["HP"] > 0 and run_or_fight != "1" and monster["HP"] > 0 and monster_fleeing is not True:
        character, monster = single_round_of_combat(character, monster)
        if character["HP"] > 0 and monster["HP"] > 0:
            if random.randint(1, 100) <= ENCOUNTER_MONSTER_PROBABILITY():
                monster_fleeing = True
            else:
                run_or_fight = get_user_command("run_mid_combat", character)
    else:
        if character["HP"] <= 0:
            return character
        elif run_or_fight == "1":
            print(f"Afraid for your life, you flee the wrath of {monster['name']}")
            chance_of_attack_while_running(character, monster)
        elif monster_fleeing is True:
            print(f'{monster["name"]} scurries away.')
        else:
            print(f'You {character_emotional_descriptions()} {monster["name"]}')
            experience_gained(character)
        return character


def chance_of_attack_while_running(character: dict, monster: dict) -> dict:
    """Determine if the character suffers any damage upon running from a fight.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition monster: monster must be a dictionary where the keys are the attributes of the player. It must have
    the following keys ("name", "HP", "damage", "damage", "attack_probability")
    :postcondition: correctly updates the character's HP if they take damage upon running from a fight
    :return: updated character dictionary after the possibility of taking damage
    """
    if random.randint(1, 100) <= ENCOUNTER_MONSTER_PROBABILITY():
        monster_damage = monster["damage"]()
        print(f"Afraid of the power of {monster['name']}, you attempt to flee")  # TEST
        character["HP"] -= monster_damage
        print(f"You've been hit! You take {monster_damage} damage.")
    else:
        print("You escape unscathed")
    return character


def single_round_of_combat(character: dict, monster: dict) -> tuple[dict, dict]:
    """Perform one round of combat.

    The high-roller will attack first, the low-roller's health is adjusted based on the damage, and then the low-roller
    attacks back, and the health of the high-roller is adjusted based on the damage.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition monster: monster must be a dictionary where the keys are the attributes of the player. It must have
    the following keys ("name", "HP", "damage", "damage", "attack_probability")
    :postcondition: correctly updates the HP of the character and monster after one round of combat
    :return: updated character and monster dictionaries returned in the form of a tuple
    """
    dice_result = {"hero": 0, "monster": 0}
    determine_the_high_roller(dice_result, character, monster)
    if dice_result["hero"] > dice_result["monster"]:
        character_deals_damage(character, monster)
        if monster["HP"] > 0:
            monster_deals_damage(character, monster)
    else:
        monster_deals_damage(character, monster)
        if character["HP"] > 0:
            character_deals_damage(character, monster)
    return character, monster


def room_descriptions() -> str:
    """Provide a random description for each grid-cell

    :return: a randomly chosen grid description
    """
    grid_descriptions = ["gryffindor common room", "room of requirement", "hufflepuff common room",
                         "professor snapes Office", "slytherin common room", "the great hall", "headmaster's office",
                         "the attic", "sybill trelawney's office", "girl's lavatory", "storeroom", "prefect's bathroom",
                         "slytherin Dungeon", "chessboard chamber", "astronomy room", "owlery", "peeve's room",
                         "flitwick's office", "hogwarts attic", "horace slughorn's office", "quidditch changing room",
                         "clock tower", "hospital wing"]
    grid_descriptions = list(map(str.title, grid_descriptions))
    return random.choice(grid_descriptions)


def make_board() -> dict:
    """Create a grid in the form of a dictionary.

    :return: a grid in the form of a dictionary where the keys are (x, y) coordinates and the values are all the boolean
    false
    """
    board = {(x, y): False for x in range(WIDTH_OF_BOARD()) for y in range(HEIGHT_OF_BOARD())}
    return board


def change_board(current_location: list, board: dict):
    """Update the board based on the player's current_location.

    :param current_location: a list
    :param board: a dictionary
    :precondition current_location: must be a list with two elements, representing the x and y coordinates of the
    player's current location on the board in that order. Current_location, when converted to a tuple, must exist
    as one of the keys in the board dictionary
    :precondition board: must be a dictionary representing the map of the game
    :postcondition: correctly changes the boolean value of the key that corresponds to the player's current location
    to True

    >>> current_location_test = [2, 2]
    >>> board_test = {(0, 0): False, (2, 2): False}
    >>> change_board(current_location_test, board_test)
    >>> board_test
    {(0, 0): False, (2, 2): True}

    >>> current_location_test = [0, 0]
    >>> board_test = {(0, 0): True, (2, 2): False}
    >>> change_board(current_location_test, board_test)
    >>> board_test
    {(0, 0): True, (2, 2): False}
    """

    board[tuple(current_location)] = True


def print_board(board: dict):
    """Print the current state of the board game.

    :param board: a dictionary
    :precondition: must be a dictionary where the keys are (x, y) coordinates of the board, and the values are True or
    False
    :postcondition: correctly prints the current state of the board where every grid-cell is represented by a "-"
    except the player's current location which is represented by a "#"
    """
    for height in range(HEIGHT_OF_BOARD()):
        for width in range(WIDTH_OF_BOARD()):
            if board[(width, height)] is False:
                print("-", end="")
            else:
                print("#", end="")
        print()


def print_character_info_log(character: dict):
    """Print player's information (HP, lvl, exp) as they progress through the game.

    :param character: a dictionary
    :precondition: must be a dictionary of the character's stats
    :postcondition: correctly prints the players' current stats
    """
    print(f" Location: {room_descriptions()}")
    print(f" Health: {character['HP']}")
    print(f" Level: {character['lvl']}")
    print(f" XP: {character['exp']}")


def generate_field(location: list, character: dict):
    """Print a two-dimensional representation of a game-board determined by character location within
       location dictionary.

       If the player is currently at a set of coordinates, a '#' will be printed. If not, a '-' will be printed.

    :param location: a list
    :param character: dictionary
    :precondition location: must be a list containing two positive integers within range of WIDTH_OF_GAME_BOARD()
                            and HEIGHT_OF_GAME_BOARD()
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
                             have the following keys
                            ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
                            "attack_probability")
    :postcondition: accurately updates surface dictionary with new boolean values of True, if dictionary key aligns
                    with character's current location
    :postcondition: accurately renders a two dimensional representation of a game board
    :return: print a two-dimensional representation of a game-board where a '#' represents current character location
            and '-' equates to an empty space
    """
    surface = make_board()
    change_board(location, surface)
    print_board(surface)
    print_character_info_log(character)


def welcome_info():
    """Print details about the game."""

    print(f"Welcome to Hogwarts!\n"
          f" _   |~  _ \n"
          f"[_]--'--[_]\n"
          f"|'|''`''|'|\n"
          f"| | /^\\ | |\n"
          f"|_|_|I|_|_|")
    time.sleep(2)
    print(f"You still can't believe it. You were chosen! You! A few weeks ago, you were just another muggle.")
    print(f"But now? You are a wizard.")
    time.sleep(4)
    print(f"Standing here in the Great Hall amongst all the other students waiting to be sorted,"
          f"you feel your heart flutter with anticipation. And then suddenly...")
    time.sleep(4)
    print(f"It is your turn.\n")
    time.sleep(4)
    print(f"You approach the old Sorting Hat with hesitation, "
          f" ignoring the snide remarks coming from the older students")
    time.sleep(4)
    print(f"The hat sits imposingly on an old stool. As it's placed on your head by Professor Mcgonagall,"
          f" you hear a gruff voice\n")


def story_info(character: dict):
    """Print details about the story of the game.

    :param character: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :postcondition: prints details about the story
    """
    print(f"Sorting Hat: Well, alright, {character['name']}. I did not think you'd choose that house."
          f"But, then again, I am just an old hat. What do I know?\n")
    time.sleep(5)
    print(f"A few days pass as you settle into your new life at Hogwarts.")
    time.sleep(5)
    print(f"One day, as you sit in the common room an owl arrives with a letter addressed to you.\n")
    print(f"You unfurl the sheaf of parchment and read:"
          f" Dear {character['name']}, I request you come visit me in the headmasters office right away. -Dumbledore\n")
    time.sleep(6)
    print(f"You waste no time and race to Dumbledore's office. You knock...")
    time.sleep(3)
    print(f"You hear a voice boom from inside the office. 'Enter!'. You open the door cautiously.\n")
    time.sleep(5)
    print(f"Dumbledore: I've been waiting for you, {character['name']}. Please sit down. I do not have much time.")
    time.sleep(5)
    print(f"Dumbledore: I was talking to the Sorting Hat over dinner, and he told me that you are "
          f"a wizard of great power.")
    time.sleep(5)
    print(f"Dumbledore: And truth be told, {character['name']}, Hogwarts is in great danger."
          f" I'm really starting to freak out! Dangerous forces have penetrated these walls. I need your help.")
    time.sleep(5)
    print(f"Dumbledore: Hogwarts requires that I publish at least three scholarly articles a year. \n"
          f"Dumbledore: Last week, as I was returning from dinner with the Sorting Hat, "
          f"I realized that my latest article had been stolen "
          f"from my office!")
    time.sleep(10)
    print(f"Dumbledore: I need you to navigate the halls of Hogwarts and search for my missing scholarly article,"
          f" or I'm totally toast. I'm already on probation...")
    time.sleep(8)
    print(f"Dumbledore: Hurry {character['name']}, but be careful. Enemies lurk around every corner!")
    time.sleep(5)
    navigation_info(character)


def navigation_info(character: dict):
    """Print the navigation commands.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: prints the navigation commands for the player
    """
    names = ["left", "right", "down", "up"]
    pairs = []
    for pair in zip(itertools.count(1), names):
        pairs.append(pair)
    print(f"Here are the navigation commands {character['name']}: {pairs}")
    time.sleep(2)
    print(f"Dumbledore:"
          f"If you wish to exit the game rather than continue on your journey, {character['name']}, just type 'quit'")
    time.sleep(3)
    print(f"Dumbledore:"
          f"If you decide to run away during a round of combat, you can type 1 or 2. Please be careful!"
          f" I hear Dolores Umbridge has taken up office in the far corner of Hogwarts. Perhaps she has my "
          f"article!")


def character_dies(character: dict):
    """Print the "game over" details of the game.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: prints details of the game when the player dies
    """
    print(f"YOU HAVE DIED.")
    print(f" _____\n"
          "/     \\ \n"
          "|() ()|\n"
          "\\  ^  /\n"
          " |||||\n"
          " |||||")
    print(f"Dumbledore: I guess the Sorting Hat was wrong about you, {character['name']}. You weren't powerful"
          f" enough to rescue my article. I needed to have that published...")
    time.sleep(3)
    print(f"Dumbledore: I've just been notified by the board that my position has been terminated. I can't believe"
          f" you've failed me.")


def mission_accomplished(character: dict):
    """Print the winning details of the game.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: prints details of the game when the player wins
    """
    print(f"CONGRATULATIONS!!!!!")
    time.sleep(2)
    print(f"  .''.                  \n"
          f" :_\\/_:                 \n"
          f".''.  :                 \n"
          f":_\\/_:'.:::.    ' *''*  \n"
          f": /\\ : :::::     *_\\/_* \n"
          f" '..'  ':::'     * /\\ * \n"
          f"   *              *..*  \n")
    time.sleep(1)
    print(f"  .''.                  \n"
          f" :_\\/_:                 \n"
          f".''.  :                 \n"
          f":_\\/_:'.:::.    ' *''*  \n"
          f": /\\ : :::::     *_\\/_* \n"
          f" '..'  ':::'     * /\\ * \n"
          f"   *              *..*  \n")
    print(f"Dumbledore: Congratulations {character['name']}, I can't believe you rescued my scholarly article!")
    time.sleep(5)
    print(f"Dumbledore: I always knew that Umbridge was out for my job. She doesn't like my transgressive ideas about "
          f"wizard relationships with talking hats.")
    time.sleep(5)
    print(f"Dumbledore: Tonight, {character['name']}, you are dining with my and the Sorting Hat! Don't worry about "
          f"class tomorrow, I'll write you a note. I am still the Headmaster, after all!.")
    time.sleep(4)
    print(f"You follow Dumbledore away from the stench of devastation, and think to yourself: I can sure get used to "
          f"this whole wizarding thing.")


def encounter_boss(character: dict) -> dict:
    """Determine the outcome of the final boss-battle.

    :param character: a dictionary
    :precondition: character must be a dictionary where the keys are the attributes of the player. It must have the
    following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate", "attack_probability")
    :postcondition: correctly determines if the player wins or loses the final battle
    :return: the final outcome of the game
    """
    monster = {"name": "Dolores Umbridge", "HP": 35, "damage": damage_generator(10, 15), "attack_probability": 5}

    print(f"Who's that huddled in the corner? What's that awful, perfumey smell? It can't be...")
    time.sleep(2)
    print(f"Dolores Umbridge: Ahhhhhh, we finally meet, {character['name']}, teheheh")
    time.sleep(2)
    print(f"Dolores Umbridge: I assume you are here to rescue Dumbledore's most recent article?")
    time.sleep(2)
    print(f"Dolores Umbridge: I'm afraid the old fool has lost his mind.")
    time.sleep(2)
    print(f"Dolores Umbridge: It's pure drivel, the inane chatter of "
          f"an old man obsessed with that blasted Sorting Hat...")
    time.sleep(2)
    print(f"Dolores Umbrdige: I admire your commitment, {character['name']},"
          f"I really do. But I'm afraid you must now die!'")
    time.sleep(4)
    print(f"BOSS FIGHT:")

    while character["HP"] > 0 and monster["HP"] > 0:
        character, monster = boss_round_of_combat(character, monster)
    else:
        if character["HP"] <= 0:
            return character
        else:
            print(f"You've killed Dolores Umbridge! Hogwarts is saved! \n"
                  f"Dumbledore can meet his yearly publishing quota!")


def boss_round_of_combat(character: dict, monster: dict) -> tuple[dict, dict]:
    """Update the HP of the character and the boss-monster during their combat.

    :param character: a dictionary
    :param monster: a dictionary
    :precondition character: character must be a dictionary where the keys are the attributes of the player. It must
    have the following keys ("name", "HP", "max_HP", "class", "lvl", "exp", "damage", "recovery_rate",
    "attack_probability")
    :precondition monster: monster must be a dictionary where the keys are the attributes of the player. It must have
    the following keys ("name", "HP", "damage", "damage", "attack_probability")
    :postcondition: correctly updates the HP of character and monster
    :return: updated HP of the character and the boss-monster
    """
    monster_deals_damage(character, monster)
    time.sleep(2)
    if character["HP"] > 0:
        character_deals_damage(character, monster)
    time.sleep(2)
    return character, monster


def game():
    """Print the result of the outcome of the game."""

    welcome_info()
    character = make_character()
    story_info(character)
    command = ""
    achieved_goal = False
    current_location = STARTING_LOCATION()
    while command != "quit" and character["HP"] > 0 and achieved_goal is False:
        valid_move = validate_command(get_user_command("direction", character), current_location)
        if valid_move == "quit":
            command = "quit"
        elif valid_move in ["1", "2", "3", "4"]:
            current_location = make_the_move(valid_move, current_location)
            generate_field(current_location, character)
            if current_location != FINAL_BOSS_LOCATION():
                outcomes_of_moving(character)
            else:
                encounter_boss(character)
                achieved_goal = True
        else:
            print(f"{character['name']} can't go that way!")
    else:
        if command == "quit":
            print(f"Dumbledore: {character['name']}, I never thought you'd quit on me like this...")
        elif character["HP"] <= 0:
            character_dies(character)
        else:
            mission_accomplished(character)


def main():
    """Drives the program"""
    game()


if __name__ == "__main__":
    main()
