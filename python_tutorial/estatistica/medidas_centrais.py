#As medidas de tendência central são as médias clássicas

import numpy as np 
from random import randint
from scipy import stats

#módulo legal para listas
import collections

lista = [randint(1, 100) for _ in range(25)]
vetor = np.array(lista)

#Média arimética
#podemos utilizar diretamente a biblioteca numpy

print(vetor.mean())


#Sobre a mediana, é legal construir a função

def mediana(v):
    tam = len(v)
    ordenado = sorted(v)

    valor_medio = tam//2

    if valor_medio%2 == 0:
        return ordenado[valor_medio]
    else:
        return (ordenado[valor_medio -1] +ordenado[valor_medio])//2

print(mediana(vetor))


#A média é muito sensível a valores discrepantes, que podem levar a conclusões enganosas

#Por exemplo, o quantil 20% (ou 20%-quantil) é o valor
#que separa os 20% menores valores dos 80% maiores de uma amostra.
#Assim, a Mediana é o quantil 50% 

def quantil(x, p):
    '''retorna o valor percentual p-ésimo em x'''
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print(quantil(vetor, 0.2))

#A última medida é a moda, usaremos scipy
print(stats.mode(vetor))