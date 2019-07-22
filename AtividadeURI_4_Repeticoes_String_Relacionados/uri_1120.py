def main():
    n_falho, valor_original = input().split()

    while n_falho != '0' and valor_original != '0':
        saida = remove_numero_com_falha(n_falho, valor_original)
        print(saida)
        n_falho, valor_original = input().split()


def remove_numero_com_falha(falho, original):
        num_saida = ''
        for i in range(len(original)):
            if original[i] == falho:
                num_saida += ''
            else:
                num_saida += original[i]
        
        if num_saida=='':
            return 0
        else:
            inteiro = int(num_saida)
            return inteiro


if __name__ == '__main__':
    main()