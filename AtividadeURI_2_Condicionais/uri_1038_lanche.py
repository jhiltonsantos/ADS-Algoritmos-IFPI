def main():
    codigo, quant = map(int, input().split())

    if codigo == 1:
        valor = quant * 4
    elif codigo == 2:
        valor = quant * 4.5
    elif codigo == 3:
        valor = quant * 5
    elif codigo == 4:
        valor = quant * 2
    elif codigo == 5:
        valor = quant * 1.5
    
    print('Total: R$ {:.2f}'.format(valor))


if __name__ == '__main__':
    main()
