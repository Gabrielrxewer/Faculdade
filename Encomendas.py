# Definindo a função que define as dimensões do objeto, calcula e retorna o volume
def dimensoesObjeto():

    # Pergunta a altura do objeto e verifica se o usuário deu uma altura válida
    while True:
        try:
            altura = float(input("Digite a altura do objeto em cm: "))
            if altura <= 0:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número válido para a altura.")

    # Pergunta o comprimento do objeto e verifica se o usuário deu um comprimento válido
    while True:
        try:
            comprimento = float(input("Digite o comprimento do objeto em cm: "))
            if comprimento <= 0:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número válido para o comprimento.")

    # Pergunta a largura do objeto e verifica se o usuário deu uma largura válida
    while True:
        try:
            largura = float(input("Digite a largura do objeto em cm: "))
            if largura <= 0:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido. Digite um número válido para a largura.")
    
    # Calcula o volume em cm³
    volume = altura * comprimento * largura
    return volume

# Pergunta as dimensões do objeto
print("Bem vindo ao programa de logística do Gabriel Roewer Pilger, Informe as dimensões do objeto:")

# Chama a função que pergunta as dimensões do objeto, calcula e retorna o volume
volume = dimensoesObjeto()

# Define os valores da tabela de dimensões
if volume < 1000:
    valor_dimensoes = 10
elif volume < 10000:
    valor_dimensoes = 20
elif volume < 30000:
    valor_dimensoes = 30
elif volume < 100000:
    valor_dimensoes = 50
else:
    print("O objeto não pode ter um volume maior ou igual a 100000 cm³.")
    exit()

# Pergunta o peso do objeto e verifica se o usuário deu um peso válido
while True:
    try:
        peso = float(input("Digite o peso do objeto em kg: "))
        if peso <= 0 or peso >= 30:
            raise ValueError
        break
    except ValueError:
        print("Valor inválido. Digite um número positivo menor que 30 para o peso.")

# Define os valores da tabela de peso
if peso <= 0.1:
    multiplicador_peso = 1
elif peso < 1:
    multiplicador_peso = 1.5
elif peso < 10:
    multiplicador_peso = 2
elif peso < 30:
    multiplicador_peso = 3
else:
    print("O objeto não pode ter um peso maior ou igual a 30 kg.")
    exit()

# Pergunta a rota do objeto e verifica se o usuário deu uma rota válida
while True:
    print("Tabela de Rotas:\nRS - De Rio de Janeiro até São Paulo\nSR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\nSB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\nRB - Rio de Janeiro até Brasília")
    rota = input("Digite a rota do objeto: ")
    if rota.upper() not in ["RS", "SR", "BS", "SB", "BR", "RB"]:
        print("Rota inválida. Digite uma rota válida.")
    else:
        break

# Define os valores da tabela de rotas
if rota.upper() == "RS" or rota.upper() == "SR":
    multiplicador_rota = 1
elif rota.upper() == "BS" or rota.upper() == "SB":
    multiplicador_rota = 1.2
elif rota.upper() == "BR" or rota.upper() == "RB":
    multiplicador_rota = 1.5

# Calcula o valor total a pagar
total = valor_dimensoes * multiplicador_peso * multiplicador_rota
print(f'O valor total a pagar é de R${total:.2f}.')
print("Dimensão: {:.2f}".format(valor_dimensoes))
print("Multiplicador do Peso: {:.2f}".format(multiplicador_peso))
print("Multiplicador do Frete: {:.2f}".format(multiplicador_rota))

