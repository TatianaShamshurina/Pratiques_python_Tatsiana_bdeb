str1 = "Salut tout le monde!"
print(str1[3])
print(str1[0])
print(str1[-1])
print(str1[-2])
print(len(str1))
print(str1[len(str1)-1])        #==print(str1[-1])

#decoupage de chaine de caractere

print(str1[0:5])        # prendre juste une parti de la phrase
print(str1[6:11])
print(str1[0:])         #toute la phrase
print(str1[6:])

str2 = "sadacada"
print(str2[1::2])       #recupere chaque deuxieme lettre a partir de la premier symbol ==a partir lequel::pas

print(str1[0::3])
print(str1[:6])         #recupere premiers 6 caracteres
print(str1[:-1])        #recupere tout
print(str1[::-1])       #renverser string

str3 = "Tatsiana"
str4 = " Shamshurina"
str5 = str3 + str4
print(str5)
print(str3, str4)
for i in str1:          #afficher chaque symvol = pour chaque i - affiche
    print(i)
for i in enumerate(str1):   #affiche index pour chaque symbol
    print(i)

