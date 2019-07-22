def main():
    numero = int(input('Digite o numero: '))

    print('\nO valor da ultima divisao eh: %.2f'\
        %divisao_sucessiva_por_dois(numero))


def divisao_sucessiva_por_dois(n):
    resultado = 2
    
    while resultado > 1:
        resultado = n / 2
        print(resultado, end=' ')
        n = resultado
    
    return resultado
    

if __name__ == '__main__':
    main()
    