print('SEJA SINCERO OU HAVERA CONSEQUENCIAS INIMAGINAVEIS')
vel=float(input('qual a velocidade em KM que voce passou na avenida antonio pereira? '))

if vel>80:
    multa= (vel-80)*7
    print(f"voce foi multado em {multa} pois excedeu o limite de velocidade de 80km/h")
else:
    print('voce nao foi multado. tenha um bom dia!!!')