
def generate_list(a,b):
    list=[]
    for i in range (a,b):
        list.append(i)
    return list

my_first_list=generate_list(1,7)

print('A:\n',my_first_list)

print('\nB')

#print(len(my_first_list))
print(my_first_list[len(my_first_list)-1])

my_first_list[4]='+'



my_second_list=my_first_list[(len(my_first_list)-3):(len(my_first_list))]
print('\nC')
print(my_second_list, 'er lik 10.')