# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ela 
a=input("digite um valor qualquer:")

print(f'Só tem espaços? {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em letras maiúsculas?{a.isupper()}')
print(f'Está em letras minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')