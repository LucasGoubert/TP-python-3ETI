def mesImpots():
    s = int(input("Quel est votre revenu : "))
    p1=10084
    p2=25710
    p3=73516
    p4=158122
    impot =0
    if s<=p1:
        return impot
    if s>p4:
        impot = (s-p4+1)*45/100
        impot += (p4-p3+1)*41/100
        impot += (p3-p2+1)*30/100
        impot += (p2-p1+1)*11/100
        return impot
    if s>p3:
        impot = (s-p3+1)*41/100
        impot += (p3-p2+1)*30/100
        impot += (p2-p1+1)*11/100
        return impot
    
    if s>p2:
        impot = (s-p2+1)*30/100
        impot += (p2-p1+1)*11/100
        return impot
    
    if s>p1:
        impot = (s-p1+1)*11/100
        return impot
    
print("T'es impôts sont de : " + str(mesImpots()) + "€")