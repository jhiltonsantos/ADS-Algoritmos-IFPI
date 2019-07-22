def main():
    valor_n = int(input())
    cont = 1
    total = 0
    coelho = 0
    sapo  = 0
    rato = 0

    while cont <= valor_n:
        quantidade, tipo = map(str, input().split())
        quant = int(quantidade)
        if tipo == 'C':
            coelho = coelho + quant
        elif tipo == 'R':
            rato = rato + quant
        elif tipo == 'S':
            sapo = sapo + quant
        
        total = total + quant
        cont += 1
    
    per_coelho = (coelho*100)/total
    per_sapo = (sapo*100)/total
    per_rato = (rato*100)/total
    
    # Saida
    print('Total: {} cobaias'.format(total))
    print('Total de coelhos: {}'.format(coelho))
    print('Total de ratos: {}'.format(rato))
    print('Total de sapos: {}'.format(sapo))
    print('Percentual de coelhos: {:.2f} %'.format(per_coelho))
    print('Percentual de ratos: {:.2f} %'.format(per_rato))
    print('Percentual de sapos: {:.2f} %'.format(per_sapo))


if __name__ == '__main__':
    main()