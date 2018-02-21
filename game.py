from random import randint


def start_position(number):
    positionDepart = 0
    xDepart = 0

    if number == 1:
        positionDepart = 0
        positionCote = [1, 20]
        xDepart = 65
    else:
        if number == 2:
            positionDepart = 6
            xDepart = 239
        elif number == 3:
            positionDepart = 8
            xDepart = 298
        elif number == 4:
            positionDepart = 12
            xDepart = 415
        elif number == 5:
            positionDepart = 14
            xDepart = 474
        elif number == 6:
            positionDepart = 18
            xDepart = 590
        positionCote = [positionDepart - 1, positionDepart + 1, positionDepart + 20]

    return positionDepart, positionCote, xDepart


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


def win_game(gold):
    return gold >= 500
