lista = [1, 2, 3, 4, 5]
outra_lista = [8, 7]

# append adiciona um elemento
lista.append(9)

# extend adiciona uma lista. Não altera a segunda
lista.extend(outra_lista)

print(lista)
lista.sort()  # Retonrna none, então é preciso tomar cuidado
print(lista)


# Para soma elementos, o python conta um uma função interna
print(sum(lista))


# Para excluir algum elemento, pode-se utilizar pop ou del

print(outra_lista.pop(1))  # retonrna o valor
del outra_lista[0]  # não retorna nada

# Também é possível excluir se soubermos o nome
lista.append(100)
print(lista)
lista.remove(100)
print(lista)
