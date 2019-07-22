# Questao INCOMPLETA
def main():
    valor_n = int(input('Quantidade de funcionarios: '))
    cont = 1
    
    while cont <= valor_n:
        codigo,horas_trabalhadas,numero_dependentes = recebe_ficha()
        
        desconto_inss,desconto_ir,salario_liquido =\
             calculo_salario(horas_trabalhadas,numero_dependentes)
        cont += 1

        imprimir(codigo,horas_trabalhadas,\
            numero_dependentes,desconto_inss,desconto_ir,salario_liquido)


def recebe_ficha():
    codigo = int(input('Codigo do funcionario: '))    
    horas_trabalhadas = int(input('Quantidade de horas trabalhadas: '))
    numero_dependentes = int(input('Numero de dependentes: '))
    return codigo,horas_trabalhadas,numero_dependentes


def calculo_salario(horas_trabalhadas,numero_dependentes):
    valor_horas_trabalhadas = horas_trabalhadas * 12
    valor_dependentes = numero_dependentes * 40
    salario_bruto = valor_horas_trabalhadas + valor_dependentes
    desconto_inss = salario_bruto * 0.085
    desconto_ir = salario_bruto * 0.05
    salario_liquido = salario_bruto - (desconto_inss+desconto_ir)
    return desconto_inss, desconto_ir, salario_liquido


def imprimir(codigo,horas_trabalhadas,numero_dependentes,\
    desconto_inss, desconto_ir,salario_liquido):
    print('_________FICHA____________')
    print('Codigo:  %d'%codigo)
    print('Horas Trabalhadas: %d'%horas_trabalhadas)
    print('Numero De Dependetes: %d'%numero_dependentes)
    print('Desconto INSS:  R$%.2f'%desconto_inss)
    print('Desconto IR: R$%.2f'%desconto_ir)
    print('Valor Liquido: R$%.2f'%salario_liquido)
    

if __name__ == '__main__':
    main()