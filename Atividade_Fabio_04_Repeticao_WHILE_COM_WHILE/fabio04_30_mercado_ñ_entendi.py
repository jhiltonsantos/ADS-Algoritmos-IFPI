# NAO ENTENDI A QUESTAO
from tools import get_valor_float_positivo,get_valor_int_positivo

def main():
    nome = input('Nome do produto: ')
    print('Preco do produto:',end=' ')
    preco = get_valor_float_positivo()
    print('Quantidade de produtos:',end=' ')
    quantidade = get_valor_int_positivo()

    valor_preco_quant = preco * quantidade
    valor_pago = valor_preco_quant
    quantidade_total = quantidade
    
    while nome != 'FIM':
        nome = input('Nome produto: ')
        if nome != 'FIM':
            quantidade = int(input('quantide: '))
        
            valor_preco_quant = preco * quantidade

            quantidade_total = quantidade_total + quantidade
            valor_pago = valor_pago + valor_preco_quant

    if quantidade_total <= 10:
        preco_pago_total = valor_pago
    elif quantidade_total >= 11 and quantidade_total <=20:
        preco_pago_total = valor_pago - (valor_pago*0.01)
    elif quantidade_total >= 21 and quantidade <=50:
        preco_pago_total = valor_pago - (valor_pago*0.02)
    else:
        preco_pago_total = valor_pago - (valor_pago*0.025)

    print('Valor total pago: %.2f'%preco_pago_total)


if __name__ == '__main__':
    main()