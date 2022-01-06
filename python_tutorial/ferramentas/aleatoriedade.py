#Existem métodos para gerar valores aleatórios, bastante úties
import random

print(random.random());

#Criando uma lista de valores aleatórios
''' Observemos que o operador _ oculta alguma possível variável'''
print([random.random() for _ in range(10)])

#temos o metodo para selecionar algum elemento de uma lista
print(random.choice(["Lucas", "Maria", "Tulio"]))

#podemos, também, obter uma amostra de valores limitados sem repetição
#aqui, ele escolhe 10 valores aleatórios dentre os de 0 a 100
amostra = range(100)
print(random.sample(amostra, 10))