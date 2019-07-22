def main():
    A,B,C = map(float, input().split())
    
    perimetro = A+B+C
       
    if abs(B-C) < A < (B+C):
        print('Perimetro = {}'.format(perimetro))
    elif abs(A-C) < B < (A+C):
        print('Perimetro = {}'.format(perimetro))
    elif abs(A-B) < C < (A+B):
        print('Perimetro = {}'.format(perimetro))
    
    else:
        area = ((A+B)/2)*C
        print('Area = {}'.format(area))


if __name__ == '__main__':
    main()