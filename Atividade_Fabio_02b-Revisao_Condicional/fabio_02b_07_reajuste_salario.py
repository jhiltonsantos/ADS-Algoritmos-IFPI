def main():
    salario = float(input('Digite o salario: '))

    #20 porcento
    if salario <= 280:
        aumento = salario * 0.2
        reajuste = salario + aumento
        print('Salario antes do reajuste: R${:.2f}. O novo salario com 20 porcento, aumento de R${:.2f}, sera de: R${:.2f}'\
            .format(salario,aumento,reajuste))
    #15 porcento
    elif 280 < salario < 700:
        aumento = salario  * 0.15
        reajuste = salario + aumento
        print('Salario antes do reajuste: R${:.2f}. O novo salario com 15 porcento, aumento de R${:.2f}, sera de: R${:.2f}'\
            .format(salario,aumento,reajuste))
    #10 porcento
    elif 700 <= salario < 1500:
        aumento = salario * 0.1
        reajuste = salario + aumento
        print('Salario antes do reajuste: R${:.2f}. O novo salario com 10 porcento, aumento de R${:.2f}, sera de: R${:.2f}'\
            .format(salario,aumento,reajuste))
    #5 porcento
    else:
        aumento = salario * 0.05
        reajuste = salario + aumento
        print('Salario antes do reajuste: R${:.2f}. O novo salario com 05 porcento, aumento de R${:.2f}, sera de: R${:.2f}'\
            .format(salario,aumento,reajuste))
    

if __name__ == '__main__':
    main()  
