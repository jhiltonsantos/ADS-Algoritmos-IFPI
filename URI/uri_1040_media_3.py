def main():
    numero_1, numero_2, numero_3, numero_4 = map(float, input().split())
    
    media = ((numero_1*2) + (numero_2*3) + (numero_3*4) + (numero_4*1)) / (2+3+4+1) 
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
