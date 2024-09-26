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
    # lista_filme= list(set(lista_filme).union(set( i['filme'])))
    lista_2 = list(i['filme'])
    # zeros_list = [0] * len(lista_filme)
    # print(lista_filme)
    for l, k in enumerate(list(i['filme'])):
        # print(l, k)
        for index_l_f, value_l_f in enumerate(lista_filme):
            # print(index_l_f)
            if k == value_l_f:
                zeros_list[index_l_f] = zeros_list[index_l_f] + 1
                # print(lista_filme)

    for l in lista_2:
        vect_util[j] += 1

# print(vect_util.index(max(vect_util)))
print(f"utiliztorul cu cele mai multe filme vizionate este {lista[vect_util.index(max(vect_util))]['nume']}")
maxim = zeros_list.index(max(zeros_list))
print(f"Cel mai vizionat film este {lista_filme[maxim]}, cu {max(zeros_list)} vizionari")

# print(zeros_list)
# print(lista_filme)
