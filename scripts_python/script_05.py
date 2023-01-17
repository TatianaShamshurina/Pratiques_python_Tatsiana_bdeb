"""def carre(nombre):
    '''Cette fonctionne prend un nombre et return nombre au carre'''    #cest une documentation
    return nombre **2
print(carre(4))
print(carre.__doc__)
print(print.__doc__)"""

def paire_impaire(nombre):
    ''' Cette fonctionne prend un nombre et return si le nombre est paire au impaire'''
    if(nombre % 2 == 0):
        return ("Nombre est pair")
    else:
        return ("Nombre est impair")
#print(parite(6))
#print(parite(7))
#print(parite.__doc__)
print(paire_impaire(8))
print(paire_impaire(9))
print(paire_impaire.__doc__)
print(print.__doc__)
