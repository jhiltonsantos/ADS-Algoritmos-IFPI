def main():
    valor = int(input('Digite o numero: '))
    fatorial = 1
    
    if valor == 0 or valor == 1:
            fatorial = 1
            print(fatorial)
    else:
        while valor > 1:
            fatorial *= valor
            valor -= 1
        print(fatorial)
            

if __name__ == '__main__':
    main()
    print('Teste')