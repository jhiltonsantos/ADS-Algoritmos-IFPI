def main():
    valor_a = int(input('Valor inicial: '))
    limite = int(input('Limite: '))
    const_r = int(input('Constante R: '))
    
    i = valor_a
    cont = 1

    while i <= limite:
        print(i)
        i = valor_a * (const_r**(cont-1))
        cont += 1
        

if __name__ == '__main__':
    main()