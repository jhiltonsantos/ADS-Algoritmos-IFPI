def main():
    valor = int(input())
    i = 2
    
    while i != valor:
        if i % 2 == 0:
            print(i)
        i += 1


if __name__ == '__main__':
    main()