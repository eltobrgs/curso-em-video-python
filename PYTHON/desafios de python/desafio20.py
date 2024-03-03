#faça um programa que escolha a ordem de apresentaçao de um trabalho 
import random
p1= str(input("digite o nome do primeiro aluno:"))
p2= str(input("digite o nome do segundo aluno:"))
p3= str(input("digite o nome do terceito aluno:"))
p4= str(input("digite o nome do quarto aluno:"))
alunos=[p1, p2, p3, p4]
random.shuffle(alunos)

print(f"a ordem de apresentaçao embaralhada é é {alunos}")
