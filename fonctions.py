# fonction de lecture du fichier.txt avec les valeurs tests
# parametre : string du path du tableau a lire
# return : un tab 2D avec les info du tableau
def readTab(path):
    with open(path) as file:
        lines = file.readlines()

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
    del var, i, k, tab_inter, ligne, j, lines  ## suppr les variable temp qu'on a créer pour fabriquer le tableau

    return tab_ligne

# fonction ajout de alpha et oméga (les sommets qui sont au début et à la fin)
# parametre : tableau de stockage avec les valeurs du .txt (sans les sommets alpha et oméga)
# return : tab 2D en parametre mais en ajoutant les sommets fictifs et leurs prédecesseur (et successeurs)
def ajoutSommetsFictifs(tab):
    # ajout du sommet alpha (premier sommet) et oméga

    # determination des prédecesseurs de oméga
    tab_pre = []
    found = 0

    for i in range(1, len(tab) + 1):  # car il n'y a aucun 0 dans les prédécesseurs
        for val in tab:
            for j in range(2, len(val)):
                if i == val[j]:
                    found = 1
        if found == 0:
            tab_pre.append(i)
        found = 0

    tab_omega = [len(tab) + 1, 0] + tab_pre

    # ajout du prédecesseur 0 pour les 2e sommets
    for ligne in tab:
        if len(ligne) == 2:
            ligne.append(0)

    # ajout de alpha et oméga
    tab_ligne = [[0, 0]] + tab + [tab_omega]  # vérifier si les prédécesseurs de oméga sont bien ceux qui n'apparaissent pas dans les prédecesseurs

    del tab_pre, found, tab_omega, i, val, j, ligne
    return tab_ligne

# fonction création du graph sous forme de matrice
# parametre : tableau dans lequel est stocké tout les sommets et leurs info
# return : matrice de valeur
# ('*' si les sommets n'ont pas d'arc les liant, la valeur de l'arc s'il existe)
def graph(tab):
    ### création du graph ### (sous forme de matrice de valeurs)
    matrice = []
    match = '*'
    temp = []
    for valH in tab:
        for valV in tab:
            if len(valV) >= 3:
                for i in range(2, len(valV)):  # vérifier
                    if valH[0] == valV[i]:
                        match = valH[1]
            temp.append(match)
            match = '*'
        matrice.append(temp)
        temp = []

    del match, temp, valV, valH, i
    return matrice

# fonction qui affiche la matrice avec les lignes et les colonnes alignées
# parametre : la matrice à afficher
def afficherMatrice(matrice):
    for val in matrice:
        print(*val, sep='   ')

# fonction pour avoir le numero des sommets entrée du graph
# parametre : le graph a étudier sous la forme du tab avec les sommets et les info (exple : return de la fonction ajoutsommetfictif())
# return : un tab avec les num des sommets entrée
def get_entree(graph):
    tab_entree = []
    for sommet in graph:
        if len(sommet) == 2:
            tab_entree.append(sommet[0])
    return tab_entree

# fonction qui supprime les sommet entrée (en les effaçant de leur successeur car ils sont stockée comme prédecesseurs)
# parametre : tab 2D avec les info de chaque sommet (comme au début)
# return : tab2D avec les sommets entrée effacé
def del_entree(tab_copie):
    tab_entree = get_entree(tab_copie)
    indice = []

    for entr in tab_entree:
        for i in range(0, len(tab_copie)):
            if tab_copie[i][0] == entr:
                indice.append(i)
                for j in range(0, len(tab_copie)):
                    if len(tab_copie[j]) <= 2:
                        continue
                    for k in range(2, len(tab_copie[j])):
                        if tab_copie[j][k] == entr:
                            tab_copie[j].pop(k)
    for i in indice:
        tab_copie.pop(i)
    return tab_copie
