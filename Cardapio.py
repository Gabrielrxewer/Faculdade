produtos = {
    100: {'descricao': 'Cachorro-Quente', 'valor': 9.00},
    101: {'descricao': 'Cachorro-Quente Duplo', 'valor': 11.00},
    102: {'descricao': 'X-Egg', 'valor': 12.00},
    103: {'descricao': 'X-Salada', 'valor': 13.00},
    104: {'descricao': 'X-Bacon', 'valor': 14.00},
    105: {'descricao': 'X-Tudo', 'valor': 17.00},
    200: {'descricao': 'Refrigerante Lata', 'valor': 5.00},
    201: {'descricao': 'Chá Gelado', 'valor': 4.00}
}

cardapio = '''
            Código   Descrição            Valor(R$)
            100      Cachorro-Quente      9,00
            101      Cachorro-Quente Duplo 11,00
            102      X-Egg                12,00
            103      X-Salada             13,00
            104      X-Bacon              14,00
            105      X-Tudo               17,00
            200      Refrigerante Lata    5,00
            201      Chá Gelado           4,00
        '''

print(cardapio)

total = 0
while True:
    codigo = int(input('Digite o código do produto desejado: '))
    if codigo not in produtos:
        print('Opção inválida!')
        continue

    produto = produtos[codigo]
    total += produto['valor']
    print(
        f'Produto selecionado: {produto["descricao"]}, Valor: R${produto["valor"]:.2f}')

    opcao = input('Deseja pedir mais alguma coisa? (S/N): ')
    if opcao.upper() == 'N':
        print(f'Total a pagar: R${total:.2f}')
        break
    elif opcao.upper() != 'S':
        print('Opção inválida!')
        break
