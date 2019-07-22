from tools import get_valor_int_positivo

def main():
    print('Numero: ',end=' ')
    numero = get_valor_int_positivo()
    while numero == 0 or numero > 999:
        if numero == 0:
            print('Nao existe simbolo para representar o "0" em romano!!!')
        else:
            print('Somente numeros de tres digitos(CDU)!!!')
        print('Numero: ',end=' ')
        numero = get_valor_int_positivo()
        
    centena = centena_romana(numero)
    dezena = dezena_romana(numero)
    unidade = unidade_romana(numero)

    print('Numero em romano: %s'%centena,\
        '%s'%dezena,'%s'%unidade)


def unidade_romana(numero):
    resto_centena = numero % 100
    unidade = resto_centena % 10
    unidade_r_1 = 'I'
    unidade_r_5 = 'V'

    if unidade > 0 and unidade < 4:
        valor_unidade = unidade_r_1 * unidade
    elif unidade == 4:
        valor_unidade = 'IV'
    elif unidade > 4 and unidade < 9:
        unidade = unidade - 5
        valor_unidade = unidade_r_5 + (unidade_r_1*unidade)
    elif unidade == 9:
        valor_unidade = 'IX'
    else:
        valor_unidade = ''

    return valor_unidade

    
def dezena_romana(numero):
    resto_centena = numero % 100
    dezena = resto_centena // 10
    
    dezena_r_10 = 'X'
    dezena_r_50 = 'L'
    
    if dezena > 0 and dezena <4:
        valor_dezena = dezena_r_10*dezena
    elif dezena == 4:
        valor_dezena = 'XL'
    elif dezena > 4 and dezena < 9:
        dezena = dezena - 5
        valor_dezena = dezena_r_50 + (dezena_r_10*dezena)
    elif dezena == 9:
        valor_dezena = 'XC'
    else:
        valor_dezena = ''

    return valor_dezena


def centena_romana(numero):
    centena = numero // 100
    
    cent_r_100 = 'C'
    cent_r_500 = 'D'
    
    if centena > 0 and centena < 4:
        valor_centena = cent_r_100 * centena
    elif centena == 4:
        valor_centena = 'CD'
    elif centena > 4 and centena < 9:
        centena = centena - 5
        valor_centena = cent_r_500 + (cent_r_100*centena)
    elif centena == 9:
        valor_centena = 'CM'
    else:
        valor_centena = ''
    
    return valor_centena


if __name__ == '__main__':
    main()