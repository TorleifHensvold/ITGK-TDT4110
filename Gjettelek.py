
import random
bers=int(input('what is the biggest number?'))
tilfeldig_tall = random.randint(1,bers)
piss=True
while(piss==True):
    svar=int(input('make a guess bitch'))
    if(svar>tilfeldig_tall):
        print('lol, too high')
    if(svar<tilfeldig_tall):
        print('lol, too low')
    if(svar==tilfeldig_tall):
        print('jepp, correct number was', tilfeldig_tall)
        piss=False

    
    
