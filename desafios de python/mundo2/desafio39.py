import datetime

# Obter o ano atual
atual = datetime.date.today().year

# Solicitar o ano de nascimento ao usuário
nascimento = int(input('Em que ano você nasceu?: '))

# Calcular a idade
idade = atual - nascimento

# Exibir a idade atual
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')

# Verificar se é necessário o alistamento
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Faltam {saldo} anos para o alistamento.')
    ano= atual+ saldo
    print(f'seu alistamento será em {ano}')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano=atual-saldo
    print(f'Seu alistamento foi em {ano}')
