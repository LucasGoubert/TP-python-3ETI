from  tkinter import *
import random
from tkinter import font

dico = ["Hippopotame","International","Tigre","Constitutionnel","Imbiber","Chouette"] #initialistation de la liste de mots

def ChooseWord(dico):
    wordChoose=random.choice(dico) #choix aléatoire d'un mot dans la liste dico
    return wordChoose

def WordDisplay(wordChoose,lettersFound):
    a = ""
    for i, L in enumerate(wordChoose): 
        if i==0 or L in lettersFound: #afficher la première lettre ainsi que les autres lettres déjà trouvées
            a+=L
        else: #afficher un "_" à la place des lettres non trouvées
            a+=" _"
    x.set(a)
    return a

def CorrectEnd(wordChoose,lettersFound):
    i=0
    for l in wordChoose:
        if l in lettersFound: #ajouter 1 au compteur si la lettre du mot est dans la liste de lettres trouvees
            i+=1
    if i==len(wordChoose): #si le nombre de lettres trouvees est égal à la longueur du mot retourner True
        return True

def MenDisplay(): #change l'aspect du pendu en fonction du nombre de vie restante
    global nbChances #définition d'une variable global pour la modifier dans une fonction
    if nbChances==6:
        item = Canevas.create_image(150,150,image=image2)
    if nbChances==5:
        item = Canevas.create_image(150,150,image=image3)
    if nbChances==4:
        item = Canevas.create_image(150,150,image=image4)
    if nbChances==3:
        item = Canevas.create_image(150,150,image=image5)
    if nbChances==2:
        item = Canevas.create_image(150,150,image=image6)
    if nbChances==1:
        item = Canevas.create_image(150,150,image=image7)
    if nbChances==0:
        item = Canevas.create_image(150,150,image=image8)      

def WrongLetterDisplay(wrongLetters): #affiche la liste des mauvaises lettres déjà proposées 
    wrongList=""
    for i in wrongLetters:
        wrongList+=i
        wrongList+=" "
    List.set("Lettres fausses : "+wrongList)
    return wrongList
    
def Verification(): #vérification que la lettre proposée est dans le mot

    global lettersFound,wrongLetters,wordChoose,nbChances
    l=Lettre.get()
    Lettre.set('')
    if l in lettersFound or l in wrongLetters: #si la lettre a déja été proposée
        info.set("Vous avez déjà proposé cette lettre.")
    elif l in wordChoose: #si la lettre proposée est dans le mot
        lettersFound.append(l) #on ajoute cette lettre à la liste des lettres trouvees
        WordDisplay(wordChoose,lettersFound) #affiche les bonnes lettres et les _
        info.set("Vous y êtes presque !")
    else :
        nbChances=nbChances-1 #supprime une chance
        wrongLetters.append(l) #ajout de la lettre dans la liste des fausses lettres
        MenDisplay()
        compt1.set("Nombre de coups restants: "+str(nbChances))
        info.set("Oups ! Raté.")
        WrongLetterDisplay(wrongLetters) #On actualise l'affichage de la liste des fausses lettres


def Pendu():
    global wordChoose,lettersFound,wrongLetters,nbChances
    WordDisplay(wordChoose,lettersFound) #Affichage du wordChoose avec les lettres trouvées
    if nbChances>0:#tant que le joueur n'a pas épuisé ses chances
        Verification()
        if CorrectEnd(wordChoose,lettersFound)==True: #si l'utilisateur a donné toutes les bonnes lettres
            info.set("C'est gagné !")
    if nbChances==0 and CorrectEnd(wordChoose,lettersFound)!=True : #si il manque des bonnes lettres et que le nombre de chance est épuisé
        info.set("C'est perdu !")

def Replay():
    global wordChoose,lettersFound,wrongLetters,nbChances
    wordChoose=ChooseWord(dico) #On choisit un nouveau mot aléatoirement
    lettersFound=[wordChoose[0]] #réinitialistation de la liste des lettres trouvées
    wrongLetters=[] #réinitialistation de la liste des fausses lettres
    nbChances = 7 #réinitialistation des cahnces
    Pendu()
    return wordChoose,lettersFound,wrongLetters,nbChances

wordChoose=ChooseWord(dico) #on choisit un nouveau mot aléatoirement
lettersFound=[wordChoose[0]] #réinitialistation de la liste des lettres trouvees
wrongLetters=[] #réinitialistation de la liste des fausses lettres
nbChances = 7 #réinitialistation des cahnces

#Création de la fenêtre
window=Tk()
window.configure(background='gray')
window.iconbitmap('TP3/icon.ico')

window.title("Le jeu du pendu")

image1=PhotoImage(master=window, file='TP3/bonhomme1.gif')
image2=PhotoImage(master=window, file='TP3/bonhomme2.gif')
image3=PhotoImage(master=window, file='TP3/bonhomme3.gif')
image4=PhotoImage(master=window, file='TP3/bonhomme4.gif')
image5=PhotoImage(master=window, file='TP3/bonhomme5.gif')
image6=PhotoImage(master=window, file='TP3/bonhomme6.gif')
image7=PhotoImage(master=window, file='TP3/bonhomme7.gif')
image8=PhotoImage(master=window, file='TP3/bonhomme8.gif')

#création du Canvas
Largeur=300
Hauteur=300
Canevas=Canvas(window, height= Hauteur, width=Largeur,bg='gray')
item = Canevas.create_image(150,150,image=image1)

#création de la toolbar
Lettre=StringVar()
buttonEntry=Entry(window,textvariable=Lettre,fg='white',bg='#878787')
buttonEntry.focus() #met le focus sur la toolbar

#création du bouton "Proposer"
buttonAsk=Button(window,text='Proposer',command = Pendu,fg='white',bg='#404040')

#création du bouton "Rejouer"
buttonReplay=Button(window,text='Rejouer',command = Replay,fg='white',bg='#404040')

#création bouton "Quitter"
buttonLeave=Button(window,text='Quitter',command = window.destroy,fg='white',bg='#404040')

#création label du mot recherché
x=StringVar()
x.set(WordDisplay(wordChoose,lettersFound))
wordLabel=Label(window,textvariable=x,font=("Times New Roman",16,"italic"),fg='white',bg='gray')

#création label nombre de coups restants
compt1=StringVar()
compt1.set("Nombre de coups restants: "+str(nbChances))
labelCoup=Label(window,textvariable=compt1,fg='white',bg='gray')

#Création label lettres fausses
List=StringVar()
wrongLetterLabel=Label(window,textvariable=List,fg='white',bg='gray')

info=StringVar()
console=Label(window, textvariable=info,fg='white',bg='gray')

#Mise en page de la fenêtre
labelCoup.grid(row=1)
Canevas.grid(row=1,column=3,rowspan=6)
wordLabel.grid(row=2)
buttonEntry.grid(row=3)
buttonAsk.grid(row=4)
buttonReplay.grid(row=6)
wrongLetterLabel.grid(row=7)
console.grid(row=7, column=3)
buttonLeave.grid(row=8,column=3,sticky=NE)


Replay()

wordChoose=Replay()[0]
lettersFound=Replay()[1]
wrongLetters=Replay()[2]
nbChances=Replay()[3]

window.mainloop()