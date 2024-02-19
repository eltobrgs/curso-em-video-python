#faça um programa que leia a largura e altura de uma parede em metros, calcule a quantidade de tinta necessaria para pinta-la
#sabendo que cada litro de tinta pinta uma area de 2m quadrados 

largura= float(input("Informe a largura da parede:"))
altura= float(input("Informe a altura da parede:"))
areaparede= float(largura*altura)
areatinta= float(largura*altura)/2 

print(f"A area da sua parede é {areaparede} metros quadrados, sabendo que um litro de tinta é usado a cada dois metros quadrados, voce tera que usar {areatinta} litros de tinta")