def main():
    while True:
        try:
            velocidade, tempo = map(int, input().split())
            print((velocidade*2) * tempo)
        except EOFError:
            break

if __name__ == '__main__':
    main()