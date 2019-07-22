def main():
    numero = int(input('Digite o numero: '))
    
    if numero > 1000:
        print('Valor Invalido!')
    
    else:
        centena = numero // 100
        resto_centena = numero % 100
        dezena = resto_centena // 10
        unidade = resto_centena % 10
    
        # Plural
        if centena == 1:
            print_centena = '{} centena'.format(centena)
        else:
            print_centena = '{} centenas'.format(centena)
        
        if dezena == 1:
            print_dezena = '{} dezena'.format(dezena)
        else:
            print_dezena = '{} dezenas'.format(dezena)
        
        if unidade == 1:
            print_unidade = '{} unidade'.format(unidade)
        else:
            print_unidade = '{} unidades'.format(unidade)
        
        # Imprimir
        if centena == 0 and dezena == 0:
            print('{}.'.format(print_unidade))
        elif dezena == 0 and unidade == 0:
            print('{}.'.format(print_centena))
        elif centena > 0 and dezena == 0:
            print('{} e {}.'.format(print_centena, print_unidade))
        elif centena == 0 and unidade == 0:
            print('{}.'.format(print_dezena))
        elif unidade == 0:
            print('{},{}.'.format(print_centena,print_dezena))
        elif centena > 0:
            print('{}, {} e {}.'\
                .format(print_centena, print_dezena, print_unidade))
        elif centena == 0:
            print('{} e {}.'.format(print_dezena, print_unidade))
       

if __name__ == '__main__':
    main()
