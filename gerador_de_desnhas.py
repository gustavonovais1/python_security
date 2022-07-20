
from queue import PriorityQueue
import random, string

print('Gerador de senhas')

tamanho = int(input('Digite o tamanho de senha desejado: '))

chars = string.ascii_letters + string.digits + '!ç@#$%&*()_+-=.;,:/?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))