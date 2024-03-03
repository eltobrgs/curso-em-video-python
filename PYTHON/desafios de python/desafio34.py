print('BOM DIA, PARA O AGRADO DOS MEUS ESCRAV... OPS, DOS MEUS FUNCIONARIOS QUE TANTO AMO. TEREMOS UM REAJUSTE SALARIAL POSITIVO... MALDITO SINDICATO!!')

salario=float(input('Quanto é o seu salario atual?:'))

if salario>=1250.00:
    novosalario=salario+(10/100)*salario
else:
    novosalario=salario+(15/100)*salario

print(f'seu novo salario é de {novosalario}')