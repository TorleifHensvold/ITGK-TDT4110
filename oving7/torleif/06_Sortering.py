


def bubbleSort(list):
	byttet=1
	varListe=[]+list
	#akkumulator=0
	while byttet==1:
		byttet=0
		for i in range (0,len(varListe)-1):
			if varListe[i] > varListe[i+1]:
				varListe[i], varListe[i+1] = varListe[i+1], varListe[i]
				#print(varListe)
				byttet=1
			#akkumulator+=1
		#print(varListe)
	#print(akkumulator)
	return varListe

liste=[6,5,4,2,3,7,9,10,1]

print(bubbleSort(liste))

def selectionSort(list):
	nyListe=[]
	gammelListe=[]+list
	akkumulator=0
	while len(gammelListe):
		maksimal=0
		for i in range (0,len(gammelListe)):
			if gammelListe[i]>maksimal:
				maksimal=gammelListe[i]
				indeks=i
				#print(maksimal, i)
			akkumulator+=1
		nyListe=[gammelListe[indeks]]+nyListe
		gammelListe.pop(indeks)
		#print(nyListe,gammelListe)
	print(akkumulator)
	return nyListe

print(selectionSort(liste))

#Bubblesort er tregere enn Selectionsort, Bubble brukte 72 iterasjoner på listen, Selection brukte 45.
#Begge er trege i forhold til andre utviklede algoritmer.
