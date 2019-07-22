def main():
    hh_ini, mm_ini, hh_fim, mm_fim = map(int, input().split())
    duracao(hh_ini, hh_fim,mm_ini,mm_fim)


def duracao(hh_ini, hh_fim,mm_ini,mm_fim):
    
    
    duracao_hora = hh_fim - hh_ini
    if hh_ini == hh_fim and mm_ini == mm_fim:
        duracao_hora = 24
        duracao_min = 0
    else:
        if mm_ini > mm_fim:
            duracao_min = 60 + (mm_fim - mm_ini)
            duracao_hora -= 1
        else:
            duracao_min = mm_fim - mm_ini
    
    if duracao_hora < 0:
        duracao_hora += 24
    
    
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(duracao_hora,duracao_min))


if __name__ == '__main__':
    main()