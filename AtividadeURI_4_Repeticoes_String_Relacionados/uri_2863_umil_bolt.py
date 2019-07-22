def main():
    while True:
        try:
            quant_tentativas = int(input())
            
            i = 0
            menor = 999
            while i < quant_tentativas:
                tempo = float(input())
                if tempo < menor:
                    menor = tempo
                i += 1
            
            print('%.2f' % menor)

        except EOFError:
            break


main()