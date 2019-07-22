def main():
    verbo = input('Digite um verbo regular terminado em -ER: ')
    
    print('Primeira pessoa do singular: EU %s'%verbo_primeira_singular(verbo))
    print('Segunda pessoa do singular: TU %s'%verbo_segunda_singular(verbo))
    print('Terceira pessoa do singular: ELE %s'%verbo_terceira_singular(verbo))
    print('Primeira pessoa do plural: NÓS %s'%verbo_primeira_plural(verbo))
    print('Segunda pessoa do plural: VÓS %s'%verbo_segunda_plural(verbo))
    print('Terceira pessoa do plural: ELES %s'%verbo_terceira_plural(verbo))


def verbo_primeira_singular(verbo):
    i = 0
    novo_verbo = ''
    
    while i < len(verbo):
        if (verbo[i]=='e') and (verbo[i+1]=='r'):
            novo_verbo += 'o'
        elif (verbo[i]=='r') and (verbo[i-1]=='e'):
            novo_verbo += ''
        else:
            novo_verbo += verbo[i]
        i += 1
    return novo_verbo


def verbo_segunda_singular(verbo):
    i = 0
    novo_verbo = ''
    
    while i < len(verbo):
        if (verbo[i]=='r') and (verbo[i-1]=='e'):
            novo_verbo += 's'
        else:
            novo_verbo += verbo[i]
        i += 1
    return novo_verbo


def verbo_terceira_singular(verbo):
    i = 1
    novo_verbo = ''
    anterior = ''

    while i <= len(verbo):
        caractere = ord(verbo[i-1])
        
        # 3 pessoa do singular
        if (caractere==82 or caractere==114) and\
             (anterior==69 or anterior==101):
            novo_verbo = novo_verbo + '' 
        else:
            str_caractere = chr(caractere)
            novo_verbo = novo_verbo + str_caractere
        
        anterior = caractere
        i += 1
    return novo_verbo


def verbo_primeira_plural(verbo):
    i = 0
    novo_verbo = ''
    
    while i < len(verbo):
        if (verbo[i]=='e') and (verbo[i+1]=='r'):
            novo_verbo += 'emos'
        elif (verbo[i]=='r') and (verbo[i-1]=='e'):
            novo_verbo += ''
        else:
            novo_verbo += verbo[i]
        i += 1
    
    return novo_verbo


def verbo_segunda_plural(verbo):
    i = 0
    novo_verbo = ''
    
    while i < len(verbo):
        if (verbo[i]=='e') and (verbo[i+1]=='r'):
            novo_verbo += 'eis'
        elif (verbo[i]=='r') and (verbo[i-1]=='e'):
            novo_verbo += ''
        else:
            novo_verbo += verbo[i]
        i += 1
    
    return novo_verbo


def verbo_terceira_plural(verbo):
    i = 0
    novo_verbo = ''
    
    while i < len(verbo):
        if (verbo[i]=='e') and (verbo[i+1]=='r'):
            novo_verbo += 'em'
        elif (verbo[i]=='r') and (verbo[i-1]=='e'):
            novo_verbo += ''
        else:
            novo_verbo += verbo[i]
        i += 1
    
    return novo_verbo


if __name__ == '__main__':
    main()
    