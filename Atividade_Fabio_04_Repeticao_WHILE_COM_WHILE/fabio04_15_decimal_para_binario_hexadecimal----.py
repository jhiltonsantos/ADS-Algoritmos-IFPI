#FALTA TERMINAR
from tools import get_valor_int_positivo

def main():
    decimal = get_valor_int_positivo()
    while decimal > 255:
        print('VALORES ENTRE 0 E 255')
        decimal = get_valor_int_positivo()

    binario = decimal_binario(decimal)
    hexa = decimal_hexadecimal(decimal)
    
    print('Valor em binario: %d'%binario)
    print('Valor em hexadimal: %d'%hexa)
    

def decimal_binario(decimal):
    if decimal == 0:
        return 0
    else:
        valor = str(decimal_binario(decimal//2))
        string = str(decimal % 2)
        binario = valor + string

        return int(binario)


def decimal_hexadecimal(decimal):
    hexadecimal = 0

    return hexadecimal


if __name__ == '__main__':
    main()