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


def display_carac(life, combat_skill, endurance, wealth_code, wit, dice):
    if dice != "":
        print('Lancer de dé : ' + dice)
        print()
    print('Voici vos caractéristiques : ')
    print('\t - Vie : ' + str(life))
    print('\t - Force : ' + str(combat_skill))
    print('\t - Endurance : ' + str(endurance))
    print('\t - Richesse : ' + str(wealth_code))
    print('\t - Multiplicateur : ' + str(wit))
    return ""


def roll_dice():
    return randint(1, 6)

def launch_event(dice, hexCliqued, life, endurance, force, richesse):
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

    treat_events(nameEvent, life, endurance, force, richesse)

    return

def win_game(gold):
    return gold >= 500


def treat_events(name_event, life, endurance, force, richesse):
    eventToTreat = ""
    for event in events:
        if event[0] == name_event:
            eventToTreat = event
            break
    nextEvent = True
    numberEvent = 1
    while nextEvent:
        nextEvent = False
        try:
            eventToTreat[numberEvent]
        except NameError:
            nextEvent = False
        else:
            if eventToTreat[numberEvent] == "redirect":
                dice = roll_dice()
                if dice == 1:
                    print("Vous allez être redirigé vers l'évènement suivant : "+eventToTreat[numberEvent+1][0])
                    #treat_events(eventToTreat[numberEvent+1][0])
                elif dice == 2:
                    print("Vous allez être redirigé vers l'évènement suivant : " + eventToTreat[numberEvent + 1][1])
                    #treat_events(eventToTreat[numberEvent+1][1])
                elif dice == 3:
                    print("Vous allez être redirigé vers l'évènement suivant : " + eventToTreat[numberEvent + 1][2])
                    #treat_events(eventToTreat[numberEvent+1][2])
                elif dice == 4:
                    print("Vous allez être redirigé vers l'évènement suivant : " + eventToTreat[numberEvent + 1][3])
                    #treat_events(eventToTreat[numberEvent+1][3])
                elif dice == 5:
                    print("Vous allez être redirigé vers l'évènement suivant : " + eventToTreat[numberEvent + 1][4])
                    #treat_events(eventToTreat[numberEvent+1][4])
                elif dice == 6:
                    print("Vous allez être redirigé vers l'évènement suivant : " + eventToTreat[numberEvent + 1][5])
                    #treat_events(eventToTreat[numberEvent+1][5])
            elif eventToTreat[numberEvent] == "pre":
                dice = roll_dice()
                eventEnCours = ""
                if dice == 1:
                    eventEnCours = eventToTreat[numberEvent+1][0]
                elif dice == 2:
                    eventEnCours = eventToTreat[numberEvent+1][1]
                elif dice == 3:
                    eventEnCours = eventToTreat[numberEvent+1][2]
                elif dice == 4:
                    eventEnCours = eventToTreat[numberEvent+1][3]
                elif dice == 5:
                    eventEnCours = eventToTreat[numberEvent+1][4]
                elif dice == 6:
                    eventEnCours = eventToTreat[numberEvent+1][5]
                print("Attention : " + eventEnCours)
                if len(eventEnCours.split(':')) > 1:
                    eventEnCoursSplit1 = eventEnCours.split(':')
                    val = 0
                    friends = 0
                    for eventEnCoursSplit2 in eventEnCoursSplit1:
                        if eventEnCoursSplit2 == 'friends':
                            friends = val
                        elif eventEnCoursSplit2 == 'force':
                            force += val
                        elif eventEnCoursSplit2 == 'endurance':
                            endurance += val
                        elif eventEnCoursSplit2 == 'richesse':
                            richesse += val
                        else:
                            val = eventEnCoursSplit2


            elif eventToTreat[numberEvent] == "choice":
                print("Vous avez "+str(len(eventToTreat[numberEvent+1]))+" possibilités :")
                for possibility in eventToTreat[numberEvent+1]:
                    print("\t- "+possibility)
                verif = False
                while not verif:
                    choice = input("Que choississez vous ?\n")
                    for possibility in eventToTreat[numberEvent + 1]:
                        if choice == possibility:
                            verif = True
                    if not verif:
                        print("Veuillez renseigner un des choix proposés ! ")
                dice = roll_dice()
                if choice == "talk":
                    print("Vous avez choisi d'argumenter.")
                    '''if dices < 4:
                        dices = roll_dice()
                        print(check_conversation(dices))
                    elif dice == 4:

                    elif dice == 5:
                    elif dice == 6:'''
                elif choice == "evade":
                    print("Vous avez choisi de vous évader.")
                elif choice == "fight":
                    print("Vous avez choisi de vous battre.")
                elif choice == "search":
                    print("Vous avez choisi de rechercher.")
                elif choice == "rest":
                    print("Vous avez choisi de vous reposer.")
                elif choice == "food":
                    print("Vous avez choisi de vous nourrir.")
            elif eventToTreat[numberEvent] == "condition":
                print("Etat actuel : "+eventToTreat[numberEvent+1][0])
                print("Resultat : "+eventToTreat[numberEvent+1][1])
            elif eventToTreat[numberEvent] == "boucle":
                condition = True
                while condition:
                    dice = roll_dice()
                    if dice < 4:
                        print("Etat : "+eventToTreat[numberEvent+1][0])
                        print("Resultat : "+eventToTreat[numberEvent+1][1])
                    else:
                        condition = False
                        print("Terminé.")
            elif eventToTreat[numberEvent] == "approche":
                condition = True

        '''try:
            eventToTreat[numberEvent+2]
        except NameError:
            nextEvent = False
        else:
            numberEvent += 2
            nextEvent = True'''
        if len(eventToTreat) > numberEvent+2:
            numberEvent += 2
            nextEvent = True
    return life, endurance, force, richesse

def check_conversation(number):
    response = ""
    if number == 1:
        response = "Un assassin vous surprend et vous tue !"
    elif number == 2:
        response = "La personne avec qui vous argumentez vous attaque !"
    elif number == 3 or number == 4:
        response == "La personne avec qui vous argumentez décide de rejoindre votre équipe."
    else:
        response = "La personne avec qui vous argumentez vous laisse partir."
    return response