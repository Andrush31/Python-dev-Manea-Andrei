cuvant = "onomatopee"
cuvant_de_inlocuit = ""
for i in cuvant:
    if i != cuvant[0] and i!= cuvant[-1]:
        cuvant_de_inlocuit = cuvant_de_inlocuit + "_"
    else:
        cuvant_de_inlocuit = cuvant_de_inlocuit + i
print(cuvant_de_inlocuit)
nr_vieti = 7
while cuvant_de_inlocuit != cuvant and nr_vieti != 0:
    caracter_cerut = input('Alege o litera:')
    if caracter_cerut in cuvant:
        lista_cuvant_de_inlocuit = list(cuvant_de_inlocuit)
        for i, v in enumerate(cuvant):
            if v == caracter_cerut:
                lista_cuvant_de_inlocuit[i] = caracter_cerut
                cuvant_de_inlocuit = "".join(lista_cuvant_de_inlocuit)
        print(cuvant_de_inlocuit)
    else:
        nr_vieti -= 1
    print(nr_vieti)

if nr_vieti == 0:
    print("ai pierdut")
