def main():
    valor_n = int(input('Valor: '))
    maior = valor_n
    novo_valor = 1
    
    while novo_valor == 1:
        if valor_n > maior:
            maior = valor_n     
            
        novo_valor = int(input('1-Continuar // 2-Encerrar '))
        while novo_valor > 2 or novo_valor < 1:
             novo_valor = int(input('1-Continuar // 2-Encerrar '))
        if novo_valor == 2:
            break

        valor_n = int(input('Valor: '))
        
    print('O maior valor será: ',maior)


if __name__ == '__main__':
    main()
    
         