import random

dico = ["Hippopotame","International","Tigre","Constitutionnel","Imbiber","Chouette"]

def ChooseWord(dico):
    wordChoose=random.choice(dico) #choix aléatoire d'un mot dans la liste dico
    return wordChoose
    
def WordDisplay(wordChoose, lettersFound):
    for i, l in enumerate(wordChoose): 
        if i==0 or l in lettersFound: #afficher la première lettre ainsi que les autres lettres déjà trouvées
            print(l)
        else: #afficher un "_" à la place des les lettres non trouvées
            print("_")

def letterInput():
    lettre=input("Proposer une lettre : ") #l'utilisateur doit entrer une lettre
    return lettre

def CorrectEnd(wordChoose,lettersFound):
    count=0
    for l in wordChoose:
        if l in lettersFound: #ajouter 1 au compteur si la lettre du mot est dans la liste de lettres trouvees
            count+=1
    if count==len(wordChoose):
        return True

def BestScore(Best): #vérifie si le score est meilleur que le score enregistré dans Best
    score=Pendu()
    if score>Best:
        Best=score
        print ("Vous avez le meilleur score !")

global Best #définition d'une variable global pour la modifier dans une fonction
Best = 0

def Pendu():
    global Best
    chance = 8
    wordChoose = ChooseWord(dico)
    lettersFound = [wordChoose[0]] #initialistation de la liste des lettres trouvées
    wrongLetters = [] #initialisation de la liste des fausses lettres proposées

    WordDisplay(wordChoose,lettersFound) #affichage des lettres trouvées et des _

    while chance>0: #boucle tant que le joueur n'a pas épuisé toutes ses chances
        Lettre=letterInput()

        if Lettre in lettersFound or Lettre in wrongLetters: 
            print ("Vous avez déjà proposé cette lettre.")
        elif Lettre in wordChoose: #si la lettre est juste
            lettersFound.append(Lettre) #on ajoute la lettre proposée à la liste des lettres trouvées
            WordDisplay(wordChoose,lettersFound) #afficher les lettres trouvées et des _
            print ("Bravo ! Cette lettre est dans le mot. Il vous reste ",chance," chances.")
        else :
            chance-=1 #supprime une chance
            wrongLetters.append(Lettre) #ajout de la lettre dans la liste des fausses lettres
            print ("Non .. Cette lettre n'est pas dans le mot. Il vous reste ",chance," chances.")
        if CorrectEnd(wordChoose,lettersFound)==True: #si l'utilisateur a trouvé le mot juste
            print ("Vous avez gagné !")
            Score=chance
            if Score>Best: #vérifie si notre score est le meilleur
                Best=Score
                print ("Vous avez le meilleur score !")
            chance=0
        else : #le jeu continue
            print ("Vous y êtes presque !")

    if chance==0 and CorrectEnd(wordChoose,lettersFound)!=True : #si le mot n'est pas trouvé et que le nombre de chance est épuisé
        print ("Vous avez perdu..")
    if chance==0 :
        replay=input("Voulez-vous rejouer ? Entrer 1 pour oui et 2 sinon : ")
        if replay==1:
            return Score, Pendu() #relance le jeu avec un nouveau mot
        else :
            print ("Votre score était de",Score,".") #clos le jeu
            return Score
        
Pendu()
BestScore(Best)