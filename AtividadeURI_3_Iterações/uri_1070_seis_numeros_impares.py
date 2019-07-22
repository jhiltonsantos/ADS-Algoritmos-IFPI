def main():
    valor = int(input())
    cont = valor
    i = 1

    while i <= 6:
        if cont % 2 != 0:
            print(cont)
            i +=1
        cont +=1 


if __name__ == '__main__':
    main()