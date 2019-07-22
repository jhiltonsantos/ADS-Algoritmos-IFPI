def main():
    dia_atual = int(input('Dia atual: '))
    mes_atual = int(input('Mes atual: '))
    ano_atual = int(input('Ano atual: '))
    
    dia_nasc = int(input('Dia do nascimento: '))
    mes_nasc = int(input('Mes do nascimento: '))
    ano_nasc = int(input('Ano do nascimento: '))
    
    ano = ano_atual - ano_nasc
    mes = mes_atual - mes_nasc
    dia = dia_atual - dia_nasc

    if 0 <= ano:
        if mes >= 0 and dia >= 0:
            print('Idade: {} ano(s), {} mes(es), {} dia(s).'\
                .format(ano,mes,dia))
        else:
            print('Data invalida!!!')
    else:
        print('Data Invalida')



if __name__ == '__main__':
    main()     