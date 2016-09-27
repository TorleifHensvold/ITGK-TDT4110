#a)
n=0
for i in range (1,101):
    n=i+n
    #print(n)
print('Summen av tallene fra og med 1 til og med 100 er:',n)

#b)
print('\nVi finner produktet av 1*2*3*...*n, frem til produktet er større enn 1000,'
      '\nog avslutter med å inkludere det produktet.\n')
i=1
n=1
o=0
while n < 1000:
    n=n*i
    o+=1
    i+=1
    #print(i,'\n', n)
print('Løkka kjørte', o, 'ganger, og produktet ble:', n, '\n\n')

#c)
brukersvar=0
while brukersvar != 12:
    brukersvar=int(input('Hva er 3*4?\n'))
if brukersvar == 12:
    print('Det er riktig, svaret er:', brukersvar)
