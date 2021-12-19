# SORTEANDO UM ITEM DENTRO DE UMA LISTA
# DEPOIS EMBARALHAMOS A LISTA

import random

aluno1 = 'Wesley'
aluno2 = 'Henrique'
aluno3 = 'Fernando'
aluno4 = 'Anderson'

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(lista)

print(sorteado)

random.shuffle(lista)
print(lista)
