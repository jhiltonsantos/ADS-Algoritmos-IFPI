def main():
    quant_casos = int(input())
    
    i =0
    while i < quant_casos:
        numero = int(input())
        print('Fib(%d) = %d' % (numero, fibonnaci(numero)))
        i += 1


def fibonnaci(numero):
    a = 0
    b = 1
    for i in range(numero):
        a, b = b, a+b
    return a


main()