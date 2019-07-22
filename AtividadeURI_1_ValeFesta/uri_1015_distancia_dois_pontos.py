def main():
    # entrada
    x1,y1 = input().split(" ")
    x2,y2 = input().split(" ")
    p1_x = float(x1)
    p1_y = float(y1)
    p2_x = float(x2)
    p2_y = float(y2)
    
    # processamento
    distancia = (((p2_x-p1_x)**2) + ((p2_y-p1_y)**2)) ** (1/2)
    
    # saida
    print('{:.4f}'.format(distancia))


if __name__ == '__main__':
    main() 