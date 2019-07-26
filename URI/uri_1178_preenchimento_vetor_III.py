def main():
    valor = float(input())
    vetor_n = [valor]
    print('N[0] = %.4f' % vetor_n[0])

    for i in range(1, 100):
        valor = valor/2
        vetor_n += [valor]
        print('N[%d] = %.4f' % (i, vetor_n[i]))


if __name__ == '__main__':
    main() 