from tools import get_valor_float_positivo,valor_modulo

def main():
    salario = get_valor_float_positivo()
    
    soma_salario_reajustada,soma_salario_atual = valor_porcentagem_reajuste(salario)

    diferenca = soma_salario_reajustada - soma_salario_atual
    diferenca_salario = valor_modulo(diferenca)
    
    print('Soma salario antes do reajuste: %.2f'%soma_salario_atual)
    print('Soma salario depois do reajuste: %.2f'%soma_salario_reajustada)
    print('Diferenca: %.2f'%diferenca_salario)    


def valor_porcentagem_reajuste(salario):
    reajuste = 0
    soma_s_atual = 0
    soma_s_reajustada = 0

    while salario != 0.0:
        if salario > 0 and salario <= 2999.99:
            reajuste = salario + (salario*0.25)
        elif salario >= 3000 and salario <= 5999.99:
            reajuste = salario + (salario*0.20)
        elif salario >= 6000 and salario <= 9999.99:
            reajuste = salario + (salario*0.15)
        elif salario > 10000:
            reajuste = salario + (salario*0.10)
        
        soma_s_atual,soma_s_reajustada = \
            calculo_atual_reajuste(soma_s_atual,soma_s_reajustada,salario,reajuste)
        salario = get_valor_float_positivo()

    return soma_s_atual,soma_s_reajustada


def calculo_atual_reajuste(soma_s_atual,soma_s_reajustada,salario,reajuste):
    soma_s_atual = soma_s_atual + salario
    soma_s_reajustada = soma_s_reajustada + reajuste

    return soma_s_atual,soma_s_reajustada
        

if __name__ == '__main__':
    main()