from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-'*15)
print('Vou pensar em um número, tente adivinhar...')
print('-=-'*15)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('Processando.....')
sleep(2)
if jogador == computador:
    print('Parabéns, você acertou!!')
else:
    print('Você errou!! Pensei no número {} e não no número {}'.format(computador, jogador))
    
