# entrada
valor_dinheiro = int (input('Digite o valor de dinheiro desejado: R$'))

# processamento
nota_100 = valor_dinheiro // 100
resto_100 = valor_dinheiro %100
nota_50 = resto_100 // 50
resto_50 = resto_100 % 50
nota_20 = resto_50 // 20
resto_20 = resto_50 % 20
nota_10 = resto_20 // 10
resto_10 = resto_20 % 10
nota_5 = resto_10 // 5
resto_5 = resto_10 % 5
nota_2 = resto_5 // 2
nota_1 = resto_5 % 2

# saida
print('Distribuição das notas:\n {} de R$100. {} de R$50.\n\
     {} de R$20.\n {} de R$10.\n {} de R$5.\n {} de R$2.\n {} de R$1\n'\
         .format(nota_100, nota_50, nota_20, nota_10, nota_5, nota_2, nota_1))