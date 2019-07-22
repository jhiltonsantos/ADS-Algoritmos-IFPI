from tools_string import nova_frase_sem_separacao

def main():
    frase = input('Digite a frase: ')
    print(nova_frase_sem_separacao(frase))
    

'''
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
'''

if __name__ == '__main__':
    main()