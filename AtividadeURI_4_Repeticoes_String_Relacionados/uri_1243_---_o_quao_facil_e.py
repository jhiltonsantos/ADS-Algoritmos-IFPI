def main():
    while True:
        try:
            frase = []
            frase = input().split()

            soma_palavra = 0
            n_palavra = 0
            
            for i in range(len(frase)):
                valor = eh_palavra(frase[i])
    
                if valor:
                    #print('Palavra')
                    soma_palavra += len(frase[i])
                    n_palavra += 1
                #else:
                    #print('Simbolo')
                
            medio = comprimento_medio(soma_palavra, n_palavra)
            
            if medio <= 3:
                print('250')
            elif medio == 4 or medio == 5:
                print('500')
            else:
                print('1000')
            
        except EOFError:
            break


def eh_palavra(frase):
    ponto = False
    # True = Palavra
    # False = Simbolo
    
    for i in range(len(frase)):
        if ord(frase[i]) == 46:
            if (i+1) < len(frase):
                ponto = True
                break

        elif ( not((ord(frase[i])>=65) and (ord(frase[i])<=90) or\
            (ord(frase[i])>=97) and (ord(frase[i])<=122)) ):
            return False

        else:
            ponto = False
    
        
    if ponto == False:
        return True
    else:
        return False


def comprimento_medio(soma, n):
    if n!=0: return (soma)//n 
    else: return 0


if __name__ == '__main__':
    main()