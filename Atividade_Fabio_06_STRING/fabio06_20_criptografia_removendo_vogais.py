def main():
    frase = input('Digite a frase: ')

    criptografada, posicao = criptografar(frase)
    print('Frase Criptografada: %s ' % criptografada)
    print('Posicao: %s' % posicao)
    
    frase_descriptografada = descriptografar(criptografada, posicao)
    print('Frase Descriptografada: %s ' % frase_descriptografada)


def criptografar(frase):
    vogais = 'AEIOUaeiou'
    i = 0
    j = 0
    frase_criptografada = ''
    posicao = ''
    
    while i < len(frase):
        
        while j < len(vogais):
            if frase[i] == vogais[j]:
                eh_vogal = True
                posicao += frase[i]
                break
            else:
                eh_vogal = False
            j += 1
        
        if eh_vogal == True:
            frase_criptografada += ''    
        else:
            frase_criptografada += frase[i]
            posicao += ' '
        i += 1
        j = 0

    return frase_criptografada, posicao


def descriptografar(criptografada, posicao):
    i = 0
    k = 0
    frase_desc = ''

    while i < len(posicao):
        if ord(posicao[i])==32:
            valor = criptografada[k]
            k += 1
        else:
            valor = posicao[i]
            
        frase_desc += valor
        i += 1

    return frase_desc


if __name__ == '__main__':
    main()