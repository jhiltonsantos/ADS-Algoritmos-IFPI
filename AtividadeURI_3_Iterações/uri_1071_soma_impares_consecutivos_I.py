def main():
    valor_x = int(input())
    valor_y = int(input())
    soma = 0

    x = valor_x
    y = valor_y

    if x < y:
        x = valor_y
        y = valor_x

    if y % 2 != 0:
        y +=1
    
    while y != x:
        if y % 2 != 0:
            soma = soma + y
            
        y += 1
    print(soma)


if __name__ == '__main__':
    main()