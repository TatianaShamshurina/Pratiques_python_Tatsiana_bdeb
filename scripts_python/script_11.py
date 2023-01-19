str1="      Salut toute le monde!  "
print(len(str1))

str2 = str1.strip()
print(str2)
print(str1.strip())
print(len(str1.strip()))        #enlever des espases au debut et a la fin

str3=str2.lstrip()
print(str3)                     #enlever des espaces au debut
str3=str1.rstrip()
print(str3)                     #enlever des espaces au debut

str4 ="***Salut**toute**monde!***"
print(str4)

str5 = str4.strip("*")
print(str5)
print(len(str4))

print(str4.replace("*","%"))        #remplacer * par un autre symbol

str6="SalUt tOoute Le monde!"
print(str6.lower())                 #tout minuscules
print(str6.upper())                 #tout majuscules

str7="SalUt tOoute Le monde monde monde!"
print(str7.count("monde"))          #count le mot qui se repete(combien fois ce mot)

print(str7.startswith("SalUt"))     #le mot se commence par ...

print(str7.startswith("Salut"))
print(str7.endswith("SalUt"))       #le mot se termine par ...

print(str7.split())                 #split par default avec ;

str8="SalUt-tOoute-Le-monde-monde-monde!"
print(str8.split("-"))              #split par default avec deliminateur -