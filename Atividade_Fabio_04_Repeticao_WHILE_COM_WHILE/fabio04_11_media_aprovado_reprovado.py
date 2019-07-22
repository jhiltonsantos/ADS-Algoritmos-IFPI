def main():
    matricula,nota_1,nota_2,nota_3 = informacao_aluno()
    contador = 1
    
    total_alunos,total_aprovados,total_reprovados =\
         calcula_media(matricula,nota_1,nota_2,nota_3,contador)
    
    print('Total de alunos: %d'%total_alunos)
    print('Total de alunos aprovados: %d'%total_aprovados)
    print('Total de alunos reprovados: %d'%total_reprovados)


def informacao_aluno():
    matricula = int(input('Digite a matricula: '))
    
    if matricula != 0:
        n1 = float(input('Digite a primeira nota: '))
        while n1 < 0 or n1 > 10:
            print('NOTA INVALIDA!!!')
            n1 = float(input('Digite a primeira nota: '))

        n2 = float(input('Digite a segunda nota: '))
        while n2 < 0 or n2 > 10:
            print('NOTA INVALIDA!!!')
            n2 = float(input('Digite a segunda nota: '))
        
        n3 = float(input('Digite a terceira nota: '))
        while n3 < 0 or n3 > 10:
            print('NOTA INVALIDA!!!')
            n3 = float(input('Digite a terceira nota: '))
    
    else:
        n1 = None
        n2 = None
        n3 = None

    return matricula,n1,n2,n3


def calcula_media(matricula,nota_1,nota_2,nota_3,contador):
    total_aprovados = 0
    total_reprovados = 0

    while matricula != 0:
        total_aprovados,total_reprovados = \
            media_final(nota_1,nota_2,nota_3,total_aprovados,total_reprovados)
        
        matricula,nota_1,nota_2,nota_3 = informacao_aluno()
        if matricula != 0:
            contador += 1
    
    return contador,total_aprovados,total_reprovados


def media_final(n1,n2,n3,total_aprovados,total_reprovados):
    
    media_final = ((2*n1)+(3*n2)+(5*n3))/10

    if media_final >= 7:
        print('ALUNO APROVADO')
        total_aprovados = total_aprovados + 1
    else:
        print('ALUNO REPROVADO')
        total_reprovados = total_reprovados + 1
    
    return total_aprovados,total_reprovados


if __name__ == '__main__':
    main()
