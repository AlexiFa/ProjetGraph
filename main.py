import fonctions
import os

# boucle main avec l'interface utilisateur :
# en commentaire pour les tests
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
    try:
        tab = fonctions.readTab(path)
    except FileNotFoundError:
        print("Fichier non trouvé")
        continue

    # on ajoute les sommets alpha et oméga qui sont au tout début et à la toute fin pour avoir un seul pt de départ et un seul pt d'arrivée
    tab = fonctions.ajoutSommetsFictifs(tab)

    # création et affichage du graph # (sous forme de matrice de valeurs)
    matrice = fonctions.graph(tab)
    fonctions.afficherMatrice(matrice)

    # vérif qu'il n'y ai pas de circuit et calcul des rangs (si jamais il y a un circuit, les rangs sont faux mais ce n'est pas grave car dans ce cas on a pas besoin de les calculer)

    tab_circ = [item[:] for item in tab]  # pour créer une copie sans que lorsqu'on modifi l'un l'autre change aussi (var indépendante)
    tab_rang = fonctions.nbPrede(tab)  # avoir un tableau de la taille de tab qu'on pourra modifier dans la fonction

    if fonctions.isCircuit(tab_circ, tab_rang):  # il faudra ajouter la fonction de vérif des arcs positifs
        print('Erreur, ce graph n\'est pas un graph d\'ordonnancement : on ne peu donc pas executer les calculs')
        continue
    else:
        print('il y a pas de circuit')
        print(tab_rang)  # les affichage ici sont pour les tests
        print(tab)
        print(tab_circ)


path = ".\\tableau_test\\table 2.txt"
## on stock les valeurs du .txt dans un tableau 2D pour y accéder facilement
try:
    tab = fonctions.readTab(path)
except FileNotFoundError:
    print('Fichier non trouvé')


## on ajoute les sommet alpha et oméga qui sont au tout début et à la toute fin pour avoir un seul pt de départ et un seul pt d'arrivée
tab = fonctions.ajoutSommetsFictifs(tab)

for val in tab:
    print(val)

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
tab_circ = [item[:] for item in tab]  # pour créer une copie sans que lorsqu'on modifi l'un l'autre change aussi (var indépendante)
tab_rang = fonctions.nbPrede(tab)  # avoir un tableau de la taille de tab qu'on pourra modifier dans la fonction

if fonctions.isCircuit(tab_circ, tab_rang):
    print('il y a un circuit')
else:
    print('il y a pas de circuit')

print(tab_rang)  # AAAAH OUI LE CALCUL DES RANG MARCHE (en tout ca ca marche pour le table 2.txt) (pour les table qui ont des circuit ce n'est pas la peine de les caculer)
print(tab)
tab_prede = fonctions.nbPrede(tab)
print(tab_prede)
