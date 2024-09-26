lista = tuple([7, 8, 9, 2, 3, 1, 4, 10, 5, 6])
sortata = list(lista)
sortata.sort()
lista=list(lista)
print(f'Lista sortata ascendent este: {sortata}')
print(f'Lista sortata descendent este: {sortata[::-1]}')
par = []
impar = []
multipli = []
for i in sortata:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

    if i % 3 == 0:
        multipli.append(i)
print(f'Lista de termeni pari: {par} \nLista de termeni impari {impar} \nLista de multipli de 3 este: {multipli}')
print(f'Lista initiala este: {lista}')
