def main():
    valor_n = int(input('Habitantes: '))
    censo(valor_n)


def censo(quant_pessoas):
    contador = 1
    salario_total = 0
    filho_total = 0
    percentual_ate_1000 = 0

    while contador <= quant_pessoas:
        salario,n_filho = ler_dados()
        
        if salario <= 1000:
            percentual_ate_1000 += 1
        
        salario_total = salario_total + salario 
        filho_total = filho_total + n_filho
        contador += 1

    media_salarial, media_filho, percentual_medio = \
        calculo_censo(quant_pessoas,salario_total,filho_total,percentual_ate_1000)
    
    imprimir(media_salarial,media_filho,percentual_medio)


def ler_dados():
    salario = float(input('Salario: '))
    quantidade_filho = int(input('Quantidade de filhos: '))
    return salario,quantidade_filho


def calculo_censo(quant_pessoas,salario,quantidade_filho,percentual):
    media_salarial = salario / quant_pessoas
    media_filhos = quantidade_filho / quant_pessoas
    percentual_medio = (percentual/quant_pessoas) * 100
    return media_salarial, media_filhos, percentual_medio


def imprimir(media_salarial,media_filho,percentual_medio):
    print('Media salarial da cidade: R$%.2f'%media_salarial)
    print('Media de filhos do familia: %.2f'%media_filho)
    print('Percentual de pessoas com salario de até R$1.000,00: %d'%percentual_medio,'%')


if __name__ == '__main__':
    main()
