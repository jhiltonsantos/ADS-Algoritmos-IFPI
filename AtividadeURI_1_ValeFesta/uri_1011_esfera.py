
def main():
    # entrada
    raio = float(input())

    # processamento
    pi = 3.14159
    volume_esfera = (4/3) * pi * (raio**3)

    # saida
    print('VOLUME = {:.3f}'.format(volume_esfera))



if __name__ == '__main__':
    main()
    