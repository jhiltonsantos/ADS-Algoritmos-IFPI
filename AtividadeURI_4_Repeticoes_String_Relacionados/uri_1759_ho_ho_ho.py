def main():
    quant_ho = int(input())
    saida = ''
    
    for i in range(quant_ho):
        if i+1 < quant_ho:
            saida += 'Ho '
        else:
            saida += 'Ho!' 

    print(saida)

main()