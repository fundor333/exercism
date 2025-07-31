"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


def yacht(dice):
    rif = dice[0]
    for e in dice:
        if e != rif:
            return 0
    return 50


def ones(dice):
    return dice.count(1)


def twos(dice):
    return dice.count(2) * 2


def threes(dice):
    return dice.count(3) * 3


def fours(dice):
    return dice.count(4) * 4


def fives(dice):
    return dice.count(5) * 5


def sixs(dice):
    return dice.count(6) * 6


def full_house(dice):
    temp_dice = set(dice)
    if len(temp_dice) == 2 and dice.count(dice[0]) != 1:
        return sum(dice)
    return 0


def four_or_a_kind(dice):
    temp_dice = set(dice)
    if len(temp_dice) == 2 or len(temp_dice) == 1:
        if dice.count(dice[0]) == 4:
            return dice[0] * 4
        elif dice.count(dice[0]) == 1:
            return dice[1] * 4
        elif dice.count(dice[0]) == 5:
            return dice[0] * 4
    return 0


def little_straight(dice):
    dice.sort()
    if [1, 2, 3, 4, 5] == dice:
        return 30
    return 0


def big_straight(dice):
    dice.sort()
    if [2, 3, 4, 5, 6] == dice:
        return 30
    return 0


# Score categories.
# Change the values as you see fit.
YACHT = yacht
ONES = ones
TWOS = twos
THREES = threes
FOURS = fours
FIVES = fives
SIXES = sixs
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_or_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = sum


def score(dice, category):
    return category(dice)
