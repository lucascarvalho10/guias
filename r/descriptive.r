# Vetor de dados (substitua isso pelos seus próprios dados)
dados <- c(10, 15, 20, 22, 25, 28, 30, 35, 40, 45)

# Medidas de Centralidade
media <- mean(dados)          # Média
mediana <- median(dados)      # Mediana
moda <- as.numeric(names(sort(table(dados), decreasing=TRUE)[1]))  # Moda (primeira moda, se houver)

# Medidas de Dispersão
variancia <- var(dados)       # Variância
desvio_padrao <- sd(dados)    # Desvio Padrão
amplitude <- max(dados) - min(dados)  # Amplitude

# Imprimindo os resultados
print(paste("Média:", media))
print(paste("Mediana:", mediana))
print(paste("Moda:", moda))
print(paste("Variância:", variancia))
print(paste("Desvio Padrão:", desvio_padrao))
print(paste("Amplitude:", amplitude))
