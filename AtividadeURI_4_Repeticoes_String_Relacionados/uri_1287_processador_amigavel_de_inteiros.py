def main():
    while True:
        try:
            valor = input()
            str_valor = transforma(valor)
        
            if str_valor.isdigit():
                int_valor = int(str_valor)
                if int_valor > 2147483647:
                    print('error')
                elif int_valor < 0:
                    print('error')
                else:
                    print(int_valor)
            else:
                print('error')
            
        except EOFError:
            break


def transforma(valor):
    valor_processado = ''
    
    for i in range(len(valor)):
        if (valor[i]=='O') or (valor[i]=='o'):
            valor_processado += '0'
        elif (valor[i]=='l'):
            valor_processado += '1'
        elif (valor[i]==' ') or (valor[i]==','):
            valor_processado += ''
        else:
            valor_processado += valor[i]
    
    return valor_processado


if __name__ == '__main__':
    main()