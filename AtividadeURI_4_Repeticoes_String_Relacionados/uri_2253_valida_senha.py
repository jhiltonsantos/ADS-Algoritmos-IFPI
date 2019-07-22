def main():
    while True:
        try:
            senha = input()
            if valida_senha(senha):
                print('Senha valida.')
            else:
                print('Senha invalida.')
        except EOFError:
            break


def valida_senha(senha):
    tamanho = tamanho_senha(senha)
    somente_letra_numero = eh_letra_numero(senha)
    tem_numero_letra = um_de_cada(senha)
    
    if tamanho and somente_letra_numero and \
        tem_numero_letra:
        return True
    else:
        return False


def tamanho_senha(senha):
    if (len(senha)>=6) and (len(senha)<=32):
        return True
    return False


def eh_letra_numero(senha):
    for i in range(len(senha)):
        if not((ord(senha[i])>=65 and ord(senha[i])<=90)\
            or (ord(senha[i])>=97 and ord(senha[i])<=122)\
                or (ord(senha[i])>=48 and ord(senha[i])<=57)):
                return False
    return True


def um_de_cada(senha):
    maiuscula = 0
    minuscula = 0
    numero = 0
    i = 0
    
    while i < len(senha):
        if (ord(senha[i])>=65 and ord(senha[i])<=90): maiuscula+=1
        if (ord(senha[i])>=97 and ord(senha[i])<=122): minuscula+=1
        if (ord(senha[i])>=48 and ord(senha[i])<=57): numero+=1 
        i += 1
    
    if (maiuscula>0) and (minuscula>0) and (numero>0):
        return True
    return False


if __name__ == '__main__':
    main()