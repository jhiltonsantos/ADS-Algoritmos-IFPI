#FAZER UMA FUNCAO ALEATORIO
from random import randint

def main():
    numero = int(input('Numero: '))
    cont = 1
    aleatorio = randint(0,999)
    
    while numero != aleatorio:
        if numero < aleatorio:
            print('Maior')
        else:
            print('Menor')
        numero = int(input('Numero: '))
        cont += 1

    print('Valor encontrado: %d'%aleatorio) 


if __name__ == '__main__':
    main()
