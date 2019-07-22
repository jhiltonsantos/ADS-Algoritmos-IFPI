def main():
    while True:
        try:
            frase = []
            frase = input().split()
            for i in range(len(frase)):
                frase[i] = transforma_palavra_em_minuscula(frase[i])
            quantidade_aliteracao(frase)
        except EOFError:
            break


def transforma_palavra_em_minuscula(palavra):
    i = 0
    nova_str = ''
    while i < len(palavra):
        letra = palavra[i]
        if (ord(letra)>=65) and (ord(letra)<=90):
            letra = chr(ord(letra)+32)
            nova_str += letra
        else:
            nova_str += palavra[i]
        i += 1
    return nova_str


def quantidade_aliteracao(frase):
    quant_aliteracao = 0
    i = 0
    j = 0
    
    while i < len(frase):
        palavra = frase[i]
        if i != 0:
            anterior = frase[i-1]
        else:
            anterior = '0'
        
        if palavra[0] == anterior[0] and j == 0:
            j = 1
            quant_aliteracao += 1
        elif palavra[0] != anterior[0]:
            j = 0
        i += 1

    print(quant_aliteracao)


if __name__ == '__main__':
    main()