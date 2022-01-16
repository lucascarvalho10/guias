# Quando existe mais de uma referência a um objeot mutável, devemos tomar muito cuidado
# Chamamos isso de Alias

a = [1, 2, 3]
b = a
print(a is b)
a.append(4)
print(b)

# Em caso de objetos imutáveis, como Strings, isso não é um problema
