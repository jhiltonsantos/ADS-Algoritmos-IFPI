from tools_string import transforma_palavra_em_maiuscula

def main():
    palavra = input('Digite a palavra: ')
    palavra = transforma_palavra_em_maiuscula(palavra)
        
    i = 0
    palindroma = ''
    while i < len(palavra):
        palindroma += palavra[(len(palavra)-1)-i]
        i += 1
    
    if palindroma == palavra:
        print('Palavra é palindroma!!!')
    else:
        print('Palavra não é palindroma!!!')


if __name__ == '__main__':
    main()