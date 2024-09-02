import random
resposta=random.randint(0,1)

print('BEM-VINDO AO CARA OU COROA!')
aposta  = input('Escolha: 0-cara ou 1-coroa\n >>>')
if (aposta == '0' and resposta == 0):
    print('Deu cara, parabéns, você ganhou!!!')
elif (aposta == '0' and resposta == 1):
    print('Deu cara, sinto muito, você perdeu!!')
elif (aposta == '1' and resposta == 0):
    print('Deu coroa, sinto muito, você perdeu!')
else:
    print('Deu coroa, parabés, você ganhou!!!')

