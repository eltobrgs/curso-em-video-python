#faça um programa que leia a quantidade de km rodado por um carro e a quantidade de dias que o carro ficou alugado.
#calcule o preço a pagar sabendo que o dia custa R$60 e o km rodado custa R$0.15

dia=int(input("quantos dias voce ficou com o carro?:"))
km= float(input("quantos km foram rodados com o carro?:"))

print(f"com {dia} dias rodados e {km} percorridos o preço final do aluguel do carro será R${(dia*60)+(km*0.15):2}")