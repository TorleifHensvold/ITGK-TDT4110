

#a)
print('A)')
my_family = {}

def add_family_member(role,name):
	if role not in my_family:		#A)
		my_family[role] = [name]
	else:							#B)
		mellom=my_family[role]
		mellom.append(name)
		my_family[role]=mellom
	#print(my_family)


add_family_member('bror','Johannes')
#print(my_family)
add_family_member('onkel','Roar')
#print(my_family)
add_family_member('onkel','Erik')
#print(my_family)
add_family_member('tante','Lilian')
#print(my_family)
add_family_member('tante','Torhild')
#print(my_family)
add_family_member('onkel','Haakon')
#print(my_family)
add_family_member('onkel','Arne')
#print(my_family)

#C)
for i in my_family:				#Her ligger det noe humbug! #Fikset!
	if len(my_family[i]) == 1:
		print(i,':\n', ''.join(my_family[i]),sep='')
		print('')
	else:
		print(i,':',sep='')
		for j in range (len(my_family[i])):
#			print(len(my_family[i]))
			print(my_family[i][j])
		print('')