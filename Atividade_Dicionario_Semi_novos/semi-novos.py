def main():
    nome_arquivo_veiculos = 'veiculos.txt'
    nome_arquivo_marcas = 'marcas.txt'

    veiculos = importar_veiculos(nome_arquivo_veiculos)
    marcas = importar_marcas(nome_arquivo_marcas)
    
    op = int(input(menu()))

    while op != 0:
        if op == 1:
            mostrar_dados_veiculos(veiculos)
        elif op == 2:
            mostrar_dados_marcas(marcas)
        elif op == 3:
            inserir_novo_veiculo(veiculos, marcas)
        elif op == 4:
            inserir_nova_marca(marcas)
        elif op == 5:
            veiculos = deletar_veiculo(veiculos)
        elif op == 6:
            marcas = deletar_marca(marcas)
        elif op == 7:
            veiculos = editar_veiculo(veiculos)
        elif op == 8:
            marcas = editar_marca(marcas)
            
        op = int(input(menu()))
    
    salvar_dados_veiculos(veiculos, nome_arquivo_veiculos)
    salvar_dados_marca(marcas, nome_arquivo_marcas)


def menu():
    menu = '====== APP SEMI-NOVOS ====='\
        + '\n1 - Mostrar Dados Veiculos'\
        + '\n2 - Mostrar Dados Marcas'\
        + '\n3 - Inserir Novo Veiculo'\
        + '\n4 - Inserir Nova Marca'\
        + '\n5 - Deletar Veiculo'\
        + '\n6 - Deletar Marca'\
        + '\n7 - Editar Veiculo'\
        + '\n8 - Editar Marca'\
        + '\n0 - Sair\n'
    
    return menu


# DADOS VEICULOS


def importar_veiculos(nome_arquivo):
    veiculos = open(nome_arquivo)
    dados_veiculo = veiculos.readlines()
    veiculos.close()
    
    d_veiculos = {}
    vetor_veiculos = []

    for i in range(len(dados_veiculo)):
        dados = dados_veiculo[i].strip().split('#')
        d_veiculos = {'placa' : dados[0], \
                    'nome' : dados[1], \
                    'marca' : int(dados[2]), \
                    'ano' : dados[3], \
                    'quilometragem' : int(dados[4]), \
                    'preco' : dados[5]}
        vetor_veiculos += [d_veiculos] 
    
    return vetor_veiculos


def salvar_dados_veiculos(veiculos, nome_arquivo):
    salva_veiculos = open(nome_arquivo, 'w')

    for i in range(len(veiculos)):
        salva_veiculos.write(formatar_dados_veiculos(veiculos[i]))
    
    salva_veiculos.close()


def formatar_dados_veiculos(dados):
    return '%s#%s#%d#%s#%d#%s\n' % (dados['placa'], dados['nome'],\
                                dados['marca'], dados['ano'], \
                                dados['quilometragem'], dados['preco'])


# DADOS MARCAS


def importar_marcas(nome_arquivo):
    marcas = open(nome_arquivo)
    dados_marcas = marcas.readlines()
    marcas.close()

    d_marcas = {}
    vetor_marcas = []

    for i in range(len(dados_marcas)):
        dados = dados_marcas[i].strip().split('#')
        d_marcas = {'id_marca' : int(dados[0]), \
                    'nome' : dados[1], \
                    'pais' : dados[2]}
        vetor_marcas += [d_marcas] 
        
    return vetor_marcas


def salvar_dados_marca(marca, nome_arquivo):
    salva_marca = open(nome_arquivo, 'w')

    for i in range(len(marca)):
        salva_marca.write(formatar_dados_marca(marca[i]))
    
    salva_marca.close()


def formatar_dados_marca(dados):
    return '%d#%s#%s\n' % (dados['id_marca'], dados['nome'], dados['pais'])


# MOSTRAR DADOS


def mostrar_dados_veiculos(veiculos):
    print('\t\t====== VEICULOS =======')
    print('PLACA    NOME    MARCA   ANO    QUILOMETRAGEM   PREÇO')
    for i in range(len(veiculos)):
        print('%s' % veiculos[i]['placa'] + '\t',end = '')
        print('%s' % veiculos[i]['nome'] + '\t',end = '  ')
        print('%s' % veiculos[i]['marca'] + '\t',end = '')
        print('%s' % veiculos[i]['ano'] + '\t',end = '    ')
        print('%s' % (veiculos[i]['quilometragem']) + '\t', end = ' ')
        print(veiculos[i]['preco'])
    print()


def mostrar_dados_marcas(marcas):
    print('\t======= MARCAS ========')
    print('ID MARCA    NOME         PAÍS')
    for i in range(len(marcas)):
        print('  %s' % marcas[i]['id_marca'] + '\t', end='    ')
        print('%s' % marcas[i]['nome'] + '\t', end='')
        print('%s' % marcas[i]['pais'] + '\t')
    print()


# INSERT NOVOS DADOS


def inserir_novo_veiculo(veiculo, marcas):
    novo_veiculo = []
    novo_veiculo = veiculo
    
    d_veiculos = {'placa' : (input('Placa: ')), \
                'nome' : (input('Nome: ')), \
                'marca' : (int(input('Id Marca: '))), \
                'ano' : (input('Ano: ')), \
                'quilometragem' : (int(input('Quilometragem: '))), \
                'preco' : (input('Preco: '))}
    
    tem = False
    for i in range(len(marcas)):
        if marcas[i]['id_marca'] == d_veiculos['marca']:
            tem = True
    id_marca = d_veiculos['marca']
    confirmacao = tem_marca_no_registo(tem, marcas, id_marca)
    
    if confirmacao:
        novo_veiculo += [d_veiculos]
        print('VEICULO INSERIDO')
    
    return novo_veiculo


def inserir_nova_marca(marcas):
    nova_marca = []
    nova_marca = marcas
    
    d_marcas = {'id_marca' : (int(input('Id Marca: '))),
                'nome' : (input('Nome: ')), \
                'pais' : (input('País: '))}
                
    nova_marca += [d_marcas]
    
    return nova_marca


def tem_marca_no_registo(valor, marcas, n_id_marca):
    if valor == False:
        op = input('Marca não esta no registro. Deseja cadastra-la(1-S|2-N): ')
        
        if op == '1':
            nova_marca = []
            nova_marca = marcas
    
            d_marcas = {'id_marca' : n_id_marca,
                        'nome' : (input('Nome: ')), \
                        'pais' : (input('País: '))}
                
            nova_marca += [d_marcas]
            return True

        else:
            print('VEICULO NAO INSERIDO!!!')
            return False
    else:
        return True


# DELETE DADOS


def deletar_veiculo(veiculos):
    print('\t====DELETAR REGISTRO DE VEICULO====')
    mostrar_dados_veiculos(veiculos)
    op = int(input('Qual registo voce quer apagar: '))
    while op not in range(1, len(veiculos)+1):
        print('OPCAO INVALIDA!')
        op = int(input('Qual registo voce quer apagar: '))
    
    novo_vetor_veiculo = []
    for i in range(len(veiculos)):
        if i != (op-1):
            novo_vetor_veiculo += [veiculos[i]]
    
    return novo_vetor_veiculo



def deletar_marca(marcas):
    print('\t====DELETAR REGISTRO DE MARCAS====')
    mostrar_dados_marcas(marcas)
    op = int(input('Qual registo voce quer apagar: '))
    while op not in range(1, len(marcas)+1):
        print('OPCAO INVALIDA!')
        op = int(input('Qual registo voce quer apagar: '))
    
    novo_vetor_marcas = []
    for i in range(len(marcas)):
        if i != (op-1):
            novo_vetor_marcas += [marcas[i]]
    
    return novo_vetor_marcas


# EDITAR DADOS


def editar_veiculo(veiculos):
    print('\t====EDITAR VEICULOS=====')
    
    op = int(input('Qual registo voce quer editar: '))
    while op not in range(1, len(veiculos)+1):
        print('OPCAO INVALIDA!')
        op = int(input('Qual registo voce quer editar: '))
    
    op_edit = int(input(('O que deseja editar: (1-PLACA|2-NOME|3-MARCA|4-ANO|5-QUILOMETRAGEM|6-PRECO)\n')))
    while op not in range(1, 6):
        print('OPCAO INVALIDA!')
        op_edit = int(input(('O que deseja editar: (1-PLACA|2-NOME|3-MARCA|4-ANO|5-QUILOMETRAGEM|6-PRECO)\n')))
    
    if op_edit == 1:
        veiculos[op-1]['placa'] = input('Digite a placa: ')
    elif op_edit == 2:
        veiculos[op-1]['nome'] = input('Digite o nome: ')
    elif op_edit == 3:
        veiculos[op-1]['marca'] = int(input('Digite o id da marca: '))
    elif op_edit == 4:
        veiculos[op-1]['ano'] = input('Digite o ano: ')
    elif op_edit == 5:
        veiculos[op-1]['quilometragem'] = input('Digite a quilometragem: ')
    elif op_edit == 6:
        veiculos[op-1]['preco'] == input('Digite o preco: ')
    
    novo_vetor_veiculo = []
    
    for i in range(len(veiculos)):
        novo_vetor_veiculo += [veiculos[i]]

    return novo_vetor_veiculo


def editar_marca(marcas):
    print('\t====EDITAR MARCA=====')
    
    op = int(input('Qual registo voce quer editar: '))
    while op not in range(1, len(marcas)+1):
        print('OPCAO INVALIDA!')
        op = int(input('Qual registo voce quer editar: '))
    
    op_edit = int(input(('O que deseja editar: (1-ID MARCA|2-NOME|3-PAÍS)\n')))
    while op not in range(1, 6):
        print('OPCAO INVALIDA!')
        op_edit = int(input(('O que deseja editar: (1-ID MARCA|2-NOME|3-PAÍS)\n')))
    
    if op_edit == 1:
        marcas[op-1]['id_marca'] = int(input('Digite o id da marca: '))
    elif op_edit == 2:
        marcas[op-1]['nome'] = input('Digite o nome: ')
    elif op_edit == 3:
        marcas[op-1]['pais'] = input('Digite o país da marca: ')
    
    novo_vetor_marcas = []
    
    for i in range(len(marcas)):
        novo_vetor_marcas += [marcas[i]]

    return novo_vetor_marcas


if __name__ == '__main__':
    main()