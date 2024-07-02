from random import *
folio=0
def primer_Folio():
    folio=randint(1, 100)
    print(folio)
    return(folio)

folio_resultado=primer_Folio()
print(folio_resultado)
folio_resultado+=1
print(folio_resultado)