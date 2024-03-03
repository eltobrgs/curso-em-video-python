ano= int(input('em que ano estamos?:'))
calc= ano%4
if calc==0:
    print('o ano é bissexto')
else:
    print('o ano nao é bissexto')