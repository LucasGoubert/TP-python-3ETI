from datetime import datetime

def isBissextile(year):
    if (year%100!=0 and year%4==0) or year%400==0:
        return True
    else:
        return False

def dayOnMonth(month):
    if (month<1 or month>12):
        return "Ce mois n'existe pas !"
    elif (month==4 or month==6 or month==9 or month==11):
        return 30
    elif (month==2):
        return 29
    else:
        return 31

def dateValid(dateStr):
    date = list(map(int,dateStr.split("/")))

    if date[1]<1 or date[1]>12 :
        return False
    if date[1]==2:
        if isBissextile(date[2])==True and date[0]>28:
            return False    
        if isBissextile(date[2])==False and date[0]>29:
            return False
        else:
            return True
    if date[1] > dayOnMonth(date[1]) or date[1]<1:
        return False
    else:
        return True

print(dateValid(input("Date en format dd/mm/yy : ")))
