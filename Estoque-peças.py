# Definindo a lista que armazenará os dicionários com os dados das peças
pecas = []

# Definindo o contador que será utilizado como código para cada peça cadastrada
codigo = 1

# Função para cadastrar uma nova peça

def cadastrarPeca():
    # Criando um dicionário para armazenar os dados da nova peça
    global codigo
    peca = {}
    peca['codigo'] = codigo
    peca['nome'] = input('Digite o nome da peça: ')
    peca['fabricante'] = input('Digite o fabricante da peça: ')
    peca['valor'] = float(input('Digite o valor da peça: '))
    # Adicionando o dicionário da nova peça à lista de peças
    pecas.append(peca)
    # Incrementando o código para a próxima peça cadastrada
    codigo += 1
    print('Peça cadastrada com sucesso!')

# Função para consultar as peças

def consultarPeca():
    while True:
        print('Escolha uma opção:')
        print('1 - Consultar Todas as Peças')
        print('2 - Consultar Peças por Código')
        print('3 - Consultar Peças por Fabricante')
        print('4 - Retornar')
        opcao = int(input())
        if opcao == 1:
            # Imprimindo todos os dicionários da lista de peças
            for peca in pecas:
                print(peca)
        elif opcao == 2:
            codigo = int(input('Digite o código da peça: '))
            # Buscando o dicionário com o código da peça
            peca = None
            for p in pecas:
                if p['codigo'] == codigo:
                    peca = p
                    break
            if peca is not None:
                print(peca)
            else:
                print('Peça não encontrada!')
        elif opcao == 3:
            fabricante = input('Digite o fabricante da peça: ')
            # Buscando todos os dicionários de peças com o fabricante
            encontradas = []
            for peca in pecas:
                if peca['fabricante'] == fabricante:
                    encontradas.append(peca)
            if len(encontradas) > 0:
                for peca in encontradas:
                    print(peca)
            else:
                print('Nenhuma peça encontrada para o fabricante informado!')
        elif opcao == 4:
            break
        else:
            print('Opção inválida!')

# Função para remover uma peça

def removerPeca():
    codigo = int(input('Digite o código da peça que deseja remover: '))
    # Buscando o dicionário com o código da peça 
    peca = None
    for p in pecas:
        if p['codigo'] == codigo:
            peca = p
            break
    if peca is not None:
        # Removendo o dicionário da lista de peças
        pecas.remove(peca)
        print('Peça removida com sucesso!')
    else:
        print('Peça não encontrada!')


# Looping principal do programa
while True:
    print('Bem vindo ao controle de estoque do Gabriel Roewer Pilger')
    print('Escolha uma opção:')
    print('1 - Cadastrar Peça')
    print('2 - Consultar Peça')
    print('3 - Remover Peça')
    print('4 - Sair')

    opcao = input('Opção escolhida: ')

    if opcao == '1':
        print('Código: '+str(codigo))
        cadastrarPeca()
    elif opcao == '2':
        consultarPeca()
    elif opcao == '3':
        removerPeca()
    elif opcao == '4':
        print('Programa Encerrado!')
        break
    else:
        print('Opção inválida, tente novamente!')
