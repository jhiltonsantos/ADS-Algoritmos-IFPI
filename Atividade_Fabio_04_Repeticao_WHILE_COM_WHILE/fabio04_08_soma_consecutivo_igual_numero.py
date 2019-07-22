from tools import numero_diferente_de_valor

def main():
    numero = float(input('Digite o numero: '))
    numero = numero_diferente_de_valor(numero,0)
    soma_lista_igual_numero(numero)
    

def soma_lista_igual_numero(numero):
    cont = None
    n = 0
    ultimo = 0
    soma_n_anteior = 0

    while cont != n:
        n = float(input())
        soma_n_anteior = n + ultimo
        
        if soma_n_anteior == numero:
            print('Os valores %.2f'%ultimo,'e %.2f'\
                %n,'= %.2f'%numero)
            break
        
        ultimo = n
        soma_n_anteior = 0
        

if __name__ == '__main__':
    main()
