# CALCULAR A HIPOTENUSA DE UM TRIÂNGULO RETÂNGULO

import math

cat1 = int(input('Digite o primeiro cateto: '))
cat2 = int(input('Digite o segundo cateto: '))

# exemplo:
# cat1 = 4
# cat2 = 3
# hip terá que ser 5
# a fórmula é hip² = cat1² + cat2² -> hip = raiz de (cat1² + cat2²)

hip = math.sqrt(cat1 ** 2 + cat2 ** 2)

print('O valor da hipotenusa é {}'.format(int(hip)))

