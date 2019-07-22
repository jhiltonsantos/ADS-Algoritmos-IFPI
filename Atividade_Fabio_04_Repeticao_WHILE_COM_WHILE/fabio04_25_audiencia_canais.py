def main():
    # Leia dados da entrevista
    num_canal,num_pessoas = dados()
    
    #  Determina quantas pessoas assistem e quais canais
    canal_2,canal_4,canal_5,canal_7,canal_10,num_total_pessoas\
         = resultado_pesquisa(num_canal,num_pessoas)
    
    # Porcentagem de audiencia para cada canal
    porcent_c2,porcent_c4,porcent_c5,porcent_c7,porcent_c10 = \
        porcentagem_canais(canal_2,canal_4,canal_5,canal_7,canal_10,num_total_pessoas)
    
    # Imprimi resultado da pesquisa por porcentagem
    print('\nQuantidade total de pessoas: %d'%num_total_pessoas)
    print('Percentual para o canal 2: %.2f'%porcent_c2,'%')
    print('Percentual para o canal 4: %.2f'%porcent_c4,'%')
    print('Percentual para o canal 5: %.2f'%porcent_c5,'%')
    print('Percentual para o canal 7: %.2f'%porcent_c7,'%')
    print('Percentual para o canal 10: %.2f'%porcent_c10,'%')


def dados():
    num_canal = int(input('Digite o numero do canal: '))
    while (num_canal!=2) and (num_canal!=4) and\
        (num_canal!=5) and (num_canal!=7) and (num_canal!=10) and (num_canal!=0):
        print('\nCANAL INVALIDO!!!\n')
        print('Canais validos: 2/4/5/7/10')
        num_canal = int(input('Digite o numero do canal: '))
    
    if num_canal != 0: 
        num_pessoas = int(input('Quantidade de pessoas que assistem: '))
    else:
        num_pessoas = 0

    return num_canal,num_pessoas


def resultado_pesquisa(num_canal,num_pessoas):
    pessoas_c2 = 0
    pessoas_c4 = 0
    pessoas_c5 = 0
    pessoas_c7 = 0
    pessoas_c10 = 0

    num_total_pessoas = 0

    while num_canal != 0:
        if num_canal == 2:
            pessoas_c2 = pessoas_c2 + num_pessoas
        elif num_canal == 4:
            pessoas_c4 = pessoas_c4 + num_pessoas
        elif num_canal == 5:
            pessoas_c5 = pessoas_c5 + num_pessoas
        elif num_canal == 7:
            pessoas_c7 = pessoas_c7 + num_pessoas
        elif num_canal == 10:
            pessoas_c10 = pessoas_c2 + num_pessoas

        num_total_pessoas = num_total_pessoas + num_pessoas    
        num_canal,num_pessoas = dados()
        
    return pessoas_c2,pessoas_c4,pessoas_c5,pessoas_c7,pessoas_c10,num_total_pessoas


def porcentagem_canais(c2,c4,c5,c7,c10,num_pessoas):
    p_c2 = (c2*100) / num_pessoas
    p_c4 = (c4*100) / num_pessoas
    p_c5 = (c5*100) / num_pessoas
    p_c7 = (c7*100) / num_pessoas
    p_c10 = (c10*100) / num_pessoas

    return p_c2,p_c4,p_c5,p_c7,p_c10


if __name__ == '__main__':
    main()