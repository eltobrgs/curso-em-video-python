import datetime

# Obter o ano atual
atual = datetime.date.today().year
# Solicitar o ano de nascimento ao usuário
nascimento = int(input('Em que ano você nasceu?: '))
# Calcular a idade
idade = atual - nascimento
if idade<=9 and idade<14:
    print(f'o nadador tem {idade} e portanto sua categoria é mirim')
elif idade<=14 and idade<19:
    print(f'o nadador tem {idade} e portanto sua categoria é infantil')
elif idade<=19 and idade<25:
    print(f'o nadador tem {idade} e portanto sua categoria é junior')
elif idade<=25:
    print(f'o nadador tem {idade} e portanto sua categoria é senior')
else:
    print(f'o nadador tem {idade} e por ser maior que 25 anos ele alcançou o patamar de MASTER!!!')