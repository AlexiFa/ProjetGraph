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
    new_matrice = []
    for num in range(0, len(matrice)):
        new_matrice.append([num] + matrice[num])
    print('', end='\t')  # pour aligner les colonnes
    for i in range(0, len(matrice)):  # pour afficher les num au niveau des colonnes
        print(i, end='\t')
    print()
    for val in new_matrice:
        print(*val, sep='\t')  # on affiche la matrice en suppr les ', les virgules et les [] pour que tout soit aligné
    del val

# fonction pour avoir le numero des sommets entrée du graph
# parametre : le graph a étudier sous la forme du tab avec les sommets et les info (exple : return de la fonction ajoutsommetfictif())
# return : un tab avec les num des sommets entrée
def get_entree(graph):
    tab_entree = []
    for sommet in graph:
        if len(sommet) == 2:  # si le sommet n'as aucun prede (donc c une entrée
            tab_entree.append(sommet[0])
    del sommet
    return tab_entree

# fonction qui supprime les sommet entrée (en les effaçant de leur successeur car ils sont stockée comme prédecesseurs), et notes les taches qui ont été suppr pour que les rangs soient attribué dans la fonction au dessus
# parametre : tab 2D avec les info de chaque sommet (comme au début)
# return : tab2D avec les sommets entrée effacé
def del_entree(tab_copie, tache):
    tab_entree = get_entree(tab_copie)  # on recup toute les entrée du graph
    indice = []  # tab avec les indices des entrée dans le tab avec tout les sommets
    indice_2 = []  # tab avec les indices des prédecesseurs qui vont être suppr

    for entr in tab_entree:  # pour chaque entrée
        for i in range(0, len(tab_copie)):  # pour chaque sommet
            if tab_copie[i][0] == entr:
                indice.append(i)  # si le sommet actuel est une entrée, on note son indice car il faudra le suppr
                # on ne suppr pas le sommet directement pour éviter de changer la taille du tableau quand on le parcours
                # et on veut suppr aussi ce sommet dans les prédécesseurs
                for j in range(0, len(tab_copie)):  # pour chaque sommets
                    if len(tab_copie[j]) <= 2:
                        continue  # si sa taille est de 2 (ou moins même si ca n'arrive jamais) alors il n'y a pas de prédécesseur à suppr car c'est une entrée
                        # le continue fait qu'on passe au sommet suivant et on skip les lignes suivantes (dans le for)
                    for k in range(2, len(tab_copie[j])):  # on regarde tous les prédécesseurs
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
                tache.append(tab_copie[i][0])  # on note le code de la tache à qui on veux ajouter le rang
                # on le fait avant que le tableau soit modifié
                tab_copie.pop(i)  # si l'indice est le même qu'on sommet entrée alors on suppr
    # jsp pk mais les del ne marchent pas dans cette fonction (à chercher)
    return tab_copie

# fonction qui suppr les sommets à petit pour determiner s'il y a un circuit, elle calcul au passage les rangs des sommets
# parametre : tab 2D avec les info de chaque sommet (comme au début), tableau qui contient les rangs des sommet aux indices correspondants
# return : 1 si il y a un circuit et 0 s'il n'y en a pas
def isCircuit(tab_voila, tab_rang):
    tab_ref = [item[:] for item in tab_voila]  # pour avoir le tableau sans modification pour avoir les bon indice lors du calcul des rangs
    tache = []  # les code des tache à qui on va ajouter le rang
    iteration = 0  # itération qui va determiner le rang du sommet en cours
    while len(tab_voila) >= 1:
        size_temp = len(tab_voila)
        tab_voila = del_entree(tab_voila, tache)
        for val in tache:  # dans ce tableau il y a toute les taches qui viennent d'etre suppr donc celle auquelles il faut tribuer les rangs
            for a in range(0, len(tab_ref)):  # pour avoir les indices exacte auquelle on doit ajouter les rangs
                if tab_ref[a][0] == val:  # si le code à cet indice correspond à un code auquelle on doit attribuer le rang
                    tab_rang[a] = iteration
        tache = []  # reset pour les taches suivantes
        iteration += 1  # a chaque fois qu'on suppr les racines actuelle, on passe à l'itération suivante
        size = len(tab_voila)
        if size < size_temp:
            size_temp = size
        else:
            del size_temp, size
            return 1
    return 0

# fonction qui calcul le nombre d'arc entrant dans un sommet (le nombre de predecesseur)
# parametre : tab 2D avec les info de chaque sommet (comme au début)
# return : un tableau 2D avec le nombre de prede de chaque sommet aux indices correspondant
#### euuuh à vérifier mais je ne sais pas si elle sert à qqch cette fonction ####
def nbPrede(tab):
    tab_nb = []
    for ligne in tab:
        nb = len(ligne)-2  # compte le nombre de case apres les deux première (le nombre de case dans la colonne des prede)
        tab_nb.append(nb)
    del ligne, nb
    return tab_nb

# fonction qui verifie s'il y a un arc à valeur négative
# parametre : tab 2D avec les infos du graph
# return : 1 s'il y a un arc négatif et 0 sinon
def isArcNegatif(tab):
    for i in range(len(tab)):
        if tab[i][1] < 0:
            return 1
    return 0

# fonction qui caclul la durée d'un chemin donné
# parametre : tab avec le chemin et un tableau complet du graph
# return : un entier egale à la duree du chemin
def calculDuree(tab_chemin, tab_ref):
    duree = 0
    for sommet in tab_chemin:
        for val in tab_ref:
            if sommet == val[0]:
                duree += val[1]
    return duree

# fonction stock le graph avec chaque sommet et ses successeurs
# parametre : tab 2D du graph avec toutes les infos
# return : tab avec chaque arc et sa durée
def graphSucc(tab):
    pre = 0
    succ = 0
    duree = 0
    arc = []  # on va stocker un sommet son succ et la durée de l'arc [sommet, duree, succ]
    tab_arc = []
    for sommet in tab:
        for i in range(2, len(sommet)):
            pre = sommet[i]
            succ = sommet[0]
            for val in tab:
                if val[0] == pre:
                    duree = val[1]
            arc = [pre, duree, succ]
            tab_arc.append(arc)
    return tab_arc

# fonction qui affiche le graph avec chacun de ses sommets et ses succ
# parametre : tab avec les successeurs et les durée donnée par la fonction graphSucc et le tab ref avec toutes les info
# return : affichage
def afficherGraph(tab, tab_ref):
    tab_temp = [item[:] for item in tab]  # avoir une copie qu'on peut modifier
    tab_temp2 = [item[:] for item in tab]
    print(len(tab_ref), ' sommets')  # affiche le nombre de sommets
    print(len(tab), ' arcs')  # affiche le nombre d'arcs
    # mettre dans l'ordre des successeurs le tableau
    tab_ordre = []
    temp = 0
    while len(tab_temp) != 0:
        tab_temp2 = [item[:] for item in tab_temp]
        i = 0
        for arc in tab_temp2:
            temp = 0
            for arc2 in range(0, len(tab_temp)):
                if arc[0] > tab_temp[arc2][0]:
                    temp = 1
                if arc == tab_temp[arc2]:
                    i = arc2
            if temp == 0:
                tab_ordre.append(arc)
                tab_temp.pop(i)
            i += 1
    for arc in tab_ordre:
        print(arc[0], ' -> ', arc[2], ' = ', arc[1])







# # TODO : fonction qui calcul un chemin (il va ptre falloir faire quelques modifs)
# # parametre : tab avec uniquement les prédécesseurs
# # return : le chemin le plus long (liste des sommets et on calculera la duree apres)
# def cheminCritique(tab_pre, tab_ref, code, tab_circuit, fini, tab_chemins):
#     # if code == 0 or fini:
#     #     return fini
#     # else:
#     #     new_tab_pre = []
#     #     for prede in tab_pre:
#     #         if not fini:
#     #             for sommet in tab_ref:
#     #                 if sommet[0] == prede and not fini:
#     #                     tab_circuit.append(sommet[0])
#     #                     code = sommet[0]
#     #                     for pre in range(2, len(sommet)):
#     #                         new_tab_pre.append(sommet[pre])
#     #                     fini = cheminCritique(new_tab_pre, tab_ref, code, tab_circuit, fini, tab_chemins)
#     #                     if not fini:
#     #                         tab_chemins.append(tab_circuit)
#     #                         tab_circuit = [len(tab_ref)-1]
#     #                     fini = True
#     #         else:
#     #             continue
#     #     #return fini
#     while code != 0 and not fini:
#         new_tab_pre = []
#         for prede in tab_pre:
#             for sommet in tab_ref:
#                 if sommet[0] == prede and not fini:
#                     tab_circuit.append(sommet[0])
#                     code = sommet[0]
#                     for pre in range(2, len(sommet)):
#                         new_tab_pre.append(sommet[pre])
#                     fini = cheminCritique(new_tab_pre, tab_ref, code, tab_circuit, fini, tab_chemins)
#                     # if not fini:
#                     #     tab_chemins.append(tab_circuit)
#                     #     tab_circuit = [len(tab_ref) - 1]
#                     fini = True
#         return fini
