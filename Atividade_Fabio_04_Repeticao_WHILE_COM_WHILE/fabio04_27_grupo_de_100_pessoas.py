from tools import get_valor_int_positivo

def main():
    sexo,idade,estado_civil = informacao_pessoa()
    
    media_idade_mulher, media_idade_homem, \
        percent_homem_solteiro, percent_mulher_solteira,\
             mulher_divor_mais_30 = calcula(sexo,idade,estado_civil)

    print('\nMédia de idade das mulheres: %.1f'%media_idade_mulher,'anos.')
    print('Média de idade dos homens: %.1f'%media_idade_homem,'anos.')
    print('Percentual de homens solteiros: %.1f'%percent_homem_solteiro,'%')
    print('Percentual de mulheres solteiras: %.1f'%percent_mulher_solteira,'%')
    print('Quantidade de mulheres divorciadas acima de 30 anos: %d'%mulher_divor_mais_30,'mulheres.')


def informacao_pessoa():
    sexo = int(input('Sexo(1-Masculino|2-Feminino): '))
    while sexo !=1 and sexo != 2:
        print('SEXO INVALIDO!!!')
        sexo = int(input('Sexo(1-Masculino|2-Feminino): '))
    
    print('Digite a idade:',end =' ')
    idade = get_valor_int_positivo()

    print('ESTADO CIVIL: 1-CASADO|2-SOLTEIRO|3-DIVORCIADO|4-VIUVO')
    print('Digite o estado civil:',end = ' ')
    estado_civil = get_valor_int_positivo()
    while estado_civil > 4 or estado_civil == 0:
        print('ESTADO CIVIL INCORRETO!!!')
        print('ESTADO CIVIL: 1-CASADO|2-SOLTEIRO|3-DIVORCIADO|4-VIUVO')
        print('Digite o estado civil.',end = ' ')
        estado_civil = get_valor_int_positivo()
    
    return sexo,idade,estado_civil


def calcula(sexo,idade,estado_civil):
    soma_idade_mulher = 0
    quant_mulher = 0
    soma_idade_homem = 0
    quant_homem = 0
    homem_solteiro = 0
    mulher_solteira = 0
    mulher_divor_mais_30 = 0

    contador = 1

    while contador <= 100: 
        print('Quantidade de pessoas lidas: %d'%contador)
        if sexo == 2:
            soma_idade_mulher = soma_idade_mulher + idade
            quant_mulher += 1 
        elif sexo == 1:
            soma_idade_homem = soma_idade_homem + idade
            quant_homem += 1
        
        if sexo==1 and estado_civil==2:
            homem_solteiro = homem_solteiro + 1  
        elif sexo==2 and estado_civil==2:
            mulher_solteira = mulher_solteira + 1

        if (sexo==2 and estado_civil==3) and idade>30:
            mulher_divor_mais_30 = mulher_divor_mais_30 + 1  
        if not(contador >= 100):
            sexo,idade,estado_civil = informacao_pessoa()
        contador += 1

    media_idade_mulher,media_idade_homem,\
        percent_homem_solteiro,percent_mulher_solteira =\
             verifica_calcula(soma_idade_mulher,quant_mulher,\
                 soma_idade_homem,quant_homem,homem_solteiro,mulher_solteira)
    
    return media_idade_mulher, media_idade_homem,\
        percent_homem_solteiro, percent_mulher_solteira, mulher_divor_mais_30


def verifica_calcula(soma_idade_mulher,quant_mulher,\
    soma_idade_homem,quant_homem,homem_solteiro,mulher_solteira):
    
    if soma_idade_mulher > 0:
        media_idade_mulher = soma_idade_mulher / quant_mulher
    else:
        media_idade_mulher = 0
    
    if soma_idade_homem > 0:
        media_idade_homem = soma_idade_homem / quant_homem
    else:
        media_idade_homem = 0
    
    if homem_solteiro > 0:
        percent_homem_solteiro = (homem_solteiro*100) / quant_homem
    else:
        percent_homem_solteiro = 0
    
    if mulher_solteira > 0:
        percent_mulher_solteira = (mulher_solteira*100) / quant_mulher
    else:
        percent_mulher_solteira = 0

    return media_idade_mulher,media_idade_homem,\
        percent_homem_solteiro,percent_mulher_solteira


if __name__ == '__main__':
    main()
