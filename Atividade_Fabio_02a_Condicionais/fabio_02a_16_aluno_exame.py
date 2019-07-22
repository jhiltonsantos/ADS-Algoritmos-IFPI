def main():
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))

    media = (nota_1+nota_2) / 2

    if media >= 7:
        print('Aprovado')
    elif 2 < media < 7:
        exame = float(input('Nota do exame: '))
        media_exame = media + exame / 2
        if media_exame >= 5:
            print('Aprovado')
        else:
            print('Reprovado')
    else:
        print('Reprovado')


if __name__ == '__main__':
    main()