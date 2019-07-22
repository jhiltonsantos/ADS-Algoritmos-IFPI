from tools import progressao_geometrica

def main():
    razao_q = float(input('Razao da PG: '))
    primeiro_termo = float(input('Valor do primeiro termo: '))
    quant_termos = int(input('Digite a quantidade de termos: '))
    
    print('\nResultado final da PG: %.1f'\
        %progressao_geometrica(razao_q,primeiro_termo,quant_termos))

'''
def progressao_geometrica(q,a1,n):
    contador = 1
    expoente = n - 1

    while contador <= n:
        valor_pg = a1 * (q**expoente)
        contador += 1

    return valor_pg
'''

if __name__ == '__main__':
    main()
