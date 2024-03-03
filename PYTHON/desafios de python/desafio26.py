frase = str(input('Digite uma frase qualquer: ')).upper().strip()
letra = str(input('Digite a letra que quer análisar: ')).upper().strip()
print(f'A letra {letra} apareceu {frase.count(letra)} vezes')
print(f'A primeira aparição da letra {letra} foi na {frase.find(letra)+1}° posição ')
print(f' aultima vez que a letra {letra} apareceu foi na {frase.rfind(letra)+1}° posição')

