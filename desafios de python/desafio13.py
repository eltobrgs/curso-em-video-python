#faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com um aumento de 15%
salarioin= float(input("Informe seu salario:"))
salario15= salarioin+(15/100*salarioin)

print(f"O seu salario corrigido com aumento de 15% é de {salario15}")