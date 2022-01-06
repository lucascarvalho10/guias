#Sâo as estruturas de dados mais simples, muito parecidas com vetores

#gerando ums lista
lista = [num for num in range(100) if num%3 == 0]
print(lista)

listaDois = [num for num in range(100) if num%5 != 0]

#com extend, podemos concatenar duas listas facilmente
print(lista.extend(listaDois))

#o operador in verifica se algo existe em uma lista
print( 0 in listaDois)

if 2 in listaDois:
    print("Pertence")

#Ìndices negativos fazem referência ao final
print(lista[-1])

#Podemos quebrar com operadores
print(lista[:3]) #até antes do 3
print(lista[12:]) #depois do 12
print(lista[3:12]) #entre 3 e 12