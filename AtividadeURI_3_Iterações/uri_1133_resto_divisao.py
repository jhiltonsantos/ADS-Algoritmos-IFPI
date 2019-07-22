def main():
    valor_x = int(input())
    valor_y = int(input())

    resto_divisao(valor_x,valor_y)

def verifica_maior(valor_x, valor_y):
    x = valor_x
    y = valor_y
    if valor_y > valor_x:
        x = valor_y
        y = valor_x
    return x,y    


def resto_divisao(valor_x, valor_y):
    x,y = verifica_maior(valor_x,valor_y)
    y += 1
    
    while y < x:
        if (y%5==2) or (y%5==3):
            print(y)
        y +=1
    

if __name__ == '__main__':
    main()