def inverter_frase(frase):
    i = 0
    frase_invertida = ''

    while i < len(frase):
        frase_invertida += frase[(len(frase)-1)-i]
        i += 1

    return frase_invertida


def nova_frase_sem_separacao(frase):
    i = 1
    new_frase = ''
    while i <= len(frase):
        letra = ord(frase[i-1])
        if letra == 32:
            imprimir = ''
        else:
            imprimir = chr(letra)    
        new_frase = new_frase + imprimir
        
        i += 1

    return new_frase


def duplica_caractere(frase):
    i = 1
    nova_frase = ''

    while i <= len(frase):
        letra = ord(frase[i-1])
        str_letra = chr(letra)
        nova_frase = nova_frase + (str_letra*2)
        i += 1

    return nova_frase


def substitui_caractere(frase):
    i = 0
    nova_frase = ''
    
    while i < len(frase):
        if (frase[i]=='r') and (frase[i-1]=='e'):
            nova_frase += 's'
        else:
            nova_frase += frase[i]
        i += 1
    
    return nova_frase


def transforma_palavra_em_maiuscula(palavra):
    i = 0
    nova_str = ''

    while i < len(palavra):
        letra = palavra[i]
        if (ord(letra)>=97) and (ord(letra)<=122):
            letra = chr(ord(letra)-32)
            nova_str += letra
        else:
            nova_str += palavra[i]
        i += 1

    return nova_str


def transforma_palavra_em_minuscula(palavra):
    i = 0
    nova_str = ''

    while i < len(palavra):
        letra = palavra[i]
        if (ord(letra)>=65) and (ord(letra)<=90):
            letra = chr(ord(letra)+32)
            nova_str += letra
        else:
            nova_str += palavra[i]
        i += 1

    return nova_str


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
            
    return inverter_frase(valor_primeiro_nome)


def ultimo_nome(nome):
    nome_ultimo = inverter_frase(nome)

    valor_sobrenome = primeiro_nome(nome_ultimo)
    
    return inverter_frase(valor_sobrenome)


def gera_usuario_iniciais(nome):
    i = 0
    nome = transforma_palavra_em_maiuscula(nome)
    valor_usuario = nome[0]

    while i <len(nome):
        if ord(nome[i])==32:
            valor_usuario += nome[i+1]
        i += 1

    return valor_usuario
