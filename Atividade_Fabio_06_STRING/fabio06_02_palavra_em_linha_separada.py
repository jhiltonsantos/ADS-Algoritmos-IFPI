def main():
    frase = input('Digite a frase: ')
    palavras_separada(frase)


def palavras_separada(frase):
    letra = 1   
    while letra <= len(frase):
        letra_sep = ord(frase[letra-1])
        if letra_sep == 32: # ASCII(32) » SPACE
            print(chr(13)) # ASCII(13) » ENTER
        else:
            print(chr(letra_sep), end='')
            
            
        letra += 1


if __name__ == '__main__':
    main()