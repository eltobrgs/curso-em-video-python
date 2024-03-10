nota1= float(input('Digite a primeira nota:'))
nota2= float(input('Digite a segunda nota: '))
media=(nota1+nota2)/2
print(f'Tirando {nota1} e {nota2}, a media do aluno será {media}')
if media<7:
    print('o aluno foi REPROVADO...')
elif media>7:
    print('o aluno está APROVADO!!!')
