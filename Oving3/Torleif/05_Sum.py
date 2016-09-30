
#Summere Xi = 1/(i**2) for i=1,2,...,N

def ForSum(number):
    accumulator=0
    for i in range(1, number+1, 1):
        accumulator = accumulator+(1/(i**2))
        #print(i, accumulator, (1/(i**2)))
    return accumulator




def mainForSum():
    print('A)\nDenne tar inn antall iterasjoner og utfører kalkulasjonen.')
    number=int(input('Skriv inn antall iterasjoner: '))
    summ=ForSum(number)
    print('Etter', number, 'iterasjoner ble summen', format(summ, '.2f'), '\n')

mainForSum()


def WhileSum(tol):
    i=1
    accumulator=0
    while 1/(i**2) > tol:
        prevAccumulator = accumulator
        accumulator = accumulator + (1/(i**2))
        print('i\t prevAccumulator\t Accumulator\t 1/i**2')
        print(i, prevAccumulator, accumulator, (1/(i**2)), sep='\t')
        i+=1
    return accumulator


def mainWhileSum():
    print('A)\nDenne tar inn toleransen og utfører kalkulasjonen.')
    tol = float(input('Skriv inn toleransen: '))
    summ2 = WhileSum(tol)
    print('Med toleranse', tol, 'ble summen', format(summ2, '.2f'), '\n')


mainWhileSum()