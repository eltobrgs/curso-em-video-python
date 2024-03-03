#crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados


num= int(input('digite um numero:'))
u= num/1%10
d= num/10%10
c= num/100%10
m= num/1000%10

print(f"a unidade é:{int(u)}")
print(f"a dezena é :{int(d)}")
print(f"a centena é:{int(c)}")
print(f"a unidade de milhar é:{int(m)}")
