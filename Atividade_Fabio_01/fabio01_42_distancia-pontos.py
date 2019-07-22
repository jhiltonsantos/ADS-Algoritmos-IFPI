# entrada
ponto1_x1 = float (input('Digite o valor de x1 no ponto um: '))
ponto1_y1 = float (input('Digite o valor de y1 no ponto um: '))
ponto2_x2 = float (input('Digite o valor de x2 no ponto dois: '))
ponto2_y2 = float (input('Digite o valor de y2 no ponto dois: '))

# processamento
distancia_pontos = ((ponto2_x2 - ponto1_x1)**2 + (ponto2_y2 - ponto1_y1)**2) ** (1/2)

# saida
print('O valor da distancia dos pontos sera de: {}'.format(distancia_pontos))