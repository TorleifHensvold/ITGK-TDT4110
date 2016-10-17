liste = [1,4,6,2,8,4,10,15,18]

def isSixAtEdge(liste):
    if 6==liste[0] or 6==liste[len(liste)-1]:
        return 1
    else:
        return 0

def average(liste):
    gjennomsnitt=(sum(liste)/len(liste))
    return gjennomsnitt

def median(liste):
    sortert=sorted(liste)
    #print(sortert)
    midterste=(int((len(sortert)-1)/2))          #fordi vi fikk oppgitt at lista var odde, kan jeg ta
                                                #halvparten av lengden-1 delt på to, pluss 1 for å finne indeks
                                                #det midterste elementet
    return sortert[midterste]


print(isSixAtEdge(liste))
print(average(liste))
print(median(liste))