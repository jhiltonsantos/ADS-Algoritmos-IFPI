def main():
    quant_teste = int(input(''))

    for i in range(quant_teste):
        frase = input('')
        print(descriptografar(frase))


def descriptografar(frase):
    frase_desc = ''
    for i in range(len(frase)):
        if (ord(frase[i])>=97) and \
                (ord(frase[i])<=122):
            frase_desc += frase[i]

    return frase_desc[::-1]


if __name__ == '__main__':
    main()
