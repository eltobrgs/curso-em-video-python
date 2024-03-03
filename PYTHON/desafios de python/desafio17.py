#faça um programa que lia o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo 
# e calcule o comprimento da hipotenusa 


#sem importaçao da classe do modulo math 
#co= float(input("digite o valor do cateto oposto do trinagulo retangulo:"))
#ca= float(input("digite o calor do cateto adjascente do tringulo retangulo:"))
#hip= (co**2+ca**2)**(1/2)
#print(f"a hipotenusa vai medir {hip:.2f}")

#agora importando a biblioteca math 

import math 
co= float(input("digite o valor do cateto oposto do trinagulo retangulo:"))
ca= float(input("digite o calor do cateto adjascente do tringulo retangulo:"))
hip= math.hypot(ca, ca)

print(f"a hipotenusa vai medir {hip:.2f}")