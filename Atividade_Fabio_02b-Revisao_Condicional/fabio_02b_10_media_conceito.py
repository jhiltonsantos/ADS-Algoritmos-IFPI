def main():
    nota_a = float(input('Digite a primeira nota: '))
    nota_b = float(input('Digite a segunda nota: '))

    media = (nota_a+nota_b) / 2

    if 9 <= media < 10:
        print('Media {}, Nota conceito: A. APROVADO.'.format(media))
    elif 7.5 <= media < 9:
        print('Media {}, Nota conceito: B. APROVADO.'.format(media))
    elif 6 <= media < 7.5:
        print('Media {}, Nota conceito: C. APROVADO.'.format(media))
    elif 4 <= media < 6:
        print('Media {}, Nota conceito: D. REPROVADO.'.format(media))
    elif 0 <= media < 4:
        print('Media {}, Nota conceito: E. REPORVADO.'.format(media))


if __name__ == '__main__':
    main()
