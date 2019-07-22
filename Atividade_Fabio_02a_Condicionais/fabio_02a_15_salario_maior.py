def main():
    hora_1 = int(input('Quantidade de horas de aula primeiro professor: '))
    valor_1 = float(input('Valor Hora aula primeiro professor: '))
    hora_2 = int(input('Quantidade de horas de aula segundo professor: '))
    valor_2 = float(input('Valor Hora aula segundo professor: '))

    salario_1 = hora_1 * valor_1
    salario_2 = hora_2 * valor_2

    if salario_1 > salario_2:
        print('Primeiro professor tem o maior salario: R$ {}'\
            .format(salario_1))
    elif salario_1 == salario_2:
        print('Salarios iguais!!!')
    else:
        print('Segundo professor tem o maior salario: R$ {}'\
            .format(salario_2))


if __name__ == '__main__':
    main()