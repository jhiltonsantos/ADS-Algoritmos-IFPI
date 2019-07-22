def main():
    while True:
        try:
            texto = input()
            print(formata_texto(texto))

        except EOFError:
            break


def formata_texto(texto):
    texto_formatado = ''
    negrito_aberto = True
    subl_aberto = True

    for i in range(len(texto)):
        if texto[i] == '*':
            if negrito_aberto:
                texto_formatado += '<b>'
                negrito_aberto = False
            else:
                texto_formatado += '</b>'
                negrito_aberto = True
        
        elif texto[i] == '_':
            if subl_aberto:
                texto_formatado += '<i>'
                subl_aberto = False
            else:
                texto_formatado += '</i>'
                subl_aberto = True
        
        else:
            texto_formatado += texto[i]
    
    return texto_formatado
    

main()