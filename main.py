
with open(".\\tableau_test\\table 1.txt") as file:
    lines = file.readlines() # lines : contenu du fichier.txt merde

# print(lines)
# print(len(lines)) # afficher la taille de lines (le nombre de ligne du fichier.txt donc le nombre de sommet du graph)

### Pour mettre les valeurs du fic.txt dans un tab avec chaque valeur séparé plutôt que tout dans un fic texte ###
var = ""
i = 0
k = 0
tab_inter = []
tab_ligne = []
for ligne in lines:
    while (i<len(ligne)): # pour toute la longueur de la ligne
        if (ligne[i]==" " or ligne[i]=="\n"): # si on arrive à la fin d'un chiffre (ils sont séparé par les espaces sauf le dernier qui fini par un \n
            for j in range(k,i):
                var = var + ligne[j] # alors on met dans var les chiffres qui précèdent à partir du dernier espace (ou bien de 0 si c'est le premier)
            var = var.replace(" ","") # on supprime l'espace qui précède le nombre car il est compris dans la ligne précedente
            if (var!=""): # avec la condition du while, si il y a un espace avant le \n, alors il l'ajoute quand même dans le tableau donc on met un if
                tab_inter.append(int(var)) # tab temporaire pour stocker 1 ligne
            k = i # on met k à i pour que dans le for la lecture continue làa ou elle s'est arreté (sinon ca recommence à 0 à chaque fois et on a plz fois le 1er nombre
            var = "" # on met var à "" pour le prochain nombre
        i = i+1
    tab_ligne.append(tab_inter) # on met la ligne dans le tab final
    tab_inter = [] # on réinitialise tout pour la prochaine ligne
    i = 0
    k = 0
    var = ""

# for val in tab_ligne:
#     print(val)

# ajout du sommet alpha (premier sommet) et oméga

# determination des prédecesseurs de oméga
tab_pre = []
found = 0

for i in range(1,len(tab_ligne)+1): # car il n'y a aucun 0 dans les prédécesseurs
    for val in tab_ligne:
        for j in range(2,len(val)):
            if(i==val[j]):
                found = 1
    if (found==0):
        tab_pre.append(i)
    found = 0

tab_omega = [len(tab_ligne)+1,0]+tab_pre

# ajout du prédecesseur 0 pour les 2e sommets
for ligne in tab_ligne:
    if (len(ligne) == 2):
        ligne.append(0)

# ajout de alpha et oméga
tab_ligne = [[0,0]]+tab_ligne+[tab_omega] # vérifier si les prédécesseurs de oméga sont bien ceux qui n'apparaissent pas dans les prédecesseurs

for val in tab_ligne:
    print(val)

### création du graph ### (sous forme de matrice de valeurs) # on va dire matrice d'adjacence pour l'instant (demander si c bien cette matrice)
matrice = []
for valH in tab_ligne:
    for valV in tab_ligne:
        TODO='faire la matrice'