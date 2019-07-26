def main():
    numerador = 1
    denominador = 0
    soma = 0

    i = 1
    while i <= 100:
        denominador += 1
        soma += (numerador/denominador)
        i += 1

    print('%.2f' % soma)


main()

