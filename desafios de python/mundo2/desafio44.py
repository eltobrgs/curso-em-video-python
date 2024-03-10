preço= float(input('DIGITE O PREÇO DO PRODUTO QUE DESEJA COMPRAR:'))
pagamento=int(input(''' Digite a condiçao de pagamento:
[1]A VISTA NO DINHEIRO OU CHEQUE 
[2]A VISTA NO CARTÃO
[3]EM ATE 2X NO CARTÃO
[4]EM 3X OU MAIS NO CARTÃO:'''))

if pagamento==1:
    preçofinal= preço-(preço*(10/100))
    print(f'Com a condiçao de pagamento sendo a vista no dinheiro ou chque voce garante 10% de desconto e de R${preço} voce leva seu produto por apenas R${preçofinal:.2f}')
elif pagamento==2:
    preçofinal= preço-(preço*(5/100))
    print(f'Com a condiçao de pagamento sendo a vista no cartão voce garante 5% de desconto e de R${preço} voce leva seu produto por apenas R${preçofinal:.2f}')
elif pagamento==3:
    print(f'Com a condiçao de pagamento sendo parcelado no cartão em ate 2x voce não garante desconto e seu produto sairá por R${preço:.2f} ')
elif pagamento==4:
    preçofinal= preço+(preço*(20/100))
    print(f'Com a condiçao de pagamento sendo parcelado no cartao em 3x ou mais voce nao garante desconto e seu produto sairá com juros de 20% totalizando um preco final de R${preçofinal:.2f} ')
else:
    print('ENTRADA INVALIDA, POR GENTILEZA, DIGITAR UMA RESPOSTA VALIDA')