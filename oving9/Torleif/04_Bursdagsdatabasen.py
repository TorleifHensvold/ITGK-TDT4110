


birthdays = {
"22 nov": ["Lars", "Mathias"],
"10 des": "Elle ",
"30 okt": ["Veronica", "Rune"],
"12 jan": "Silje",
"31 okt": "Willy",
"8 jul": ["Brage", "Øystein"],
"1 mar": "Nina"
}

def add_birthday_to_date(date, name):
	try:
		birthdays[date].append(name)
	except Exception as err:			#Legger feilmeldingen inn som var slik at den kan skrives ut.
		print(err)
		print('Det gikk ikke å bare legge til en person til.\n'
			  'Prøver å løse problemet')
		try:							#Prøver å lage en liste med personer som legges til på datoen
			liste=[]
			liste.append(birthdays[date])
			#print(liste)
			liste.append(name)
			birthdays[date]=liste
			print('Løste problemet.')
		except Exception as err2:		#Legger feilmeldingen inn som var slik at den kan skrives ut.
			print(err2)
			try:						#Prøver å legge til en ny dato personer kan ha bursdag på.
				birthdays[date]=name
				print('Løste Problemet')
			except Exception as err3:	#Legger feilmeldingen inn som var slik at den kan skrives ut.
				print(err3)


add_birthday_to_date("12 jan", "Sindre")
add_birthday_to_date("9 feb", "Lillian")

for i in birthdays:
	print(i,'\t:\t',birthdays[i])