def main():
    pergunta_1 = bool(input('Telefonou para a vitima? (1-Sim||0-Nao) '))
    pergunta_2 = bool(input('Esteve no local do crime? (1-Sim||0-Nao) '))
    pergunta_3 = bool(input('Mora perto da vitima? (1-Sim||0-Nao) '))
    pergunta_4 = bool(input('Devia para a vitima? (1-Sim||0-Nao) '))
    pergunta_5 = bool(input('Ja trabalhou com a vitima? (1-Sim||0-Nao) '))

    if pergunta_1 == False:
        p1 = int(pergunta_1)
        p1 == 0
    else:
        p1 = int(pergunta_1)
        p1 == 1

    if pergunta_2 == False:
        p2 = int(pergunta_2)
        p2 == 0
    else:
        p2 = int(pergunta_2)
        p2 == 1

    if pergunta_3 == False:
        p3 = int(pergunta_3)
        p3 == 0
    else:
        p3 = int(pergunta_3)
        p3 == 1

    if pergunta_4 == False:
        p4 = int(pergunta_4)
        p4 == 0
    else:
        p4 = int(pergunta_4)
        p4 == 1

    if pergunta_5 == False:
        p5 = int(pergunta_5)
        p5 == 0
    else:
        p5 = int(pergunta_5)
        p5 == 1
    
    soma = p1 + p2 + p3 + p4 + p5
    
    print(soma)
    if soma == 2:
        print('Suspeita')
    elif soma == 3 or soma == 4:
        print('Cumplice')
    elif soma == 5:
        print('Assassino')
    elif soma == 1 or soma == 0:
        print('Inocente')
    else:
        print('Valor invalido')
    

if __name__ == '__main__':
    main()
