

def count_coins(coins):
    return sum(coins)

def mynt(numbers,kroner):
    antall=int(((numbers - numbers % kroner) / kroner))
    rest=numbers-antall*kroner
    return antall, rest

def min_mynter(numbers):
    tjuekroner,numbers=mynt(numbers,20)
    tikroner,numbers=mynt(numbers,10)
    femkroner,numbers=mynt(numbers,5)
    enkroner,numbers=mynt(numbers,1)
    return [tjuekroner,tikroner,femkroner,enkroner]

def num_coins(numbers):
    liste=[]
    for i in range (0,len(numbers)):
        liste.append(min_mynter(numbers[i]))
        #print(liste)
    return liste

#print (mynt(43,20))

liste=[12,23,34,45,56,67,78,89,90,98,87,76,65,54,43,32,21]

def main():
    antall_mynter=num_coins(liste)
    for i in range (0,len(liste)):
        print('For', liste[i],'er det minste antall mynter',antall_mynter[i])





main()