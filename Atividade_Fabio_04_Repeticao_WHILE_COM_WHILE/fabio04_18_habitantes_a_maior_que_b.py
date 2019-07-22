from tools import verifica_maior_menor

def main():
    '''
    cidade_a = 200000
    taxa_a = 0.035
    cidade_b = 800000
    taxa_b = 0.0135
    '''
    
    cidade_a,cidade_b,taxa_a,taxa_b = leia_valores()
    ano = 1

    if taxa_a < taxa_b:
        taxa_a = taxa_b
        taxa_b = taxa_a
    
    while cidade_a < cidade_b:
        cidade_a = cidade_a + (cidade_a*taxa_a)
        cidade_b = cidade_b + (cidade_b*taxa_b)
        ano += 1
    ano -= 1
    print('Serao necessarios: %d'%ano,'anos.')


def leia_valores():
    cidade_a = int(input('Quantidade de habitantes na cidade A: '))
    taxa_a = float(input('Taxa de crescimento da cidade A: '))
    taxa_a = taxa_a / 100
    cidade_b = int(input('Quantidade de habitantes na cidade B: '))
    taxa_b = float(input('Taxa de crescimento da cidade B: '))
    taxa_b = taxa_b / 100
    # Cidade B sempre maior
    cidade_b,cidade_a = verifica_maior_menor(cidade_a,cidade_b)
    
    return cidade_a,cidade_b,taxa_a,taxa_b


if __name__ == '__main__':
    main()
