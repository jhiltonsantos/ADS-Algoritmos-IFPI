def main():
    # entrada
    valor = int(input())

    # processamento
    nota_100 = valor // 100
    resto_100 = valor % 100
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
    print('{}'.format(valor))
    print('{} nota(s) de R$ 100,00'.format(nota_100))
    print('{} nota(s) de R$ 50,00'.format(nota_50))
    print('{} nota(s) de R$ 20,00'.format(nota_20))
    print('{} nota(s) de R$ 10,00'.format(nota_10))
    print('{} nota(s) de R$ 5,00'.format(nota_5))
    print('{} nota(s) de R$ 2,00'.format(nota_2))
    print('{} nota(s) de R$ 1,00'.format(nota_1))


if __name__ == '__main__':
    main()
    