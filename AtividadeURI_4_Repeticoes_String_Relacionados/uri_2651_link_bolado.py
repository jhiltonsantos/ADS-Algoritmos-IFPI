def main():
    referencia_carta = input()
    nome = referencia_carta.lower()
    print(link_zelda(nome))


def link_zelda(nome):
    for i in range(len(nome)-1):
        if (nome[i]=='z') and (nome[i+1]=='e') and\
            (nome[i+2]=='l') and (nome[i+3]=='d') and\
                (nome[i+4]=='a'):
                 return 'Link Bolado'
    return 'Link Tranquilo'


main()