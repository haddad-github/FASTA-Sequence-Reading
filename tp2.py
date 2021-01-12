#Rafic Haddad
#20157600 
#Remis le 9 Octobre 2020

contenu = open("sequences.fasta", "r") #ouvrir le fichier fasta
description = open("descriptions.txt", "w") #créer fichier text où on insérera les descriptions
ids = open("ids.txt", "w") #créer fichier text où on insérera les ids

compteur = 0

for ligne in contenu:

    if ligne[0] == ">": #si le premier index est ">"
        compteur += 1 #compter ces lignes
        description.write(ligne[1:]) #écrire dans description.txt, en enlevant le premier caractère (soit ">")
        ids.write(ligne[1:].split()[0]+"\n") #écrire en enlevant ">"; premier mot (avant premier espace de la ligne) et rajouter un saut de ligne

with open("sequences.fasta", "r") as contenu: #réitérer le fichier fraîchement

 lignes = contenu.readlines() #lire les lignes

 lignes_sequence1 = lignes[1:58] #les lignes 2 à 57 (index 1 à 58(non inclu)), soit les lignes de la séquence 1

 sequence1 = sum(len(lignes.replace("\n", "")) for lignes in lignes_sequence1) #enleve sauts de lignes; ensuite somme caractères pour ces lignes

print("Il y a {} sequences".format(compteur)) #imprimer le nombre de lignes avec la fonction format()
print("Il y a {} acides aminees dans la premiere sequence".format(sequence1)) #imprimer la longueur avec la fonction format()
