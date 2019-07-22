from math import log


def main():
    while True:
        try:
            print(int(log(int(input()), 2)))
        except EOFError:
            break


if __name__ == '__main__':
    main()