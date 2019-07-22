# entrada
numero = int (input('Digite o numero de tres digitos: ')) 

# processamento
num1 = numero // 100
resto_num1 = numero % 100
num2 = resto_num1 // 10
num3 = resto_num1 % 10

media = (num1+num2+num3) / 3

# saida
print('O valor da media dos numeros é: {}'.format(media))