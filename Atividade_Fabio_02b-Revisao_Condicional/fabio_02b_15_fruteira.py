def main():
    # Entrada
    kg_morango = float(input('Quantidade (em Kg) de morango: '))
    kg_maca = float(input('Quantidade (em Kg) de maçã: '))

    # Morango
    if kg_morango <= 5:
        valor_morango = 2.50 * kg_morango
    else:
        valor_morango = 2.20 * kg_morango
    # Maça
    if kg_maca <= 5:
        valor_maca = 1.8 * kg_maca
    else:
        valor_maca = 1.5 * kg_maca
    
    soma_frutas = kg_maca + kg_morango
    valor_total = valor_morango + valor_maca
    
    if soma_frutas > 8 or valor_total > 25:
        desconto = valor_total - (valor_total * 0.1)
        print('\nValor Morango: R${:.2f}\nValor Maçã: R${:.2f}\nValor com desconto: R${:.2f}\n'\
            .format(valor_morango,valor_maca,desconto))
    else:
        print('\nValor Morango: R${:.2f}\nValor Maçã: R${:.2f}\nValor sem desconto: R${:.2f}\n'\
            .format(valor_morango,valor_maca,valor_total))


if __name__ == '__main__':
    main()
