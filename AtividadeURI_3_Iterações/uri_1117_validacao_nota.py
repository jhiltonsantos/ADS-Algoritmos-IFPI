def main():
    nota = 0
    cont = 1
    soma = 0

    while (nota < 0 or nota > 10) or cont <=2:
        nota = float(input())
        
        if 0 <= nota <= 10:
            soma = soma + nota
            cont += 1
        else:
            print('nota invalida')
    
    media = soma / 2
    print('media = {:.2f}'.format(media))
        
    
if __name__ == '__main__':
    main()