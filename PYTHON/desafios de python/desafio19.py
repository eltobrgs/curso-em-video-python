#faça um programa para sortear um entre 4 alunos em uma listta
import random
n1= str(input("digigte o primeiro aluno:"))
n2= str(input("digigte o segundo aluno:"))
n3= str(input("digigte o terceiro aluno:"))
n4= str(input("digigte o quarto aluno:"))
alunos=[n1, n2, n3, n4]
escolhido= random.choice(alunos)
print(f'o aluno escolhido foi o aluno {escolhido}')