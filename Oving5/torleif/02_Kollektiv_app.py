#I forbindelse med en kul app du er i ferd med å lage for brukere av kollektivtrafikken i
# byen du har flyttet til, skal du lage en enkel funksjon som returnerer hvilken billettpris
# brukeren skal betale utifra ett input-parameter; alder.

#Prisen er bestemt utifra følgende tabell:

#Kategori
#Alder(år)
#Pris(kr)
#Småbarn	< 5	Gratis
#Barn	5-20	20
#Student	21-25	50
#Voksen	26-60	80
#Honør	> 60	Gratis

def alder(x):
    if x<0:
        return 'Du er ikke født enda!'
    elif x<5:
        return 'Billetten er gratis.'
    elif x<=20:
        return 'Billetten koster 20 kroner.'
    elif x<=25:
        return 'Billetten koster 50 kroner.'
    elif x<=60:
        return 'Billetten koster 80 kroner.'
    elif x>60:
        return 'Billetten er gratis'

def main():
    x=int(input('Hvor gammel er du? '))
    print(alder(x))

main()