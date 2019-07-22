def main():
    start_h, final_h = map(int, input().split())

    if start_h > final_h or start_h == final_h:
        duration = (24 - start_h) + final_h
        print('O JOGO DUROU {} HORA(S)'.format(duration))
    else:
        duration = final_h - start_h
        print('O JOGO DUROU {} HORA(S)'.format(duration))


if __name__ == '__main__':
    main()
