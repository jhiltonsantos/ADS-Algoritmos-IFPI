def main():
    opcao = int(input\
        ('Operacao (1-Adicao | 2-Subtracao | 3-Multiplicacao | 4-Divisao): '))
    
    if 0 < opcao <= 4:
        n1 = float(input('Numero 1: '))
        n2 = float(input('Numero 2: '))

        if opcao == 1:
            soma = n1 + n2
            print('A soma dos numero eh: {:.2f}'.format(soma))
        elif opcao == 2:
            subtracao = n1 - n2
            print('A subtracao dos numero eh: {:.2f}'.format(subtracao))
        elif opcao == 3:
            multiplicar = n1 * n2
            print('A multiplicacao dos numeros eh: {:.2f}'.\
                format(multiplicar))
        else:
            divisao = n1 / n2
            print('A divisao dos numeros eh: {:.2f}'.format(divisao))
    else:
        print('Opcao invalida')


if __name__ == '__main__':
    main()
