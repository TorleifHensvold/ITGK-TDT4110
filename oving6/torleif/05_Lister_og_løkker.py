
def number_gen(start, stopp):
    list=[]
    for i in range (start,stopp+1):
        list.append(i)
    return list

number_list=number_gen(0,99)

#print(number_list)

def ti_og_tre_summering():
    akkumulator=0
    for i in range (0,len(number_list)):
        if number_list[i]%3 == 0 or number_list[i]%10 == 0:
            akkumulator+=number_list[i]
            #print(number_list[i],akkumulator)
    return akkumulator

print(ti_og_tre_summering())

def venstreflytt_partall(liste):
    modifisert=[]
    for i in range (0,len(liste)):
        if i % 2 == 0:
            modifisert.append(liste[i+1])
            modifisert.append(liste[i])
            #print(modifisert)
    return modifisert

#print (venstreflytt_partall(number_list))

def reverser(liste):
    modifisert=[]
    for i in range (0,len(liste)):
        modifisert.append(liste[len(liste)-1-i])
        #print(modifisert)
    return modifisert

reversed_list=reverser(venstreflytt_partall(number_list))
print(reversed_list)