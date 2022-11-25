
with open("table 1.txt") as file:
    lines = file.readlines() # lines : contenu du fichier.txt merde

print(lines)
print(len(lines)) # afficher la taille de lines (le nombre de ligne du fichier.txt donc le nombre de sommet du graph)

### Pour mettre les valeurs du fic.txt dans un tab avec chaque valeur séparé plustot que tout dans un fic texte ###
var = ""
i = 0
k = 0
tab_inter = []
tab_ligne = []
for ligne in lines:
    while (i<len(ligne)):
        if (ligne[i]==" " or ligne[i]=="\n"):
            for j in range(k,i):
                var = var + ligne[j]
            var = var.replace(" ","")
            if (var!=""):
                tab_inter.append(var)
            k = i
            var = ""
        i = i+1
    tab_ligne.append(tab_inter)
    tab_inter = []
    i = 0
    k = 0
    var = ""

# for val in tab_ligne:
#     print(val)