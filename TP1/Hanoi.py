global tours
tours = 0

def hanoiIA(n,A,B,C):
    global tours
    if n==1:
        print ("Déplacer le disque du plot",A,"vers le plot",B)
        tours = tours + 1
        return
    hanoiIA(n-1, A, C, B)
    print ("Déplacer le disque du plot",A,"vers le plot",B)
    tours = tours + 1

    hanoiIA(n-1, C, B, A)



hanoiIA(int(input("Nombre de disques : ")),'1','2','3') 
print("Il a fallut " + str(tours) + " tours")