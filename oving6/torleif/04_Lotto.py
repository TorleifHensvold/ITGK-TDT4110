import random



def number_gen():
    liste=[]
    for i in range (1,35):
        liste.append(i)
    return liste

numbers=number_gen()

myGuess=[5,10,11,14,27,30,32]

def drawing_numbers(liste,n):
    liste1=liste
    liste2=[]
    for i in range (0,n):
        indeks=random.randint(0,len(liste1)-1)
        #trekk ut n tilfeldige tall av liste
        liste2.append(liste1.pop(indeks))
        #legg til i liste for trekking
        #print(liste1,liste2)
    #return liste og liste 2
    return liste1,liste2

#drawing_numbers(numbers,7)
#print(numbers)

def trekning():
    resterende,vinnertall=drawing_numbers(number_gen(),7)
    asda,ekstratall=drawing_numbers(resterende,3)
    #print('Vinnertallene er:',vinnertall,'og ekstratallene er:',ekstratall)
    return vinnertall,ekstratall

def compList(liste,compListe):
    akkumulator=0
    for i in range (0,len(compListe)):
        #print(len(compListe))
        if compListe[i] in liste:
            akkumulator+=1
            #print(compListe[i])
    return akkumulator

#sjekkliste1=[1,3,5,7,9,2,4]
#sjekkliste2=[1,4]

#compList(sjekkliste1,sjekkliste2)

def premiering(tippekupong):
    vinnertall,ekstratall=trekning()
    antall_rette=compList(vinnertall,tippekupong)
    antall_ekstratall=compList(ekstratall,tippekupong)
    if antall_rette == 7:
        return 2749455
    elif antall_rette ==6 and antall_ekstratall == 1:
        return 102110
    elif antall_rette == 6:
        return 3385
    elif antall_rette == 5:
        return 95
    elif antall_rette == 4 and antall_ekstratall == 1:
        return 45
    else:
        return 0


def main():
    for i in range (0,30):
        premie=premiering(myGuess)
        print('Du vant', premie,'kroner denne gangen')


main()
print('--------------------------------------------------')

def million_tipping():
    akkumulator=0
    kostnad=0
    for i in range (0,1000000):
        premie=premiering(myGuess)
        akkumulator+=premie
        kostnad+=5
    print('Etter 1 000 000 tippinger har du vunnet', akkumulator, 'og det har kostet', kostnad,'kroner.')



million_tipping()