import string



#	f = open(filename)
#	variabel = f.read()
#	f.close()
#	liste = variabel.split('\n')
#	print(liste)
#	my_dictionary = {}
#	while liste:
#		if liste[0] in my_dictionary:
#			midlertidig = my_dictionary[liste[0]]
#			print(midlertidig)
#			midlertidig += 1
#			print(midlertidig)
#			my_dictionary[liste[0]] = midlertidig
#			print(my_dictionary)
#			liste.pop(0)
#		else:
#			my_dictionary[liste[0]] = 1
#			liste.pop(0)
#		print(my_dictionary)
#	return my_dictionary






def read_from_file(filename):
	f = open(filename,'r')
	variabel=f.read()
	f.close()
	return variabel

def remove_symbols(text):
	validchars = string.ascii_letters + ' '
	clean_string = ''.join(a for a in text if a in validchars)
	lower_clean_string = clean_string.lower()
	return lower_clean_string

def count_words(filename):
	variabel = read_from_file(filename)
#	print(variabel)
	variabel = remove_symbols(variabel)
	liste=variabel.split()
#	print(liste)
	my_dictionary = {}
	while liste:
		if liste[0] in my_dictionary:
			midlertidig=1+my_dictionary[liste[0]]
			my_dictionary[liste[0]]=midlertidig
			liste.pop(0)
		else:
			my_dictionary[liste[0]]=1
			liste.pop(0)
	return my_dictionary



bible_dict = count_words('BIBLE.txt')
for word, value in bible_dict.items():
	print(word,value)

