def main():
    nota_um = float(input('Digite a primeira nota: '))
    nota_dois = float(input('Digite a segunda nota: '))

    media = (nota_um + nota_dois) / 2
    
    if nota_um < 0 or nota_um > 10 or nota_dois < 0 or nota_dois > 10:
        print('Nota invalida')
    else: 
        if media == 10.0:
            print('Aprovado com Distincao')
        elif 7 <= media < 10:
            print('Aprovado')
        else:
            print('Reprovado')


if __name__ == '__main__':
    main()
