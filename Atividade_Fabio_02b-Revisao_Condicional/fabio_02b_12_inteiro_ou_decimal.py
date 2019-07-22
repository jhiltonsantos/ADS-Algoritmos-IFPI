def main():
    numero = float(input('Numero: '))
    
    if (numero%1) != 0:
        print('Numero nao e decimal')
    else:
        print('Numero decimal')
    

if __name__ == '__main__':
    main()
