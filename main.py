import fonctions

## on stock les valeurs du .txt dans un tableau 2D pour y accéder facilement
tab = fonctions.readTab(".\\tableau_test\\table 1.txt")

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

## methode de Roy-Warshall

i = 0
MA_trans = matrice # matrice d'adjacence de la fermueture transitive
for sommet in range(0,15):
    for prede in tab[sommet]:
        for succ in matrice[sommet]:
            a=2