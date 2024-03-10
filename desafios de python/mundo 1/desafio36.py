valorcasa= float(input('Qual é o valor da casa?:'))
salario= float(input("qual é o seu salario?:"))
anos= float(input('em quantos anos pretende pagar a casa?:'))
meses= anos*12

print(f'voce tera que me pagar {valorcasa/meses}R$ por mes por {anos} para conseguir quitar a casa')
if (30/100)*salario> meses/valorcasa:
    print('Parabéns, seu financiamento foi aprovado!!')
else:
    print("Infelizmente seu financiamento foi negado")