# CONVERTER O VALOR DE DÓLAR PARA REAIS
# LIMITANDO CASAS DECIMAIS

dolar = float(input('Digite um valor em dólar: '))
reais = dolar * 5.5
print('O valor em dólar digitado foi {} e convertido em reais é R$ {:.2f}.'.format(dolar, reais))
