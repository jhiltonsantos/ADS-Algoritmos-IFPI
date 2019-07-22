def main():
    # entrada
    tempo = int(input())

    # processamento
    hora = tempo // 3600
    resto_hora = tempo % 3600
    minuto = resto_hora // 60
    segundo = resto_hora % 60

    # saida
    print('{}:{}:{}'.format(hora, minuto, segundo))


if __name__ == '__main__':
    main()