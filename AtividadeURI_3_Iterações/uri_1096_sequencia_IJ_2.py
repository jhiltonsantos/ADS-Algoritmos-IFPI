def main():
    i = 1
    j = 7
    
    while i <= 9:
        while j >= 5:
            print('I={} J={}'.format(i,j))
            j -= 1
        
        j = 7    
        i += 2


if __name__ == '__main__':
    main()