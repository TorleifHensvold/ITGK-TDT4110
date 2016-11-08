

#a)
print('A)')
my_family = {}

def add_family_member(role,name):
	if role not in my_family:		#A)
		my_family[role] = name
	else:							#B)
		mellom=[]
		mellom.append(my_family[role])
		mellom.append(name)
		my_family[role]=mellom
	#print(my_family)


add_family_member('bror','Johannes')
add_family_member('onkel','Roar')
add_family_member('onkel','Erik')
#print(my_family)

#C)
for i in my_family:				#Her ligger det noe humbug!
	if len(i) == 1:
		print(i,':\n', my_family[i],sep='')
	else:
		print(i)
		for j in range (len(i)-1):
			print(my_family[i][j])