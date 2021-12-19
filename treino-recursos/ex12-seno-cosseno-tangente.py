# CÁLCULO DO SENO, COSSENO E TANGENTE

import math

ang = math.radians(float(input('Digite o valor de um ângulo: ')))


sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)

print('O valor do seno é {:.2f}.'.format(sen))
print('O valor do cosseno é {:.2f}.'.format(cos))
print('O valor da tangente é {:.2f}.'.format(tan))

