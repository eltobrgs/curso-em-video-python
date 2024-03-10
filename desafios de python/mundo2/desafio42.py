a= float(input('Digite o comprimento da primeira reta:'))
b= float(input('Digite o comprimento da segunda reta:'))
c= float(input('Digite o comprimento da terceira reta:'))

if a+b>c and a+c>b and b+c>a:
    print(f'as retas de tamanhos {a}, {b} e {c} podem formar um triangulo')
    if a==b==c:
        print('E será um trinagulo EQULATERO')
    elif (a == b) or (a == c) or (b == c):
        print("E será um triângulo ISÓSCELES.")
    else:
        print('E será um triangulo Escaleno')
else:
    print(f'as retas de tamanhos {a}, {b} e {c} nao podem formar um triangulo')