from tools_string import transforma_palavra_em_maiuscula

def main():
    nome = input('Digite seu nome: ')

    print(gera_usuario_iniciais(nome))


def gera_usuario_iniciais(nome):
    i = 0
    nome = transforma_palavra_em_maiuscula(nome)
    valor_usuario = nome[0]

    while i <len(nome):
        if ord(nome[i])==32:
            valor_usuario += nome[i+1]
        i += 1

    return valor_usuario


if __name__ == '__main__':
    main()