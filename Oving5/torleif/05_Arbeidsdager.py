dager=['mandag','tirsdag','onsdag','torsdag','fredag','lørdag','søndag']

def isLeapYear(year):
    if year%400==0:
        return 1
    elif year%100==0:
        return 0
    elif year%4==0:
        return 1
    return 0

def weekday_newyear(year):
    ukedag=0
    aar=1900
    while aar < year:
        dag=1+isLeapYear(aar)   #Sjekker om vi må legge til 1 eller 2 dager
        ukedag+=dag             #setter ukedag for 1.jan til forrige års+dag
        aar+=1                  #øker årstallet
        ukedag%=7               #finner om det er utenfor antall dager i en uke, og hopper til
                                #neste uke hvis det er slånn.
    return aar, ukedag

def oppgave_A():
    print('A')
    for i in range(1900,1920):
        aar,dagger=weekday_newyear(i)
        dagger=dager[dagger]
        print(aar, ':', dagger)

oppgave_A()

def is_workday(day):
    if day<5:
        return 1
    else:
        return 0

def workdays_in_year(year):
    aar,starting_day=weekday_newyear(year)  #må ha aar først for å få riktig starting day.
    leapyear=isLeapYear(year)               #Sjekker om året er 365 eller 366 dager langt.
    counter=0                               #holder rede på arbeidsdager
    for i in range (0,365+leapyear):
        if is_workday(starting_day):        #hvis det er mandag til og med fredag gjør den det under
            counter+=1                      #legg til en på arbeidsdagscounter
        starting_day+=1                     #gjør klart til å sjekke neste dag.
        starting_day=starting_day%7         #Passer på at dagene er i [0 , 7]
        #print(starting_day, dager[starting_day], leapyear, counter)
    return counter

def oppgave_b():
    print('B,C')
    year=1900
    counter=workdays_in_year(year)
    print(year,'har',counter,'arbeidsdager.')

workdays_in_year(1900)
oppgave_b()

def oppgave_c():
    print('CCC')
    for i in range (1900,1920):
        counter=workdays_in_year(i)
        print(i, 'har', counter, 'arbeidsdager.')

oppgave_c()