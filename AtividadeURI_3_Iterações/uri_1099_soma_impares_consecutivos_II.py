def main():
    valor_n = int(input())
    cont = 1
    

    while cont <= valor_n:
        valor_x, valor_y = map(int, input().split())
        x = valor_x
        y = valor_y

        if y > x:
            x = valor_y
            y = valor_x
            
        if y % 2 != 0:
            y += 1
        
        soma = 0
        while y < x:
            if y % 2 != 0:
                soma = soma + y
            y += 1
    
        print(soma)
        cont += 1


if __name__ == '__main__':
    main()