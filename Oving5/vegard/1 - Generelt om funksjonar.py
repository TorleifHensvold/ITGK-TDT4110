def test(x,y):
    produkt = x*y
    return produkt
faktor1= int(input('Kva er den første faktoren? '))
faktor2= int(input('Kva er den andre faktoren? '))
svar = test(faktor1,faktor2)
print(svar)

def skriv(x):
    return x
tekst=str(input('Skriv inn noko. '))
svar = skriv(tekst)
print(svar)

def sau(x):
    return 2
to =int(input('Skriv inn eit kva som helst heiltal. '))
løsning = sau(to)
print(løsning)
