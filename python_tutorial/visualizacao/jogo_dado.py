'''Distribuição binomial de um jogo de dados'''

import numpy as np 
from matplotlib import pyplot as plt
from random import randint

jogadas = [randint(1, 6) + randint(1, 6) for _ in range (1000000)]

plt.hist(jogadas, range=(2, 12), bins=20, rwidth=0.9)
plt.title("Distribuição das Somas das Jogadas de Dados")
plt.xlabel("Soma")
plt.ylabel("Quantidade")

plt.show()