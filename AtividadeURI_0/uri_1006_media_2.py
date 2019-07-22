def main():
    valor_a = float(input())
    valor_b = float(input())
    valor_c = float(input())

    nota_a = valor_a * 2
    nota_b = valor_b * 3
    nota_c = valor_c * 5

    media = (nota_a + nota_b + nota_c) / 10

    print('MEDIA = {:.1f}'.format(media))


if __name__ == '__main__':
    main()
    