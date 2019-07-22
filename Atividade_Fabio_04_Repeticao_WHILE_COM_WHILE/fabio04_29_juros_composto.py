from tools import get_valor_float_positivo

def main():
    print('Digite o valor do investimento ao mês: ',end=' ')
    valor_inv_mes = get_valor_float_positivo()
    print('Taxa de juros mensal: ',end=' ')
    taxa_juros_mes = get_valor_float_positivo()
    
    ano = 12
    verifica = 1
    taxa_juros_mes = taxa_juros_mes/100
    
    while verifica == 1:
        montante = valor_inv_mes*((1+taxa_juros_mes)**ano)

        print('Saldo do investimento após 1 ano: R$%.2f'%montante)
        verifica = int(input('Deseja processar mais um ano (1-Sim|2-Nao): '))
        while verifica != 1 and verifica != 2:
            print('RESPOSTA INVALIDA!!!')
            verifica = int(input('Deseja processar mais um ano (1-Sim|2-Nao): '))
        
        ano += 12


if __name__ == '__main__':
    main()