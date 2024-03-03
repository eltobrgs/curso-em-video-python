
# Crie um programa que leia o nome completo de uma pessoa:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome:
nome = str(input("Digite seu nome: ")).strip()
print(f"o seu nome em maiusculo é {nome.upper()}")
print(f"o seu nome em minusculo é {nome.lower()}")
print(f"seu nome ao todo {len(nome)- nome.count(' ')} letras")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")