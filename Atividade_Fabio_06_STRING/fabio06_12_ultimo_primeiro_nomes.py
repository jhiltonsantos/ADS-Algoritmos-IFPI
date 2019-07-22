from tools_string import transforma_palavra_em_maiuscula, primeiro_nome, ultimo_nome

def main():
    nome_completo = input('Digite o nome completo: ')
    nome_completo = transforma_palavra_em_maiuscula(nome_completo)
    
    primeiro = primeiro_nome(nome_completo)
    ultimo = ultimo_nome(nome_completo)

    print(ultimo + '/' + primeiro)


'''
def primeiro_nome(nome):
    i = 0
    j = 1
    valor_primeiro_nome = ''

    while i < len(nome):
        if ord(nome[i]) == 32:
            while j <= i:
                valor_primeiro_nome += nome[i-j]
                j += 1
            break
        i += 1
    
    return valor_primeiro_nome[::-1]


def ultimo_nome(nome):
    nome_ultimo = nome[::-1]

    valor_sobrenome = primeiro_nome(nome_ultimo)
    return valor_sobrenome[::-1]
'''


if __name__ == '__main__':
    main()