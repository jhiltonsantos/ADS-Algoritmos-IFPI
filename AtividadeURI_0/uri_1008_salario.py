
def main():
    n_func = int(input())
    hora_func = int(input())
    valor_hora = float(input())

    salario = hora_func * valor_hora

    print('NUMBER = {}'.format(n_func))
    print('SALARY = U$ {:.2f}'.format(salario))

if __name__ == '__main__':
    main()
    