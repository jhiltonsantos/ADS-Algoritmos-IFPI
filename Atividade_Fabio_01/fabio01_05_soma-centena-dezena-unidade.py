# entrada
numero = int(input('Digite um numero inteiro de tres digitos: '))

# processamento
centena = numero // 100
resto_cent = numero % 100
dezena = resto_cent // 10
unidade =  resto_cent % 10

soma = centena + dezena + unidade

# saida
print('A soma dos numeros é: {}'.format(soma))

