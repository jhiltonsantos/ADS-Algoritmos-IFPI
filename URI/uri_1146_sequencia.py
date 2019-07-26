def main():
    n = int(input())
    
    while n != 0:
        i = 1
        saida = ''
        
        while i <= n:
            if i < n: saida += str(i)+' ' 
            else: saida += str(i)
            i += 1
        
        print(saida)
        n = int(input())    


main()