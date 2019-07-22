def main():
    valor = float(input())

    if imposto(valor) <= 0:
        print('Isento')
    else:
        print('R$ {:.2f}'.format(imposto(valor)))


def imposto(valor):
    if 2000 < valor <= 3000:
        valor -= 2000
        imposto = valor * 0.08
    elif 3000 < valor <= 4500:
        valor -= 3000
        imposto = (1000*0.08) + (valor*0.18)
    else:
        valor -= 4500
        imposto = (1000*0.08) + (1500*0.18) + (valor*0.28)
    
    return imposto
            

if __name__ == '__main__':
    main()
