from tools import numero_diferente_de_valor

def main():
    numero = int(input('Digite o numero: '))
    numero = numero_diferente_de_valor(numero,0)
    cont = numero
    n = 0
    
    while cont != n:
        n = int(input())
    print('Valor encontrado!')


if __name__ == '__main__':
    main()
