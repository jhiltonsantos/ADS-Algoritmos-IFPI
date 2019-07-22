from tools_string import transforma_palavra_em_maiuscula, ultimo_nome

def main():
    nome_completo = input('Digite o nome completo: ')
    nome_completo = transforma_palavra_em_maiuscula(nome_completo)
        
    ultimo = ultimo_nome(nome_completo)
    primeiro, segundo = iniciais(nome_completo)

    print('%s, %s. %s..' % (ultimo, primeiro, segundo))


def iniciais(nome):
    i = 0

    while i < len(nome):
        primeiro_nome_inicial = nome[0]

        if ord(nome[i]) == 32:
            segundo_nome_inicial = nome[i+1]
            break
        
        i += 1

    return primeiro_nome_inicial, segundo_nome_inicial


if __name__ == '__main__':
    main()