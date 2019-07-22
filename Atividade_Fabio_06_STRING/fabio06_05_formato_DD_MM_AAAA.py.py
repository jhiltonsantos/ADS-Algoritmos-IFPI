###FALTA TERMINAR
def main():
    data = input('Digite a data: ')
    
    mes = pegar_valor_mes(data)
    
    valor_dia = dia(data)
    str_mes = valor_mes(mes)
    str_ano = ano(data)

    print('%s'%valor_dia,'de %s'%str_mes,'de %s.'%str_ano)



def dia(data):
    i = 1
    while i <= len(data):
        dia = data[0] + data[1]
        i += 1

    return dia


def ano(data):
    i = 1
    ano = ''
    
    while i <= len(data):
        if i > 6  and i <=10:
            valor_ano = chr(ord(data[i-1]))
            ano += str(valor_ano)
        i += 1

    return ano


def pegar_valor_mes(data):
    i = 1
    while i <= len(data):
        caractere = ord(data[i-1])
        if caractere == 47:
            i += 1
            valor_1 = chr(ord(data[i-1]))
            i += 1
            valor_2 = chr(ord(data[i-1]))
            
        if caractere == 47 and i>4:
            break
        i += 1
    mes = valor_1 + valor_2
    
    return str(mes)


def valor_mes(mes):
    str_mes = ''
    if mes == '01':
        str_mes = 'JANEIRO'
    elif mes == '02':
        str_mes = 'FEVEREIRO'
    elif mes == '03':
        str_mes = 'MARCO'
    elif mes =='04':
        str_mes = 'ABRIL'
    elif mes == '05':
        str_mes = 'MAIO'
    elif mes == '06':
        str_mes = 'JUNHO'
    elif mes == '07':
        str_mes = 'JULHO'
    elif mes == '08':
        str_mes = 'AGOSTO'
    elif mes == '09':
        str_mes = 'SETEMBRO'
    elif mes == '10':
        str_mes = 'OUTUBRO'
    elif mes == '11':
        str_mes = 'NOVEMBRO'
    else:
        str_mes = 'DEZEMBRO'

    return str_mes


if __name__ == '__main__':
    main()