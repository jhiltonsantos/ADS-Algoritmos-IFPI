def main():
    frase = input('Digite a frase: ')
    print(numero_por_extenso(frase))


def numero_por_extenso(frase):
    i = 1
    nova_frase = ''

    while i <= len(frase):
        caractere = ord(frase[i-1])
        
        if caractere == 48:
            imprimir = 'ZERO'
        elif caractere == 49:
            imprimir = 'UM'
        elif caractere == 50:
            imprimir = 'DOIS'
        elif caractere == 51:
            imprimir = 'TRES'
        elif caractere == 52:
            imprimir = 'QUATRO'
        elif caractere == 53:
            imprimir = 'CINCO'
        elif caractere == 54:
            imprimir = 'SEIS'
        elif caractere == 55:
            imprimir = 'SETE'
        elif caractere == 56:
            imprimir = 'OITO'
        elif caractere == 57:
            imprimir = 'NOVE'
        else:
            imprimir = chr(caractere)    
        
        nova_frase = nova_frase + imprimir
        
        i += 1

    return nova_frase


if __name__ == '__main__':
    main()