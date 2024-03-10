a= float(input('Digite o comprimento da primeira reta:'))
b= float(input('Digite o comprimento da segunda reta:'))
c= float(input('Digite o comprimento da terceira reta:'))

if a+b>c and a+c>b and b+c>a:
    print(f'as retas de tamanhos {a}, {b} e {c} podem formar um triangulo')
else:
    print(f'as retas de tamanhos {a}, {b} e {c} nao podem formar um triangulo')