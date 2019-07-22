def main():
    leia_opiniao = informacao_pesquisa()
    quantidade = 1

    serra,dilma,ciro,outros,indeciso,nulo_branco,quantidade =\
         dados_da_entrevista(leia_opiniao,quantidade)
    
    total_entrevistados = quantidade - 1
    
    porcent_serra,porcent_dilma,porcent_ciro,porcent_outros,porcent_indeciso,porcent_nulo_branco =\
        valores_porcentagem(serra,dilma,ciro,outros,indeciso,nulo_branco,total_entrevistados)

    segundo_turno = valida_segundo_turno(porcent_serra,porcent_dilma,porcent_ciro)
        
    print('TOTAL DE ENTREVISTADOS: %d'%total_entrevistados)
    print('____PONCENTAGEM CANDIDADOS____')
    print('Serra: %.2f'%porcent_serra,'%')
    print('Dilma: %.2f'%porcent_dilma,'%')
    print('Ciro: %.2f'%porcent_ciro,'%')
    print('Outros: %.2f'%porcent_outros,'%')
    print('Porcentagem de indecisos: %.2f'%porcent_indeciso,'%')
    print('Porcentagem de votos nulo/branco: %.2f'%porcent_nulo_branco,'%')
    print('Chance de segundo turno: ',segundo_turno)
            

def informacao_pesquisa():
    print('Valores validos: 45-Serra||13-Dilma||23-Ciro||99-Indeciso||98-Outros||0-Nulo/Branco')
    leia_opiniao = int(input('Qual o seu voto nas eleicoes:'))
    
    while not(leia_opiniao == 45 or leia_opiniao == 13 or leia_opiniao == 23\
        or leia_opiniao == 99 or leia_opiniao == 98 or leia_opiniao == 0 or leia_opiniao == -1):
        print('Valor invalido!!!')
        print('Valores validos: 45-Serra||13-Dilma||23-Ciro||99-Indeciso||98-Outros||0-Nulo/Branco')    
        leia_opiniao = int(input('Qual o seu voto nas eleicoes:'))
   
    return leia_opiniao


def dados_da_entrevista(leia_opiniao,quantidade):
    serra = 0
    dilma = 0
    ciro = 0 
    indeciso = 0
    nulo_branco = 0
    outros = 0
    
    while leia_opiniao != -1:
        if leia_opiniao == 45:
            serra += 1
        elif leia_opiniao == 13:
            dilma += 1
        elif leia_opiniao == 23:
            ciro += 1
        elif leia_opiniao == 99:
            indeciso += 1
        elif leia_opiniao == 98:
            outros += 1
        elif leia_opiniao == 0:
            nulo_branco += 1
        leia_opiniao = informacao_pesquisa()
        quantidade += 1
    
    return serra,dilma,ciro,outros,indeciso,nulo_branco,quantidade


def valores_porcentagem(serra,dilma,ciro,outros,indeciso,nulo_branco,total_entrevistados):    
    porcent_serra = (serra*100) / total_entrevistados
    porcent_dilma = (dilma*100) / total_entrevistados
    porcent_ciro = (ciro*100) / total_entrevistados
    porcent_outros = (outros*100) / total_entrevistados
    porcent_indeciso =(indeciso*100) / total_entrevistados
    porcent_nulo_branco = (nulo_branco*100) / total_entrevistados

    return porcent_serra,porcent_dilma,porcent_ciro,porcent_outros,porcent_indeciso,porcent_nulo_branco


def valida_segundo_turno(porcent_serra,porcent_dilma,porcent_ciro):
    if (porcent_serra>=51) or (porcent_dilma>=51) or (porcent_ciro>=51):
        segundo_turno = False
    else:
        segundo_turno = True
    
    return segundo_turno


if __name__ == '__main__':
    main()
    