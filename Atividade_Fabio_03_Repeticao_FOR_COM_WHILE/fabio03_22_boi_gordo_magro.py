def main():
    quant_fichas = int(input('Digite a quantidade de fichas: '))
    cont = 2
    n_ident,nome,peso = ficha()
    
    #INICIALIZANDO VARIAVEIS
    peso_anterior = 0
    id_maior,id_menor = n_ident,n_ident
    nome_maior,nome_menor = nome,nome
    maior = peso_anterior
    menor = peso_anterior

    while cont <= quant_fichas:
        if peso > peso_anterior and peso >= maior:
            maior = peso
            id_maior = n_ident
            nome_maior = nome
            
        elif peso < peso_anterior and peso <= menor:
            menor = peso
            id_menor = n_ident
            nome_menor = nome
            
        cont += 1
        peso_anterior = peso
        n_ident,nome,peso = ficha()
    
    print('______FICHA_BOI_MENOR______')
    print('Identificacao: %d'%id_menor,'\nNome: %s'%nome_menor,'\nPeso: %.3f'%menor,'kg')
    
    print('______FICHA_BOI_MAIOR______')
    print('Identificacao: %d'%id_maior,'\nNome: %s'%nome_maior,'\nPeso: %.3f'%maior,'kg')


def ficha():
    n_identificacao = int(input('Numero de identificacao: '))
    nome = input('Nome do boi: ')
    peso = float(input('Peso do boi: '))
    return n_identificacao,nome,peso

if __name__ == '__main__':
    main()