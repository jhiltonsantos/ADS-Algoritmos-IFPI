def main():
    valor = int(input())
    cont = 1
    
    calcule(valor,cont)
    

def calcule(valor, cont):
    x = 0
    y = 0
    z = 0
    while cont <= valor:
        x += 1
        y = x**2
        z = x**3
        print('{} {} {}'.format(x,y,z))
        cont += 1


if __name__ == '__main__':
    main()