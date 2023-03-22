from random import randint
from time import sleep
computador = randint(0,5) #faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar ...')
print('-=-' * 20)
jogador = (int(input('Qual numero eu pensei ? '))) #jogador tenta adivinhar
print('PROCESSANDO')
sleep(2)
if jogador == computador:
    print('Parabens! Você acertou')
else:
    print('Eu Ganhei, pensei no numero {} e não no {}!'.format(computador,jogador))