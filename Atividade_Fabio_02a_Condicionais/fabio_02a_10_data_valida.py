def main():
    print('Qual a data(separe por /): ')
    d,m,a = input().split("/")
    dia = int(d)
    mes = int(m)
    ano = int(a)
    modulo = abs(2016 - ano)
    
    if 0 < dia<=31 and 0 < mes<=12 and ano<=2019:
        if dia<= 31 and mes==1 or mes==3 or \
            mes==5  or mes==7 or mes==8 or mes==10 or mes==12:
            print('Data valida!!!')
        elif dia<=30 and mes==4 or mes==6 or mes==9 or mes==11:
            print('Data valida!!!')
        elif dia<=28 and mes==2:
            print('Data valida!!!')
        elif dia==29 and mes==2 and modulo==4 or modulo==0:
            print('Data valida!!! Ano Bissexto!!!')
        else:
            print('Data Invalida')
    else:
        print('Data invalida!!!')
    
if __name__ == '__main__':
    main()