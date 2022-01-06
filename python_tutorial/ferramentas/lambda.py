#Assim como em JS, funções são de Primeira Classe
def soma(a, b):
    return a + b

print(soma(10, 2))

#podemos, então, atribuí-las a variáveis

somaL = lambda x,y: x + y

'''Existe um pequeno padrão que prefere
    def somaL(x, y): return x + x
'''

print(somaL(10, 2))


#Um exemplo um pouco mais arrojado
import random

valores = range(50)

par = lambda vetor: vetor%2 == 0

for num in random.sample(valores, 10) :
    print(num, par(num))