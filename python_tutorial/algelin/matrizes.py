#Matrizes, em python, são listas de listas. 

# A possui duas linhas e três colunas e B possui três linhas e duas colunas
A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2], [3, 4], [5, 6]]


#Vamos devolver o formato da matriz: o operador len retorna o tamanho de uma lista
def forma(A):
    linhas = len(A)
    colunas = len(A[0])
    return linhas, colunas

l, c = forma(A)

print(l, c)


