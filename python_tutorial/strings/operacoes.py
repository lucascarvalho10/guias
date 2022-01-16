# com a função len, podemos obter o tamanho de caracteres de uma coleção tipo string
palavra = 'Lucas'
print(len(palavra))

# Podemos acessar valores com índices negativos, eles percorrem de trás para frente
print(palavra[-1])

# também vale p processo de seleção
print(palavra[:], palavra[:2], palavra[1:3], palavra[::2])

# Strings são imutáveis, não é possíve alterar algo apenas pelo índice, acarretaria um erro
