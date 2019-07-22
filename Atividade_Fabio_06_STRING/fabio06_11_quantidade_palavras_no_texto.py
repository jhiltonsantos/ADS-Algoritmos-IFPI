def main():
    texto = input('Digite o texto: ')

    print('Quantidade de palavras no texto: %d palavras.'\
         % quantidade_de_palavras(texto))


def quantidade_de_palavras(texto):
    quant_palavras = 0
    i = 0
    
    while i < len(texto):
        if (ord(texto[i])==32) and (ord(texto[i-1])==32):
            quant_palavras += 0
        elif ord(texto[i]) == 32:
            quant_palavras += 1
        
        i += 1
    
    if ord(texto[len(texto)-1]) == 32:
        quant_palavras -= 1     

    return quant_palavras + 1


if __name__ == '__main__':
    main()