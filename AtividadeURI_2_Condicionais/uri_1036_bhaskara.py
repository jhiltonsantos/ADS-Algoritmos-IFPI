def main():
    valor_a, valor_b, valor_c = map(float, input().split(" "))
    
    delta = (valor_b**2) - (4*valor_a*valor_c)
    
    
    if valor_a == 0 or delta <=0:
        print('Impossivel calcular')
    
    else:
        
        x_r1 = (-valor_b + (delta ** (1/2))) / (2 * valor_a)
        x_r2 = (-valor_b - (delta ** (1/2))) / (2 * valor_a)
        print('R1 = {:.5f}'.format(x_r1))
        print('R2 = {:.5f}'.format(x_r2))


if __name__ == '__main__':
    main()