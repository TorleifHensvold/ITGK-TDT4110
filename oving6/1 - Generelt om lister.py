my_first_list = [1,2,3,4,5,6]
print(my_first_list[5]) #fordi det er nullindeksert
my_first_list[4] = 'pluss'
my_second_list =[my_first_list[x+3] for x in range(0,3)]
print(my_second_list)
print('er lik 10') #korleis få desse på same linje?
