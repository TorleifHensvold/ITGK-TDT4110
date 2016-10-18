number_list=[i for i in range(100)]
sum = 0
for element in number_list:
    if element % 3 == 0 or element % 10 == 0:
        sum = sum + element
print(sum)
for i in range(len(number_list)):
    if i % 2 == 0:
        number_list[i] = i + 1
    else:
        number_list[i] = i-1

reversed_list = []
for i in range(len(number_list)):
    reversed_list.append(number_list[99-i])

print(reversed_list)
    
