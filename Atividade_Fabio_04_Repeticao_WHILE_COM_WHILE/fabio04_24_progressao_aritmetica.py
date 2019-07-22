from tools import progressao_aritmetica


def main():
    razao_r = float(input('Digite a razao: '))
    primeiro_termo = float(input('Primeiro termo: '))
    num_termos = int(input('Quantidade de termos: '))

    print('\nValor final da PA: %.1f'\
        %progressao_aritmetica(razao_r,primeiro_termo,num_termos))

'''
def progressao_aritmetica(razao,a1,num_termos):
    contador = 1
    while contador <= num_termos:
        valor_pa = a1 + (contador-1)*razao
        print(valor_pa)
        contador += 1
    
    return valor_pa
'''
    
if __name__ == '__main__':
    main()