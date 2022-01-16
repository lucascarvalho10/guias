#Alguma noção de módulo e distância é importante

from math import sqrt

vetorA = [1, 2, 3, 4, 5]
vetorB = [6, 7, 8, 9, 10]

#Vamos para o produto escalar, a soma dos produtos das coordenadas (base ortnormal)

def prod_esc(v, w):
    return sum(v_i*w_i for v_i, w_i in zip(v, w))

#Agora, o cálculo do módulo de um vetor: raiz da soma dos quadrados das coordenadas

def soma_quad(v):
    return prod_esc(v, v)

def modulo(v):
    return sqrt(soma_quad(v))

#A distância entre dois vetores é o módulo da diferença
def sub(v, w):
    return [v_i - w_i for w_i, v_i in zip(v, w)]

def distancia(v, w):
    return modulo(sub(v, w))

print(prod_esc(vetorA, vetorB), soma_quad(vetorA), modulo(vetorA), distancia(vetorB, vetorA))