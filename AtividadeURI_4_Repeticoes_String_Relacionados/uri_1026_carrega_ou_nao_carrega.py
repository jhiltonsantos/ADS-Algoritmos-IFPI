def main():
    while True:
        try:
            x, y = map(int, input().split())
            
            bin_x = bin(x)[2::]
            bin_y = bin(y)[2::]
            
            resultado_bin = calculo(bin_x, bin_y)
            decimal_resultado = binario_p_decimal(resultado_bin)
            print(decimal_resultado)

        except EOFError:
            break


def binario_p_decimal(valor):
    decimal = 0
    valor = valor[::-1]
    
    for i in range(len(valor)):
        if valor[i] == '1':
            decimal += 2**i

    return decimal


def maior(bin_x, bin_y):
    inverte_x = bin_x[::-1]
    inverte_y = bin_y[::-1]
    
    if len(inverte_x) > len(inverte_y):
            quant = len(inverte_x) - len(inverte_y)
            inverte_y += (quant*'0')

    if len(inverte_x) < len(inverte_y):
            quant = len(inverte_y) - len(inverte_x)
            inverte_x += (quant*'0')
        
    return inverte_x, inverte_y
    

def calculo(bin_x, bin_y):
    valor = ''
    inverte_x , inverte_y = maior(bin_x,bin_y)
    
    for i in range(len(inverte_x)):
        if ((inverte_x[i]=='0') and (inverte_y[i]=='1')) or\
            ((inverte_x[i]=='1') and (inverte_y[i]=='0')):
            valor += '1'
        else:
            valor += '0'

    return valor[::-1]


if __name__ == '__main__':
    main()