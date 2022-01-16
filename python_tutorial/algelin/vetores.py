#Vetores são elementos de espaços vetoriais.
#Existem alguns métodos bastante interessantes para estudar e manipulá-los em Python

#De modo abstrado, são elementos que podem ser somados e multiplicados por escalares
#Squi, serão tratados como pontos no espaço

#Listas são frequentemente utilizadas para isso, mas precisamos construir a aritmética

vetorA = [1, 2, 3, 4, 5]
vetorB = [6, 7, 8, 9, 10]

#A função zip cria um paralelismo nos vetores

def soma (v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def sub (v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

#Produto por escalar

def escalar(v, a):
    return [v_i*a for v_i in v]


print(soma(vetorA, vetorB), sub(vetorB, vetorA), escalar(vetorA, 10))


#Agora, vamos para algumas operações mais complexas

