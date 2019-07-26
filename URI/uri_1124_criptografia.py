def main():
    n = int(input())
    i = 0
    while i < n:
        frase = input()
        print(criptografia(frase))
        i += 1


def criptografia(frase):
    primeira = primeira_etapa(frase)
    segunda = primeira[::-1]
    criptografada = ultima_etapa(segunda)

    return criptografada


def primeira_etapa(frase):
    etapa_um = ''
    for i in range(len(frase)):
        if (ord(frase[i])>=65 and ord(frase[i])<=90) or\
            (ord(frase[i])>=97 and ord(frase[i])<=122):
            etapa_um += chr(ord(frase[i]) + 3)
        else:
            etapa_um += frase[i]

    return etapa_um


def ultima_etapa(frase):
    metade = int(len(frase)/2)
    soma = ''
    for i in range(len(frase)):
        if i >= metade:
            soma += chr(ord(frase[i]) - 1)
        else:
            soma += frase[i]

    return soma


main()