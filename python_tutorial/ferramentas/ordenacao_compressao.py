#Ordenação de listas (vetores):

x = [4,1,2,3]

y = sorted(x) # é [1,2,3,4], x não mudou
x.sort() # agora x é [1,2,3,4]

print(x);

#Como contar do menor para o maior:
# organiza a lista pelo valor absoluto do maior para o menor
print(sorted([-4,1,-2,3], key=abs, reverse=True)) # is [-4,3,-2,1]

print(sorted([-4,1,-2,3], reverse=True))


#Como comprimir uma lista: transformar em outra:

pares = [x for x in range(5) if x % 2 == 0] # [0, 2, 4]

numeros = [1, 10, -10, 8, 5, 6, 7, 15, 20, 65, 7, 8, 9];

quero = [num for num in numeros if num%5 == 0]
quero_dobrado = [valor*2 for valor in numeros if valor%2 == 0]
pares_ao_quadrado = [x**2 for x in pares if x%2 == 0]

print(quero, quero_dobrado, pares_ao_quadrado)