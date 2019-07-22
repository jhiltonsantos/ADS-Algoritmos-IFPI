def main():
    nota = 0
    novo_calculo = 1


    while not(novo_calculo == 2):
        cont = 1
        soma = 0
        while cont <= 2:
            nota = float(input())
        
            while not(nota >= 0 and nota <=10):
                print('nota invalida')
                nota = float(input())
            soma = soma + nota
            cont += 1

        media = soma / 2
        print('media = {:.2f}'.format(media))
        print('novo calculo (1-sim 2-nao)')
        novo_calculo = int(input())
        
        while not(novo_calculo == 1 or novo_calculo == 2):
            print('novo calculo (1-sim 2-nao)')
            novo_calculo = int(input())

if __name__ == '__main__':
    main()
