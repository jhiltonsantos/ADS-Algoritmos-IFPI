def main():
                            
    valor = float(input())

    nota_100 = valor // 100
    resto_100 = (valor %100)
    nota_50 = resto_100 // 50
    resto_50 = (resto_100 % 50)
    nota_20 = resto_50 // 20
    resto_20 = (resto_50 % 20)
    nota_10 = resto_20 // 10
    resto_10 = (resto_20 % 10)
    nota_5 = resto_10 // 5
    resto_5 = (resto_10 % 5)
    nota_2 = resto_5 // 2
    
    moeda_100 = (resto_5 % 2)
    
    novo_valor = moeda_100 * 100
    moeda_50 = novo_valor // 50
    if moeda_50 %2 == 0:
        moeda_50 = 0
    elif not(moeda_50%2==0) and moeda_50>1:
        moeda_50 = moeda_50 - 2
    resto_m50 = novo_valor % 50
    moeda_25 = resto_m50 // 25
    resto_m25 = round(resto_m50 % 25)
    moeda_10 = resto_m25 // 10
    resto_m10 = round(resto_m25 % 10)
    moeda_5 = resto_m10 // 5
    resto_m5 = round(resto_m10 % 5)
    moeda_1 = (resto_m5 // 1)
    
    print('NOTAS:')
    print('%d nota(s) de R$ 100.00' % nota_100)
    print('%d nota(s) de R$ 50.00' % nota_50)
    print('%d nota(s) de R$ 20.00' % nota_20)
    print('%d nota(s) de R$ 10.00' % nota_10)
    print('%d nota(s) de R$ 5.00' % nota_5)
    print('%d nota(s) de R$ 2.00' % nota_2)
    print('MOEDAS:')
    print('%d moeda(s) de R$ 1.00' % moeda_100)
    if moeda_50 != 1:
        print('%d moeda(s) de R$ 0.50' % 0)
    else:
        print('%d moeda(s) de R$ 0.50' % moeda_50)
    print('%d moeda(s) de R$ 0.25' % moeda_25)
    print('%d moeda(s) de R$ 0.10' % moeda_10)
    print('%d moeda(s) de R$ 0.05' % moeda_5)
    print('%d moeda(s) de R$ 0.01' % (moeda_1))


main()