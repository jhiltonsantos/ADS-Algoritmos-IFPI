def main():
    numero_consultas = int(input())
    
    while numero_consultas != 0:
        ponto_div_n, ponto_div_m = \
            map(int, input().split())
        
        ponto_x_y(ponto_div_n,ponto_div_m,numero_consultas)
        numero_consultas = int(input())


def ponto_x_y(div_n,div_m,num_consulta):
    for i in range(num_consulta):
        c_x, c_y = \
            map(int, input().split())
        
        if (c_x==div_n or c_x==div_m) or \
            (c_y==div_n or c_y==div_m):
            print('divisa')
        elif c_x > div_n and c_y > div_m:
            print('NE')
        elif c_x < div_n and c_y > div_m:
            print('NO')
        elif c_x < div_n and c_y < div_m:
            print('SO')
        elif c_x > div_n and c_y < div_m:
            print('SE')


if __name__ == '__main__':
    main()