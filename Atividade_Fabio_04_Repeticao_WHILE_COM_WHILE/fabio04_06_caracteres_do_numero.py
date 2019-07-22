from tools import get_valor_int_positivo

def main():
    numero = get_valor_int_positivo()
    print('\nA quantidade eh: %d'\
        %separa_numero_com_fatiamento_string(numero))


def separa_numero_com_fatiamento_string(numero):
    n = 1
    while numero != -1:
        separa = str(numero)[n-1:n]
        if separa == '':
            break
        print(separa, end=' ')
        n += 1
        
    quant = n-1
    return quant


if __name__ == '__main__':
    main()