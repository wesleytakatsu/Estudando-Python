# VERIFICANDO CARACTERÍSTICAS DA STRING
txt = input('Digite algo: ')
print('O tipo primitivo desse dado é:', type(txt))
print('Só tem espaços?', txt.isspace())
print('É um número?', txt.isnumeric())
print('É alfabético?', txt.isalpha())
print('É alfanumérico?', txt.isalnum())
print('Está toda maiúscula?', txt.isupper())
print('Está toda em minúscula?', txt.islower())
print('Está capitalizada?', txt.istitle())

