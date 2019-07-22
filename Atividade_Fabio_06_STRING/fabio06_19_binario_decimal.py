'''
MUDAR:
PEGAR A POSICAO DE [I] E INVERTER-LA ((0/1/2/3) → (3/2/1/0)),
PEGANDO O VALOR NA POSICAO E, SE DIFERENTE DE "1", 
ELEVA AO QUADRADO ATÉ A POSICAO[0]
'''

def main():
    binario = input('Digite o valor em binario: ')
    print('Valor em decimal: %s' %valor_decimal(binario))


def valor_decimal(binario):
    i = 0
    valor_decimal = ''
    
    while i < len(binario):
        if i==0:
            potencia = 8
            valor_decimal += str(calculo(binario, i, potencia))
        
        elif i==1:
            potencia = 4
            soma = int(valor_decimal) + calculo(binario, i, potencia)
            valor_decimal = str(soma) 

        elif i==2:
            potencia = 2
            soma = int(valor_decimal) + calculo(binario, i, potencia)
            valor_decimal = str(soma) 

        elif i==3:
            potencia = 1
            soma = int(valor_decimal) + calculo(binario, i, potencia)
            valor_decimal = str(soma) 

        i += 1

    return valor_decimal


def calculo(binario, i, potencia):
    int_binario = int(binario[i])
    valor = potencia * int_binario
    
    return valor


if __name__ == '__main__':
    main()    
