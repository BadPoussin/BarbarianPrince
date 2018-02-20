from random import randint


def next_tour(tour):
    nextTour = int(tour) + 1
    print()
    print("Vous venez de passer au tour n°" + str(nextTour))
    return nextTour


def display_carac(combat_skill, endurance, wealth_code, wit, dice):
    if dice != "":
        print('Lancer de dé : ' + dice)
        print()
    print('Voici vos caractéristiques : ')
    print('\t - Force : ' + str(combat_skill))
    print('\t - Endurance : ' + str(endurance))
    print('\t - Richesse : ' + str(wealth_code))
    print('\t - Multiplicateur : ' + str(wit))
    return ""


def roll_dice():
    return randint(1, 6)
