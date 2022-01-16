# podemos converter uma string em lista

nome = 'Lucas'
t = list(nome)
print(t)

# também é possível quebrar uma string em palaras, análogo a JS, usamos split
nome = 'Lucas e aluno da poli-usp'
t = nome.split()
print(t)

# podemos manipular algumas coisas de forma bem legal

nome = 'Lucas-aluno-da-Eng comp'
t = nome.split('-')  # dizemos para separar se encontrar algum -
print(t)

# agora, podemos juntar
# indicamos o que vai separar cada elemento e então, usamos join - a sintaxe é a inversa do JS
outro_nome = ' '.join(t)
print(outro_nome)


# Objeto e valor, no rigor dos termos, são conceitos diferentes
nome = "Lucas"
outro_nome = "Lucas"
# Aqui, o Python criou apenas um objeto, que as duas variáveis apontam
# Chamamos cada associação a um objeto de referência. Temos duas referências, portanto.
print(nome is outro_nome)

t = [1, 2, 4]
nome = [1, 2, 4]
# Aqui, em contrapartida, são objetos diferentes, mas com o mesmo valor
print(t is nome)
