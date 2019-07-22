def main():
    idade,opiniao = leia_espectador()
    media_idade_otimo, num_regular, porcent_bom = resultado_pesquisa(idade,opiniao)
    
    print('Idade media de quem respondeu otimo: %.1f'\
        %media_idade_otimo,'anos.')
    print('Quantidade que respondeu regular: %d'%num_regular,'pessoas.')
    print('Porcentagem que respondeu bom: %.1f'%porcent_bom,'%.')


def leia_espectador():
    idade = int(input('Digite a idade: '))
    
    if idade != -1:
        opiniao = int(input('Opiniao sobre o filme: '))
        while opiniao < 1 or opiniao > 4:
            print('VALOR INVALIDO!!!')
            print('Valores validos: 1-OTIMO|2-BOM|3-REGULAR|4-PESSIMO') 
            opiniao = int(input('Opiniao sobre o filme: '))
    else:
        opiniao = 0
    
    return idade,opiniao


def resultado_pesquisa(idade,opiniao):
    total_pessoas = 0
    idade_op_otimo = 0
    num_regular = 0
    quant_respondeu_otimo = 0
    quant_respondeu_bom = 0

    while idade != -1:
        if opiniao == 1:
            idade_op_otimo = idade_op_otimo + idade
            quant_respondeu_otimo += 1       
        elif opiniao == 2:
            quant_respondeu_bom += 1
        elif opiniao == 3:
            num_regular = num_regular + 1
        
        idade,opiniao = leia_espectador()
        total_pessoas += 1

    media_otimo = idade_op_otimo / quant_respondeu_otimo
    porcent_bom = (quant_respondeu_bom*100) / total_pessoas

    return media_otimo,num_regular,porcent_bom


if __name__ == '__main__':
    main()