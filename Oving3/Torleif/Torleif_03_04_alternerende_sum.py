#Hvis du ikke skjønner det, sorry. Var litt hodebry, så du får tenke litt selv også :D


def addisjon(number):
    accumulator=0
    for i in range(1,number+1):
        if i%2:
            accumulator = accumulator + i**2#adder med -(i^2)
        else:
            accumulator = accumulator - i**2#adder med i^2
        #print(i, accumulator)
    return accumulator

def intro():
    print('A)')
    print('Vi adderer 1^2-2^2+3^2-4^2...+-n^2')
    number=int(input('Hvor mange ledd ønsker du? '))
    sum=addisjon(number)
    print('Summen av', number, 'ledd ble', sum)
    print()


intro()

def addisjon2(k):
    accumulator=0
    i=0
    while accumulator <= k:
        prevAccumulator=accumulator
        i=i+1
        if i%2==0:
            accumulator = accumulator - i**2#adder med -(i^2)
        else:
            accumulator = accumulator + i**2#adder med i^2
        #print(prevAccumulator, i, accumulator)
        #if accumulator > k:
            #accumulator=prevAccumulator
            #print(accumulator)
        if accumulator < -1000:
            break
        elif accumulator > 1000:
            break
    accumulator=prevAccumulator
    i=i-1
    #print(accumulator)
    return accumulator, i

def intro2():
    print('B)')
    print('Vi adderer 1^2-2^2+3^2-4^2...+-n^2')
    k=int(input('Hvilken sum ønsker du å avslutte før summen er større enn? '))
    sum,ledd=addisjon2(k)
    print('Summen av leddene under eller lik verdien', k, 'er',sum,'\nVi hadde', ledd, 'ledd i utregningen.')

intro2()
