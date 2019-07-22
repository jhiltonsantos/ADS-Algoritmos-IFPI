from tools import valor_modulo

def main():
    atribuicao_ponto = passa_ponto()
    
    jogador_a = 0
    jogador_b = 0
    diferenca = 0
    final = False
    
    while final == False:
        if atribuicao_ponto == 1:
            jogador_a = jogador_a +1
        else:
            jogador_b = jogador_b + 1
        
        subtracao = jogador_a - jogador_b
        diferenca = valor_modulo(subtracao)
        
        final = jogo_finalizado(jogador_a,jogador_b,diferenca)    
        
        if final == False:
            atribuicao_ponto = passa_ponto()
    
    if jogador_a > jogador_b:
        print('JOGADOR A VENCEU')
    else:
        print('JOGADOR B VENCEU')


def passa_ponto():
    atribuicao_ponto=int(input('Ponto para: (1-Jogador A||2-Jogador B)'))
    while atribuicao_ponto < 1 or atribuicao_ponto > 2:
        print('PONTO INVALIDO!!!')
        atribuicao_ponto=int(input('Ponto para: (1-Jogador A||2-Jogador B)'))

    return atribuicao_ponto


def jogo_finalizado(a,b,diferenca):
    final = False
    if ((a==5)or(b==5)) and diferenca >= 2:
        print('JOGO FINALIZADO')
        final = True
    elif ((a>5)or(b>5)) and diferenca >= 2:
        print('JOGO FINALIZADO')
        final = True
    
    return final


if __name__ == "__main__":
    main()