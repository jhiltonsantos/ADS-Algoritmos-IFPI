def main():
    x, y = map(int, input().split())
    
    i = 1
    while i <= y:
        if i % x == 0:
            print(i)
        else:
            print(i, end=' ')
        i +=1
    
    
main()