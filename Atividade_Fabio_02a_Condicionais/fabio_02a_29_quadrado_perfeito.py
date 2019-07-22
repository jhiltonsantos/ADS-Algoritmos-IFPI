def main():
    numero = int(input("Digite o numero: "))

    str_milhar = str(numero // 1000)
    resto_milhar = numero % 1000
    str_centena = str(resto_milhar // 100)
    resto_centena = resto_milhar % 100
    str_dezena = str(resto_centena // 10)
    str_unidade = str(resto_centena % 10)

    dezena_1 = int(str_milhar + str_centena) 
    dezena_2 = int(str_dezena + str_unidade)

    soma = dezena_1+dezena_2
    raiz = int((numero ** (1/2)))
    
    if raiz == soma:
        print('Numero eh um quadrado perfeito!!!')
    else:
        print('Numero nao eh um quadrado perfeito!!!')
    

if __name__ == '__main__':
    main() 
