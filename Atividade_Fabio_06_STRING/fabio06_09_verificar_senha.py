import getpass

def main():
    recebe_senha = getpass.getpass('Senha: ')
    
    asterisco, correta = senha(recebe_senha)
    print(asterisco)
    
    verificada = verifica_senha(correta)
    while verificada == False:
        print('\nSenha invalida!!! Digite novamente')
        verificada = verifica_senha(correta)
    print(verificada)


def senha(recebe_senha):
    i = 0
    senha_asterisco = ''
    senha_correta = ''

    while i < len(recebe_senha):
        if recebe_senha[i]:
            senha_asterisco += '*'
            senha_correta += recebe_senha[i]
        i += 1

    return senha_asterisco, senha_correta


def verifica_senha(senha_correta):
    senha_testada = input('Digite a senha para verificar: ')
    while len(senha_testada) != len(senha_correta):
        print('Quantidae de digitos incorreta!!!')
        senha_testada = input('Digite a senha para verificar: ')
    
    j = 0
    nova_senha = ''

    while j < len(senha_testada):
        if senha_testada [j] == senha_correta [j]:
            nova_senha += 'V'
        else:
            nova_senha += 'F'
        j += 1
    
    if nova_senha == ('V'*j):
        return True
    else:
        return False


if __name__ == '__main__':
    main()