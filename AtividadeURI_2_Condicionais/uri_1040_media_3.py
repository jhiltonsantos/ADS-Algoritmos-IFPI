def main():
    dados = input().split(" ")
    numero_1, numero_2, numero_3, numero_4 = map(float, dados)
    
    p1 = 2
    p2 = 3
    p3 = 4
    p4 = 1
    media = ((numero_1*p1) + (numero_2*p2) + (numero_3*p3) + (numero_4*p4)) / (p1+p2+p3+p4) 
    print('Media: {:.1f}'.format(media))
        
    if media >= 7.0:
        print('Aluno aprovado.')
    
    elif (media >= 5.0) and (media < 6.9):
        print('Aluno em exame.')
        
        nota_exame = float(input())
        print('Nota do exame: {:.1f}'.format(nota_exame))
        media_exame = ((nota_exame+media) / 2)
        
        if  media_exame >= 5.0:
            print('Aluno aprovado.')
            print('Media final: {:.1f}'.format(media_exame))
        else:
            print('Aluno reprovado.')
            print('Media final: {:.1f}'.format(media_exame))
    
    else:
        print('Aluno reprovado.')


if __name__ == '__main__':
    main()
