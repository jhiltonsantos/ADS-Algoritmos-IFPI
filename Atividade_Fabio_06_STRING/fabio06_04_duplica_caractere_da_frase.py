from tools_string import duplica_caractere

def main():
    frase = input('Frase: ')
    print(duplica_caractere(frase))


'''
def duplica_caractere(frase):
    i = 1
    nova_frase = ''

    while i <= len(frase):
        letra = ord(frase[i-1])
        str_letra = chr(letra)
        nova_frase = nova_frase + (str_letra*2)
        i += 1

    return nova_frase
'''


if __name__ == '__main__':
    main()