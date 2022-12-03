# fonction de lecture du fichier.txt avec les valeurs tests
# parametre : string du path du tableau a lire
# return : un tab 2D avec les info du tableau
def readTab(path):
    with open(path) as file:
        lines = file.readlines()  # un tab avec chaque ligne du fic.txt

    ### Pour mettre les valeurs du fic.txt dans un tab avec chaque valeur séparé plutôt que tout dans un fic texte ###
    var = ""
    i = 0
    k = 0
    tab_inter = []
    tab_ligne = []
    for ligne in lines:
        while i < len(ligne):  # pour toute la longueur de la ligne
            if ligne[i] == " " or ligne[i] == "\n":  # si on arrive à la fin d'un chiffre (ils sont séparé par les espaces sauf le dernier qui fini par un \n
                for j in range(k, i):
                    var = var + ligne[j]  # alors on met dans var les chiffres qui précèdent à partir du dernier espace (ou bien de 0 si c'est le premier)
                var = var.replace(" ", "")  # on supprime l'espace qui précède le nombre car il est compris dans la ligne précedente
                if var != "":  # avec la condition du while, si il y a un espace avant le \n, alors il l'ajoute quand même dans le tableau donc on met un if
                    tab_inter.append(int(var))  # tab temporaire pour stocker 1 ligne
                k = i  # on met k à i pour que dans le for la lecture continue làa ou elle s'est arreté (sinon ca recommence à 0 à chaque fois et on a plz fois le 1er nombre
                var = ""  # on met var à "" pour le prochain nombre
            i = i + 1
        tab_ligne.append(tab_inter)  # on met la ligne dans le tab final
        tab_inter = []  # on réinitialise tout pour la prochaine ligne
        i = 0
        k = 0
        var = ""
    del var, i, k, tab_inter, ligne, j, lines  # suppr les variable temp qu'on a créer pour fabriquer le tableau

    return tab_ligne

# fonction ajout de alpha et oméga (les sommets qui sont au début et à la fin)
# parametre : tableau de stockage avec les valeurs du .txt (sans les sommets alpha et oméga)
# return : tab 2D en parametre mais en ajoutant les sommets fictifs et leurs prédecesseur (et successeurs)
def ajoutSommetsFictifs(tab):
    # determination des prédecesseurs de oméga
    tab_pre = []
    found = 0

    for i in range(1, len(tab) + 1):  # i = les num des sommets (dans les tab ca commence tout le tps à 1)
        for val in tab:
            for j in range(2, len(val)):  # recherche dans les prédecesseur (à partir de la case d'indice 2)
                if i == val[j]:
                    found = 1  # on a trouvé un sommet qui a comme prédecesseur i (donc i n'est pas un sommet sortie/ un predecesseur de omega)
        if found == 0:
            tab_pre.append(i)  # si i est un sommet sortie alors on l'ajoute au tab_pre (ce sera tout les predecesseurs de omega)
        found = 0  # reinitialise pour le prochain sommet

    tab_omega = [len(tab) + 1, 0] + tab_pre  # oméga sera le sommet de num N+1 de temps 0 et avec les predecesseurs obtenu au dessus

    # ajout du prédecesseur 0 pour les 2e sommets
    for ligne in tab:
        if len(ligne) == 2:
            ligne.append(0)  # si le sommet n'as aucun predecesseur alors c une entrée il aura comme predecesseur alpha (de num 0)

    # ajout de alpha et oméga
    tab_ligne = [[0, 0]] + tab + [tab_omega]  # tab avec alpha qui n'a pas de durée et de pre et omega qu'on a obtenu plus haut

    del tab_pre, found, tab_omega, i, val, j, ligne  # del des variables temporaires
    return tab_ligne

# fonction création du graph sous forme de matrice
# parametre : tableau dans lequel est stocké tout les sommets et leurs info
# return : matrice de valeur
# ('*' si les sommets n'ont pas d'arc les liant, la valeur de l'arc s'il existe)
def graph(tab):
    ### création du graph ### (sous forme de matrice de valeurs)
    matrice = []
    match = '*'  # '*' si l'arc n'existe pas donc la val par defaut
    temp = []
    for valH in tab:
        for valV in tab:  # pour chaque case de la matrice carré avec les sommets
            if len(valV) >= 3:  # si le sommet correspondant à la valeur en colonne a un prédécesseur
                for i in range(2, len(valV)):  # pour chaque prede
                    if valH[0] == valV[i]:
                        match = valH[1]  # si le prede correspond à la ligne actuelle alors on met dans match la durée du sommet actuel
            temp.append(match)  # et on ajoute cette durée dans la case de [prede][succ]
            match = '*'  # reset de match pour la suite
        matrice.append(temp)  # ajout du tableau avec le sommet et les valeurs des arc le liant aux autre sommet (avec les indice qui correspondent au sommets)
        #  exple : temp[2] correspond à la valeur de l'arc liant le sommet actuel dans temp au sommet 2
        temp = []  # reset de temp pour qu'il accueil le prochain sommet

    del match, temp, valV, valH, i
    return matrice

# fonction qui affiche la matrice avec les lignes et les colonnes alignées
# parametre : la matrice à afficher
def afficherMatrice(matrice):
    for val in matrice:
        print(*val, sep='\t')  # on affiche la matrice en suppr les ', les virgules et les [] pour que tout soit aligné

# fonction pour avoir le numero des sommets entrée du graph
# parametre : le graph a étudier sous la forme du tab avec les sommets et les info (exple : return de la fonction ajoutsommetfictif())
# return : un tab avec les num des sommets entrée
def get_entree(graph):
    tab_entree = []
    for sommet in graph:
        if len(sommet) == 2:  # si le sommet n'as aucun prede (donc c une entrée
            tab_entree.append(sommet[0])
    return tab_entree

# fonction qui supprime les sommet entrée (en les effaçant de leur successeur car ils sont stockée comme prédecesseurs)
# parametre : tab 2D avec les info de chaque sommet (comme au début)
# return : tab2D avec les sommets entrée effacé
def del_entree(tab_copie):
    tab_entree = get_entree(tab_copie)  # on recup toute les entrée du graph
    indice = []  # tab avec les indices des entrée dans le tab avec tout les sommets
    indice_2 = []  # tab avec les indices des prédecesseurs qui vont être suppr

    for entr in tab_entree:  # pour chaque entrée
        for i in range(0, len(tab_copie)):  # pour chaque sommet
            if tab_copie[i][0] == entr:
                indice.append(i)  # si le sommet actuel est une entrée, on note son indice car il faudra le suppr
                # on ne suppr pas le sommet directement pour eviter de changer la taille du tableau quand on le parcours
                # et on veux suppr aussi ce sommet dans les prédecesseurs
                for j in range(0, len(tab_copie)):  # pour chaque sommets
                    if len(tab_copie[j]) <= 2:
                        continue  # si sa taille est de 2 (ou moins même si ca n'arrive jamais) alors il n'y a pas de predecesseur à suppr car c'est une entrée
                        # le continue fait qu'on passe au sommet suivant et on skip les lignes suivantes (dans le for)
                    for k in range(2, len(tab_copie[j])):  # on regarde tout les predecesseurs
                        if tab_copie[j][k] == entr:
                            indice_2.append(k)  # si on trouve le prede, alors on note son indice car il faudra le suppr
                    for h in indice_2:  # apres avoir parcouru les prede du sommet on suppr aux indices qu'on a noté
                        tab_copie[j].pop(h)  # ne marche pas s'il y a deux fois le même predecesseur (mais en dans les tab de test ca n'arrive jamais et ca n'aurai pas de sens quand on parle d'un projet avec des taches et des durée)
                        # techniquement on pourrai faire une boucle inverse pour pouvoir suppr deux prede en même temps mais comme il ne peut pas avoir deux fois le meme prede alors on l'a pas fait
                        # TODO : si on a le temps, on peu améliorer le code en suppr tout les prede en mm temps (ca pour l'instant on les fait un par un)
                        # ca sera plus opti car moins de boucle dans les boucle
                    indice_2 = []  # reset des indices pour le sommet suivant
    for i in reversed(range(0, len(tab_copie))):  # pour chaque sommet (reversed pas obliatoire)
        for ind in reversed(indice):  # pour chaque indice (reversed car les sommets sont rangé dans l'ordre croissant donc comme ca on ne change pas les indices si on suppr plz sommet en mm temps)
            if i == ind:
                tab_copie.pop(i)  # si l'indice est le même qu'on sommet entrée alors on suppr
    return tab_copie

# fonction qui suppr les sommets à petit pour determiner s'il y a un circuit
# parametre : tab 2D avec les info de chaque sommet (comme au début)
# return : 1 si il y a un circuit et 0 s'il n'y en a pas
def isCircuit(tab_voila):
    while len(tab_voila) >= 1:
        size_temp = len(tab_voila)
        tab_voila = del_entree(tab_voila)
        size = len(tab_voila)
        if size < size_temp:
            size_temp = size
        else:
            return 1
            break
    return 0
