from tools_string import inverter_frase

def main():
    frase = input('Digite a frase: ')
    
    frase_invertida = inverter_frase(frase)
    frase_criptografada = substituir_maisculas(frase_invertida)

    print('Frase Criptografada: %s' % frase_criptografada)


def substituir_maisculas(frase):
    i = 0
    nova_frase = ''

    while i < len(frase):
        if (ord(frase[i])>=65) and (ord(frase[i])<=90):
            nova_frase += chr(35) # ASCII(35) ► '#'
        else:
            nova_frase += frase[i]
        i += 1

    return nova_frase


if __name__ == '__main__':
    main()