def main():
    nome,altura,peso = ficha()
    
    nome_alta,alta,nome_baixa,baixa,nome_magra,\
        magra,nome_gorda,gorda = concurso(altura,peso,nome)
    
    print('A modelo mais alta é: %s'%nome_alta,'. Altura: %.1f'%alta)
    print('A modelo mais baixa é: %s'%nome_baixa,'. Altura: %.1f'%baixa)
    print('A modelo mais magra é: %s'%nome_magra,'. Peso: %.1f'%magra)
    print('A modelo mais gorda é: %s'%nome_gorda,'. Peso: %.1f'%gorda)


def ficha():
    nome = input('Digite o nome: ')
    
    if nome != 'FIM':
        altura = float(input('Digite a altura: '))
        peso = float(input('Digite o peso: '))
    else:
        altura = 0
        peso = 0
        
    return nome,altura,peso,


def concurso(altura,peso,nome):
    baixa = altura
    alta = altura
    magra = peso
    gorda = peso
    
    while nome != 'FIM':
        if peso <= magra:
            magra = peso
            nome_magra = nome
        elif peso >= gorda:
            gorda = peso
            nome_gorda = nome
        
        if altura <= baixa:
            baixa = altura
            nome_baixa = nome
        elif altura >= alta:
            alta = altura
            nome_alta = nome
        nome,altura,peso = ficha()
    
    return nome_alta,alta,nome_baixa,baixa,nome_magra,\
        magra,nome_gorda,gorda


if __name__ == '__main__':
    main()