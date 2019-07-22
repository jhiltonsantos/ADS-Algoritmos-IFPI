def main():
    quant_casos = input()
    quant_casos = int(quant_casos)
    while quant_casos != 0:
        quant_casos = nomes_e_maior(quant_casos)
        if not(quant_casos == 0):
            print()


def nomes_e_maior(n):
    nome = []
    maior = ''
    
    for i in range(n):
        nome += [input()]
        if len(nome[i]) > len(maior):
            maior = nome[i]
    
    for j in range(len(nome)):
        nome[j] = nome[j][::-1]
        quant = len(maior) - len(nome[j])
        nome[j] += quant*' '
    
        nome[j] = nome[j][::-1]
        print(nome[j])

    
    quant_casos = int(input())    
    return quant_casos


if __name__ == '__main__':
    main()