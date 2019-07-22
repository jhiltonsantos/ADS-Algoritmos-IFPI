def main():
    numero = int(input('Digite o limite: '))
    contador = 1
    
    while contador <= numero:
        if contador == 1:
            soma = 1
        else:
            soma = soma + contador
        
        contador += 1
    
    print(f'O somatório é: {soma}')


if __name__ == '__main__':
    main()