'''Exemplo adaptado do livro: Data Science com Python'''

from matplotlib import pyplot as plt

#lista de valores
anos = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
notas = [9.2, 9.7, 9.1, 9, 9, 8.7, 10]

#gráfico de linha, com anos no eixo e notas no eixo y
plt.plot(anos, notas, color='red', marker='*', linestyle='solid')

#título
plt.title("Evolução das Notas")

#nome do eixo vertical
plt.ylabel("Notas")
plt.xlabel("Ano")

#apresenta o gráfico
plt.show()