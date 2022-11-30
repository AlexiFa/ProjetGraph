import fonctions

path = ".\\tableau_test\\table 1.txt"
## on stock les valeurs du .txt dans un tableau 2D pour y accéder facilement
tab = fonctions.readTab(path)

# for val in tab:
#     print(val)

## on ajoute les sommet alpha et oméga qui sont au tout début et à la toute fin pour avoir un seul pt de départ et un seul pt d'arrivée
tab = fonctions.ajoutSommetsFictifs(tab)

# for val in tab:
#     print(val)

### création du graph ### (sous forme de matrice de valeurs)

matrice = fonctions.graph(tab)
# fonctions.afficherMatrice(matrice)

## on a ajouter le point d'entrée et le point de sortie manuellement donc on est sur qu'il y en a qu'un de chaque

## vérification qu'il n'y ai pas de circuit ##

# stocker les predececeurs et les successeurs
# for val in tab_ligne:
#     print(val)
tab_pre = []
for sommet in tab:
    if(len(sommet)>=3):
        for pre in sommet:
            tab_pre.append(pre)

# for val in tab_pre:
#     print(val)

# get tout les sommets entrée du graph
tab_voila = fonctions.del_entree(tab)  # attention marche pour la premiere occurence mais pas pour celle d'apres

# for ivref in range(0, len(tab)):
#     tab_voila = fonctions.del_entree(tab_voila)  # ne marche pas
