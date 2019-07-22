def main():
    peso_esq, peso_dir, rep = map(int, input().split())
    
    resultado_total = 0
    i = 0
    while (peso_dir!=0) and (peso_esq!=0) and (rep!=0):
        peso_total = (peso_esq+peso_dir)/2
        resultado = peso_total*(1+(rep/30))
        resultado_total += resultado
        i += 1
        
        if (resultado>=1) and (resultado<13):
            print('Nao vai da nao')
        elif (resultado>=13) and (resultado<14):
            print('E 13')
        elif (resultado>=14) and (resultado<40):
            print('Bora, hora do show! BIIR!')
        elif (resultado>=40) and (resultado<=60):
            print('Ta saindo da jaula o monstro!')
        elif resultado>60:
            print('AQUI E BODYBUILDER!!')

        peso_esq, peso_dir, rep = map(int, input().split())

    media = resultado_total / i
    
    if media > 40:
        print('\nAqui nois constroi fibra rapaz! Nao e agua com musculo!')


main()
     