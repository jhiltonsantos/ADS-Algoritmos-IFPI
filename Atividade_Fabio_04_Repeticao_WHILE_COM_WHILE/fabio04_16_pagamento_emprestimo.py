from tools import get_valor_float_positivo

def main():
    valor_emprestimo, valor_diario = dados()
    cont = 1
    
    while valor_emprestimo > 0.0:
        diferenca = valor_emprestimo - valor_diario
        valor_emprestimo = diferenca + (diferenca*0.0085)
        cont +=1    
    dias = cont - 1

    print('Quantidade de dias uteis necessarios: %d'%dias)


def dados():
    print('Valor do emprestimo. ',end='')
    emprestimo = get_valor_float_positivo()
    print('Valor pago diario. ',end='')
    diario = get_valor_float_positivo()
    
    return emprestimo,diario

if __name__ == '__main__':
    main()