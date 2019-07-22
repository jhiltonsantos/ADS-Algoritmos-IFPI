from tools import verifica_maior

def main():
    valor_n1 = int(input('Numero 1: '))
    valor_n2 = int(input('Numero 2: '))
    
    verifica_mmc(valor_n1,valor_n2)
    

def verifica_mmc(n1,n2):
    contador = 0
    maior = verifica_maior(n1,n2)
    while contador == 0:
        if (maior%n1==0) and (maior%n2==0):
            print('Minimo Multiplo Comum = %.2f'%maior)
            contador = 1
        else:
            maior += 1


if __name__ == '__main__':
    main()