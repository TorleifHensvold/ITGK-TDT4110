
# vim:set fileencoding=latin-1:
import random # Importerer modulen random (generere tilfeldige tall)

def pick_sentence(sentences):
  return sentences[random.randint(0, len(sentences)-1)]

def print_sentence(a,b,c):
  print(a, ' ' ,b, c)
 

def intro_text():
    for i in range(19):
        print( )
    print('Hei, eg heiter Eliza og vil gjerne snakke med deg.')
    print('Ikkje start svar med stor bokstav og bruk heile setningar.')
    print('Skriv "hade'' viss du vil avslutte samtalen')
    print ( )
 

def main():
  answer = "ikke hade" # Sørger for at while-løkka kjører første gang
 
  questions = ['Hva gjør du', 'Hvordan går det', 'Hvorfor heter du',
              'Liker du å hete', 'Føler du deg bra', 'Hva har du gjort idag',
              'Hva tenker du om framtida', 'Hva gjør deg glad', 'Hva gjør deg trist']
 
  follow_ups = ['Hvorfor sier du', 'Hva mener du med', 'Hvor lenge har du sagt',
               'Hvilke tanker har du om', 'Kan du si litt mer om',
               'Når tenkte du første gang på']

  responses = ['Fint du sier det', 'Det skjønner jeg godt', 'Så dumt da', 'Føler meg også sånn',
              'Blir trist av det du sier', 'Så bra', 'Du er jammen frekk']

  print(intro_text())

  navn =  input('Kva heiter du? ')
 
  while answer != "hade":

        spørmål = pick_sentence(questions)
        print_sentence(spørmål , navn , '?')    

        answer = input('Svar: ')

        if answer != 'hade':
          follow = pick_sentence(follow_ups)
          print_sentence(follow, answer, '?')
          answer = input('Svar: ')

        if answer != 'hade':
           tilbakemld = pick_sentence(responses)
           print_sentence(tilbakemld, navn, '.')
 


