def main():
    numero_de_container = int(input('Quantidade de containers: '))
    peso_container = float(input('Peso de cada container: '))
    quant_total_bagagens, cont_passageiro = informacao_passageiros()
    
    peso_total_pasageiro,peso_total_carga,quant_combustivel,status_decolagem=\
        decola_ou_nao(quant_total_bagagens,cont_passageiro,numero_de_container,peso_container)
    
    print('Quantidade de passageiros: %d'%cont_passageiro)
    print('Quantidade de bagagens no aviao: %d'%quant_total_bagagens)
    print('Peso total de passageiros: %.2f'%peso_total_pasageiro)
    print('Peso total de cargas: %.2f'%peso_total_carga)
    print('Quantidade de combustivel: %.2f'%quant_combustivel)
    print('Status da decolagem do aviao: ',status_decolagem)


def informacao_passageiros():
    
    num_bilhete_passageiro = int(input('Numero do bilhete: '))
    quant_bagagem = int(input('Quantidade de bagagens: '))
    cont_passageiro = 0
    quant_total_bagagens = quant_bagagem
    
    while num_bilhete_passageiro != 0:
        cont_passageiro += 1
        quant_total_bagagens = quant_total_bagagens + quant_bagagem
        num_bilhete_passageiro = int(input('Numero do bilhete: '))
        if num_bilhete_passageiro != 0:
            quant_bagagem = int(input('Quantidade de bagagens: '))
    
    return quant_total_bagagens,cont_passageiro


def decola_ou_nao(quant_total_bagagens,\
    cont_passageiro,numero_de_container,peso_container):
    
    quant_combustivel = int(input('Qual a quantidade de combustivel: '))
    while quant_combustivel < 1000:
        print('Combustivel abaixo de minimo!!! O aviao não vai decolar!!!')
        quant_combustivel = int(input('Qual a quantidade de combustivel: '))

    status_decolagem = False     

    peso_total_combustivel = quant_combustivel * 1.5        
    peso_total_pasageiro = (cont_passageiro*70) + (quant_total_bagagens*10)
    peso_total_carga = numero_de_container * peso_container
    peso_total_de_decolagem=peso_total_combustivel+peso_total_carga+peso_total_pasageiro
    
    if peso_total_de_decolagem != 500000:
        status_decolagem = False
    else:
        status_decolagem = True

    return peso_total_pasageiro,peso_total_carga,quant_combustivel,status_decolagem
    

if __name__ == '__main__':
    main()