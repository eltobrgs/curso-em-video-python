altura=float(input('Forneça sua altura em M:'))
peso= float(input('Forneça seu peso em KG:'))
IMC=peso/altura**2
print(f'Seu IMC é de {IMC:.2f}')
if IMC<=18.5:
    print('E voce está abaixo do peso...')
elif IMC>=18.5 and IMC<25:
    print('E voce está no peso ideal!!')
elif IMC<=25 and IMC<30:
    print('E voce está em sobrepeso...')
elif IMC<=30 and IMC<40:
    print('E voce esta com obesidade... cuidado')
else:
    print('E voce está com obesidade morbida, cuidado!!')