
def fibonacci(k):
    a, b, c = 0, 1, 0   #a er her k=0, b er k=1, c er
    for i in range(0,k,1):
        a2=b
        b2=a+b
        c2=a+c
        #print(a, b, c, a2, b2, c2, sep='\t')
        a=a2
        b=b2
        c=c2
        #print(a, b, c, a2, b2, c2, sep='\t')
    return a

def main():
    print('A)')
    k=int(input('Hvilket fibonaccitall ønsker du å vite? '))
    tallet=fibonacci(k)
    print('Det ', k, '. fibonaccitallet er: ', tallet, '\n', sep='')


######################################################################
main()
######################################################################


def fibonacci2(k):
    a, b, c = 0, 1, 0   #a er her k=0, b er k=1, c er
    accumulator = 0
    for i in range(0,k,1):
        a2=b
        b2=a+b
        c2=a+c
        #print(i, a, b, c, a2, b2, c2, sep='\t')
        a=a2
        b=b2
        c=c2
        accumulator = accumulator + a
        #print(i+1, a, b, c, sep='\t')
    return a, accumulator

def main2():
    print('b)')
    k=int(input('Hvilket fibonaccitall ønsker du å vite? '))
    tallet, summ2 = fibonacci2(k)
    print('Det ', k, '. fibonaccitallet er: ', tallet, sep='')
    print('Summen av fibonaccitallene opp til', tallet, 'er:', summ2)


main2()