def main():
    dia_entregue, dia_final = map(int, input().split())

    if dia_entregue > dia_final or dia_entregue >= 24 :
        print('Eu odeio a professora!')
    elif (dia_entregue<=24) and (dia_entregue <= (dia_final-3)):
        print('Muito bem! Apresenta antes do Natal!')
    else:
        print('Parece o trabalho do meu filho!')
        if (dia_entregue + 2) < 24:
            print('TCC Apresentado!')
        else:
            print('Fail! Entao eh nataaaaal!')


if __name__ == '__main__':
    main()