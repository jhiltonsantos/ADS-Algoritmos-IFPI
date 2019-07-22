def main():
    valor_x = int(input())
    valor_y = int(input())

    print('{}'.format(multiplo(valor_x,valor_y)))    


def verifica_maior(valor_x, valor_y):
    x = valor_x
    y = valor_y
    
    if valor_y > valor_x:
        x = valor_y
        y = valor_x
    
    return x,y    


def multiplo(valor_x, valor_y):
    x,y = verifica_maior(valor_x,valor_y)
    soma = 0
    
    while y <= x:
        if y % 13 != 0:
            soma = soma + y
        y += 1
    
    return soma


if __name__ == '__main__':
    main()