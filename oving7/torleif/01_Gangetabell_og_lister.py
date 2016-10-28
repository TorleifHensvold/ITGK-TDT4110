

def number_gen(start,stopp):
    liste=[]
    for i in range (start,stopp+1):
        liste.append(i)
    return liste

liste=number_gen(1,20)

def separate(numbers,threshold):
    numbers=sorted(numbers)
    minListe=[]
    maxListe=[]
    for i in range (0,len(numbers)):
        if numbers[i] < threshold:
            minListe.append(numbers[i])
        #print(minListe)
        if numbers[i] >= threshold:
            maxListe.append(numbers[i])
    #print(minListe)
    #print(maxListe)


separate(liste,5)

def n_gangen(n,m):
    liste=[]
    for i in range (1,m+1):
        liste.append(i*n)
    return liste

#print(n_gangen(2,4))

def multiplication_table(n):
    liste=[]
    for i in range (1,n+1):
        liste.append(n_gangen(i,n))
    return liste

#print(multiplication_table(5)format())

def gangetabell_print_to_screen(n):
    gangetabellen=multiplication_table(n)
    for i in range (0,n):
        print(gangetabellen[i])

gangetabell_print_to_screen(5)

