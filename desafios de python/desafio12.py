#crie um algoritmo que leia o preço de um produto e mostre o novo preço com 5% de desconto
produtoin= float(input('Digite o preço inicial do produto:'))
produtofn= float(produtoin-(5/100*produtoin))

print(f"O produto passa a ser {produtofn} reias com o desconto de 5% aplicado")