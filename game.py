from random import randint
from grid import *
from events import *

preEvent = ['Elfe', 'Nain', 'Semi-Homme']
noEvent = ['Maison de magicien', 'Petite tempête', 'Tombe', 'Orcs', 'Gobelins', 'Cache gobeline', 'Mésaventure',
           'Pluie', 'Chute de pierre', 'Ville cachée', 'Passage étroit', 'Passe haut', 'Risques', 'Mines des nains',
           'Mines abandonnées', 'Temple secret', 'Ruines']


def start_position(number, listColored):
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

    listColored.append(positionDepart)

    for position in positionCote:
        listColored.append(position)

    return positionDepart, positionCote, xDepart, listColored


def road_taken(old, new):
    roadTaken = False

    if old > new:
        if (new, old) in routes:
            roadTaken = True
    else:
        if (old, new) in routes:
            roadTaken = True

    return roadTaken


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


def launch_event(dice, hexCliqued):
    dice1 = int(dice)
    dice2 = roll_dice()
    terrain = str(listTerrain[typeTerrain[hexCliqued]])
    nameEvent = ""

    print("Vous arrivez dans une zone de type " + terrain + ".")
    print("Vos dés ont pour résultat : " + str(dice1) + " et " + str(dice2) + ".")

    if terrain == "montagnes":
        for event in event_mountain:
            if event[0] == (dice1, dice2):
                nameEvent = event[1]

    print("L'évènement déclenché est le suivant : " + nameEvent + ".")

    return

def win_game(gold):
    return gold >= 500


def treat_events():
    name_event = "magicien"
    eventToTreat = ""
    for event in events:
        if event[0] == name_event:
            eventToTreat = event[0]
            break
    if eventToTreat[1]:
        if eventToTreat[1] == "redirect":
            dice = roll_dice()
            if dice == 1:
            elif dice == 2:
            elif dice == 3:
            elif dice == 4:
            elif dice == 5:
            elif dice == 6:
        elif eventToTreat[1] == "pre":
        elif eventToTreat[1] == "choice":