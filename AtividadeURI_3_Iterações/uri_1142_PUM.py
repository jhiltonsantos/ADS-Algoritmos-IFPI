def main():
    valor = int(input())
    
    saida_pum(valor)


def saida_pum(valor):
    cont = 1
    x = 0
    i = 1
    
    while cont <= valor:
        i = 0
        while i <= 4:
            x += 1
            if x % 4 == 0:
                print('PUM')
                break
            print(x, end=' ')
            i += 1
        
        cont +=1


if __name__ == '__main__':
    main()

    