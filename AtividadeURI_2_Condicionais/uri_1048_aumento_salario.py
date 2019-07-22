def main():
    salario = float(input())

    if 0 < salario <=400.00:
        reajuste = salario * 0.15
        salario = salario + reajuste
        percentual = 15
    elif 400.01 <= salario <= 800.00:
        reajuste = salario * 0.12
        salario = salario + reajuste
        percentual = 12
    elif 800.01 <= salario <= 1200.00:
        reajuste = salario * 0.10
        salario = salario + reajuste
        percentual = 10
    elif 1200.01 <= salario <= 2000.00:
        reajuste = salario * 0.07
        salario = salario + reajuste
        percentual = 7
    else:
        reajuste = salario * 0.04
        salario = salario + reajuste
        percentual = 4
    
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %'\
        .format(salario,reajuste,percentual))


if __name__ == '__main__':
    main()
    