def main():
    valor_x = int(input())
    valor_z = int(input())
    
    while (valor_x == valor_z) or (valor_x > valor_z):
        valor_z = int(input())

    cont = 1
    valor = valor_x
    while valor_x <= valor_z:
        valor_x += (valor+cont)
        cont += 1

    print(cont)

main()
