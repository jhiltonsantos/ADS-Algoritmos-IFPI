def main():
    numero = int(input('Digite o Numero:(0 - para parar) '))
    
    while numero != 0:
        print('O numero eh: %d'%numero)
        verifica_divisores(numero)
        numero = int(input('\nDigite o Numero:(0 - para parar) '))


def verifica_divisores(numero):
    contador = 1
    print('DIVISORES: ',end=' ')
    while contador <= numero:
        if numero % contador == 0:
            print(contador,end=' ')
        contador +=1


if __name__ == '__main__':
    main()
