# Amostra (substitua isso pelos seus próprios dados)
amostra <- c(8, 9, 10, 11, 12, 11, 9, 10, 11, 10)

# Valor da média para teste de hipótese
media_teste <- 10

# Realizando o teste de hipótese para a média
resultado_teste <- t.test(amostra, mu = media_teste)

# Extraindo os resultados
print(resultado_teste)

# Interpretando o resultado
if (resultado_teste$p.value < 0.05) {
  print("Rejeitamos a hipótese nula. Há evidências estatísticas para concluir que a média é diferente de 10.")
} else {
  print("Não há evidências estatísticas para rejeitar a hipótese nula. Não podemos concluir que a média é diferente de 10.")
}
