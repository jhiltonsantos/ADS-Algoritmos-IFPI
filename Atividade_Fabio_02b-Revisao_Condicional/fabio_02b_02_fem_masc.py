def main():
    sexo = input('Digite o sexo(F-Feminino || M-Masculino):')

    if sexo == 'F' or sexo == 'f':
        print('Sexo Feminino.')
    elif sexo == 'M' or sexo == 'm':
        print('Sexo Masculino.')
    else:
        print('Sexo Invalido.')


if __name__ == '__main__':
    main()
