def maior():
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    n3 = int(input('Numero 3: '))
    n4 = int(input('Numero 4: '))
    n5 = int(input('Numero 5: '))

    if n5 > n4 > n3 > n2 > n1:
        print('Maior: {}. Menor: {}'.format(n5,n1))
    elif n5 > n4 > n3 > n1 > n2:
        print('Maior: {}. Menor: {}'.format(n5,n2))
    elif n5 > n4 > n3 > n2 > n1:
        print('Maior: {}. Menor: {}'.format(n5,n1))         

if __name__ == '__main__':
    maior()