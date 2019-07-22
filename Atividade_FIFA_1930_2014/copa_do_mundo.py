from os import system
from utils import *


def main():
    nome_arquivo_dados = 'dados.csv'
    copa = importar_dados_arquivo(nome_arquivo_dados)
    
    resposta = int(input(menu()))
    escolha(resposta, copa)


def menu():
    msg()
    menu = ('\t===== MENU ======\n'\
        + '01 - MOSTRAR TODOS OS DADOS\n'\
        + '02 - QUANTIDADE TOTAL DE PARTIDAS\n'\
        + '03 - BUSCAR PARTIDAS POR NOME DA SELECAO\n'\
        + '04 - BUSCAR PARTIDAS POR NOME DA SELECAO E LISTAR ANO DECRESCENTE\n'\
        + '05 - MOSTRAR TODAS AS FINAIS\n'\
        + '06 - BUSCAR POR RESULTADO DA PARTIDA\n'\
        + '07 - MEDIA DE GOLS EM FINAIS DE COPAS DO MUNDO\n'\
        + '08 - MEDIA DE GOLS EM UMA COPA DO MUNDO\n'\
        + '09 - TOTAL DE GOLS EM UMA COPA DO MUNDO E POR ANO\n'\
        + '10 - MEDIA DE GOLS EM TODAS AS COPAS DO MUNDO E POR ANO\n'\
        + '11 - DADOS DE COPA DO MUNDO COM MAIOR NUMERO DE GOLS\n'\
        + '12 - TOTAL DE GOLS FEITOS E SOFRIDOS POR SELECAO\n'\
        + '\n0 - Sair\n')

    return menu


def escolha(resposta, copa):
    while resposta != 0:
        if resposta == 1:
            print('==============\tCOPAS DO MUNDO\t==================')
            mostrar_dados_copas(copa)
        elif resposta == 2:
            quantidade_total_de_partidas(copa)
        elif resposta == 3:
            busca_por_nome(copa)
        elif resposta == 4:
            ordenar_por_decrescente_ano(copa)
        elif resposta == 5:
            todas_as_finais(copa)
        elif resposta == 6:
            buscar_por_resultado_da_partida(copa)
        elif resposta == 7:
            print('MEDIA DE GOLS FEITOS EM FINAIS DE COPA DO MUNDO EH DE: %.2f GOLS.' \
                % media_de_gols_em_finais(copa))
        elif resposta == 8:
            ano = ler_ano()
            print('MEDIA DE GOLS NA COPA DO MUNDO DE %s EH: %.2f GOLS.' \
                % (ano, media_de_gols_numa_copa(copa, ano)))
        elif resposta == 9:
            ano = ler_ano()
            todas_copas, copa_especificada = total_de_gols_em_copas_e_por_ano(copa, ano)
            print('TOTAL DE GOLS EM TODAS AS COPAS: %d GOLS.\nTOTAL DE GOLS NA COPA DO MUNDO DE %s EH: %d GOLS.' \
                % (todas_copas, ano, copa_especificada))
        elif resposta == 10:
            ano = ler_ano()
            t, media_todas, media_espec = media_de_gols_de_todas_as_copas(copa, ano)
            print('MEDIA DE GOLS EM TODAS AS COPAS DO MUNDO EH: %.2f GOLS.\nMEDIA DE GOLS NA COPA DO MUNDO DE %s EH: %.2f GOLS'\
                % (media_todas, ano, media_espec))
        elif resposta == 11:
            dados_de_copa_com_mais_gols(copa)
        elif resposta == 12:
            selecao = input('DIGITE A SELECAO: ')
            print('GOLS FEITOS PELA SELECAO DO(A) %s: %d GOLS.' % \
                (selecao.upper(), total_de_gols_feitos_por_uma_selecao(copa, selecao)))
            print('GOLS SOFRIDOS PELA SELECAO DO(A) %s: %d GOLS.\n' % \
                (selecao.upper(), total_de_gols_sofridos_por_uma_selecao(copa, selecao)))

        resposta = int(input(menu()))


def importar_dados_arquivo(arquivo):
    arquivo_copas = open(arquivo, encoding='ISO-8859-1')
    dados_copas = arquivo_copas.readlines()
    arquivo_copas.close() 
    
    d_copa = {}
    vetor_copas = []

    for i in range(1, len(dados_copas)):
        dados = dados_copas[i].strip().split(';')
        gols_time1 = int(dados[6])
        gols_time2 = int(dados[7])

        d_copa = {'ano' : dados[0],\
                  'dado_hora' : dados[1],\
                  'fase' : dados[2],\
                  'estadio' : dados[3],\
                  'cidade' : dados[4],\
                  'time_casa' : dados[5],\
                  'time_casa_gols' : gols_time1,\
                  'time_fora_gols' : gols_time2,\
                  'time_fora' : dados[8], \
                  'total_gols' : total_de_gols(gols_time1, gols_time2),\
                  'resultado' : resultado_da_partida(gols_time1, gols_time2, dados[5], dados[8])}
        
        vetor_copas += [d_copa]
        
    return vetor_copas


def mostrar_dados_copas(copas):
    for i in range(len(copas)):
        #print('ANO\tHORARIO\t\tFASE\tESTADIO\t\tCIDADE\tTIME DA CASA\tGOLS TIME DA CASA'\
        #    +'\tGOLS TIME DE FORA\tTIME DE FORA\tTOTAL DE GOLS NA PARTIDA\tRESULTADO')
        print('%s' % copas[i]['ano'] + '\t',end = '')
        print('%s' % copas[i]['dado_hora'] + '\t',end = '')
        print('%s' % copas[i]['fase'] + '\t',end = '')
        print('%s' % copas[i]['estadio'] + '\t',end = '')
        print('%s' % copas[i]['cidade'] + '\t',end = '')
        print('%s' % copas[i]['time_casa'] + '\t',end = '')
        print('%s' % copas[i]['time_casa_gols'] + '\t',end = '')
        print('%s' % copas[i]['time_fora_gols'] + '\t',end = '')
        print('%s' % copas[i]['time_fora'] + '\t', end='')
        print('%s' % copas[i]['total_gols'] + '\t', end='')
        print('%s' % copas[i]['resultado'] + '\t')
    print()


def total_de_gols(time_a, time_b):
    return time_a + time_b


def resultado_da_partida(gols_time_a, gols_time_b, time_casa, time_fora):
    if gols_time_a > gols_time_b:
        return time_casa
    elif gols_time_a < gols_time_b:
        return time_fora
    else:
        return 'EMPATE'


def quantidade_total_de_partidas(vetor):
    print('FORAM REALIZADAS %d PARTIDAS EM COPAS DO MUNDO.' % len(vetor))


def busca_por_nome(copa):
    nome_selecao = input('DIGITE O NOME DA SELECAO: ')
    
    for i in range(len(copa)):
        if (copa[i]['time_casa']==nome_selecao) or ((copa[i]['time_fora'])==nome_selecao):
            mostrar_dados_copas([copa[i]])


def ordenar_por_decrescente_ano(copa):
    busca_por_nome((copa)[::-1])


def todas_as_finais(copa):
    for i in range(len(copa)):
        if (copa[i]['fase']=='Final'):
            mostrar_dados_copas([copa[i]])


def buscar_por_resultado_da_partida(copa):
    copa = copa[::-1]

    print('\t==== RESULTADO DA PARTIDA ====')
    gols_time1, gols_time2 = map(int, input('DIGITE O RESULTADO DA PARTIDA(EX.:1X0): ').upper().split('X'))

    for i in range(len(copa)):
        if ((copa[i]['time_casa_gols']==gols_time1 and copa[i]['time_fora_gols']==gols_time2)) \
            or ((copa[i]['time_casa_gols']==gols_time2 and copa[i]['time_fora_gols']==gols_time1)):
            mostrar_dados_copas([copa[i]])
    

def media_de_gols_em_finais(copa):
    total_de_gols_em_finais = 0
    quant_de_finais = 0
    
    for i in range(len(copa)):
        if (copa[i]['fase']=='Final'):
            quant_de_finais += 1
            total_de_gols_em_finais += copa[i]['total_gols']
    
    return total_de_gols_em_finais / quant_de_finais


def media_de_gols_numa_copa(copa, ano):
    total_de_gols = 0
    quant_partidas = 0
    
    for i in range(len(copa)):
        if (copa[i]['ano']==ano):
            quant_partidas += 1
            total_de_gols += copa[i]['total_gols']  

    return total_de_gols / quant_partidas


def total_de_gols_em_copas_e_por_ano(copa, ano):
    total_gols_esp = 0
    for i in range(len(copa)):
        if (copa[i]['ano']==ano):
            total_gols_esp += copa[i]['total_gols']
    
    total_de_gols = 0
    for j in range(len(copa)):
        total_de_gols += copa[j]['total_gols']
    
    return total_de_gols, total_gols_esp


def media_de_gols_de_todas_as_copas(copa, ano):
    total_de_partidas = 0
    total_de_gols = 0
    for i in range(len(copa)):
        total_de_partidas += 1
        total_de_gols += copa[i]['total_gols']
    
    total_partidas_esp = 0
    total_gols_esp = 0
    for j in range(len(copa)):
        if (copa[j]['ano']==ano):
            total_partidas_esp += 1 
            total_gols_esp += copa[j]['total_gols']
    
    media_todas_copas =  total_de_gols / total_de_partidas
    media_esp_copa =  total_gols_esp / total_partidas_esp
    
    return total_gols_esp, media_todas_copas, media_esp_copa


def dados_de_copa_com_mais_gols(copa):
    maior = 0
    maior_ano = 0
    
    i = 1930
    while i <= 2014:
        if (i != 1942) and (i != 1946):
            ano = str(i)
            total_gols, m, n = media_de_gols_de_todas_as_copas(copa, ano)        
            if total_gols > maior:
                maior = total_gols
                maior_ano = i
        i += 4

    for i in range(len(copa)):
        if copa[i]['ano']==str(maior_ano):
            mostrar_dados_copas([copa[i]])


def total_de_gols_feitos_por_uma_selecao(copa, selecao):
    total_de_gols = 0
    
    for i in range(len(copa)):
        if copa[i]['time_casa']==selecao:
            total_de_gols += copa[i]['time_casa_gols']
        elif copa[i]['time_fora']==selecao:
            total_de_gols += copa[i]['time_fora_gols']
    
    return total_de_gols


def total_de_gols_sofridos_por_uma_selecao(copa, selecao):
    total_de_gols = 0

    for i in range(len(copa)):
        if copa[i]['time_casa']==selecao:
            total_de_gols += copa[i]['time_fora_gols']
        elif copa[i]['time_fora']==selecao:
            total_de_gols += copa[i]['time_casa_gols']
    
    return total_de_gols


if __name__ == '__main__':
    main()
