def main():
    # entrada
    idade_dia = int(input())

    # processamento
    ano = idade_dia // 365
    resto_ano = idade_dia % 365
    mes = resto_ano // 30
    dia = resto_ano % 30

    # saida
    print('{} ano(s)'.format(ano))
    print('{} mes(es)'.format(mes))
    print('{} dia(s)'.format(dia))


if __name__ == '__main__':
    main()