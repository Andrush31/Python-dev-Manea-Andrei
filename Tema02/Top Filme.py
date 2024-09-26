lista = [{'nume': 'George',
          'filme': ['Shrek', 'Bond', 'Fight Club']},

         {'nume': 'Cristian',
          'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},

         {'nume': 'Stefan',
          'filme': ['Fight Club', 'Slumdog Millionaire']}]
lista_filme = []
for i in lista:  # lista de referinta
    lista_filme = list(set(lista_filme).union(set(i['filme'])))

zeros_list = [0] * len(lista_filme)
vect_util = [0] * len(lista)

for j, i in enumerate(lista):  # pentru a afla cel mai vizionat film
    lista_2 = list(i['filme'])
    for l, k in enumerate(list(i['filme'])):
        if k in lista_filme:
            zeros_list[lista_filme.index(k)] = zeros_list[lista_filme.index(k)] + 1
    for l in lista_2:
        vect_util[j] += 1

print(zeros_list)
# print(lista_filme)
for i,j in enumerate(vect_util):
    if j == max(vect_util):
        print(f"utiliztorul cu cele mai multe filme vizionate este {lista[i]['nume']}")
 #zeros_list.index(max(zeros_list))
for j, i in enumerate(zeros_list):
    if i == max(zeros_list):
        print(f"Cel mai vizionat film este {lista_filme[j]}, cu {zeros_list[j]} vizionari")

# print(f"Cel mai vizionat film este {lista_filme[maxim]}, cu {zeros_list[maxim_list[0]]} vizionari")
