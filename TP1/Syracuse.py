def syracuseSuite(N):
    while N!=1:
        if N%2==0:
            N = N/2
        else:
            N = N*3 + 1
        print(N)
    
def altMax(N):
    listN = []
    M = N
    if N!=1:
        while N!=1:
            if N%2==0:
                N = N/2
            else:
                N = N*3 + 1
            listN.append(N)
        print("L'altitude maximum est " + str(max(listN)) + " pour " + str(M))
        return max(listN)
    else:
        print("L'altitude maximum est 1 pour 1")
        return 1

def flightTime(N):
    tp = 0
    while N!=1:
        if N%2==0:
            N = N/2
        else:
            N = N*3 + 1
        tp += 1
    print("Le temps de vol est " + str(tp) + " pour " + str(N))
    return tp

def maxFT(n):
    max = 0
    for i in range(1,n):
        if flightTime(i)>max:
            max = flightTime(i)
            maxIndex = i
    print("Le temps de vol maximum pour les nombres de 1 à " + str(n) +" est "+ str(maxIndex)+ " et vaut "+ str(max))

#maxFT(int(input("Trouver le max pour les nombres de 1 à : ")))

def maxAlt():  
    max = 0
    for i in range(1,1001):
        if altMax(i)>max:
            max = altMax(i)
            maxIndex = i
    print("Le temps de vol maximum pour les nombres de 1 à 1000 est "+ str(maxIndex)+ " et vaut "+ str(max))

maxAlt()