def main():
    distancia_percorrida,quant_litros_consumido =\
         aparelho_de_desempenho()
    
    consumo,distancia_acomulada,litros_gasolina =\
        calculo_distancia(distancia_percorrida,quant_litros_consumido)
    
    print('\nConsumo: %.2f'%consumo,'km/l.')
    print('Distancia percorrida: %.2f'%distancia_acomulada,'km.')
    print('Quantidade de litros de gasolina que restou: %.2f'\
        %litros_gasolina,'l.')


def aparelho_de_desempenho():
    distancia_percorrida = float(input('Qual a distancia percorrida desde a ultima medicao: '))
    quant_litros_consumido = float(input('Quantidade de gasolina consumida: '))

    return distancia_percorrida,quant_litros_consumido


def calculo_distancia(distancia_percorrida,quant_litros_consumido):
    distancia_acomulada = 0
    litros_gasolina = 50

    while distancia_acomulada < 600 and litros_gasolina >= 0:
        
        distancia_acomulada = distancia_acomulada + distancia_percorrida
        litros_gasolina = litros_gasolina - quant_litros_consumido

        if distancia_acomulada < 600 and litros_gasolina <= 0:
            print('\nO carro nao chegou ao destino!!!')
            break
        elif distancia_acomulada < 600 and litros_gasolina >=0:
            distancia_percorrida,quant_litros_consumido = aparelho_de_desempenho()
        
    consumo = distancia_acomulada/50

    return consumo,distancia_acomulada,litros_gasolina


if __name__ == '__main__':
    main()