#a) Skriv en funksjon som tar inn verdier x og y, og deretter returnerer verdien til x*y.

#b) Skriv en funksjon som tar inn et argument og så skriver det ut til skjermen.

#c) Skriv en funksjon som alltid returnerer tallet 2. (Tar ikke inn noen argumenter)

#Husk å skrive ut svarene til konsoll, slik at du ser at koden din gjør det den skal.

def xy_gang(x,y):
    return x*y

def arg_print(arg):
    print(arg)

def to_returner():
    return 2

def main():
    x=int(input('Skriv inn et heltall: '))
    y=int(input('Skriv inn et annet heltall: '))
    arg=xy_gang(x,y)
    arg_print(arg)
    print(to_returner())


main()