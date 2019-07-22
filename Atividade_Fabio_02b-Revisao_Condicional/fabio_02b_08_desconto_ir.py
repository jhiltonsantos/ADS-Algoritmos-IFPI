def main():
    valor_hora = float(input('Digite o valor da hora trabalhada: '))
    quant_hora = int(input('Digite a quantidade de horas trabalhadas: '))
    
    salario_bruto = valor_hora * quant_hora
    valor_inss = salario_bruto * 0.1
    valor_fgts = salario_bruto * 0.11
    
    # Isento
    if salario_bruto <= 900:
        salario_liquido = salario_bruto - valor_inss
        total_descontos = valor_inss
        
        print('\nSalario Bruto:({}*{})  :R${:.2f}\
            \n(-)IR(0%)     :R$0.00\
            \n(-)INSS(10%)     :R${:.2f}\
            \nFGTS(11%)     :R${:.2f}\
            \nTotal de descontos     :R${:.2f}\
            \nSalario Liquido     :R${:.2f}\n'\
            .format(valor_hora,quant_hora,salario_bruto,valor_inss,\
                valor_fgts,total_descontos,salario_liquido))
    # 5% de desconto
    elif 900 < salario_bruto <= 1500:
        valor_ir = salario_bruto * 0.05
        salario_liquido = salario_bruto - valor_inss - valor_ir
        total_descontos = valor_inss + valor_ir
        
        print('\nSalario Bruto:({}*{})  :R${:.2f}\
            \n(-)IR(5%)     :R${:.2f}\
            \n(-)INSS(10%)     :R${:.2f}\
            \nFGTS(11%)     :R${:.2f}\
            \nTotal de descontos     :R${:.2f}\
            \nSalario Liquido     :R${:.2f}\n'\
            .format(valor_hora,quant_hora,salario_bruto,valor_ir,valor_inss,\
                valor_fgts,total_descontos,salario_liquido))
    # 10% de desconto
    elif 1500 < salario_bruto <= 2500:
        valor_ir = salario_bruto * 0.1
        salario_liquido = salario_bruto - valor_inss - valor_ir
        total_descontos = valor_inss + valor_ir
        
        print('\nSalario Bruto:({}*{})  :R${:.2f}\
            \n(-)IR(10%)     :R${:.2f}\
            \n(-)INSS(10%)     :R${:.2f}\
            \nFGTS(11%)     :R${:.2f}\
            \nTotal de descontos     :R${:.2f}\
            \nSalario Liquido     :R${:.2f}\n'\
            .format(valor_hora,quant_hora,salario_bruto,valor_ir,valor_inss,\
                valor_fgts,total_descontos,salario_liquido))
    # 20% de desconto
    else:
        valor_ir = salario_bruto * 0.20
        salario_liquido = salario_bruto - valor_inss - valor_ir
        total_descontos = valor_inss + valor_ir
        
        print('\nSalario Bruto:({}*{})  :R${:.2f}\
            \n(-)IR(20%)     :R${:.2f}\
            \n(-)INSS(10%)     :R${:.2f}\
            \nFGTS(11%)     :R${:.2f}\
            \nTotal de descontos     :R${:.2f}\
            \nSalario Liquido     :R${:.2f}\n'\
            .format(valor_hora,quant_hora,salario_bruto,valor_ir,valor_inss,\
                valor_fgts,total_descontos,salario_liquido))


if __name__ == '__main__':
    main()

