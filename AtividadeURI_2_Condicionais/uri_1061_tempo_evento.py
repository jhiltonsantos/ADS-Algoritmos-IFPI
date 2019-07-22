def main():
    dd_ini = input().split()
    dia_ini = int(dd_ini[1])
    hh_ini, mm_ini, ss_ini = map(int, input().split(' : '))
    dd_fim = input().split()
    dia_fim = int(dd_fim[1])
    hh_fim, mm_fim, ss_fim = map(int, input().split(' : '))
    
    tempo_inicio = [hh_ini,mm_ini,ss_ini]
    tempo_fim = [hh_fim,mm_fim,ss_fim]
    
    tempo(tempo_inicio, tempo_fim, dia_fim, dia_ini)
    

def tempo(tempo_inicio, tempo_fim, dia_fim, dia_ini):
    dia = dia_fim - dia_ini
    
    if tempo_inicio[0] > tempo_fim[0]:
        hora = (tempo_fim[0] - tempo_inicio[0]) + 24
        dia = dia - 1
    else:
        hora = tempo_fim[0] - tempo_inicio[0]

    if tempo_inicio[1] > tempo_fim[1]:
        minuto = (tempo_fim[1] - tempo_inicio[1]) + 60
        hora = hora - 1
    else: 
        minuto = tempo_fim[1] - tempo_inicio[1]

    if tempo_inicio[2] > tempo_fim[2]:
        segundo = (tempo_fim[2] - tempo_inicio[2]) + 60
        minuto = minuto - 1
    else:
        segundo = tempo_fim[2] - tempo_inicio[2]
        
    if dia <= 0:
        dia = 0

    print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'\
        .format(dia, hora, minuto, segundo))
    

if __name__ == '__main__':
    main()
