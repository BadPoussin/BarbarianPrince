events = [("Epeiste", "choice", ("talk", "evade", "fight")),
          ("Amazones", "choice", ("talk", "evade", "fight")),
          ("Nain", "pre", ("seul", "seul", "seul", "avec un ami (force 5, endurance 6, richesse 12)",
                           "avec trois amis (force 5, endurance 6, richesse 12)",
                           "avec cinq amis (force 5, endurance 6, richesse 12)"), "choice", ("talk", "evade", "fight")),
          ("Elfe", "pre",
           ("Rien ne se passe.", "Il est le leader d'une bande d'elfes.", "C'est un magicien avec une bombe à gaz.",
            "Il possède un remède au poison et est accompagné par un assistant (force 3, endurance 3, richesse 2)",
            "C'est un prêtre d'un culte de la forêt qui possède une potion de soin",
            "Il est avec un ami (force 4, endurance 4, richesse 7)"),
           "choice", ("talk", "evade", "fight")),
          ("Semi-Homme", "pre",
           ("Conversation banale. C'est une perte de temps.", "Le semi-homme vous indique la position de son village.",
            "Rien.", "Rien.", "Rien.", "Rien.")),
          ("Rencontre magicien", "approche", ("Le magicien vous rejoint dans votre quête",
                                              "Le magicien vous attaque, détruit votre groupe et vous retire 5 points de vie.")),
          ("Magicien", "choice", ("talk", "evade", "fight")),
          ("Tombe", "redirect", ("Mommie", "Piller la tombe", "Fantômes", "Colère des guerriers", "Spectre de la tombe",
                                 "Dangers et trésors")),
          ("Gobelins", "choice", ("evade", "fight")),
          ("Cache gobeline", "choice", ("evade", "fight")),
          ("Orcs", "choice", ("evade", "fight")),
          ("Nains", "choice", ("talk", "evade", "fight")),
          ("Ruines", "choice", ("search", "evade")),
          ("Maison de magicien", "redirect", (
              "Magicien", "Magicien", "Attaque de Magicien", "Rencontre magicien", "Tour de magicien",
              "Tour de magicien")),
          ("Mésaventure", "condition", ("Avoir cheval", "Perte du cheval")),
          ("Pluie", "boucle", ("pluie", "-1 vie")),
          ("Passe haut", "pre", (
              "Rien ne se passe", "Rien ne se passe", "Rien ne se passe", "Rien ne se passe", "Rien ne se passe",
              "Rien ne se passe", "Rien ne se passe", "Tout le monde perd 1 de vie",
              "Tout le monde perd 2 de vie et les montures meurent",
              "Tout le monde perd 3 de vie et les montures meurent",
              "Tout le monde perd 4 de vie et les montures meurent",
              "Tout le monde perd 4 de vie et les montures meurent",)),
          ("Chute de pierre", "pre", (
              "Les pierres vous passent à côté", "Les pierres vous passent à côté", "Les pierres vous passent à côté",
              "Les pierres vous passent à côté", "Le héros perd 1 point de vie", "Le héros perd 6 points de vie")),
          ("Rocher", "choice", ("evade", "fight")),
          ("Griffon", "choice", ("talk", "evade", "fight")),
          ("Harpie", "choice", ("talk", "evade", "fight")),
          ("Géant", "choice", ("talk", "evade", "fight")),
          ("Risques", "condition", ("Avoir cheval", "Perte du cheval")),
          ("Mines des nains", "choix", ("rest", "food", "evade")),
          ("Temple secret", "choix", ("rest", "food", "evade")),
          ("Ville cachée", "choix", ("rest", "food", "evade"))
          ]

event_mountain = [((1, 1), 'Epeiste'), ((1, 2), 'Rocher'), ((1, 3), 'Tombe'), ((1, 4), 'Mésaventure'),
                  ((1, 5), 'Passage étroit'),
                  ((1, 6), 'Géant'),
                  ((2, 1), 'Mercenaires'), ((2, 2), 'Griffon'), ((2, 3), 'Tombe'), ((2, 4), 'Mésaventure'),
                  ((2, 5), 'Passage étroit'),
                  ((2, 6), 'Gobelins'),
                  ((3, 1), 'Amazones'), ((3, 2), 'Magicien'), ((3, 3), 'Nains'), ((3, 4), 'Pluie'),
                  ((3, 5), 'Passe haut'),
                  ((3, 6), 'Mines des nains'),
                  ((4, 1), 'Nain'), ((4, 2), 'Maison de magicien'), ((4, 3), 'Orcs'), ((4, 4), 'Pluie'),
                  ((4, 5), 'Passe haut'),
                  ((4, 6), 'Mines abandonnées'),
                  ((5, 1), 'Elfe'), ((5, 2), 'Harpie'), ((5, 3), 'Gobelins'), ((5, 4), 'Chute de pierre'),
                  ((5, 5), 'Passe haut'),
                  ((5, 6), 'Temple secret'),
                  ((6, 1), 'Semi-Homme'), ((6, 2), 'Petite tempête'), ((6, 3), 'Cache gobeline'),
                  ((6, 4), 'Ville cachée'), ((6, 5), 'Risques'), ((6, 6), 'Ruines')]

event_road = [((1, 1), 'Prêtre'), ((1, 2), 'Police locale'), ((1, 3), 'Mercenaires'), ((1, 4), 'Elfe'),
              ((1, 5), 'Menestrel itinérant'), ((1, 6), 'Mésaventure'),
              ((2, 1), 'Moines'), ((2, 2), 'Bandits'), ((2, 3), 'Mercenaires'), ((2, 4), 'Elfe'),
              ((2, 5), 'Fugitif'), ((2, 6), 'Mésaventure'),
              ((3, 1), 'Magicien'), ((3, 2), 'Bandits'), ((3, 3), 'Amazones'), ((3, 4), 'Troll'),
              ((3, 5), 'Patrouille montée'), ((3, 6), 'Pluie'),
              ((4, 1), 'Sorcière'), ((4, 2), 'Bandits'), ((4, 3), 'Nains'), ((4, 4), 'Rencontre avec un seigneur'),
              ((4, 5), 'Marchand'), ((4, 6), 'Pluie'),
              ((5, 1), 'Ferme'), ((5, 2), 'Epeiste'), ((5, 3), 'Nain'), ((5, 4), 'Marchand'),
              ((5, 5), 'Caravane de marchand'),
              ((5, 6), 'Marchand'),
              ((6, 1), 'Ferme'), ((6, 2), 'Epeiste'), ((6, 3), 'Semi-Homme'),
              ((6, 4), 'Marchand'), ((6, 5), 'Caravane de marchand'),
              ((6, 6), 'Caravane de marchand')]

event_river = [((1, 1), 'Epeiste'), ((1, 2), 'Equipage du radeau'), ((1, 3), 'Chevalier du pont'),
               ((1, 4), 'Crocodiles'),
               ((1, 5), 'Attaque de sanglier'), ((1, 6), 'Equipage du radeau'),
               ((2, 1), 'Mercenaires'), ((2, 2), 'Equipage du radeau'), ((2, 3), 'Chevalier du pont'),
               ((2, 4), 'Crocodiles'), ((2, 5), 'Chat de chasse'), ((2, 6), 'Equipage du radeau'),
               ((3, 1), 'Amazones'), ((3, 2), 'Equipage du radeau'), ((3, 3), 'Troll'), ((3, 4), 'Serpent'),
               ((3, 5), 'Cheveaux sauvages'), ((3, 6), 'Equipage du radeau'),
               ((4, 1), 'Nain'), ((4, 2), 'Ferme'), ((4, 3), 'Troll'), ((4, 4), 'Serpent'),
               ((4, 5), 'Radeau'), ((4, 6), 'Radeau qui chavire'),
               ((5, 1), 'Elfe'), ((5, 2), 'Bandits'), ((5, 3), 'Gobelins'), ((5, 4), 'Loups'),
               ((5, 5), 'Radeau'), ((5, 6), 'Radeau pris dans le courant'),
               ((6, 1), 'Semi-Homme'), ((6, 2), 'Araignées'), ((6, 3), 'Orcs'),
               ((6, 4), 'Ours'), ((6, 5), 'Radeau'),
               ((6, 6), 'Radeau en eau agitée')]

event_country = [((1, 1), ''), ((1, 2), ''), ((1, 3), ''), ((1, 4), ''),
                 ((1, 5), ''),
                 ((1, 6), ''),
                 ((2, 1), ''), ((2, 2), ''), ((2, 3), ''), ((2, 4), ''),
                 ((2, 5), ''),
                 ((2, 6), ''),
                 ((3, 1), ''), ((3, 2), ''), ((3, 3), ''), ((3, 4), ''),
                 ((3, 5), ''),
                 ((3, 6), ''),
                 ((4, 1), ''), ((4, 2), ''), ((4, 3), ''), ((4, 4), ''),
                 ((4, 5), ''),
                 ((4, 6), ''),
                 ((5, 1), ''), ((5, 2), ''), ((5, 3), ''), ((5, 4), ''),
                 ((5, 5), ''),
                 ((5, 6), ''),
                 ((6, 1), ''), ((6, 2), ''), ((6, 3), ''),
                 ((6, 4), ''), ((6, 5), ''),
                 ((6, 6), '')]

event_desert = [((1, 1), ''), ((1, 2), ''), ((1, 3), ''), ((1, 4), ''),
                ((1, 5), ''),
                ((1, 6), ''),
                ((2, 1), ''), ((2, 2), ''), ((2, 3), ''), ((2, 4), ''),
                ((2, 5), ''),
                ((2, 6), ''),
                ((3, 1), ''), ((3, 2), ''), ((3, 3), ''), ((3, 4), ''),
                ((3, 5), ''),
                ((3, 6), ''),
                ((4, 1), ''), ((4, 2), ''), ((4, 3), ''), ((4, 4), ''),
                ((4, 5), ''),
                ((4, 6), ''),
                ((5, 1), ''), ((5, 2), ''), ((5, 3), ''), ((5, 4), ''),
                ((5, 5), ''),
                ((5, 6), ''),
                ((6, 1), ''), ((6, 2), ''), ((6, 3), ''),
                ((6, 4), ''), ((6, 5), ''),
                ((6, 6), '')]

event_forest = [((1, 1), ''), ((1, 2), ''), ((1, 3), ''), ((1, 4), ''),
                ((1, 5), ''),
                ((1, 6), ''),
                ((2, 1), ''), ((2, 2), ''), ((2, 3), ''), ((2, 4), ''),
                ((2, 5), ''),
                ((2, 6), ''),
                ((3, 1), ''), ((3, 2), ''), ((3, 3), ''), ((3, 4), ''),
                ((3, 5), ''),
                ((3, 6), ''),
                ((4, 1), ''), ((4, 2), ''), ((4, 3), ''), ((4, 4), ''),
                ((4, 5), ''),
                ((4, 6), ''),
                ((5, 1), ''), ((5, 2), ''), ((5, 3), ''), ((5, 4), ''),
                ((5, 5), ''),
                ((5, 6), ''),
                ((6, 1), ''), ((6, 2), ''), ((6, 3), ''),
                ((6, 4), ''), ((6, 5), ''),
                ((6, 6), '')]

event_farm = [((1, 1), ''), ((1, 2), ''), ((1, 3), ''), ((1, 4), ''),
              ((1, 5), ''),
              ((1, 6), ''),
              ((2, 1), ''), ((2, 2), ''), ((2, 3), ''), ((2, 4), ''),
              ((2, 5), ''),
              ((2, 6), ''),
              ((3, 1), ''), ((3, 2), ''), ((3, 3), ''), ((3, 4), ''),
              ((3, 5), ''),
              ((3, 6), ''),
              ((4, 1), ''), ((4, 2), ''), ((4, 3), ''), ((4, 4), ''),
              ((4, 5), ''),
              ((4, 6), ''),
              ((5, 1), ''), ((5, 2), ''), ((5, 3), ''), ((5, 4), ''),
              ((5, 5), ''),
              ((5, 6), ''),
              ((6, 1), ''), ((6, 2), ''), ((6, 3), ''),
              ((6, 4), ''), ((6, 5), ''),
              ((6, 6), '')]

event_hills = [((1, 1), ''), ((1, 2), ''), ((1, 3), ''), ((1, 4), ''),
               ((1, 5), ''),
               ((1, 6), ''),
               ((2, 1), ''), ((2, 2), ''), ((2, 3), ''), ((2, 4), ''),
               ((2, 5), ''),
               ((2, 6), ''),
               ((3, 1), ''), ((3, 2), ''), ((3, 3), ''), ((3, 4), ''),
               ((3, 5), ''),
               ((3, 6), ''),
               ((4, 1), ''), ((4, 2), ''), ((4, 3), ''), ((4, 4), ''),
               ((4, 5), ''),
               ((4, 6), ''),
               ((5, 1), ''), ((5, 2), ''), ((5, 3), ''), ((5, 4), ''),
               ((5, 5), ''),
               ((5, 6), ''),
               ((6, 1), ''), ((6, 2), ''), ((6, 3), ''),
               ((6, 4), ''), ((6, 5), ''),
               ((6, 6), '')]

event_swamp = [((1, 1), ''), ((1, 2), ''), ((1, 3), ''), ((1, 4), ''),
               ((1, 5), ''),
               ((1, 6), ''),
               ((2, 1), ''), ((2, 2), ''), ((2, 3), ''), ((2, 4), ''),
               ((2, 5), ''),
               ((2, 6), ''),
               ((3, 1), ''), ((3, 2), ''), ((3, 3), ''), ((3, 4), ''),
               ((3, 5), ''),
               ((3, 6), ''),
               ((4, 1), ''), ((4, 2), ''), ((4, 3), ''), ((4, 4), ''),
               ((4, 5), ''),
               ((4, 6), ''),
               ((5, 1), ''), ((5, 2), ''), ((5, 3), ''), ((5, 4), ''),
               ((5, 5), ''),
               ((5, 6), ''),
               ((6, 1), ''), ((6, 2), ''), ((6, 3), ''),
               ((6, 4), ''), ((6, 5), ''),
               ((6, 6), '')]
