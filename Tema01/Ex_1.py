from unicodedata import numeric
sirul = input("Introdu sirul dorit: ")
lista = list(sirul)
n = 0
s = 0
for i in lista:
    if i.isdigit():
        n += 1
    else:
        s += 1
if s == 0:
    nume = input("Introdu numele tau: ")
    print(f"Sirul de caractere de tip numeric a fost gasit de {nume}")
elif n != 0 and s !=0:
    nume = input("Introdu numele tau: ")
    print(f"Sirul mixt de caractere a fost gasit de {nume}")
elif n == 0:
    nume = input("Introdu numele tau: ")
    print(f"Sirul de caractere de tip string a fost gasit de {nume}")