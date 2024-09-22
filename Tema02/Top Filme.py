# Avand o lista de utilizatori si filme vizionate, listati
# Cel mai vizionat film - Fight Club in cazul de mai sus
# Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus
# Extra
# Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...
# Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan
from itertools import count
from operator import index

lista = [ { 'nume': 'George',
   'filme': ['Shrek', 'Bond', 'Fight Club']},

{'nume' : 'Cristian',
 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},

{'nume' : 'Stefan',
 'filme': ['Fight Club', 'Slumdog Millionaire'] } ]
lista_filme = []
suma = 0
vect = 0
xee = 0
index_lista = {0}
for i in lista:
    lista_filme= list(set(lista_filme).union(set( i['filme'])))
    lista_2 = list(i['filme'])
    for l, k in enumerate(lista_filme):
        if l == index(list(lista_filme)):
            continue
        index_lista = list(index_lista.add(0))

print(vect)
print(lista_filme)
