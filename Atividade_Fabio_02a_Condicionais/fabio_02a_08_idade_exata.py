def main():
    dia_atual = int(input('Dia atual: '))
    mes_atual = int(input('Mes atual: '))
    ano_atual = int(input('Ano atual: '))
    
    dia_nasc = int(input('Dia do nascimento: '))
    mes_nasc = int(input('Mes do nascimento: '))
    ano_nasc = int(input('Ano do nascimento: '))
    
    calc_dia = dia_atual - dia_nasc
    calc_mes = mes_atual - mes_nasc
    
    if calc_dia > 0 and calc_mes > 0:
        idade = ano_atual - ano_nasc
        print('{} anos.'.format(idade))
    elif calc_dia < 0 and calc_mes > 0:
        idade = ano_atual - ano_nasc
        print('{} anos.'.format(idade))
    elif calc_dia > 0 and calc_mes == 0:
        idade = ano_atual - ano_nasc
        print('{} anos.'.format(idade))
    else:
        idade = (ano_atual - ano_nasc) - 1
        print('{} anos.'.format(idade))
           

if __name__ == '__main__':
    main()