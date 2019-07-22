def main():
    valor_a = int(input('A: '))
    limite = int(input('Limite: '))
    const_r = int(input('Constante R: '))
    i = valor_a
    cont = 1
    
    while i <= limite:
        print(i)
        i = i + const_r
        cont += 1
        

if __name__ == '__main__':
    main()