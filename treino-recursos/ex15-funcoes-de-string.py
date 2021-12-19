# TRANSFORMANDO E MANIPULANDO STRINGS DE DIVERSAS MANEIRAS

frase = '  Treinamento do Wesley  '

# MOSTRA DA POSIÇÃO 3 ATÉ A 4 - NO CASO 2 LETRAS
print('Do 3 ao 4:')
print(frase[3:5])

# MOSTRA DO PRIMEIRO CARACTERE ATÉ O 4
print('\nDo começo ao 3, no caso 4 letras:')
print(frase[:4])

# BUSCA O TERMO DENTRO DA STRING E RETORNA A PRIMEIRA POSIÇÃO
print('\nMostra a posição que começa o Wes:')
print(frase.find('Wes'))

# VERIFICA SE EXISTE O TERMO DENTRO DA STRING E RETORNA TRUE OU FALSE
print('\nVerifica se existe o termo dentro da string e retorna true ou false:')
print('Wesley' in frase)

# SUBSTITUI UM TERMO NA FRASE POR OUTRO
print('\nSubstitui um termo. Antes: {}'.format(frase))
print('Substitui um termo. Depois: {}'.format(frase.replace('Wesley', 'Takatsu')))

# SEPARA AS PALAVRAS DA STRING E RETORNA UMA LISTA
print('\nSepara as palavras da frase em uma lista:')
lista = frase.split()
print(lista[0])
print(lista[1])
print(lista[2])

# JUNTA AS STRINGS DA LISTA EM UMA STRING, PODENDO COLOCAR ALGO ENTRE OS TERMOS
# NO CASO USEI O - MAS PODE COLOCAR OUTRO CARACTER E ATÉ MESMO MAIS DE 1
print('\nJunta as palavras de uma lista em uma string:')
juntou = '-'.join(lista)
print(juntou)

print('\nColoca toda a String em maiúscula:')
print(frase.upper())

print('\nColoca toda a String em minúscula:')
print(frase.lower())

print('\nTudo minúsculo, Só a 1ª letra da String maiúscula:')
print(frase.capitalize())

print('\nElimina os espaços vazios no começo e no final da String:')
print(frase.strip())

print('\nTodas as palavras começam com maiúsculas, o resto minúsculo:')
print(frase.title())









