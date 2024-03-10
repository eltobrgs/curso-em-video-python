#faça um programa que leia um angulo qualquer e mostre na tela seu seno cosseno e tangente 
import math
ang= float(input("Digite o algulo em graus:"))
#a tag math.radians(ang) transforma graus em radianos, fazemos isso pois as tags math.sin, math.cos e math.tg leem radianos e nao graus 
sen= math.sin(math.radians(ang))
cos= math.cos(math.radians(ang))
tg= math.tan(math.radians(ang))

print(f"Quando o angulo é {ang}, seu seno será {sen:.2f}, seu cosseno {cos:.2f} e sua tangente {tg:.2f}")