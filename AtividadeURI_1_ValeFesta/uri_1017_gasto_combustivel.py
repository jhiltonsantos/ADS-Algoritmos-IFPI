def main():
    # entrada
    tempo_gasto = int(input())
    v_media = int(input())
    
    # processamento
    consumo = 12
    valor_gasto = (tempo_gasto*v_media) / consumo

    # saida
    print('{:.3f}'.format(valor_gasto))

if __name__ == '__main__':
    main()