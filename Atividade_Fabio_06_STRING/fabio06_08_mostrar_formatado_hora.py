def main():
    hora = input('Digite a hora: ')

    while (len(hora)!=8) or (ord(hora[2])!=58 or ord(hora[5])!=58):
        print('HORA INVALIDA!!! FORMATO VALIDO: HH:MM:SS')
        hora = input('Digite a hora: ')

    print(frase(hora))


def frase(hora):
    i = 0
    nova_frase = ''

    while i < (len(hora)):
        if (ord(hora[i])==58) and (i==2):
            nova_frase +=  hora[i-2] + hora[i-1] + ' hora(s), '
        elif (ord(hora[i])==58) and (i==5):
            nova_frase +=  hora[i-2] + hora[i-1] + ' minuto(s) e '
        elif (i>=7):
            nova_frase +=  hora[i-1] + hora[i] + ' segundo(s).'
        else:
            nova_frase += ''
        i += 1

    return nova_frase


if __name__ == '__main__':
    main()