


#def number_of_lines(filename):
#	f = open(filename)
#	variabel = f.read()
#	f.close()
#	print(variabel)
#	linjer=0
#	for line in open(filename):
#		linjer+=1
#	print(linjer)
#	return linjer

def antall_linjer(filename):
	f = open(filename)
	variabel = f.read()
	f.close()
	linjer=len(variabel.split('\n'))
	#print(linjer)
	return linjer

#def test(filename):
#	f = open(filename)
#	variabel = f.read()
#	f.close()
#	linjer=variabel.split('\n')
#	print(linjer)
#	return linjer

def number_frequency(filename):
	f = open(filename)
	variabel = f.read()
	f.close()
	liste=variabel.split('\n')
	#print(liste)
	#legge til tallet som pluss 1 på indeksen tallet
	my_dictionary={}
	while liste:
		if liste[0] in my_dictionary:
			midlertidig=my_dictionary[liste[0]]
			#print(midlertidig)
			midlertidig+=1
			#print(midlertidig)
			my_dictionary[liste[0]]=midlertidig
			#print(my_dictionary)
			liste.pop(0)
		else:
			my_dictionary[liste[0]]=1
			liste.pop(0)
			#print(my_dictionary)
	return my_dictionary


def print_to_screen(filename):
	my_dictionary=number_frequency(filename)
	tries = 0
	i=0
	while tries < (len(my_dictionary)):
		if str(i) in my_dictionary:
			print(i,'\t:\t',my_dictionary[str(i)])
			i+=1
			tries+=1
		else:
			i+=1



#test('numbers.txt')
print('Antall linjer i filen "numbers.txt":' ,antall_linjer('numbers.txt'))
#number_of_lines('numbers.txt')
print(number_frequency('numbers.txt'))
print_to_screen('numbers.txt')

