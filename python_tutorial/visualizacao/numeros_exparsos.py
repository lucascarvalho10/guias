'''Problema de distribuição estatística básico
Encontrar a distribuição média em valores aleatórios entre 0 e 1
'''

import numpy as np 
from matplotlib import pyplot as plt

n = 10**6

#gerando os valores de tendência
ratios = np.random.random(n)/np.random.random(n)

print((np.floor(ratios) %2 ==  0).mean())

plt.hist(ratios, range=(0, 20), bins=20, rwidth=0.9)

plt.show()