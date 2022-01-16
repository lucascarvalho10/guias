# podemos percorrer uma lista

lista = [7, 6, 8, 10, 100, 12]

for elemento in lista:
    print(elemento*2)

# Algumas operações interessantes com listas:

# Aqui, repetimos a lista o número dado de vezes
nova_lista = lista*2
print(nova_lista)

# Podemos concatenar as lista

ultima_lista = nova_lista + lista
print(ultima_lista)

# Podemos fatiar elementos para dicionar na lista
t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
