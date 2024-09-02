import random
jogo_maquina = random.randint(1,5)

print('BEM VINDO AO PAR OU ÍMPAR!')
escolha = input('Escolha p-par ou i-ímpar\n >>>')
aposta_joggador = int(input('Digite um número de 1 a 5 para jogar:\n >>>'))
resposta = jogo_maquina + aposta_joggador
if (escolha == 'p' and resposta % 2 == 0):
    print('Deu {}. Parabés você ganhou!!!'.format(resposta))
elif (escolha == 'p' and resposta % 2 != 0):
    print('Deu {}. Sinto muito, você perdeu!'.format(resposta))
elif (escolha == 'i' and resposta % 2 == 0):
    print('Deu {}. Sinto muito, você perdeu!'.format(resposta))
else:
    print('Deu {}. Parabés você ganhou!!!'.format(resposta))