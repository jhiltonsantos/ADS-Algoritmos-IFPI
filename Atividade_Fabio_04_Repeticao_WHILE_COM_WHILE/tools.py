def get_valor_int_positivo():
    numero_posivito = int(input())
    while numero_posivito < 0:
        print('Digite um valor positivo')
        numero_posivito = int(input('Valor: '))
    return numero_posivito


def get_valor_float_positivo():
    float_posivito = float(input())
    while float_posivito < 0.0:
        print('Digite um valor positivo')
        float_posivito = int(input('Valor: '))
    return float_posivito


def verifica_divisores(numero):
    contador = 1
    while contador <=numero:
        if numero % contador == 0:
            return print(contador,end=' ')
        contador +=1


def verifica_maior_menor(n1,n2):
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    return maior, menor


def fibonacci_recursivo(valor):
    if valor == 0:
        sequencia = 0
    elif valor == 1:
        sequencia = 1
    else:
        sequencia = fibonacci(valor-1) + fibonacci(valor-2)

    return sequencia


def fibonnaci_posicao(numero):
    a = 0
    b = 1
    for i in range(numero):
        a, b = b, a+b
    return a


def verifica_maior(n1,n2):
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    return maior


def verifica_menor(n1,n2):
    if n1 < n2:
        menor = n1
    else:
        menor = n2
    return menor


def eh_primo(numero):
    if numero != 0 and numero != 1:
        if numero != 2:
            for i in range(2, numero):
                if numero % i == 0:
                    return False
        return True
    return False


def verifica_mmc(n1,n2):
    contador = 0
    maior = verifica_maior(n1,n2)
    while contador == 0:
        if (maior%n1==0) and (maior%n2==0):
            contador = 1
            return maior
        else:
            maior += 1


def verifica_mdc(n1,n2):
    numero_1,numero_2 = verifica_maior_menor(n1,n2)
    while numero_2 != 0:
        resto = numero_1 % numero_2
        numero_1 = numero_2
        numero_2 = resto
    mdc = numero_1
    return mdc


def separa_numero_com_fatiamento_string(numero):
    n = 1
    contador = 1
    while contador != 0:
        separa = str(numero)[n-1:n]
        if separa == '':
            break
        print(separa, end=' ')
        n += 1
        
    quant = n-1
    return quant


def numero_diferente_de_valor(numero,valor):
    while numero == valor:
        print('Numero deve ser diferente de %.2f'%valor)
        numero = float(input('Digite o numero: '))
    return numero


def valor_modulo(numero):
    if numero >= 0:
        return numero
    else:
        absoluto = numero * -1
        return absoluto    


def progressao_aritmetica(razao,a1,num_termos):
    contador = 1
    while contador <= num_termos:
        valor_pa = a1 + ((contador-1)*razao)
        print(valor_pa, end = ' ')
        contador += 1
    
    return valor_pa


def progressao_geometrica(razao_q,primeiro_termo,numero_termos):
    contador = 1
    
    while contador <= numero_termos:
        valor_pg = primeiro_termo * (razao_q**(contador-1))
        print(valor_pg, end=' ')
        contador += 1

    return valor_pg


