



def write_to_file(data):
	f = open('my_file.txt','w')
	f.write(data)
	f.close()

def read_from_file(filename):
	f = open(filename,'r')
	variabel=f.read()
	f.close()
	return variabel

def file_check():
	try:
		f = open('my_file.txt','r')
		sefd=f.read()
		f.close()
	except:
		write_to_file('')

def main():
	file_check()
	print('Denne funksjonen lar deg velge om du skal skrive til en fil eller lese fra en fil')
	print('Skriv "done" når du er ferdig')
	brukersvar=input('Vil du skrive eller lese? ')
	while brukersvar.lower() != 'done':
		if brukersvar.lower() == 'skrive':
			innputt=input('Hva vil du skrive til filen? ')
			write_to_file(innputt)
			brukersvar = input('Vil du skrive eller lese? ')
		elif brukersvar.lower() == 'lese':
			print(read_from_file('my_file.txt'))
			brukersvar = input('Vil du skrive eller lese? ')
		else:
			print('Jeg er bare en dum datamaskin, skriv nøyaktig. ')
			brukersvar=input('Vil du skrive eller lese? ')



main()



