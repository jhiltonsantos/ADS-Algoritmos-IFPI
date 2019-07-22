def main():
    valor = int(input('Numero: '))
        
    soma(valor)
    subtracao(valor)
    multiplicacao(valor)
    divisao(valor)


def soma(valor):
    s = 1
    while s <= 10:
        soma = s + valor
        print("{} + {} = {}".format(s,valor,soma))
        s += 1
        

def subtracao(valor):
    i = valor
    limite = valor + 9
    while i <= limite:
        subtracao = i - valor
        print("{} - {} = {}".format(i,valor,subtracao))
        i += 1


def multiplicacao(valor):
    m = 1
    while m <= 10:
        multiplicacao = m * valor
        print("{} * {} = {}".format(m,valor,multiplicacao))
        m += 1
        

def divisao(valor):
    d = valor
    limite = valor *10
    while d <= limite:
        divisao = d / valor
        print("{} / {} = {}".format(d,valor,divisao))
        d += valor

if __name__ == '__main__':
    main()