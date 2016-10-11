alder = int(input('Kor gamal er du? '))
def pris(x):
      if x < 5 or x > 60:
           penger = 0
      elif x < 21:
           penger = 20
      elif x < 26:
           penger = 50
      else:
           penger = 80
      return penger

Kostnad=pris(alder)
print('Du må betale ' , str(Kostnad) , 'kroner for din billett.') 
          

      
