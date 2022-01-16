import csv
with open(filename, 'r') as f:
    data = function_that_gets_data_from(f)
# neste ponto f já foi fechado, não tente usá-lo
process(data)


# para pular linhas em um arquivos
starts_with_hash = 0
with open('input.txt', 'r') as f:
    for line in file:  # observe cada linha do arquivo
        if re.match("^#", line):  # use um regex para ver se começa com '#'
            starts_with_hash += 1  # se começar, adicione 1 à contagem


# Caso estejamos trabalhando com planilhas:


with open('tab_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)
