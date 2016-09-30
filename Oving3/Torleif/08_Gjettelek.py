import random

n=1
m=100
tilfeldig_tall = random.randint(n,m)
svar = m+1

while svar != tilfeldig_tall:
    if svar < m+1:
        if svar < tilfeldig_tall:
            print('Tallet du skal finne er større.')
        elif svar > tilfeldig_tall:
            print('Tallet du skal finne er mindre.')
    print('Gjett et heltall mellom', n, 'og', m, end=':')
    svar = int(input(' '))
    #print(tilfeldig_tall)
if svar == tilfeldig_tall:
    print('Du fant det riktige tallet;', tilfeldig_tall)


#Hvis man ønsker at brukeren skal kunne bestemme intervallet kan man be brukeren om
#m=int(input(******)) og
#n=int(input(******)) før man starter løkka.