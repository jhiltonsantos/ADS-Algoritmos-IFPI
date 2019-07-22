# Elaborar segundo turno
def main():
    numero_eleitores = int(input('Quantidade de eleitores: '))
    urna(numero_eleitores)


def urna(eleitores):
    contador = 1
    voto_branco = 0
    voto_nulo = 0
    candidato_a,candidato_b,candidato_c = 0,0,0

    while contador <= eleitores:
        leia_voto = int(input('Digite seu Voto: '))
        
        while (leia_voto<0) or (3<leia_voto<9) or (leia_voto>9):
            print('VOTO INVALIDO!!! VOTOS VALIDOS:[0,1,2,3,9]!!!')
            leia_voto = int(input('Digite seu Voto: '))
        
        if leia_voto == 0:
            voto_branco += 1
        elif leia_voto == 1:
            candidato_a += 1
        elif leia_voto == 2:
            candidato_b += 1
        elif leia_voto == 3:
            candidato_c += 1
        elif leia_voto == 9:
            voto_nulo += 1

        contador += 1

    vencedor = resultado_urna(candidato_a,candidato_b,candidato_c)
    imprimir(vencedor,voto_branco,voto_nulo)


def resultado_urna(a,b,c):
    vencedor = 0
    if a > b and a > c:
        vencedor = 'CANDIDATO A'
    elif b > a and b > c:
        vencedor = 'CANDIDATO B'
    elif c > a and c > b:
        vencedor = 'CANDIDATO C'
    elif (a==b and a>c) or (a==c and a>b)\
         or (a==b and b==c):
        vencedor = 'EMPATE'
    
    return vencedor


def imprimir(vencedor,nulo,branco):
    print('O candidato eleito eh: %s'%vencedor)
    print('Quantidade de votos nulos: %d'%nulo)
    print('Quantidade de votos brancos: %d'%branco)


if __name__ == '__main__':
    main()    
