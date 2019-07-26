def main():
    n = int(input())
    
    for i in range(n):
        p_a, p_b, cres_a, cres_b = map(float, input().split())
        anos = crescimento_populacional(p_a, p_b, cres_a, cres_b)

        if anos > 100:
            print('Mais de 1 seculo.')
        else:
            print('%d anos.' % anos)


def crescimento_populacional(a, b, cres_a, cres_b):
    porc_a = cres_a / 100
    porc_b = cres_b / 100
    quant_anos = 0

    while a <= b:
        crescimento_a = int(a*porc_a)
        crescimento_b = int(b*porc_b)
        a += crescimento_a
        b += crescimento_b
        quant_anos += 1
        
        if quant_anos > 100:
            break

    return quant_anos


main()