def main():
    inter,gremio = map(int, input().split())
    
    calculo_grenal(inter,gremio)


def calculo_grenal(i,g):
    quant_grenal = 0
    cont_inter = 0
    cont_gremio = 0
    cont_empate = 0
    novo_grenal = 0

    while novo_grenal != 2:
        quant_grenal += 1
        if i > g:
            cont_inter += 1
        elif i < g:
            cont_gremio += 1
        else:
            cont_empate += 1
        
        novo_grenal = int(input('Novo grenal (1-sim 2-nao)\n'))
        if novo_grenal == 1:
            i,g = map(int, input().split())
        

    imprimir(quant_grenal,cont_inter,cont_gremio,cont_empate)


def imprimir(quant_grenal,inter,gremio,empate):
    print('{} grenais'.format(quant_grenal))
    print('Inter:{}'.format(inter))
    print('Gremio:{}'.format(gremio))
    print('Empates:{}'.format(empate))

    if inter > gremio:
        print('Inter venceu mais')
    elif gremio > inter:
        print('Gremio venceu mais')
    else:
        print('Nao houve vencedor')


if __name__ == '__main__':
    main()
