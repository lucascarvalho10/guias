# Uma distribuição clássica
# As variáveis aleatórias devem ser independentes e detemrinísticas
import math
from matplotlib import pyplot as plt


def dist_normal(x, mu=0, sigma=1):
    raiz_pi = math.sqrt(2*math.pi)
    return (math.exp(-(x - mu)**2/2/sigma**2)/(raiz_pi*sigma))


xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [dist_normal(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.show()

# É chamada de distribuição normal padrão quando μ = 0 e σ = 1. Se Z é uma
# variável aleatória normal padrão, então:
#       X = σZ + μ

# utilizamos a função de erro, para permitir a função cumulativa


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2
