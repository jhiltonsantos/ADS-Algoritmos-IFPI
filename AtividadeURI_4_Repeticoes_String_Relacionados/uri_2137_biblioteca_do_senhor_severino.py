def main():
    while True:
        try:
            
            n = int(input())
            i = 0
            v_livro = []

            # Cod_Livro no vetor
            while i < n:
                cod_livro = input()
                if len(cod_livro)<4:
                    cod_livro = cod_livro[::-1]
                    quant = 4 - len(cod_livro)
                    cod_livro += quant*'0'
                    cod_livro = cod_livro[::-1]         
                v_livro += [cod_livro]
                i += 1

            v_livro = sorted(v_livro)
            for i in range(len(v_livro)):
                print(v_livro[i])

        except EOFError:
            break


main()
