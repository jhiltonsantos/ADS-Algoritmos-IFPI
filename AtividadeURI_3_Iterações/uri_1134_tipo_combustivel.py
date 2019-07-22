def main():
    tipo = 0

    tipo_combustivel(tipo)
    
    
def tipo_combustivel(tipo):
    cont_alcool = 0
    cont_gasolina = 0
    cont_diesel = 0

    while tipo != 4:
        tipo = int(input())
        while tipo < 1 or tipo > 4:
            tipo = int(input())
        
        if tipo == 1:
            cont_alcool += 1
        elif tipo == 2:
            cont_gasolina += 1
        elif tipo == 3:
            cont_diesel += 1
    
    imprimir(cont_alcool,cont_gasolina,cont_diesel) 
        

def imprimir(alcool, gasolina, diesel):
    print('MUITO OBRIGADO')
    print('Alcool: {}'.format(alcool))
    print('Gasolina: {}'.format(gasolina))
    print('Diesel: {}'.format(diesel))


if __name__ == '__main__':
    main()    
    