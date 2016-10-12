


def forenkling(a,b):
    while b!=0:
        gammel_b=b
        b=a%b
        a=gammel_b
        #print(a,b)
    return a

print(forenkling(30,20))
print(forenkling(10,2))

def gcd(a,b):
    a=forenkling(a,b)
    return a


def reduce_fraction(a,b):
    divisor=forenkling(a,b)
    a=int(a/divisor)
    b=int(b/divisor)
    return a,b

def main():
    print('Dette forkorter brøker på formen a/b:')
    a = int(input('Skriv inn et heltall a: '))
    b = int(input('Skriv inn et heltall b: '))
    a,b=reduce_fraction(a,b)
    if a!=b:
        print('Forkortningen av brøken gir: ',a,'/',b,sep='')
    else:
        print('Forkortningen av brøken gir: 1')

main()
