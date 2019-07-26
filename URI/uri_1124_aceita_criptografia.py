def main():
    n = input()
    n = int(n)
    
    for i in range(n):
        frase = input()
        print(criptografia(frase))


def criptografia(frase):
    # PRIMEIRA ETAPA
    etapa_um = ''
    tamanho_frase = len(frase)
    
    for i in range(tamanho_frase):
        posicao = frase[i]
        if ((posicao>='A') and (posicao<='Z')) or\
            ((posicao>='a') and (posicao<='z')):
            etapa_um += chr(ord(posicao) + 3)
        else:
            etapa_um += posicao
    
    # SEGUNDA ETAPA
    etapa_um = etapa_um[::-1]

    # TERCEIRA ETAPA
    soma = ''
    tamanho_e1 = len(etapa_um)
    divisao = tamanho_e1/2
    divisao = int(divisao)

    for i in range(tamanho_e1):
        posicao_e1 = etapa_um[i]
        if i >= divisao:
            soma += chr(ord(posicao_e1) - 1)
        else:
            soma += posicao_e1

    return soma


main()