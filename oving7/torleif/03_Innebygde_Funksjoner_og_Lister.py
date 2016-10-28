import random



def random_num(antall,fra,tilOgMed):
    liste=[]
    for i in range (0,antall):
        liste.append(random.randint(fra,tilOgMed))
    return liste



random_numbers=random_num(100,0,9)

#print(random_numbers)
#print(len(random_numbers))

def finding_2(liste,tall=2):
    akkumulator=0
    for i in range (0,len(liste)):
        if liste[i]==tall:
            akkumulator+=1
    return akkumulator

print('Summen av de tilfeldige tallene er: ', sum (random_numbers))

sorted_random_numbers=sorted(random_numbers)

#print(sorted_random_numbers)

def antall(liste,minste_tall,storste_tall):
    teller=[]
    for i in range (minste_tall,storste_tall+1):
        teller.append(finding_2(liste,i))
    return teller

#print(antall(sorted_random_numbers,0,9))

def typetall(liste,minste_tall,storste_tall):
    teller=antall(liste,minste_tall,storste_tall)
    maksfrekvens=max(teller)
    alfa=[]
    for i in range (0,len(teller)):
        if teller[i]==maksfrekvens:
            alfa.append(i)
            #print(alfa)
    return alfa

tall=['nulltall','entall','totall','tretall','firetall','femtall','sekstall','syvtall','åttetall','nitall']
typisk=typetall(sorted_random_numbers,0,9)
fikser=''
n=1
for i in range (0,len(typisk)):
    fikser+=str(tall[typisk[i]])
    if len(typisk)>n:
        fikser+=' og '
    n+=1

print('Det var flest ', fikser)

for i in range (0,len(sorted_random_numbers)):
    print(sorted_random_numbers[-(i+1)],end=',')
