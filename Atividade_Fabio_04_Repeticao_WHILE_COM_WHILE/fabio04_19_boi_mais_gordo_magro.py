from tools import get_valor_float_positivo

def main():
    numero_id,peso = ficha()

    id_magro,magro,id_gordo,gordo =\
        definir_gordo_magro(peso,numero_id)
    
    print('____Boi mais magro____')
    print('Nº Identificacao: %d'%id_magro)
    print('Peso: %.1f'%magro)

    print('____Boi mais gordo____')
    print('Nº Identificacao: %d'%id_gordo)
    print('Peso: %.1f'%gordo)


def ficha():
    n_identidade = int(input('Digite o numero de identificacao: '))
    if n_identidade != 0:
        print('Digite o peso do boi. ')
        peso = get_valor_float_positivo()
    else:
        peso = 0

    return n_identidade,peso


def definir_gordo_magro(peso,numero_id):
    magro = peso
    id_magro = numero_id
    gordo = peso
    id_gordo = numero_id

    while numero_id != 0:
        if peso >= gordo:
            gordo = peso
            id_gordo = numero_id
        elif peso <= magro:
            magro = peso
            id_magro = numero_id
        numero_id,peso = ficha()
    
    return id_magro,magro,id_gordo,gordo


if __name__ == '__main__':
    main()