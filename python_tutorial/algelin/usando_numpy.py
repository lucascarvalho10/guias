import numpy as np 

#transformando uma lista em vetor
lista = [1, 2, 3, 4, 5]
listaB = [6, 7, 8, 9, 10]

vetor = np.array(lista)
vetorB = np.array(listaB)

#Média dos valores
print(vetor.mean())

#Soma do atual com anteriores - retorna outro vetor
print(vetor.cumsum())

#Máximo e mínimo
print(vetor.max(), vetor.min())

#Somando vetores - podemos apenas utilizar o operador convencional
print(np.add(vetor, vetorB), vetorB - vetor)

#O mesmo para a subtração
print(vetorB - vetor)