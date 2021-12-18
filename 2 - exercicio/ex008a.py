# IMPORTANDO BIBLIOTECAS

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('O num digitado foi {}, a raiz dele é {:.2f}.'.format(num, raiz))
print('A raiz arrendodada pra cima é {}'.format(math.ceil(raiz)))

# from math import sqrt -> importa somente "sqrt" da biblioteca "math"
# from math import sqrt, ceil -> importa 2 funcionalidades da "math"
#
# -> BIBLIOTECA math
# ceil -> arredonda pra cima
# floor -> arredonda pra baixo
# trunc -> elimina da vírgula pra frente
# pow -> potência
# sqrt -> raiz
# factorial -> calcula a fatorial