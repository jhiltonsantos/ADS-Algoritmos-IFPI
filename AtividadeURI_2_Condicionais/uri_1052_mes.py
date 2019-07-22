def main():
    valor = int(input())

    print(mes(valor))


def mes(valor):
    if valor == 1:
        return 'January'
    elif valor == 2:
        return 'February'
    elif valor == 3:
        return 'March'
    elif valor == 4:
        return 'April'
    elif valor == 5:
        return 'May'
    elif valor == 6:
        return 'June'
    elif valor == 7:
        return 'July'
    elif valor == 8:
        return 'August'
    elif valor == 9:
        return 'September'
    elif valor == 10:
        return 'October'
    elif valor == 11:
        return 'November'
    elif valor == 12:
        return 'December'


if __name__ == '__main__':
    main()
