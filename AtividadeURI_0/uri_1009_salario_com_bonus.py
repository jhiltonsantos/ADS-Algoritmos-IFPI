
def main():
   # entrada 
   nome_vendedor = input()
   salario = float(input())
   venda = float(input())

   # processamento
   montante_venda = (venda*0.15)
   total_final_mes = salario + montante_venda

   # saida
   print('TOTAL = R$ {:.2f}'.format(total_final_mes))


if __name__ == '__main__':
    main()
    