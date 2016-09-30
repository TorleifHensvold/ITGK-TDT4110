

def GeometriskWhile(number, r):
    i=0
    accumulator=0
    while i <= number:
        accumulator = accumulator + (r**i)
        #print(i, accumulator, sep='\t')
        i+=1
    return accumulator

def mainGeoWhile():
    print('a)')
    print('Summering av rekken r^0+r^1+r^2+...+r^n for r mellom [-1,1]')
    r=float(input('Hva ønsker du å bruke som r: '))
    number=int(input('Hva ønsker du å bruker som n: '))
    summ1=GeometriskWhile(number, r)
    print('Summen av rekken er', summ1, '\n')


mainGeoWhile()


def GeometriskTol(tol, r):
    grenseverdi = (1/(1-r))
    differanse = 1000
    i=0
    accumulator=0
    print('grenseverdi:', grenseverdi)
    while differanse > tol:
        #prevAccumulator = accumulator
        accumulator = accumulator + (r**i)
        differanse = (r**i)
        #print(i, prevAccumulator, accumulator, differanse, sep='\t')
        i+=1
    verdisprik=grenseverdi-accumulator
    return accumulator, i, verdisprik


def mainGeoTol():
    print('b)')
    print('Summering av rekken r^0+r^1+r^2+...+r^n for r mellom (-1,1)')
    r = float(input('Hva ønsker du å bruke som r: '))
    tol = float(input('Hva ønsker du å bruke som toleranse: '))
    summ2, iterasjoner, verdisprik = GeometriskTol(tol, r)
    print('Summen av rekken er', summ2, '\n')
    print('For å være innenfor toleransegrensen', tol, 'kjørte løkken', iterasjoner, 'ganger.')
    print('Da var differansen mellom lim og kalkulert verdi:', verdisprik)


mainGeoTol()