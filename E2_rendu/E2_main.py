import fonctions
import os
import sys

# boucle main avec l'interface utilisateur :
# en commentaire pour les tests
while 1:
    # exécuté une seule fois pour la création des fichiers et l'écriture des premières phrases
    # for files in os.listdir('./tableau_test'):
    #     sys.stdout = open(".\\execution_textes\\" + files, "w")
    print('\nVoici les fichiers texte disponible\n')
    for file in os.listdir('./tableau_test'):
        # exécuté 1 fois pour écrire les noms des fichiers dedans (car il faut les tapper dans la console)
        # fic = open(".\\execution_textes\\"+file, "a")
        # fic.write(file)
        print(file, end=' | ')
    print('\n\nVeuillez en choisir un (entrez le nom complet du fichier avec l\'extention) :')
    print('Si vous voulez quitter, tappez "quit" ou "exit"')
    fichier = input()
    if fichier == 'quit' or fichier == 'exit':
        break
    path = ".\\tableau_test\\"+fichier
    # uniquement pour écrire dans les fichiers textes d'exécution
    # sys.stdout = open(".\\execution_textes\\" + fichier, "a")


    # on stock les valeurs du .txt dans un tableau 2D pour y accéder facilement
    try:
        tab = fonctions.readTab(path)
    except FileNotFoundError:
        print("Fichier non trouvé")
        continue

    # on ajoute les sommets alpha et oméga qui sont au tout début et à la toute fin pour avoir un seul pt de départ et un seul pt d'arrivée
    tab = fonctions.ajoutSommetsFictifs(tab)
    print()

    # création d'un tab avec les sommets et les succésseurs et affichage
    tab_arc = fonctions.graphSucc(tab)
    fonctions.afficherGraph(tab_arc, tab)
    print()

    # création et affichage du graph # (sous forme de matrice de valeurs)
    matrice = fonctions.graph(tab)
    fonctions.afficherMatrice(matrice)

    # vérif qu'il n'y ai pas de circuit et calcul des rangs (si jamais il y a un circuit, les rangs sont faux mais ce n'est pas grave car dans ce cas on a pas besoin de les calculer)

    tab_circ = [item[:] for item in tab]  # pour créer une copie sans que lorsqu'on modifi l'un l'autre change aussi (var indépendante)
    tab_rang = fonctions.nbPrede(tab)  # avoir un tableau de la taille de tab qu'on pourra modifier dans la fonction

    if fonctions.isCircuit(tab_circ, tab_rang) or fonctions.isArcNegatif(tab):
        print('Erreur, ce graph n\'est pas un graph d\'ordonnancement : on ne peu donc pas executer les calculs')
        continue
    else:
        print('Le graph est bien un graph d\'ordonnancement')
        print()
        print('Sommets :', end='\t')
        for i in range(len(tab)):
            print(i, end='\t')
        print('\nRang :', end='\t\t')
        for i in range(len(tab_rang)):
            print(tab_rang[i], end='\t')
        print()

    # uniquement pour écrire dans les fichiers textes d'exécution
    # sys.stdout.close()
