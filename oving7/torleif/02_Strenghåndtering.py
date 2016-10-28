



def checkEqual(streng1,streng2):
    equal=1
    if len(streng1)>=len(streng2):
        a=len(streng1)
    else:
        a=len(streng2)
    i=0
    while equal:
        if streng1[i]!=streng2[i]:
            equal=0
        i+=1
        if i>a-1:
            return equal
    return equal

def printToScreenEqual(streng1,streng2):
    a=checkEqual(streng1,streng2)
    if a:
        print('True')
    else:
        print('False')


streng1='hei'
streng2='hallo'
streng3='hallo'

printToScreenEqual(streng1,streng2)
printToScreenEqual(streng2,streng3)

def reversed_word(streng):
    a=len(streng)
    liste=[]
    b=''
    for i in range (1,a+1):
        liste.append(streng[-i])
    for i in range (0,a):
        b=b+str(liste[i])
    return b

print(reversed_word('Morna Jens'))

def check_palindrome(streng):
    if streng == reversed_word(streng):
        return 1
    else:
        return 0

print(check_palindrome('abba'))

def contains_string(streng1,streng2):
    index=0
    if streng2 in streng1:              #Sjekker om streng 2 er i streng 1
        for i in range (0,len(streng1)):
            for j in range (0,len(streng2)):
                if streng1[i]==streng2[j]:
                    


#sjekke om første av streng 2 er i indeks av streng1.
#Hvis første av streng 2 er i indeks av streng1, sjekk om indeks+1 av streng 2 er i indeks+1 av streng1. Rep




streng1='pepperkaker'
streng2='per'
streng3='hei'

contains_string(streng1,streng2)

