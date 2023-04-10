#Escreve o boas vindas e o nome da loja
print("Bem vindo a loja do Gabriel Roewer Pilger")

#Input para colocar o valor unitário do produto
valor_unitario = float(input("Digite o valor unitário do produto: "))

#Input para colocar a quantidade de produtos
quantidade = int(input("Digite a quantidade do produto: "))

#Calcula o valor total sem desconto com base no resultado dos inputs
valor_total_sem_desconto = valor_unitario * quantidade

#Calcula o desconto se a quantidade for menor que 10
if quantidade < 10:
    desconto = 0
#Calcula o desconto se a quantidade for menor que 100 e maior que 10    
elif quantidade < 100:
    desconto = 0.05
#Calcula o desconto se a quantidade for menor que 1000 e maior que 100    
elif quantidade < 1000:
    desconto = 0.1
#Calcula o desconto se a quantidade for maior que 1000    
else:
    desconto = 0.15

#Aplica o desconto calculado no valor total sem desconto
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto)

#Calcula o percentual de desconto
percentual_desconto = (1 - valor_total_com_desconto / valor_total_sem_desconto) * 100

#Escreve no prompt o Valor total sem desconto
print("Valor total sem desconto: R$ {:.2f}".format(valor_total_sem_desconto))

#Escreve no prompt o Valor total com desconto
print("Valor total com desconto: R$ {:.2f}".format(valor_total_com_desconto))

#Escreve no prompt o desconto total aplicado em % 
print ("O percentual de desconto aplicado foi de {:.0f}%".format(percentual_desconto))