import fonctions
import os

# boucle main avec l'interface utilisateur :

while 1:
    print('Voici les fichiers texte disponible\n')
    for file in os.listdir('./tableau_test'):
        print(file, end=' | ')
    print('\n\nVeuillez en choisir un (entrez le nom complet du fichier avec l\'extention) :')
    print('Si vous voulez quitter, tappez "quit" ou "exit"')
    fichier = input()
    if fichier == 'quit' or fichier == 'exit':
        break
    path = ".\\tableau_test\\"+fichier

    # on stock les valeurs du .txt dans un tableau 2D pour y accéder facilement
    tab = fonctions.readTab(path)  # TODO : faire une exception si le fichier n'est pas trouvé

    # on ajoute les sommets alpha et oméga qui sont au tout début et à la toute fin pour avoir un seul pt de départ et un seul pt d'arrivée
    tab = fonctions.ajoutSommetsFictifs(tab)

    # création et affichage du graph # (sous forme de matrice de valeurs)
    matrice = fonctions.graph(tab)
    fonctions.afficherMatrice(matrice)

    # vérif qu'il n'y ai pas de circuit

    if fonctions.isCircuit(tab):  # il faudra ajouter la fonction de vérif des arcs positifs
        print('Erreur, ce graph n\'est pas un graph d\'ordonnancement : on ne peu donc pas executer les calculs')
        continue
    else:
        print('il y a pas de circuit')


path = ".\\tableau_test\\table 1.txt"
## on stock les valeurs du .txt dans un tableau 2D pour y accéder facilement
tab = fonctions.readTab(path)  # TODO : faire une exception si le fichier n'est pas trouvé

# for val in tab:
#     print(val)

## on ajoute les sommet alpha et oméga qui sont au tout début et à la toute fin pour avoir un seul pt de départ et un seul pt d'arrivée
tab = fonctions.ajoutSommetsFictifs(tab)

# for val in tab:
#     print(val)

### création du graph ### (sous forme de matrice de valeurs)

matrice = fonctions.graph(tab)
fonctions.afficherMatrice(matrice)

## on a ajouter le point d'entrée et le point de sortie manuellement donc on est sur qu'il y en a qu'un de chaque

## vérification qu'il n'y ai pas de circuit ##

# stocker les predececeurs et les successeurs
# for val in tab_ligne:
#     print(val)
tab_pre = []
for sommet in tab:
    if len(sommet) >= 3:
        for pre in sommet:
            tab_pre.append(pre)

# for val in tab_pre:
#     print(val)

# get tout les sommets entrée du graph
# tab_voila = fonctions.del_entree(tab)  # attention marche pour la premiere occurence mais pas pour celle d'apres

# while len(tab_voila) >= 1:
#     size_temp = len(tab_voila)
#     tab_voila = fonctions.del_entree(tab_voila)
#     size = len(tab_voila)
#     if size < size_temp:
#         size_temp = size
#     else:
#         print("il y a un circuit")
#         break

if fonctions.isCircuit(tab):
    print('il y a un circuit')
else:
    print('il y a pas de circuit')