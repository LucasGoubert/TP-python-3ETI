def tricolore(n):
    c = n*n
    for i in str(c):
        if i!="1" and i!="4" and i!="9":
            return False
    return True

#print(tricolore(10))

def allTricolor(N):
    listN = []
    for i in range(1,N+1):
        if tricolore(i)==True:
            listN.append(i)
    return listN


print(allTricolor(1000))