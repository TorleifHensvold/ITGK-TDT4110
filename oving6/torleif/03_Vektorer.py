import math


def vektor_inndata():
    vektor=[]
    #print('Skriv inn vektoren:', end='')
    addisjon1,addisjon2,addisjon3=input('Skriv inn vektoren (komma skiller koordinatene): ').split(',')
    print(addisjon1,addisjon2,addisjon3)
    addisjon1, addisjon2, addisjon3=float(addisjon1),float(addisjon2),float(addisjon3)
    vektor=[addisjon1,addisjon2,addisjon3]
    #print(vektor)
    return vektor
    #print()

#vektor_inndata()

def printToScreen(vektor):
    print('Vektoren er:', vektor)

#printToScreen()

def vektorSkalering(vektor, skalar):
    liste=[]
    for i in range (0,len(vektor)):
        liste.append(vektor[i]*skalar)
    #print(liste)
    return liste

#vektorSkalering([1,3,5],2)

def vektorlengde(vektor):
    liste=[]
    for i in range (0,len(vektor)):
        liste.append(vektor[i]**2)
    summering=sum(liste)
    lengde=math.sqrt(summering)
    return lengde

#print(vektorlengde([2,0,0]))

def forholdstall(lengde1,lengde2):
    return lengde1/lengde2

def prikkprodukt(vec1,vec2):
    liste=[]
    for i in range (0,len(vec1)):
        liste.append(vec1[i]*vec2[i])
    summen=sum(liste)
    return summen

def main():
    vec1=vektor_inndata()
    printToScreen(vec1)
    skalar=float(input('Legg inn en skalar: '))
    vec2=vektorSkalering(vec1,skalar)
    printToScreen(vec2)
    print('Lengden av originalvektoren er: ',vektorlengde(vec1),'\nLengden av den skalerte vektoren er: ', vektorlengde(vec2), sep='')
    print('Den skalerte vektoren er ', forholdstall(vektorlengde(vec2),vektorlengde(vec1)), ' ganger lengden til originalvektoren.', sep='')
    print('Prikkproduktet av originalvektoren og den skalerte er:',prikkprodukt(vec1,vec2))

main()