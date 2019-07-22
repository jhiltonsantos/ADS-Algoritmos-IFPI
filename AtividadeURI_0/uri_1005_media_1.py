
def main():
    valor_a = float(input())
    valor_b = float(input())

    nota_a = valor_a * 3.5
    nota_b = valor_b * 7.5

    media = (nota_a + nota_b) / 11

    print('MEDIA = {:.5f}'.format(media))


if __name__ == '__main__':
    main()