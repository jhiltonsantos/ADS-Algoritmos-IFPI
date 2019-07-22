def main():
    letra = input('Digite a letra: ')

    if letra == 'a' or letra == 'e'\
         or letra == 'i' or letra == 'o' or letra == 'u':
         print('A letra digitada é vogal.')
    else:
        print('A letra digitada é consoante.')


if __name__ == '__main__':
    main()
