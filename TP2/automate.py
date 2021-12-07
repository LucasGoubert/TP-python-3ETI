#dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,"mange" : 3, "joue" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,"bleu" : 1, "verte" : 1, "blanc" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

dictionnaire = {}
with open('TP2/dico.txt') as f:
    for line in f:
        if len(line.split()) == 2:
            (key, val) = line.split()
            if int(val) in range(5):
                dictionnaire[key] = int(val)
            else:
                print("La ligne \""+ str(line) + "\" du dictionnaire est incorrect et ne sera pas prise en compte.")
        else:
            print("La ligne \""+ str(line) + "\" du dictionnaire est incorrect et ne sera pas prise en compte.")


phrase1 = "Le joli chat joue."
phrase2 = "La grosse souris verte mange le joli petit chat blanc." 
phrase3 = "La grosse souris verte mange jean." 
phrase4 = "Jean joue."

phraseF1 = "." # ne commence pas par article
phraseF2 = "" # chaîne vide
phraseF3 = "le joli chat joue" # pas ’.’ final
phraseF4 = "le joli chat dort." # ’dort’ inconnu
phraseF5 = "le ,joli chat ; joue."


tab =  [
                        [1,8,8,8,4,8,8],
                        [8,1,2,8,8,8,8],
                        [8,2,8,3,8,8,8],
                        [5,8,8,8,7,9,8],
                        [8,8,8,3,8,8,8],
                        [8,5,6,8,8,8,8],
                        [8,6,8,8,8,9,8],
                        [8,8,8,8,8,9,8],
                        [8,8,8,8,8,8,8],
                        [8,8,8,8,8,8,8]]

def convertToEtat(entree):
    etat = []
    for i in entree:
        if i.upper() in str(dictionnaire.keys()).upper():
            etat.append(dictionnaire[i.lower()])
        else:
            etat.append(6)
    return etat

def main(phrase):
    entrees = (phrase.replace("."," .")).split()
    etat = convertToEtat(entrees)
    sortie = 0
    for k in etat:
        sortie = tab[sortie][k]
    if sortie == 9:
        return "La phrase est juste."
    else:
        return "La phrase est fausse."

print(main(phrase3))
#print(main(input("Saisissez la phrase à vérifier : ")))

