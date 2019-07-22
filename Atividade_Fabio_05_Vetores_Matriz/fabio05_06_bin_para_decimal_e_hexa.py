from tools_vetor import add_vetor


def main():
    valor = input('Digite o valor: ')
    valor_vetor = add_vetor(8, valor)
    
    if valor_vetor != False:
        valor = transformar_em_string(valor_vetor)
        valor_decimal = binario_decimal(valor)
        valor_hexa = bin_para_hexa(valor_decimal)

        print('Valor em binario: %s' % valor)
        print('Valor em decimal: %d' % valor_decimal)
        print('Valor em hexadecimal: %s' % valor_hexa)

    else:
        print('Valor excedeu o limite de 8 bits')


def binario_decimal(valor):
    return int(('%s' % valor), 2)


def bin_para_hexa(valor):
    hexadecimal = ''

    while (valor==16) or (valor%16 != 0):
        resto = str(valor%16)
        hexadecimal += transforma_hexa(resto)
        valor = valor // 16
    
    return hexadecimal[::-1]


def transforma_hexa(valor):
    if valor == '10':
        return 'A'
    elif valor == '11':
        return 'B'
    elif valor == '12':
        return 'C'
    elif valor == '13':
        return 'D'
    elif valor == '14':
        return 'E'
    elif valor == '15':
        return 'F'
    else:
        return valor    


def transformar_em_string(valor):
    str_valor = ''
    for i in range(len(valor)):
        str_valor += valor[i]

    return str_valor


if __name__ == '__main__':
    main()