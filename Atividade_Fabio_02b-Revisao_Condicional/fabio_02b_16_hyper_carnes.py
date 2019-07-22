def main():
    tipo_carne = input('Tipo de carne(F-File|A-Alcatra|P-Picanha): ')
    quant_carne = float(input('Quantidade de carne(kg): '))
    tipo_compra = input('Compra feita com: (D-Dinheiro|C-Cartao Tabajara) ')

    if tipo_carne == 'F' or tipo_carne == 'A' or tipo_carne == 'P':
        if tipo_carne == 'F':
            tipo_carne = 'File    '
            if quant_carne <= 5:
                valor = 4.9 * quant_carne
            else:
                valor = 5.8 * quant_carne
        # Alcatra
        elif tipo_carne == 'A':
            tipo_carne = 'Alcatra '
            if quant_carne <= 5:
                valor = 5.9 * quant_carne
            else:
                valor = 6.8 * quant_carne
        # Picanha
        elif tipo_carne == 'P':
            tipo_carne = 'Picanha '
            if quant_carne <= 5:
                valor = 6.9 * quant_carne
            else:
                valor = 7.8 * quant_carne
        # Tipo compra
        if tipo_compra == 'D' or tipo_compra == 'C':
            if tipo_compra == 'D':
                tipo_compra = 'Dinheiro       '
                desconto = 0
                valor_total = valor - desconto
            elif tipo_compra == 'C':
                tipo_compra = 'Cartao Tabajara'
                desconto = valor * 0.05
                valor_total = valor - desconto
            #37 12 10 10
            #Cupom Fiscal
            print('\n************Cupom Fiscal************\
                    \n*Tipo de carne: {}           *\
                    \n*Quantidade de carne(kg): {}      *\
                    \n*Preco: R${:.2f}                    *\
                    \n*Tipo de pagamento: {}*\
                    \n*Valor do desconto: R${:.2f}         *\
                    \n*Valor a pagar: R${:.2f}            *\
                    \n************************************\n'\
                    .format(tipo_carne,quant_carne,valor,tipo_compra,desconto,valor_total))    
        else:
            print('Tipo de compra invalido!')
    else:
        print('Tipo de carne invalido!')


if __name__ == '__main__':
    main()