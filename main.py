# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

with open("table 1.txt") as file:
    lines = file.readlines()

print(lines)
print(len(lines)) # afficher la taille de lines (le nombre de ligne du fichier.txt donc le nombre de sommet du graph)
codetemp = 0
durationtemp = 0
pretemp = []
task_code = [] # task_code : le 1er nombre de chaque ligne
task_duration = [] # task_duration : le 2e nombre de chaque ligne
task_pre = [[]] # task_pre : tout les nombres suivants

# Attention : le for suivant est un peu fait de manière dégeulasse
for val in lines: # rempli le tableau (marche que si les nombre a remplir ont 1 ou deux chiffre) (faudrai améliorer ca)
    if (val[1]==' '):
        codetemp = val[0]
        if (val[3]==' '):
            durationtemp = val[2]
            temp = 0
            test = len(val)
            while(val[temp+4]!='\n'):
                pretemp.append(val[temp+4])
                temp = temp + 1
        elif (val[4]==' '):
            durationtemp = val[2]+val[3]
            temp = 0
            while (val[temp+5] != '\n'):
                pretemp.append(val[temp + 5])
                temp = temp + 1
    elif (val[2]==' '):
        codetemp = val[0]+val[1]
        if (val[4]==' '):
            durationtemp = val[3]
            temp = 0
            while (val[temp+5] != '\n'):
                pretemp.append(val[temp + 5])
                temp = temp + 1
        elif (val[5]==' '):
            durationtemp = val[3]+val[4]
            temp = 0
            while (val[temp+6] != '\n'):
                pretemp.append(val[temp + 6])
                temp = temp + 1
    task_code.append(codetemp)
    task_duration.append(durationtemp)
    task_pre.append(pretemp)

for v in task_pre:
    print(v)

#
# duree = {}
# j=0
# valeur = 0
#
# for a in lines:
#     valeur = a[0]+a[1]
#
# for i in lines:
#     code_tache[j]=i[0]
#     duree[j]=i[2]
#     j=j+1
#
# for k in code_tache:
#     print('tache :',code_tache[k])
#
# for h in duree:
#     print('durée :',duree[h])