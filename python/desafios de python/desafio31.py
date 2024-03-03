kmviagem= float(input('qual a distancia em KM voce ira percorrer na viagem:'))

if kmviagem<=200:
    preço1=kmviagem*0.50
    print(f'o preço da sua passagem será de {preço1}R$')
else:
    preço2= kmviagem*0.45
    print(f'o preço da sua passagem será de {preço2}R$')