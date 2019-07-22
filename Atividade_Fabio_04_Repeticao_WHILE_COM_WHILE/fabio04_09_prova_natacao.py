def main():
    numero_prova = int(input('Qual o numero da prova: '))
    quant_nadadores = int(input('Quantos nadadores: '))
    cont = 1
    ponto_nadador = 0
    clube_a_pontos = 0
    clube_b_pontos = 0
    total_pontos_ca = 0
    total_pontos_cb = 0


    while numero_prova != 0 and quant_nadadores != 0:
        while cont <= quant_nadadores:
            classificacao,clube = informacoes_do_nadador()
            ponto_nadador = tabela_pontos(classificacao)    
            
            # QUAL O CLUBE
            if clube == 1:
                clube_a_pontos = clube_a_pontos + ponto_nadador
            else:
                clube_b_pontos = clube_b_pontos + ponto_nadador

            cont +=1

        total_pontos_ca = total_pontos_ca + clube_a_pontos
        total_pontos_cb = total_pontos_cb + clube_b_pontos
        
        numero_prova = int(input('\nQual o numero da prova: '))
        quant_nadadores = int(input('Quantos nadadores: '))
        cont = 1
        clube_a_pontos = 0
        clube_b_pontos = 0
            
    vencedor = clube_vencedor(total_pontos_ca,total_pontos_cb)
    print('\nPontos clube A: %d'%total_pontos_ca)
    print('Pontos clube B: %d'%total_pontos_cb)
    print('\nVencedor: %s'%vencedor)


def informacoes_do_nadador():
    nome_nadador = input('Nome do Nadador: ',end=' ')
    print(nome_nadador)
    
    classificacao = int(input('Qual a posicao do nadador: '))
    while classificacao<1 and classificacao>4:
        classificacao = int(input('Qual a posicao do nadador: '))
    
    tempo_prova = float(input('Qual o tempo da prova: ',end=' '))
    print(tempo_prova)
    
    clube = int(input('Qual o clube do nadador(1-A||2-B): '))
    while clube!=1 and clube!=2:
        clube = int(input('Qual o clube do nadador(1-A||2-B): '))

    return classificacao,clube


def tabela_pontos(classificacao):
    if classificacao == 1:
        ponto_nadador = 9
    elif classificacao == 2:
        ponto_nadador = 6
    elif classificacao == 3:
        ponto_nadador = 4
    else:
        ponto_nadador = 3
    
    return ponto_nadador


def clube_vencedor(total_pontos_ca,total_pontos_cb):
    if total_pontos_ca > total_pontos_cb:
        vencedor = 'CLUBE A'
    elif total_pontos_ca < total_pontos_cb:
        vencedor = 'CLUBE B'
    else:
        vencedor = 'EMPATE'
    
    return vencedor    


if __name__ == '__main__':
    main()