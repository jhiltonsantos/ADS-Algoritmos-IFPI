def main():
    value_a, value_b = map(int, input().split())

    if ((value_a % value_b) == 0) or ((value_b % value_a) == 0):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
    

if __name__ == '__main__':
    main()
