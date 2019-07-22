def main():
    quant_casos = int(input())
    i = 0

    while i < quant_casos:
        nome_vilao = input()
        print(capturado_ou_nao(nome_vilao))
        i += 1


def capturado_ou_nao(nome):
    if nome != 'Batmain':
        return 'Y'
    else:
        return 'N'


main()