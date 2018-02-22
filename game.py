from random import randint
from grid import *
from events import *

preEvent = ['Elfe', 'Nain', 'Semi-Homme']
noEvent = ['Maison de magicien', 'Petite tempête', 'Tombe', 'Orcs', 'Gobelins', 'Cache gobeline', 'Mésaventure',
           'Pluie', 'Chute de pierre', 'Ville cachée', 'Passage étroit', 'Passe haut', 'Risques', 'Mines des nains',
           'Mines abandonnées', 'Temple secret', 'Ruines']
equipe = []

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
    print("Vous venez de passer au tour n°" + str(nextTour) + "\n")
    return nextTour


def display_carac(life, combat_skill, endurance, wealth_code, wit, dice):
    if dice != "":
        print('Lancer de dé : ' + dice+".")
        print()
    print('Voici vos caractéristiques : ')
    print('\t - Vie : ' + str(life))
    print('\t - Force : ' + str(combat_skill))
    print('\t - Endurance : ' + str(endurance))
    print('\t - Richesse : ' + str(wealth_code))
    print('\t - Multiplicateur : ' + str(wit))
    return ""


def roll_dice(max_jet = 6):
    return randint(1, max_jet)

def launch_event(dice, hexCliqued, life, endurance, force, richesse):
    dice1 = int(dice)
    dice2 = roll_dice()
    terrain = str(listTerrain[typeTerrain[hexCliqued]])
    nameEvent = ""

    print("\nVous arrivez dans une zone de type " + terrain + ".")
    print("Vos dés ont pour résultat : " + str(dice1) + " et " + str(dice2) + ".")

    '''if terrain == "montagnes":
        for event in event_mountain:
            if event[0] == (dice1, dice2):
                nameEvent = event[1]'''
    for event in event_mountain:
        if event[0] == (dice1, dice2):
            nameEvent = event[1]

    print("L'évènement déclenché est le suivant : " + nameEvent + ".")

    #treat_events(nameEvent, life, endurance, force, richesse)
    life, endurance, force, richesse = treat_events(nameEvent, life, endurance, force, richesse)

    return life, endurance, force, richesse

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
                print("Oh ! Mince ! Redirection impossible...")
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
                if len(eventEnCours.split(':')) > 1:
                    eventEnCoursSplit1 = eventEnCours.split(':')
                    val = 0
                    friends = 0
                    newForce = 0
                    newEndurance = 0
                    newRichesse = 0
                    for eventEnCoursSplit2 in eventEnCoursSplit1:
                        if eventEnCoursSplit2 == 'friends':
                            friends = int(val)
                        elif eventEnCoursSplit2 == 'force':
                            newForce += int(val)
                        elif eventEnCoursSplit2 == 'endurance':
                            newEndurance += int(val)
                        elif eventEnCoursSplit2 == 'richesse':
                            newRichesse += int(val)
                        else:
                            val = eventEnCoursSplit2
                    if friends != 0:
                        print("L'adversaire possède "+str(friends)+" ami(s) :\n\t- Force : "+str(newForce)+"\n\t- Endurance : "+str(newEndurance)+"\n\t- Richesse : "+str(newRichesse))
                    else:
                        force = int(force) + newForce
                        endurance = int(endurance) + newEndurance
                        richesse = int(richesse) + newRichesse
                        print("Vos compétences augmentent :\n\t- Force +" + str(newForce) + "\n\t- Endurance +" + str(newEndurance) + "\n\t- Richesse +" + str(newRichesse))
                else:
                    print(eventEnCours)
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
                if choice == "Parler":
                    val = 0
                    type = ""
                    print("Vous avez choisi d'argumenter.")
                    for perso in perso_carac:
                        if perso[0] == eventToTreat[0]:
                            val = int(int(perso[1]) / 2)
                            type = perso[2]
                            break
                    if type == "richesse":
                        newRichesse = val
                        print("Votre adversaire vous donne " + str(val) + " pièces d'or.")
                        richesse = int(richesse) + newRichesse
                    elif type == "vie":
                        newLife = val
                        print("Votre adversaire s'énerve et vous tape. Vous perdez " + str(val) + " points de vie.")
                        life = int(life) + newLife
                        print("Votre vie est maintenant de " + str(life) + " points de vie.")
                    else:
                        print("La discussion est terminée.")
                elif choice == "S\'évader":
                    print("Vous avez choisi de vous évader.")
                elif choice == "Se battre":
                    val = 0
                    type = ""
                    print("Vous avez choisi de vous battre.")
                    for perso in perso_carac:
                        if perso[0] == eventToTreat[0]:
                            val = int(perso[1])
                            type = perso[2]
                            break
                    if type == "richesse":
                        newRichesse = val
                        print("Vous gagnez l'argent de votre adversaire : "+str(val)+" pièces d'or.")
                        richesse = int(richesse) + newRichesse
                    elif type == "vie":
                        newLife = val
                        print("Vous perdez le combat, vous perdez " + str(val) + " points de vie.")
                        life = int(life) + newLife
                        print("Votre vie est maintenant de " + str(life) + " points de vie.")
                    else:
                        print("Le combat est terminé.")
                elif choice == "Rechercher":
                    val = 0
                    type = ""
                    print("Vous avez choisi de faire des recherches.")
                    for perso in perso_carac:
                        if perso[0] == eventToTreat[0]:
                            val = int(perso[1])
                            type = perso[2]
                            break
                    if type == "nourriture":
                        newLife = val
                        print("Vous vous nourrissez, vous gagnez " + str(val) + " points de vie.")
                        life = int(life) + newLife
                        print("Votre vie est maintenant de " + str(life) + " points de vie.")
                    elif type == "richesse":
                        newRichesse = val
                        print("Vous gagnez l'argent de votre adversaire : "+str(val)+" pièces d'or.")
                        richesse = int(richesse) + newRichesse
                    else:
                        print("Vous ne trouvez rien.")
                elif choice == "Se reposer":
                    print("Vous avez choisi de vous reposer. Vous allez faire une bonne sieste pendant 1 tour !")
                elif choice == "Se nourrir":
                    print("Vous avez choisi de vous nourrir car vous avez très faim ! Malheureusement, il n'y a pas de nourriture...")
            elif eventToTreat[numberEvent] == "condition":
                print("Etat actuel : "+eventToTreat[numberEvent+1][0])
                print("Resultat : "+eventToTreat[numberEvent+1][1])
                if eventToTreat[numberEvent+1][0] == "Avoir une équipe":
                    equipe.clear()
            elif eventToTreat[numberEvent] == "boucle":
                condition = True
                while condition:
                    dice = roll_dice()
                    if dice < 4:
                        print("Problème : " + eventToTreat[numberEvent + 1][0] + " !")
                        if eventToTreat[numberEvent+1][1].split(':')[1] == "vie":
                            newLife = int(eventToTreat[numberEvent+1][1].split(':')[0])
                            life = int(life) + newLife
                            print("Resultat : Vous perdez "+str(newLife)+" points de vie. Il vous reste "+str(life)+" points de vie.")
                    else:
                        condition = False
                        print("Problème terminé.")
            elif eventToTreat[numberEvent] == "approche":
                dice = roll_dice(2)
                if dice == 1:
                    print(eventToTreat[numberEvent+1][0])
                else:
                    eventEnCoursSplit1 = eventToTreat[numberEvent+1][0].split(':')
                    newLife = 0
                    for eventEnCoursSplit2 in eventEnCoursSplit1:
                        if eventEnCoursSplit2 == "vie":
                            newLife = int(val)
                        elif eventEnCoursSplit2 == "destroy":
                            equipe.clear()
                        else:
                            val = eventEnCoursSplit2
                    life = int(life) + int(newLife)
                    print("Votre équipe est détruite, vous perdez "+str(newLife)+" points de vie.\nIl vous reste "+str(life)+" points de vie.")
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

def is_lost(typeTerrain):
    lostTable = [('plaine', 8), ('fermes', 10), ('collines', 8), ('forêt', 8), ('marais', 5), ('montagnes', 7),
                 ('desert', 6)]
    minToLost = 0

    for object in lostTable:
        if object[0] == typeTerrain:
            minToLost = object[1]

    dices = roll_dice(12)

    if dices > minToLost:
        print(
            "Vous lancez les dés. Votre résultat total est " + str(dices) + ". Etant dans un terrain de type \"" + str(typeTerrain) + "\", vous vous êtes perdus, vous perdez votre tour.")
        return True
    else:
        print(
            "Vous lancez les dés. Votre résultat total est " + str(dices) + ". Etant dans un terrain de type \"" + str(typeTerrain) + "\", vous pouvez continuer votre chemin.")
        return False