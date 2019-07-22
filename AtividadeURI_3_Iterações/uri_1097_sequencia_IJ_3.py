def main():
    i = 1
    j = 7
    cont =1
    
    while i <= 9:
        while cont <= 3:
            print('I={} J={}'.format(i,j))
            j -= 1
            cont += 1
        
        j += 5    
        i += 2
        cont = 1


if __name__ == '__main__':
    main()