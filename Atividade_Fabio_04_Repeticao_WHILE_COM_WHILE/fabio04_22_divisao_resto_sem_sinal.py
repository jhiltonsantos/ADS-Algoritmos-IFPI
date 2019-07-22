def main():
    numero_1 = int(input('Numero 1: '))
    numero_2 = int(input('Numero 2: '))

    if numero_1 < numero_2:
        print('Divisao por inteiro nao exata')
    else:
        print('Resultado da divisao: %d'%func_divisao(numero_1,numero_2))
        print('Resto da divisao: %d'%func_resto(numero_1,numero_2))


def func_divisao(n1,n2):
    soma = n2
    resultado = 0

    while soma <= n1:
        soma = soma + n2
        resultado += 1

    return resultado


def func_resto(n1,n2):
    resultado = func_divisao(n1,n2)
    
    valor_anterior = resultado * n2
    resto = n1 - valor_anterior

    if resto <= 0:
        return 0
    else:
        return resto


if __name__ == '__main__':
    main()