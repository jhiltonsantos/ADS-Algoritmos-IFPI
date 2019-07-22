def main():
    # entrada
    distancia_percorrida = int(input())
    valor_real = float(input())

    # processamento
    consumo = distancia_percorrida / valor_real
    # saida
    print('{:.3f} km/l'.format(consumo))

    
if __name__ == '__main__':
    main() 