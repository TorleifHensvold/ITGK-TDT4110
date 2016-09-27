#doble løkker b
test=int
tall=int
q=0
prim=bool
for tall in range(2,100000):
    prim=True
    for test in range(2,tall):
        sjekk=tall%test
        if(sjekk==0 and test!=tall):
            prim=False       
    if(prim==True):
        print(tall)
        q=q+1
print(q)

            

