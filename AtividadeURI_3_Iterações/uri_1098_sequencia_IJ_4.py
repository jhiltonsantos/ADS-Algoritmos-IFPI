def main():
    i = 0
    j = 1
    cont =1
    
    while i <= 2:
        while cont <= 3:
            if (i > 1.9 and i < 2.1)  or (i % 1 == 0):
                print('I={:.0f} J={:.0f}'.format(i,j))
            else:
                print('I={:.1f} J={:.1f}'.format(i,j))
            j += 1
            cont += 1
        
        j -= 2.8    
        i += 0.2
        cont = 1


if __name__ == '__main__':
    main()
