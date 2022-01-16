palavra = "palavra"

# Chamar um método é o que denominamos invocar
print(palavra.upper())

# para retornar apenas a primeira maiúcila
print(palavra.capitalize())


# retorna o índice da primeira aparição
print(palavra.find('a'))

# retorna a quantidade de vezes que aparece
print(palavra.count('a'))

# verifica se uma string termina com um determinado sufixo
print(palavra.endswith('s'))


# O in verifica se uma substring está contida na segunda
print('avra' in palavra)


# Legal: os operadores de comparação funcionam perfeitamente em strings, com o mesmo significado

print("banana" < 'melao')
print('bala' == "bala")
